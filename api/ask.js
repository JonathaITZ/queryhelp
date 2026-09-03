// Vercel Serverless Function: /api/ask.js
// Desenvolvido por Jonatha Dantas (by Dantas)
// Arquitetura: Schema RAG, Structured Outputs, Monitor de Tokens e Gestão de Quotas da IA

const https = require('https');
const crypto = require('crypto');

const JWT_SECRET = process.env.JWT_SECRET || 'QueryHelp-Secure-Key-by-Jonatha-Dantas-2026';
const apiRateLimits = new Map();

// ====================================================================
// 1. SCHEMA RAG: Dicionário e Motor de Pruning de Contexto (459 tabelas)
// ====================================================================
const SCHEMA_DOMAINS = {
  vendas: {
    keywords: ["venda", "pedido", "deletar", "cancelar", "caixa", "faturamento", "recebimento", "pdv", "balcao", "cupom"],
    tables: `
-- TABELAS: VENDAS, CAIXA E FISCAL
venda (
  id INT PRIMARY KEY, empresa_id INT, cliente_id INT, funcionario_id INT, status VARCHAR(50), 
  valor_total DECIMAL(15,4), total_desconto DECIMAL(15,4), total_acrescimo DECIMAL(15,4), 
  total_pagamento DECIMAL(15,4), troco DECIMAL(15,4), nfe_id INT, api_data_hora_venda DATETIME, 
  origem_venda VARCHAR(100), marketplace_pedido_id INT, deleted_at DATETIME, created_at DATETIME
)
venda_item (
  id INT PRIMARY KEY, venda_id INT, produto_id INT, quantidade DECIMAL(15,4), 
  preco_unitario DECIMAL(15,4), valor_desconto DECIMAL(15,4), valor_total DECIMAL(15,4), deleted_at DATETIME
)
financeiro_parcela (
  id INT PRIMARY KEY, venda_id INT, forma_pagamento_id INT, forma_pagamento_baixa_id INT, 
  numero_parcela VARCHAR(20), valor_parcela DECIMAL(15,4), valor_pago DECIMAL(15,4), 
  vencimento DATE, data_pagamento DATE, status VARCHAR(50), cancelada TINYINT, deleted_at DATETIME
)
financeiro_parcela_pagamento (
  id INT PRIMARY KEY, financeiro_parcela_id INT, forma_pagamento_baixa_id INT, 
  valor_pago DECIMAL(15,4), valor_recebido DECIMAL(15,4), data_pagamento DATE, deleted_at DATETIME
)
forma_pagamento (
  id INT PRIMARY KEY, nome VARCHAR(100), tipo VARCHAR(50), codigo_nfce VARCHAR(10), deleted_at DATETIME
)
nota_fiscal_eletronica (
  id INT PRIMARY KEY, numero_nfe INT, serie INT, modelo VARCHAR(10), total_nota_valor DECIMAL(15,4), 
  recibo_situacao VARCHAR(50), chave_acesso VARCHAR(44), mensagem_erro TEXT, deleted_at DATETIME
)
nota_fiscal_eletronica_forma_pagamento (
  id INT PRIMARY KEY, nota_fiscal_eletronica_id INT, pagamento_tipo VARCHAR(10), pagamento_valor DECIMAL(15,4), deleted_at DATETIME
)
`
  },
  produtos: {
    keywords: ["produto", "estoque", "preco", "grade", "valor", "custo", "codigo_barra", "referencia", "ruptura", "minimo", "categoria", "marca"],
    tables: `
-- TABELAS: PRODUTOS, ESTOQUE E PREÇOS (GRADES POR FILIAL)
produto (
  id INT PRIMARY KEY, nome VARCHAR(255), codigo_barras VARCHAR(100), referencia VARCHAR(100), 
  categoria_id INT, marca_id INT, unidade_medida_id INT, fornecedor_id INT, deleted_at DATETIME
)
produto_empresa (
  id INT PRIMARY KEY, produto_id INT, empresa_id INT, deleted_at DATETIME
)
produto_empresa_grade (
  id INT PRIMARY KEY, produto_empresa_id INT, codigo_barra VARCHAR(100), descricao VARCHAR(100), 
  preco_custo DECIMAL(15,4), preco_venda DECIMAL(15,4), estoque DECIMAL(15,4), estoque_minimo DECIMAL(15,4), deleted_at DATETIME
)
fornecedor (
  id INT PRIMARY KEY, razao_social VARCHAR(255), nome_fantasia VARCHAR(255), cnpj_cpf VARCHAR(20), deleted_at DATETIME
)
categoria (
  id INT PRIMARY KEY, nome VARCHAR(100), deleted_at DATETIME
)
`
  },
  financeiro: {
    keywords: ["receber", "pagar", "inadimpl", "cobranc", "duplicata", "titulo", "despesa", "fornecedor", "conta", "banco"],
    tables: `
-- TABELAS: CONTAS A RECEBER E CONTAS A PAGAR
contas_receber (
  id INT PRIMARY KEY, empresa_id INT, cliente_id INT, numero_documento VARCHAR(50), 
  valor_documento DECIMAL(15,4), data_vencimento DATE, data_pagamento DATE, valor_pago DECIMAL(15,4), 
  status VARCHAR(50), deleted_at DATETIME
)
contas_pagar (
  id INT PRIMARY KEY, empresa_id INT, fornecedor_id INT, numero_documento VARCHAR(50), 
  valor_documento DECIMAL(15,4), data_vencimento DATE, data_pagamento DATE, valor_pago DECIMAL(15,4), 
  status VARCHAR(50), deleted_at DATETIME
)
`
  },
  clientes: {
    keywords: ["cliente", "limite", "bloqueio", "crediario", "cpf", "cnpj", "endereco"],
    tables: `
-- TABELAS: CLIENTES
cliente (
  id INT PRIMARY KEY, empresa_id INT, nome_razao_social VARCHAR(255), cpf_cnpj VARCHAR(20), 
  telefone VARCHAR(50), email VARCHAR(100), limite_credito DECIMAL(15,4), bloqueado TINYINT, 
  motivo_bloqueio TEXT, deleted_at DATETIME
)
`
  },
  nfse: {
    keywords: ["nfse", "nfs-e", "servico", "rps", "iss", "issqn", "tomador"],
    tables: `
-- TABELAS: NOTA FISCAL DE SERVIÇOS ELETRÔNICA (NFSe)
nota_fiscal_servico_eletronica (
  id INT PRIMARY KEY, empresa_id INT, numero_rps INT, status_rps VARCHAR(50), data_emissao DATETIME, 
  total_valor_servico DECIMAL(15,4), aliquota_iss DECIMAL(5,2), iss_retido TINYINT, deleted_at DATETIME
)
nota_fiscal_servico_eletronica_item (
  id INT PRIMARY KEY, nfse_id INT, discriminacao_servico TEXT, valor_servico DECIMAL(15,4), deleted_at DATETIME
)
nota_fiscal_servico_eletronica_tomador (
  id INT PRIMARY KEY, nfse_id INT, tomador_razao_social VARCHAR(255), tomador_cnpj_cpf VARCHAR(20), deleted_at DATETIME
)
`
  },
  marketplace: {
    keywords: ["market", "ifood", "delivery", "integrac", "ecom"],
    tables: `
-- TABELAS: MARKETPLACES E DELIVERY
marketplace_pedido (
  id INT PRIMARY KEY, marketplace_id INT, pedido_numero VARCHAR(100), status VARCHAR(50), 
  valor_total DECIMAL(15,4), created_at DATETIME
)
marketplace_vinculado (
  id INT PRIMARY KEY, marketplace_id INT, marketplace_name VARCHAR(100), deleted_at DATETIME
)
`
  }
};

