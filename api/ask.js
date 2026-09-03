// Vercel Serverless Function: /api/ask.js
// Desenvolvido por Jonatha Dantas (by Dantas)
// Arquitetura: Schema RAG (Context Pruning), Structured Outputs (JSON Schema Mode) e Fallbacks Auditados

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

  // Ordena pelos maiores acertos e seleciona até os 2 domínios mais relevantes
  matched.sort((a, b) => b.score - a.score);
  
  if (matched.length > 0) {
    return matched.slice(0, 2).map(m => m.tables).join("\n");
  }

  // Fallback padrão: tabelas vitais de Vendas e Produtos
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
// 3. STRUCTURED OUTPUTS: Chamada Gemini com JSON Schema Mode
// ====================================================================
function callGeminiStructured(message, apiKey) {
  return new Promise((resolve) => {
    try {
      const relevantSchema = retrieveRelevantSchema(message);

      const systemPrompt = `Você é o Especialista Sênior em Banco de Dados do Softcomshop (MySQL 8.0).
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
            if (data.candidates && data.candidates[0] && data.candidates[0].content && data.candidates[0].content.parts && data.candidates[0].content.parts[0]) {
              const textOutput = data.candidates[0].content.parts[0].text;
              const parsed = JSON.parse(textOutput);
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

    const rawMessage = typeof body.message === "string" ? body.message : "";
    const message = rawMessage.slice(0, 1500).trim();
    const activeKey = body.apiKey || process.env.GEMINI_API_KEY;

    // Se houver chave do Gemini, executa via Structured Outputs
    if (activeKey) {
      const geminiRes = await callGeminiStructured(message, activeKey);
      if (geminiRes && (geminiRes.sql_final || geminiRes.sql)) {
        return res.status(200).json(sanitizeData(geminiRes));
      }
    }

    // ====================================================================
    // 5. MOTOR DETERMINÍSTICO DE FALLBACK AUDITADO
    // ====================================================================
    const p = message.toLowerCase();
    const isDelete = p.includes("delete") || p.includes("deletar") || p.includes("excluir") || p.includes("apagar") || p.includes("cancelar") || p.includes("remover");
    const isUpdate = p.includes("update") || p.includes("alterar") || p.includes("atualizar") || p.includes("mudar") || p.includes("modificar") || p.includes("ajust");

    // FALLBACK ESPECÍFICO 1: DELETAR VENDAS COM VALIDAÇÃO FISCAL E FINANCEIRA
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
-- ROLLBACK;`
      }));
    }

    // FALLBACK 2: ALTERAR PREÇO OU ESTOQUE (PRODUTO_EMPRESA_GRADE)
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

COMMIT;`
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
ORDER BY total_faturado DESC;`
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
ORDER BY v.id DESC;`
      }));
    }

    // FALLBACK GERAL: ÚLTIMAS VENDAS
    return res.status(200).json(sanitizeData({
      tipo_operacao: "SELECT",
      tabelas_utilizadas: ["venda"],
      explicacao: "Consulta base com as últimas vendas registradas aplicando filtros recomendados de empresa e exclusão lógica.",
      sql_validacao: "",
      sql_final: `-- Últimas Vendas Registradas
SELECT 
    v.id AS venda_id, 
    v.api_data_hora_venda AS data_venda, 
    v.status, 
    v.valor_total, 
    v.total_desconto,
    v.total_pagamento
FROM venda v
WHERE v.deleted_at IS NULL 
  AND v.empresa_id = 1
ORDER BY v.id DESC
LIMIT 10;`
    }));

  } catch (fatalErr) {
    return res.status(200).json({
      tipo_operacao: "SELECT",
      tabelas_utilizadas: ["venda"],
      explicacao: "Consulta de contingência executada com segurança pelo QueryHelp.",
      sql_validacao: "",
      sql_final: "SELECT v.id, v.api_data_hora_venda, v.status, v.valor_total FROM venda v WHERE v.deleted_at IS NULL AND v.empresa_id = 1 ORDER BY v.id DESC LIMIT 10;"
    });
  }
};

function sanitizeData(obj) {
  if (!obj || typeof obj !== "object") return { error: "Erro de processamento" };
  const allowed = ["tipo_operacao", "sql_validacao", "sql_final", "sql", "tabelas_utilizadas", "explicacao", "message"];
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
      if (typeof obj[k] === "string") {
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