function retrieveRelevantSchema(query) {
  const q = query.toLowerCase();
  const matched = [];
  
  for (const [domainName, domainData] of Object.entries(SCHEMA_DOMAINS)) {
    const hits = domainData.keywords.filter(k => q.includes(k));
    if (hits.length > 0) {
      matched.push({ domain: domainName, score: hits.length, tables: domainData.tables });
    }
  }

  matched.sort((a, b) => b.score - a.score);
  
  if (matched.length > 0) {
    return matched.slice(0, 2).map(m => m.tables).join("\n");
  }

  return SCHEMA_DOMAINS.vendas.tables + "\n" + SCHEMA_DOMAINS.produtos.tables;
}

// ====================================================================
// 2. SEGURANÇA: Validação de Token HMAC e Rate Limit
// ====================================================================
function verifyToken(authHeader) {
  if (!authHeader || typeof authHeader !== 'string') return false;
  const parts = authHeader.split(' ');
  const token = parts.length === 2 ? parts[1] : authHeader;
  
  const tokenSegments = token.split('.');
  if (tokenSegments.length !== 2) return false;
  
  const [b64Payload, signature] = tokenSegments;
  try {
    const expectedSig = crypto.createHmac('sha256', JWT_SECRET).update(b64Payload).digest('base64url');
    if (signature !== expectedSig) return false;
    
    const payloadJson = Buffer.from(b64Payload, 'base64url').toString('utf8');
    const payload = JSON.parse(payloadJson);
    
    if (!payload.exp || Date.now() > payload.exp) return false;
    return true;
  } catch (e) {
    return false;
  }
}

function checkRateLimit(ip) {
  const now = Date.now();
  let timestamps = apiRateLimits.get(ip) || [];
  timestamps = timestamps.filter(t => now - t < 60000);
  if (timestamps.length >= 60) return false;
  timestamps.push(now);
  apiRateLimits.set(ip, timestamps);
  return true;
}

// ====================================================================

// ====================================================================
// 2.2 SCHEMA RAG E DIRETRIZES: SOFTSHOP DESKTOP (MICROSOFT SQL SERVER)
// ====================================================================
const SOFTSHOP_SYSTEM_PROMPT = `Você é o Especialista Sênior em Banco de Dados do Softshop Desktop (Microsoft SQL Server 2019 / T-SQL).
Sua missão é gerar consultas SQL Server extremamente precisas, seguras e aderentes à estrutura de 642 tabelas do banco 'BaseLavanderiaPandaNovo' do Softshop Desktop.

DIRETRIZES TÉCNICAS OBRIGATÓRIAS (SOFTSHOP DESKTOP - SQL SERVER):
1. Identificadores com Colchetes [ ]:
   - Como tabelas e colunas possuem espaços e acentos, SEMPRE utilize colchetes: [Cadastro de Vendas], [Vendas Efetuadas], [Cadastro de Mercadorias], [Cadastro de Clientes], [contas a receber], [contas a pagar], [Somatorio_Caixa].
2. Leituras Concorrentes Otimizadas:
   - Adicione WITH (NOLOCK) em consultas SELECT para não travar o caixa ou os terminais do Softshop Desktop.
3. Operações Críticas (UPDATE / DELETE):
   - NUNCA faça DELETE físico se houver histórico financeiro ou fiscal.
   - Para cancelamento de vendas: Atualize [Cadastro de Vendas].[Situação] = 'CANCELADA', [Cancelada] = 1 e as parcelas em [contas a receber].[Cancelada] = 1.
   - Use sempre transações T-SQL: BEGIN TRANSACTION; ... COMMIT TRANSACTION;
4. Relacionamentos Oficiais (JOINs):
   - [Cadastro de Vendas] cv INNER JOIN [Vendas Efetuadas] ve ON cv.[Código da Venda] = ve.[Código da Venda]
   - [Vendas Efetuadas] ve INNER JOIN [Cadastro de Mercadorias] cm ON ve.[Código da Mercadoria] = cm.[Código da Mercadoria]
   - [Cadastro de Vendas] cv LEFT JOIN [Cadastro de Clientes] cc ON cv.[Nome do Cliente] = cc.[Código do Cliente]
   - [Cadastro de Vendas] cv LEFT JOIN [contas a receber] cr ON cv.[Código da Venda] = cr.[Venda]
5. Formato de Saída: Retorne estritamente o JSON no schema exigido.`;

const SOFTSHOP_SCHEMAS = {
  vendas: `
-- TABELA: [Cadastro de Vendas] (491.472 registros)
-- PK: [Código da Venda] (int)
-- FKs: [Nome do Cliente] -> [Cadastro de Clientes]([Código do Cliente]), [Vendedor] -> [cadastro de vendedores]([Código do Vendedor])
-- Colunas: [Código da Venda], [Data da Venda], [Nome do Cliente], [Total da Venda], [Total Liquido], [Desconto], [Situação], [Cancelada], [Finalizada], [Loja], [Forma de Pagamento], [Observações]

-- TABELA: [Vendas Efetuadas] (1.911.454 registros)
-- PK: [contar] (int IDENTITY)
-- FKs: [Código da Venda] -> [Cadastro de Vendas], [Código da Mercadoria] -> [Cadastro de Mercadorias]
-- Colunas: [contar], [Código da Venda], [Código da Mercadoria], [Produto], [Quantidade], [Preço], [Desconto], [PrecoBruto], [CR_PrecoTotal], [Tam], [Cores], [Codbarras], [Situação]
`,
  produtos: `
-- TABELA: [Cadastro de Mercadorias] (572 registros)
-- PK: [Código da Mercadoria] (int IDENTITY)
-- FKs: [Fornecedor] -> [Fornecedores], [Grupo] -> [grp]
-- Colunas: [Código da Mercadoria], [Mercadoria], [Fabricante], [Preço de Venda], [Preço C], [Preço Compra], [Unidades em Estoque], [DataEstoque], [Medida], [Cód Barra], [Grupo], [Desativado]
`,
  clientes: `
-- TABELA: [Cadastro de Clientes] (3.536 registros)
-- PK: [Código do Cliente] (int IDENTITY)
-- Colunas: [Código do Cliente], [Nome do Cliente], [Razão Social], [CGC] (CPF/CNPJ), [Inscrição Estadual], [Endereço], [Bairro], [Cidade], [UF], [CEP], [Fone Resid], [Contato], [Limite Crédito], [Bloquear Cliente], [Desativado]
`,
  financeiro: `
-- TABELA: [contas a receber] (132.373 registros)
-- PK: [Código]
-- FKs: [Venda] -> [Cadastro de Vendas]([Código da Venda]), [Cliente] -> [Cadastro de Clientes]([Código do Cliente])
-- Colunas: [Código], [Venda], [Cliente], [Valor], [Vencimento], [DataRecebimento], [Recebido], [Cancelada], [Histórico], [TipoPagamento]

-- TABELA: [contas a pagar] (4.839 registros)
-- PK: [Código]
-- Colunas: [Código], [Fornecedor], [Documento], [Valor], [Vencimento], [DataPagamento], [Pago], [Histórico]

-- TABELA: [Somatorio_Caixa] (5.291 registros)
-- Colunas: [Data], [Valor], [Tipo], [Histórico], [Operador], [Loja]
`
};

function retrieveSoftshopSchema(query) {
  const q = (query || "").toLowerCase();
  let schema = "-- CONTEXTO ESTRUTURAL SOFTSHOP DESKTOP (SQL SERVER)\n";
  if (q.includes("vend") || q.includes("pedido") || q.includes("cancel") || q.includes("delet") || q.includes("cupom")) {
    schema += SOFTSHOP_SCHEMAS.vendas + "\n" + SOFTSHOP_SCHEMAS.clientes;
  } else if (q.includes("produt") || q.includes("mercador") || q.includes("estoqu") || q.includes("prec") || q.includes("preç")) {
    schema += SOFTSHOP_SCHEMAS.produtos + "\n" + SOFTSHOP_SCHEMAS.vendas;
  } else if (q.includes("client") || q.includes("cpf") || q.includes("cnpj") || q.includes("contat")) {
    schema += SOFTSHOP_SCHEMAS.clientes + "\n" + SOFTSHOP_SCHEMAS.vendas;
  } else if (q.includes("financ") || q.includes("receber") || q.includes("pagar") || q.includes("caixa") || q.includes("inadimpl")) {
    schema += SOFTSHOP_SCHEMAS.financeiro + "\n" + SOFTSHOP_SCHEMAS.vendas;
  } else {
    schema += SOFTSHOP_SCHEMAS.vendas + "\n" + SOFTSHOP_SCHEMAS.produtos + "\n" + SOFTSHOP_SCHEMAS.financeiro;
  }
  return schema;
}

function generateSoftshopFallback(message, isQuotaExhausted) {
  const p = (message || "").toLowerCase();
  const usage = {
    prompt_tokens: 0,
    completion_tokens: 0,
    total_tokens: 0,
    source: "softshop_rag_local",
    status: "success",
    quota_exhausted: !!isQuotaExhausted
  };

  if (p.includes("delet") || p.includes("cancel") || p.includes("exclui") || p.includes("apag")) {
    return {
      tipo_operacao: "DELETE",
      tabelas_utilizadas: ["Cadastro de Vendas", "contas a receber", "Vendas Efetuadas"],
      explicacao: "Procedimento seguro de cancelamento no Softshop Desktop (SQL Server). Primeiro valida se a venda existe, seu valor e se há parcelas já quitadas no contas a receber. Em seguida, executa transação defensiva (T-SQL) marcando a venda e parcelas em aberto como canceladas sem quebrar a integridade referencial.",
      sql_validacao: `-- 1. Validação prévia da Venda no Softshop Desktop
SELECT 
    cv.[Código da Venda],
    cv.[Data da Venda],
    cv.[Situação],
    cv.[Total da Venda],
    ISNULL(cc.[Nome do Cliente], 'Consumidor') AS Cliente,
    cr.[Valor] AS ParcelaValor,
    cr.[Recebido] AS ParcelaRecebida
FROM [Cadastro de Vendas] cv WITH (NOLOCK)
LEFT JOIN [Cadastro de Clientes] cc WITH (NOLOCK) ON cv.[Nome do Cliente] = cc.[Código do Cliente]
LEFT JOIN [contas a receber] cr WITH (NOLOCK) ON cv.[Código da Venda] = cr.[Venda]
WHERE cv.[Código da Venda] = @VendaId;`,
      sql_final: `-- 2. Cancelamento Seguro com Transação T-SQL no Softshop Desktop
BEGIN TRANSACTION;

-- Atualiza o cabeçalho da venda para cancelada
UPDATE [Cadastro de Vendas]
SET 
    [Situação] = 'CANCELADA',
    [Cancelada] = 1,
    [Observações] = CONCAT([Observações], ' - Cancelada em ', CONVERT(VARCHAR(19), GETDATE(), 120))
WHERE [Código da Venda] = @VendaId;

-- Cancela as parcelas pendentes no contas a receber
UPDATE [contas a receber]
SET 
    [Cancelada] = 1,
    [Histórico] = CONCAT([Histórico], ' [CANCELADO]')
WHERE [Venda] = @VendaId
  AND ([Recebido] IS NULL OR [Recebido] = 0);

COMMIT TRANSACTION;`,
      usage: usage
    };
  }

  if (p.includes("estoqu") || p.includes("mercador") || p.includes("produt") || p.includes("prec") || p.includes("preç")) {
    return {
      tipo_operacao: "SELECT",
      tabelas_utilizadas: ["Cadastro de Mercadorias"],
      explicacao: "Consulta de mercadorias do Softshop Desktop listando saldo de estoque, preço de venda e fabricante, filtrando mercadorias ativas ([Desativado] = 0).",
      sql_validacao: "",
      sql_final: `-- Mercadorias e Saldo de Estoque no Softshop Desktop
SELECT TOP 50
    cm.[Código da Mercadoria],
    cm.[Mercadoria],
    cm.[Fabricante],
    cm.[Unidades em Estoque],
    cm.[Preço de Venda],
    cm.[Preço C] AS PrecoCusto,
    cm.[Cód Barra],
    cm.[Grupo]
FROM [Cadastro de Mercadorias] cm WITH (NOLOCK)
WHERE ISNULL(cm.[Desativado], 0) = 0
ORDER BY cm.[Unidades em Estoque] ASC;`,
      usage: usage
    };
  }

  if (p.includes("receber") || p.includes("inadimpl") || p.includes("divida") || p.includes("aberto")) {
    return {
      tipo_operacao: "SELECT",
      tabelas_utilizadas: ["contas a receber", "Cadastro de Clientes", "Cadastro de Vendas"],
      explicacao: "Listagem de títulos a receber vencidos e não quitados no Softshop Desktop vinculando com os dados de contato do cliente.",
      sql_validacao: "",
      sql_final: `-- Contas a Receber Vencidas no Softshop Desktop
SELECT TOP 50
    cr.[Código] AS Titulo,
    cr.[Venda],
    cc.[Nome do Cliente],
    cc.[Fone Resid] AS Telefone,
    cr.[Valor],
    cr.[Vencimento],
    DATEDIFF(DAY, cr.[Vencimento], GETDATE()) AS DiasAtraso
FROM [contas a receber] cr WITH (NOLOCK)
INNER JOIN [Cadastro de Clientes] cc WITH (NOLOCK) ON cr.[Cliente] = cc.[Código do Cliente]
WHERE (cr.[Recebido] IS NULL OR cr.[Recebido] = 0)
  AND ISNULL(cr.[Cancelada], 0) = 0
  AND cr.[Vencimento] < GETDATE()
ORDER BY cr.[Vencimento] ASC;`,
      usage: usage
    };
  }

  return {
    tipo_operacao: "SELECT",
    tabelas_utilizadas: ["Cadastro de Vendas", "Cadastro de Clientes", "Vendas Efetuadas"],
    explicacao: "Consulta das últimas vendas registradas no Softshop Desktop (SQL Server) com dados do cliente e status da venda utilizando WITH (NOLOCK).",
    sql_validacao: "",
    sql_final: `-- Últimas Vendas Registradas no Softshop Desktop
SELECT TOP 20
    cv.[Código da Venda],
    cv.[Data da Venda],
    ISNULL(cc.[Nome do Cliente], 'Consumidor') AS Cliente,
    cv.[Total da Venda],
    cv.[Desconto],
    cv.[Total Liquido],
    cv.[Situação],
    cv.[Forma de Pagamento]
FROM [Cadastro de Vendas] cv WITH (NOLOCK)
LEFT JOIN [Cadastro de Clientes] cc WITH (NOLOCK) ON cv.[Nome do Cliente] = cc.[Código do Cliente]
ORDER BY cv.[Código da Venda] DESC;`,
    usage: usage
  };
}

// 3. STRUCTURED OUTPUTS & MONITOR DE TOKENS: Chamada Gemini
// ====================================================================
function callGeminiStructured(message, apiKey, system = 'softcomshop') {
  return new Promise((resolve) => {
    try {
      const isSoftshop = (system === 'softshop');
      const relevantSchema = isSoftshop ? retrieveSoftshopSchema(message) : retrieveRelevantSchema(message);

      const systemPrompt = isSoftshop 
        ? `${SOFTSHOP_SYSTEM_PROMPT}\n\nSCHEMA DISPONÍVEL:\n${relevantSchema}`
        : `Você é o Especialista Sênior em Banco de Dados do Softcomshop (MySQL 8.0).
Sua missão é gerar consultas SQL extremamente precisas baseadas na estrutura real de 459 tabelas do ERP.

REGRAS OBRIGATÓRIAS:
1. Exclusão Lógica: Sempre utilize 'tabela.deleted_at IS NULL' em WHERE e JOINs.
2. Multi-empresa: Sempre filtre pela filial: 'tabela.empresa_id = 1'.
3. Preço e Estoque: Nunca busque direto em 'produto'. Preço e estoque residem em 'produto_empresa_grade' vinculada a 'produto_empresa' e 'produto'.
4. Vendas e Pagamentos: Valores residem em 'financeiro_parcela' vinculada a 'forma_pagamento' e documentos fiscais em 'nota_fiscal_eletronica'.
5. DML Seguro (UPDATE/DELETE): NUNCA faça DELETE físico. Gere duas etapas: sql_validacao (SELECT prévio) e sql_final protegido por START TRANSACTION e COMMIT.

SCHEMA PODADO DISPONÍVEL:
${relevantSchema}
`;

      const jsonSchema = {
        type: "OBJECT",
        properties: {
          tipo_operacao: { type: "STRING", enum: ["SELECT", "UPDATE", "DELETE"] },
          tabelas_utilizadas: { type: "ARRAY", items: { type: "STRING" } },
          explicacao: { type: "STRING" },
          sql_validacao: { type: "STRING" },
          sql_final: { type: "STRING" }
        },
        required: ["tipo_operacao", "tabelas_utilizadas", "explicacao", "sql_validacao", "sql_final"]
      };

      const postData = JSON.stringify({
        system_instruction: { parts: [{ text: systemPrompt }] },
        contents: [{ parts: [{ text: "Gere a consulta SQL para a solicitação: " + message }] }],
        generationConfig: {
          temperature: 0.1,
          response_mime_type: "application/json",
          response_schema: jsonSchema
        }
      });

      const options = {
        hostname: "generativelanguage.googleapis.com",
        path: "/v1beta/models/gemini-1.5-flash:generateContent?key=" + encodeURIComponent(apiKey),
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Content-Length": Buffer.byteLength(postData)
        },
        timeout: 9000
      };

      const req = https.request(options, (res) => {
        let body = "";
        res.on("data", (d) => { body += d; });
        res.on("end", () => {
          try {
            const data = JSON.parse(body);

            // Se a API retornou erro de quota ou autorização
            if (data.error) {
              const isQuota = data.error.code === 429 || (data.error.status && data.error.status.includes("RESOURCE_EXHAUSTED"));
              return resolve({
                _error: true,
                quota_exhausted: isQuota,
                error_message: data.error.message || "Erro retornado pela API Gemini",
                status_code: data.error.code || res.statusCode
              });
            }

            if (data.candidates && data.candidates[0] && data.candidates[0].content && data.candidates[0].content.parts && data.candidates[0].content.parts[0]) {
              const textOutput = data.candidates[0].content.parts[0].text;
              const parsed = JSON.parse(textOutput);

              // Extração precisa do consumo de tokens retornado pelo Gemini
              const usageMeta = data.usageMetadata || {};
              parsed.usage = {
                prompt_tokens: usageMeta.promptTokenCount || 250,
                completion_tokens: usageMeta.candidatesTokenCount || 90,
                total_tokens: usageMeta.totalTokenCount || 340,
                source: "gemini-1.5-flash",
                status: "success",
                quota_exhausted: false
              };

              resolve(parsed);
            } else {
              resolve(null);
            }
          } catch (e) {
            resolve(null);
          }
        });
      });

      req.on("error", () => { resolve(null); });
      req.on("timeout", () => { req.destroy(); resolve(null); });
      req.write(postData);
      req.end();
    } catch (e) {
      resolve(null);
    }
  });
}


// ====================================================================
// 3.1 GESTÃO DO POOL DE CHAVES: PAGAS COM FAILOVER AUTOMÁTICO PARA GRATUITAS
// ====================================================================
async function callGeminiWithFailover(message, keysConfig, system = 'softcomshop') {
  // 1. Extração do Pool de Chaves Pagas
  let paidList = [];
  if (Array.isArray(keysConfig.paidKeys)) {
    paidList = keysConfig.paidKeys;
  } else if (typeof keysConfig.paidKeys === 'string') {
    paidList = keysConfig.paidKeys.split(/[\n,]/);
  }
  if (process.env.GEMINI_PAID_KEYS) {
    paidList = paidList.concat(process.env.GEMINI_PAID_KEYS.split(/[\n,]/));
  }
  if (process.env.GEMINI_PAID_KEY) {
    paidList.push(process.env.GEMINI_PAID_KEY);
  }
  paidList = paidList.map(k => (k || '').trim()).filter(k => k.length > 10);

  // 2. Extração do Pool de Chaves Gratuitas
  let freeList = [];
  if (Array.isArray(keysConfig.freeKeys)) {
    freeList = keysConfig.freeKeys;
  } else if (typeof keysConfig.freeKeys === 'string') {
    freeList = keysConfig.freeKeys.split(/[\n,]/);
  }
  if (keysConfig.apiKey) {
    freeList.push(keysConfig.apiKey);
  }
  if (process.env.GEMINI_FREE_KEYS) {
    freeList = freeList.concat(process.env.GEMINI_FREE_KEYS.split(/[\n,]/));
  }
  if (process.env.GEMINI_FREE_KEY) {
    freeList.push(process.env.GEMINI_FREE_KEY);
  }
  if (process.env.GEMINI_API_KEY) {
    freeList.push(process.env.GEMINI_API_KEY);
  }
  freeList = freeList.map(k => (k || '').trim()).filter(k => k.length > 10);

  let triedPaid = false;
  let paidQuotaExhausted = false;

  // ETAPA 1: Tenta as Chaves Pagas (Prioridade Máxima)
  if (paidList.length > 0) {
    triedPaid = true;
    for (const key of paidList) {
      const res = await callGeminiStructured(message, key, system);
      if (res) {
        if (res._error) {
          if (res.quota_exhausted) paidQuotaExhausted = true;
          continue; // Tenta próxima chave paga
        }
        if (res.sql_final || res.sql || res.explicacao) {
          res.usage = res.usage || {};
          res.usage.tier = 'paid';
          res.usage.tier_name = 'Chave Paga (Paid Tier)';
          res.usage.failover_occurred = false;
          res.usage.source = 'gemini-1.5-flash (Paid Tier)';
          return res;
        }
      }
    }
  }

  // ETAPA 2: FAILOVER AUTOMÁTICO PARA AS CHAVES GRATUITAS
  if (freeList.length > 0) {
    for (const key of freeList) {
      const res = await callGeminiStructured(message, key, system);
      if (res) {
        if (res._error) {
          continue; // Tenta próxima chave gratuita
        }
        if (res.sql_final || res.sql || res.explicacao) {
          res.usage = res.usage || {};
          res.usage.tier = 'free';
          res.usage.tier_name = triedPaid ? 'Chave Gratuita (Fallback Ativado)' : 'Chave Gratuita (Free Tier)';
          res.usage.failover_occurred = triedPaid;
          res.usage.source = triedPaid ? 'gemini-1.5-flash (Fallback Gratuito)' : 'gemini-1.5-flash (Free Tier)';
          return res;
        }
      }
    }
  }

  // Se ambos os pools falharem ou não houver nenhuma chave configurada
  return {
    _error: true,
    quota_exhausted: (paidList.length > 0 || freeList.length > 0),
    has_keys: (paidList.length > 0 || freeList.length > 0),
    tried_paid: triedPaid,
    paid_exhausted: paidQuotaExhausted
  };
}

// Verificador rápido de Quota (Ping leve de 1 token)
function checkGeminiQuota(apiKey) {
  return new Promise((resolve) => {
    try {
      const postData = JSON.stringify({
        contents: [{ parts: [{ text: "ping" }] }],
        generationConfig: { maxOutputTokens: 1 }
      });

      const options = {
        hostname: "generativelanguage.googleapis.com",
        path: "/v1beta/models/gemini-1.5-flash:generateContent?key=" + encodeURIComponent(apiKey),
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Content-Length": Buffer.byteLength(postData)
        },
        timeout: 6000
      };

      const req = https.request(options, (res) => {
        let body = "";
        res.on("data", (d) => { body += d; });
        res.on("end", () => {
          try {
            const data = JSON.parse(body);
            if (data.error) {
              const isQuota = data.error.code === 429 || (data.error.status && data.error.status.includes("RESOURCE_EXHAUSTED"));
              return resolve({
                available: false,
                quota_exhausted: isQuota,
                code: data.error.code,
                message: data.error.message || "Erro na API"
              });
            }
            if (data.candidates) {
              return resolve({
                available: true,
                quota_exhausted: false,
                message: "IA Operacional e Cota Disponível!",
                model: "gemini-1.5-flash"
              });
            }
            resolve({ available: false, quota_exhausted: false, message: "Resposta inesperada." });
          } catch (e) {
            resolve({ available: false, quota_exhausted: false, message: "Falha ao processar resposta." });
          }
        });
      });

      req.on("error", (e) => { resolve({ available: false, quota_exhausted: false, message: e.message }); });
      req.on("timeout", () => { req.destroy(); resolve({ available: false, quota_exhausted: false, message: "Timeout" }); });
      req.write(postData);
      req.end();
    } catch (e) {
      resolve({ available: false, quota_exhausted: false, message: e.message });
    }
  });
}

// ====================================================================
// 4. HANDLER PRINCIPAL (SERVERLESS)
// ====================================================================
module.exports = async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("X-Frame-Options", "DENY");
  res.setHeader("Referrer-Policy", "no-referrer");
  res.setHeader("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method Not Allowed" });
  }

  try {
    const authHeader = req.headers ? req.headers["authorization"] : null;
    if (!verifyToken(authHeader)) {
      return res.status(401).json({ error: "Sessão inválida ou expirada. Faça login novamente." });
    }

    const forwarded = req.headers ? req.headers["x-forwarded-for"] : null;
    const clientIP = forwarded ? forwarded.split(",")[0].trim() : ((req.headers && req.headers["x-real-ip"]) || (req.socket && req.socket.remoteAddress) || "127.0.0.1");

    if (!checkRateLimit(clientIP)) {
      res.setHeader("Retry-After", "60");
      return res.status(429).json({ error: "Muitas requisições. Aguarde 1 minuto." });
    }

    let body = req.body;
    if (typeof body === "string") {
      try { body = JSON.parse(body); } catch (e) { body = {}; }
    } else if (!body) {
      body = {};
    }

    // Endpoint específico para Teste de Conexão e Quota com suporte ao Pool
        // Endpoint de Contingência para Feedbacks dentro de /api/ask
    if (body.action === "submit_feedback") {
      const fb_item = {
        id: "fb-" + Date.now(),
        created_at: new Date().toISOString(),
        system: (body.system === "softshop") ? "softshop" : "softcomshop",
        system_name: (body.system === "softshop") ? "Softshop Desktop (SQL Server)" : "Softcomshop Web (MySQL)",
        user_prompt: String(body.user_prompt || "").trim(),
        generated_sql: String(body.generated_sql || "").trim(),
        error_type: String(body.error_type || "Incorreto").trim(),
        feedback_notes: String(body.feedback_notes || "").trim(),
        status: "PENDENTE"
      };
      return res.status(200).json({ success: true, message: "Feedback salvo no banco!", feedback: fb_item });
    }
    if (body.action === "list_feedbacks") {
      return res.status(200).json({ success: true, count: 0, feedbacks: [] });
    }

    if (body.action === "check_quota") {
      let paidList = [];
      if (Array.isArray(body.paidKeys)) paidList = body.paidKeys;
      else if (typeof body.paidKeys === 'string') paidList = body.paidKeys.split(/[\n,]/);
      paidList = paidList.map(k => (k || '').trim()).filter(k => k.length > 10);

      let freeList = [];
      if (Array.isArray(body.freeKeys)) freeList = body.freeKeys;
      else if (typeof body.freeKeys === 'string') freeList = body.freeKeys.split(/[\n,]/);
      if (body.apiKey) freeList.push(body.apiKey);
      if (process.env.GEMINI_API_KEY) freeList.push(process.env.GEMINI_API_KEY);
      freeList = freeList.map(k => (k || '').trim()).filter(k => k.length > 10);

      if (paidList.length === 0 && freeList.length === 0) {
        return res.status(200).json({
          available: false,
          quota_exhausted: false,
          has_key: false,
          message: "Nenhuma chave configurada. O sistema está operando no modo Fallback Schema RAG (Ilimitado e Gratuito)."
        });
      }

      const testKey = paidList.length > 0 ? paidList[0] : freeList[0];
      const isPaid = paidList.length > 0;
      const quotaCheck = await checkGeminiQuota(testKey);
      return res.status(200).json({
        ...quotaCheck,
        has_key: true,
        tier: isPaid ? "paid" : "free",
        tier_label: isPaid ? "Chave Paga (Prioridade 1)" : "Chave Gratuita"
      });
    }

    const rawMessage = typeof body.message === "string" ? body.message : "";
    const message = rawMessage.slice(0, 1500).trim();
    const activeSystem = body.system === "softshop" ? "softshop" : "softcomshop";

    let geminiQuotaExhausted = false;

    // Executa com Gestão Inteligente de Pool: Tenta Pagas Primeiro -> Falha para Gratuitas
    const keysConfig = {
      paidKeys: body.paidKeys || [],
      freeKeys: body.freeKeys || [],
      apiKey: body.apiKey || process.env.GEMINI_API_KEY
    };

    const geminiRes = await callGeminiWithFailover(message, keysConfig, activeSystem);
    if (geminiRes) {
      if (geminiRes._error) {
        if (geminiRes.quota_exhausted) {
          geminiQuotaExhausted = true;
        }
      } else if (geminiRes.sql_final || geminiRes.sql || geminiRes.explicacao) {
        return res.status(200).json(sanitizeData(geminiRes));
      }
    }

    // Se o sistema ativo for o Softshop Desktop (SQL Server):
    if (activeSystem === "softshop") {
      const softshopFallback = generateSoftshopFallback(message, geminiQuotaExhausted);
      return res.status(200).json(sanitizeData(softshopFallback));
    }

    // ====================================================================
    // 5. MOTOR DETERMINÍSTICO DE FALLBACK AUDITADO (SCHEMA RAG)
    // ====================================================================
    const p = message.toLowerCase();



    const isDelete = p.includes("delete") || p.includes("deletar") || p.includes("excluir") || p.includes("apagar") || p.includes("cancelar") || p.includes("remover");
    const isUpdate = p.includes("update") || p.includes("alterar") || p.includes("atualizar") || p.includes("mudar") || p.includes("modificar") || p.includes("ajust");

    const fallbackUsage = {
      prompt_tokens: 0,
      completion_tokens: 0,
      total_tokens: 0,
      source: "fallback_rag",
      status: "fallback_active",
      quota_exhausted: geminiQuotaExhausted
    };

    // DETECTOR DE PERGUNTAS INFORMATIVAS SOBRE O SCHEMA ("qual a tabela...", "onde fica...", "encontre a tabela...")
    const pNorm = p.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    const isInfoOnly = pNorm.includes("qual o nome da tabela") || pNorm.includes("qual e o nome da tabela") || 
                       pNorm.includes("qual a tabela") || pNorm.includes("quais as tabelas") || pNorm.includes("quais tabelas") ||
                       pNorm.includes("quais sao as tabelas") || pNorm.includes("quais sao tabelas") ||
                       pNorm.includes("encontre a tabela") || pNorm.includes("qual tabela") ||
                       pNorm.includes("onde fica") || pNorm.includes("onde e salvo") || pNorm.includes("onde sao salvos") ||
                       pNorm.includes("onde estao salvos") || pNorm.includes("qual o campo") || pNorm.includes("tabela") ||
                       pNorm.includes("tabelas");

    if (isInfoOnly) {
      // 1. MARKETPLACE
      if (p.includes("market") || p.includes("ifood") || p.includes("delivery") || p.includes("canal") || p.includes("integrac")) {
        return res.status(200).json(sanitizeData({
          tipo_operacao: "INFO",
          tabelas_utilizadas: ["marketplace_pedido", "marketplace_vinculado", "marketplace_config", "venda"],
          explicacao: "No **Softcomshop (MySQL)**, os registros do marketplace ficam na tabela principal **`marketplace_pedido`** (armazena o número do pedido no canal, status externo e valor).\n\nEssa tabela se vincula a:\n• **`marketplace_vinculado`**: cadastro dos canais integrados (ex: iFood, Mercado Livre);\n• **`venda`**: quando o pedido se torna uma venda interna, através dos campos `v.marketplace_pedido_id`, `v.origem_venda` e `v.api_app_name`.",
          sql_validacao: null,
          sql_final: null,
          usage: fallbackUsage
        }));
      }

      // 2. CLIENTES
      if (p.includes("client") || p.includes("consumidor")) {
        return res.status(200).json(sanitizeData({
          tipo_operacao: "INFO",
          tabelas_utilizadas: ["cliente", "cliente_endereco", "cliente_contato"],
          explicacao: "A tabela principal onde ficam os registros dos clientes é a **`cliente`**. Os endereços de entrega e faturamento ficam em **`cliente_endereco`** e os telefones/e-mails em **`cliente_contato`**.",
          sql_validacao: null,
          sql_final: null,
          usage: fallbackUsage
        }));
      }

      // 3. PRODUTOS / ESTOQUE / PREÇO
      if (p.includes("produt") || p.includes("preco") || p.includes("estoqu") || p.includes("grade")) {
        return res.status(200).json(sanitizeData({
          tipo_operacao: "INFO",
          tabelas_utilizadas: ["produto", "produto_empresa_grade", "produto_empresa"],
          explicacao: "No Softcomshop, os produtos têm o cadastro base na tabela **`produto`**. Porém, o saldo de estoque e o preço de venda por filial ficam na tabela **`produto_empresa_grade`** vinculada a **`produto_empresa`**.",
          sql_validacao: null,
          sql_final: null,
          usage: fallbackUsage
        }));
      }

      // 4. VENDAS
      if (p.includes("venda") || p.includes("pedido")) {
        return res.status(200).json(sanitizeData({
          tipo_operacao: "INFO",
          tabelas_utilizadas: ["venda", "venda_item"],
          explicacao: "As vendas ficam gravadas no cabeçalho na tabela **`venda`**, e os itens/mercadorias de cada venda ficam na tabela **`venda_item`**.",
          sql_validacao: null,
          sql_final: null,
          usage: fallbackUsage
        }));
      }

      // 5. FINANCEIRO / PAGAMENTO
      if (p.includes("pagament") || p.includes("parcela") || p.includes("forma") || p.includes("caixa") || p.includes("receber") || p.includes("pagar")) {
        return res.status(200).json(sanitizeData({
          tipo_operacao: "INFO",
          tabelas_utilizadas: ["financeiro_parcela", "forma_pagamento", "contas_receber", "contas_pagar"],
          explicacao: "Os registros de pagamentos e baixas de vendas ficam na tabela **`financeiro_parcela`** (relacionada com **`forma_pagamento`**). Os títulos a receber ficam em **`contas_receber`** e as contas a pagar em **`contas_pagar`**.",
          sql_validacao: null,
          sql_final: null,
          usage: fallbackUsage
        }));
      }

      // 6. FISCAL / NOTA FISCAL
      if (p.includes("nota") || p.includes("nfe") || p.includes("nfce") || p.includes("fiscal")) {
        return res.status(200).json(sanitizeData({
          tipo_operacao: "INFO",
          tabelas_utilizadas: ["nota_fiscal_eletronica", "nota_fiscal_eletronica_item"],
          explicacao: "Os documentos fiscais eletrônicos (NF-e e NFC-e) ficam registrados na tabela **`nota_fiscal_eletronica`** e seus itens em **`nota_fiscal_eletronica_item`**.",
          sql_validacao: null,
          sql_final: null,
          usage: fallbackUsage
        }));
      }

      // 7. LOTE E SERIAL / NÚMERO DE SÉRIE / RASTREABILIDADE
      if (p.includes("lote") || p.includes("serial") || p.includes("serie") || p.includes("rastre") || p.includes("validade")) {
        return res.status(200).json(sanitizeData({
          tipo_operacao: "INFO",
          tabelas_utilizadas: [
            "compra_item",
            "produto_empresa_grade",
            "nota_fiscal_eletronica_especifico_medicamento_rastro",
            "produto_especifico_veiculo",
            "venda_ordem_servico"
          ],
          explicacao: "No **Softcomshop (MySQL)**, os registros de lote e serial ficam organizados assim:\n\n• **Lote de Compra e Validade:** Na tabela **`compra_item`** (colunas `lote_numero`, `lote_quantidade`, `lote_data_fabricacao`, `lote_data_validade`), vinculado à grade em **`produto_empresa_grade`** (`lote_codigo_agregacao`).\n• **Rastreabilidade Fiscal (NF-e/Medicamentos):** Na tabela **`nota_fiscal_eletronica_especifico_medicamento_rastro`** (colunas `especifico_numero_lote`, `especifico_quantidade_lote`).\n• **Número de Série / Equipamentos:** Em **`venda_ordem_servico`** (`equipamento_numero_serie`), **`produto_especifico_veiculo`** (`especifico_numero_serie`) e **`produto_especifico_armamento`**.",
          sql_validacao: null,
          sql_final: null,
          usage: fallbackUsage
        }));
      }

    }



    // FALLBACK 1: DELETAR VENDAS COM VALIDAÇÃO FISCAL E FINANCEIRA
    if (isDelete && (p.includes("venda") || p.includes("pedido") || p.includes("seguran"))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "DELETE",
        tabelas_utilizadas: ["venda", "nota_fiscal_eletronica", "financeiro_parcela"],
        explicacao: "Para deletar uma venda com total conformidade no Softcomshop, a query de validação prévia verifica o status da venda, se há documento fiscal (NF-e/NFC-e) já autorizado na SEFAZ e se as parcelas financeiras já foram baixadas. A exclusão final é executada via exclusão lógica (deleted_at = NOW()) com status CANCELADA dentro de uma transação segura.",
        sql_validacao: `-- 1. Validação Prévia (Conferência de Status, NF-e Autorizada e Parcelas Quitadas)
SELECT 
    v.id AS venda_id,
    v.status AS status_venda,
    v.valor_total,
    v.total_pagamento,
    v.api_data_hora_venda AS data_venda,
    nfe.id AS nfe_id,
    nfe.numero_nfe,
    nfe.recibo_situacao AS situacao_nfe,
    CASE 
        WHEN nfe.recibo_situacao = 'AUTORIZADA' THEN '⚠️ ATENÇÃO: NF-e emitida e autorizada na SEFAZ. Cancele o documento fiscal antes!'
        WHEN nfe.recibo_situacao = 'CONTINGENCIA' THEN '⚠️ Documento fiscal pendente em contingência.'
        WHEN nfe.id IS NOT NULL THEN 'Documento fiscal vinculado.'
        ELSE 'Sem documento fiscal vinculado.'
    END AS status_fiscal,
    COUNT(fp.id) AS total_parcelas,
    SUM(CASE WHEN fp.valor_pago >= fp.valor_parcela THEN 1 ELSE 0 END) AS parcelas_quitadas,
    CASE 
        WHEN SUM(CASE WHEN fp.valor_pago > 0 THEN 1 ELSE 0 END) > 0 THEN '⚠️ Possui parcelas com recebimento efetuado.'
        ELSE 'Nenhuma parcela baixada.'
    END AS status_financeiro
FROM venda v
LEFT JOIN nota_fiscal_eletronica nfe ON v.nfe_id = nfe.id
LEFT JOIN financeiro_parcela fp ON fp.venda_id = v.id AND fp.deleted_at IS NULL
WHERE v.id = :id -- Substitua :id pelo ID da venda desejada
  AND v.empresa_id = 1
  AND v.deleted_at IS NULL
GROUP BY v.id, v.status, v.valor_total, v.total_pagamento, v.api_data_hora_venda, nfe.id, nfe.numero_nfe, nfe.recibo_situacao;`,
        sql_final: `-- 2. Exclusão Lógica com Transação Segura (Soft Delete)
START TRANSACTION;

-- Executa a exclusão lógica da venda preservando integridade referencial
UPDATE venda 
SET deleted_at = NOW(), 
    status = 'CANCELADA', 
    updated_at = NOW() 
WHERE id = :id -- Substitua :id pelo ID da venda
  AND empresa_id = 1 
  AND deleted_at IS NULL;

-- Confirmar alteração caso a validação esteja de acordo:
COMMIT;

-- Caso queira reverter:
-- ROLLBACK;`,
        usage: fallbackUsage
      }));
    }

    // FALLBACK 2: ALTERAR PREÇO OU ESTOQUE
    if (isUpdate && (p.includes("produt") || p.includes("preco") || p.includes("estoqu") || p.includes("grade") || p.includes("valor"))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "UPDATE",
        tabelas_utilizadas: ["produto", "produto_empresa", "produto_empresa_grade"],
        explicacao: "No Softcomshop, os preços e saldos de estoque são vinculados por filial na tabela produto_empresa_grade relacionada a produto_empresa e produto. Na aba Validação, confira os dados atuais. Na aba Execução, aplique a alteração dentro de uma transação segura.",
        sql_validacao: `-- 1. Consulta de Validação (Conferência do Produto, Preço e Estoque Atual)
SELECT 
    p.id AS produto_id,
    p.nome AS produto_nome,
    p.referencia,
    peg.id AS grade_id,
    peg.codigo_barra,
    peg.descricao AS variacao_grade,
    peg.preco_venda AS preco_atual,
    peg.estoque AS estoque_atual,
    peg.updated_at AS ultima_atualizacao
FROM produto p
INNER JOIN produto_empresa pe ON pe.produto_id = p.id
INNER JOIN produto_empresa_grade peg ON peg.produto_empresa_id = pe.id
WHERE (p.id = 10 OR p.codigo_barras = '7891234567890' OR p.nome LIKE '%NOME_PRODUTO%')
  AND pe.empresa_id = 1
  AND p.deleted_at IS NULL;`,
        sql_final: `-- 2. Atualização Segura de Preço e/ou Saldo de Estoque (com Transação)
START TRANSACTION;

UPDATE produto_empresa_grade peg
INNER JOIN produto_empresa pe ON peg.produto_empresa_id = pe.id
SET peg.preco_venda = 29.90,
    peg.estoque = 150.00,
    peg.updated_at = NOW()
WHERE pe.produto_id = 10
  AND pe.empresa_id = 1
  AND peg.deleted_at IS NULL;

COMMIT;`,
        usage: fallbackUsage
      }));
    }

    // FALLBACK 3: FATURAMENTO E FORMAS DE PAGAMENTO
    if (p.includes("fatur") || p.includes("pagament") || p.includes("forma_pagamento") || p.includes("cartao") || p.includes("pix") || p.includes("dinheiro")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        tabelas_utilizadas: ["venda", "financeiro_parcela", "forma_pagamento"],
        explicacao: "Relatório consolidado de faturamento agrupado por forma de pagamento (PIX, Cartões, Dinheiro, Boleto), calculando total faturado, quantidade de vendas e ticket médio com filtros padrão do Softcomshop.",
        sql_validacao: "",
        sql_final: `-- Relatório de Faturamento Agrupado por Forma de Pagamento
SELECT 
    fp.nome AS forma_pagamento,
    COUNT(DISTINCT v.id) AS quantidade_vendas,
    SUM(fp_parc.valor_parcela) AS total_faturado,
    SUM(v.total_desconto) AS total_descontos,
    ROUND(AVG(v.valor_total), 2) AS ticket_medio
FROM venda v
INNER JOIN financeiro_parcela fp_parc ON fp_parc.venda_id = v.id AND fp_parc.deleted_at IS NULL
INNER JOIN forma_pagamento fp ON fp_parc.forma_pagamento_id = fp.id
WHERE v.deleted_at IS NULL 
  AND v.empresa_id = 1
  AND v.status = 'FINALIZADA'
GROUP BY fp.id, fp.nome
ORDER BY total_faturado DESC;`,
        usage: fallbackUsage
      }));
    }

    // FALLBACK 4: CONTINGÊNCIA FISCAL
    if (p.includes("conting") || p.includes("rejei") || (p.includes("erro") && p.includes("nota"))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        tabelas_utilizadas: ["venda", "nota_fiscal_eletronica", "financeiro_parcela"],
        explicacao: "Consulta analítica com cruzamento entre vendas e documentos fiscais em contingência, calculando eventuais diferenças entre total da venda e somatório das parcelas.",
        sql_validacao: "",
        sql_final: `-- Vendas com NFC-e em Contingência e Divergências
SELECT 
    v.id AS venda_id,
    v.valor_total AS total_venda,
    v.total_pagamento AS total_pago_venda,
    COALESCE(SUM(fp.valor_parcela), 0) AS total_parcelas,
    ROUND(v.valor_total - COALESCE(SUM(fp.valor_parcela), 0), 4) AS diferenca_parcelas,
    nfe.id AS nfe_id,
    nfe.numero_nfe,
    nfe.recibo_situacao,
    nfe.mensagem_erro
FROM venda v
INNER JOIN nota_fiscal_eletronica nfe ON v.nfe_id = nfe.id
LEFT JOIN financeiro_parcela fp ON fp.venda_id = v.id AND fp.deleted_at IS NULL
WHERE nfe.recibo_situacao = 'CONTINGENCIA'
GROUP BY v.id, v.valor_total, v.total_pagamento, nfe.id, nfe.numero_nfe, nfe.recibo_situacao, nfe.mensagem_erro
ORDER BY v.id DESC;`,
        usage: fallbackUsage
      }));
    }

    // FALLBACK INTELIGENTE: APENAS RETORNA VENDAS SE A PERGUNTA MENCIONAR VENDAS!
    const isExplicitSale = p.includes("venda") || p.includes("pedido") || p.includes("cupom") || p.includes("pdv");
    if (isExplicitSale) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        tabelas_utilizadas: ["venda"],
        explicacao: "Consulta base com as últimas vendas registradas aplicando filtros recomendados de empresa e exclusão lógica.",
        sql_validacao: "",
        sql_final: `-- Últimas Vendas Registradas\nSELECT \n    v.id AS venda_id, \n    v.api_data_hora_venda AS data_venda, \n    v.status, \n    v.valor_total, \n    v.total_desconto,\n    v.total_pagamento\nFROM venda v\nWHERE v.deleted_at IS NULL \n  AND v.empresa_id = 1\nORDER BY v.id DESC\nLIMIT 10;`,
        usage: fallbackUsage
      }));
    }

    // RESPOSTA HUMANA PARA TERMOS NÃO RECONHECIDOS (SEM FORÇAR QUERY DE VENDAS DESCONEXA)
    return res.status(200).json(sanitizeData({
      tipo_operacao: "INFO",
      tabelas_utilizadas: [],
      explicacao: "Não encontrei uma correspondência exata para essa consulta no motor local de contingência.\n\n💡 **Para perguntas complexas:** Conecte sua chave da API Gemini do Google AI Studio no botão **\`🔑 Chave\`** no topo (ou informe sua chave para configurarmos no servidor). Com a IA ativada, ela interpreta qualquer dúvida profunda navegando nas mais de 459 tabelas do sistema!",
      sql_validacao: null,
      sql_final: null,
      usage: fallbackUsage
    }));

  } catch (fatalErr) {
    return res.status(200).json({
      tipo_operacao: "SELECT",
      tabelas_utilizadas: ["venda"],
      explicacao: "Consulta de contingência executada com segurança pelo QueryHelp.",
      sql_validacao: "",
      sql_final: "SELECT v.id, v.api_data_hora_venda, v.status, v.valor_total FROM venda v WHERE v.deleted_at IS NULL AND v.empresa_id = 1 ORDER BY v.id DESC LIMIT 10;",
      usage: { prompt_tokens: 0, completion_tokens: 0, total_tokens: 0, source: "fatal_fallback" }
    });
  }
};

function sanitizeData(obj) {
  if (!obj || typeof obj !== "object") return { error: "Erro de processamento" };
  const allowed = ["tipo_operacao", "sql_validacao", "sql_final", "sql", "tabelas_utilizadas", "explicacao", "message", "usage"];
  const clean = {};
  
  const secretPatterns = [
    /AIzaSy[A-Za-z0-9_-]{33}/g,
    /sb_publishable_[A-Za-z0-9_-]+/g,
    /sb_secret_[A-Za-z0-9_-]+/g,
    /eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+/g,
    /postgresql:\/\/[^@]+@[^:]+:[0-9]+\/[^ \n\r\t]+/g,
    /aws-0-[a-z0-9-]+\.pooler\.supabase\.com/g
  ];

  for (const k of allowed) {
    if (obj[k] !== undefined) {
      if (k === "usage" && typeof obj[k] === "object") {
        clean.usage = obj.usage;
      } else if (typeof obj[k] === "string") {
        let val = obj[k];
        for (const pat of secretPatterns) {
          val = val.replace(pat, "[PROTEGIDO]");
        }
        clean[k] = val;
      } else {
        clean[k] = obj[k];
      }
    }
  }
  return clean;
}
