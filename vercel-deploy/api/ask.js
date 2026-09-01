// Vercel Serverless Function: /api/ask
// Desenvolvido por Jonatha Dantas (by Dantas)
// Segurança: Zero Tokens Expostos, Sanitização Profunda e Proxy Server-to-Server

const apiRateLimits = new Map(); // ip -> [timestamps]

function checkRateLimit(ip) {
  const now = Date.now();
  let timestamps = apiRateLimits.get(ip) || [];
  timestamps = timestamps.filter(t => now - t < 60000);
  if (timestamps.length >= 30) {
    return false;
  }
  timestamps.push(now);
  apiRateLimits.set(ip, timestamps);
  return true;
}

module.exports = async function handler(req, res) {
  try {
    const forwarded = req.headers['x-forwarded-for'];
    const clientIP = forwarded ? forwarded.split(',')[0].trim() : (req.headers['x-real-ip'] || req.socket?.remoteAddress || '127.0.0.1');

    if (!checkRateLimit(clientIP)) {
      res.setHeader('Retry-After', '60');
      return res.status(429).json({ error: 'Muitas requisições. Aguarde 1 minuto.' });
    }

    // Headers Defensivos de Cyber Segurança (OWASP Standard)
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('X-Frame-Options', 'DENY');
    res.setHeader('Referrer-Policy', 'no-referrer');
    res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');

    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method Not Allowed' });
    }

    // Defesa de Tamanho de Entrada (Input Validation)
    const body = req.body || {};
    const rawMessage = typeof body.message === 'string' ? body.message : '';
    const message = rawMessage.slice(0, 1500).trim();
    const activeKey = body.apiKey || process.env.GEMINI_API_KEY;

    const SYSTEM_PROMPT = \
Você é o Especialista Sênior em Engenharia de Dados e Estrutura de Banco de Dados do sistema comercial Softcomshop (MySQL 8.0).
Sistema e plataforma projetados por Jonatha Dantas (by Dantas).

DIRETRIZES DE PRIVACIDADE E SEGURANÇA:
- NUNCA retorne senhas, chaves de API, tokens de conexão ou credenciais internas.
- Gere consultas SQL MySQL precisas, limpas e seguras considerando deleted_at IS NULL e empresa_id = 1.
- Quando a operação for de alteração (UPDATE) ou exclusão (DELETE/cancelar/apagar), forneça SEMPRE:
  1. \\\sql_validacao\\\: Um SELECT de conferência prévia com os mesmos filtros.
  2. \\\sql_final\\\: O comando definitivo envolvido em START TRANSACTION e COMMIT.

Para consultas normais de leitura (SELECT), deixe \\\sql_validacao\\\ vazio "" e coloque o SQL em \\\sql_final\\\.

Responda OBRIGATORIAMENTE em JSON:
{
  "tipo_operacao": "SELECT" | "UPDATE" | "DELETE",
  "sql_validacao": "SELECT ... (se for alteração/exclusão)",
  "sql_final": "comando SQL definitivo",
  "tabelas_utilizadas": ["lista", "de", "tabelas"],
  "explicacao": "explicação concisa, natural e humana em português"
}
\;

    if (activeKey) {
      try {
        const url = \https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=\\;
        const payload = {
          system_instruction: { parts: [{ text: SYSTEM_PROMPT }] },
          contents: [{ parts: [{ text: \Gere a consulta SQL para: \\ }] }],
          generationConfig: {
            temperature: 0.1,
            response_mime_type: "application/json"
          }
        };

        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        const resData = await response.json();
        if (resData.candidates && resData.candidates[0]?.content?.parts?.[0]?.text) {
          const parsed = JSON.parse(resData.candidates[0].content.parts[0].text);
          return res.status(200).json(sanitizeData(parsed));
        }
      } catch (err) {
        console.error('Fallback Gemini ativado:', err);
      }
    }

    // --- MOTOR SEMÂNTICO DE REGRAS E FALLBACK LOCAL ---
    const p = message.toLowerCase();
    const isUpdate = p.includes('update') || p.includes('alterar') || p.includes('atualizar') || p.includes('mudar') || p.includes('modificar');
    const isDelete = p.includes('delete') || p.includes('excluir') || p.includes('apagar') || p.includes('cancelar') || p.includes('remover');

    // 1. ALTERAR PREÇO OU ESTOQUE DE PRODUTO (2 ETAPAS)
    if (isUpdate && (p.includes('produt') || p.includes('preco') || p.includes('preço') || p.includes('estoqu') || p.includes('grade') || p.includes('valor'))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "UPDATE",
        sql_validacao: \-- 1. Consulta de Validação (Conferência do Produto, Preço e Estoque Atual)
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
  AND p.deleted_at IS NULL;\,
        sql_final: \-- 2. Atualização Segura de Preço e/ou Saldo de Estoque (com Transação)
START TRANSACTION;

-- No Softcomshop, preço e saldo residem na tabela produto_empresa_grade
UPDATE produto_empresa_grade peg
INNER JOIN produto_empresa pe ON peg.produto_empresa_id = pe.id
SET peg.preco_venda = 29.90, -- Novo preço de venda
    peg.estoque = 150.00,    -- Novo saldo de estoque
    peg.updated_at = NOW()
WHERE pe.produto_id = 10     -- Informe o ID do produto
  AND pe.empresa_id = 1
  AND peg.deleted_at IS NULL;

COMMIT;\,
        tabelas_utilizadas: ['produto', 'produto_empresa', 'produto_empresa_grade'],
        explicacao: 'No Softcomshop, os preços e saldos de estoque são vinculados por filial na tabela \produto_empresa_grade\ relacionada a \produto_empresa\ e \produto\. Na aba 1. Validação, confira os valores atuais. Na aba 2. Execução, aplique a alteração dentro da transação.'
      }));
    }

    // 2. DELETE / EXCLUSÃO DE VENDAS (2 ETAPAS)
    if (isDelete && (p.includes('venda') || p.includes('pedido'))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "DELETE",
        sql_validacao: \-- 1. Consulta de Validação (Execute para conferir os registros antes de deletar)
SELECT id AS venda_id, status, valor_total, total_pagamento, cliente_id, nfe_id, api_data_hora_venda, deleted_at
FROM venda
WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;\,
        sql_final: \-- 2. Comando de Exclusão (Soft Delete com Transação)
START TRANSACTION;
UPDATE venda SET deleted_at = NOW(), status = 'CANCELADA', updated_at = NOW() WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;
COMMIT;\,
        tabelas_utilizadas: ['venda', 'venda_item', 'financeiro_parcela'],
        explicacao: 'Utilize a aba Validação para conferir a venda antes de aplicar o Soft Delete dentro da transação segura.'
      }));
    }

    // 3. FATURAMENTO POR FORMA DE PAGAMENTO (PIX, CARTÃO, DINHEIRO)
    if (p.includes('fatur') || p.includes('pagament') || p.includes('forma_pagamento') || p.includes('cartao') || p.includes('cartão') || p.includes('pix') || p.includes('dinheiro') || p.includes('recebimento')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Relatório de Faturamento Agrupado por Forma de Pagamento
SELECT 
    fp.descricao AS forma_pagamento,
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
GROUP BY fp.id, fp.descricao
ORDER BY total_faturado DESC;\,
        tabelas_utilizadas: ['venda', 'financeiro_parcela', 'forma_pagamento'],
        explicacao: 'Relatório consolidado de faturamento agrupado por forma de pagamento (PIX, Cartões, Dinheiro, Boleto), calculando total faturado, quantidade de vendas e ticket médio com filtros padrão do Softcomshop.'
      }));
    }

    // 4. CONTAS A RECEBER / INADIMPLÊNCIA
    if (p.includes('receber') || p.includes('inadimpl') || p.includes('cobranc') || p.includes('cobranç') || p.includes('duplicata')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Relatório de Contas a Receber / Inadimplência
SELECT 
    c.id AS cliente_id,
    c.nome_razao_social AS cliente_nome,
    c.cpf_cnpj,
    c.telefone,
    cr.id AS titulo_id,
    cr.numero_documento,
    cr.valor_documento,
    cr.data_vencimento,
    DATEDIFF(CURRENT_DATE, cr.data_vencimento) AS dias_atraso,
    cr.status
FROM contas_receber cr
INNER JOIN cliente c ON cr.cliente_id = c.id
WHERE cr.deleted_at IS NULL 
  AND cr.empresa_id = 1
  AND cr.status = 'ABERTO'
ORDER BY cr.data_vencimento ASC;\,
        tabelas_utilizadas: ['contas_receber', 'cliente'],
        explicacao: 'Consulta analítica de títulos a receber com status em aberto, calculando dias de atraso e dados do cliente para cobrança.'
      }));
    }

    // 5. CONTAS A PAGAR / FORNECEDORES
    if (p.includes('pagar') || p.includes('fornecedor') || p.includes('despesa')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Relatório de Contas a Pagar por Fornecedor
SELECT 
    f.id AS fornecedor_id,
    f.razao_social AS fornecedor,
    f.cnpj_cpf,
    cp.id AS titulo_id,
    cp.numero_documento,
    cp.valor_documento,
    cp.data_vencimento,
    cp.status
FROM contas_pagar cp
INNER JOIN fornecedor f ON cp.fornecedor_id = f.id
WHERE cp.deleted_at IS NULL 
  AND cp.empresa_id = 1
ORDER BY cp.data_vencimento ASC;\,
        tabelas_utilizadas: ['contas_pagar', 'fornecedor'],
        explicacao: 'Consulta analítica de obrigações financeiras a pagar vinculadas aos seus respectivos fornecedores com data de vencimento e status.'
      }));
    }

    // 6. ESTOQUE CRÍTICO / RUPTURA / ABAIXO DO MÍNIMO
    if (p.includes('ruptura') || p.includes('minimo') || p.includes('mínimo') || (p.includes('estoqu') && (p.includes('baixo') || p.includes('falta') || p.includes('critico') || p.includes('crítico') || p.includes('zerad')))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Relatório de Produtos com Estoque Abaixo do Mínimo (Ruptura)
SELECT 
    p.id AS produto_id,
    p.nome AS produto_nome,
    p.referencia,
    peg.codigo_barra,
    peg.estoque AS estoque_atual,
    peg.estoque_minimo,
    ROUND(peg.estoque_minimo - peg.estoque, 2) AS quantidade_repor,
    peg.preco_venda,
    f.razao_social AS fornecedor_padrao
FROM produto p
INNER JOIN produto_empresa pe ON pe.produto_id = p.id
INNER JOIN produto_empresa_grade peg ON peg.produto_empresa_id = pe.id
LEFT JOIN fornecedor f ON p.fornecedor_id = f.id
WHERE pe.empresa_id = 1
  AND peg.estoque <= peg.estoque_minimo
  AND peg.deleted_at IS NULL
  AND p.deleted_at IS NULL
ORDER BY (peg.estoque_minimo - peg.estoque) DESC;\,
        tabelas_utilizadas: ['produto', 'produto_empresa', 'produto_empresa_grade', 'fornecedor'],
        explicacao: 'Identificação de itens em ruptura ou estoque crítico por filial (\produto_empresa_grade\), calculando a sugestão de compra para reposição.'
      }));
    }

    // 7. CURVA ABC / PRODUTOS MAIS VENDIDOS / RANKING
    if (p.includes('abc') || p.includes('mais vendid') || p.includes('ranking') || p.includes('top produt') || p.includes('campeoes')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Relatório de Ranking / Curva ABC de Produtos Mais Vendidos
SELECT 
    p.id AS produto_id,
    p.nome AS produto_nome,
    p.referencia,
    SUM(vi.quantidade) AS total_quantidade_vendida,
    SUM(vi.valor_total) AS faturamento_total_bruto,
    SUM(vi.total_desconto) AS total_descontos,
    ROUND(SUM(vi.valor_total) - SUM(vi.total_desconto), 2) AS faturamento_liquido
FROM venda_item vi
INNER JOIN venda v ON vi.venda_id = v.id
INNER JOIN produto p ON vi.produto_id = p.id
WHERE v.deleted_at IS NULL 
  AND v.status = 'FINALIZADA'
  AND v.empresa_id = 1
GROUP BY p.id, p.nome, p.referencia
ORDER BY faturamento_liquido DESC
LIMIT 20;\,
        tabelas_utilizadas: ['venda', 'venda_item', 'produto'],
        explicacao: 'Ranking dos 20 produtos de maior faturamento líquido e volume de vendas, com base no histórico de vendas finalizadas do sistema.'
      }));
    }

    // 8. CLIENTES / LIMITES DE CRÉDITO
    if (p.includes('client') || p.includes('limite') || p.includes('bloqueio') || p.includes('crediario') || p.includes('crediário')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Relatório Geral de Clientes, Limites e Status
SELECT 
    c.id AS cliente_id,
    c.nome_razao_social AS cliente_nome,
    c.cpf_cnpj,
    c.telefone,
    c.email,
    c.limite_credito,
    c.bloqueado,
    c.motivo_bloqueio,
    c.created_at AS data_cadastro
FROM cliente c
WHERE c.deleted_at IS NULL 
  AND c.empresa_id = 1
ORDER BY c.nome_razao_social ASC
LIMIT 50;\,
        tabelas_utilizadas: ['cliente'],
        explicacao: 'Consulta de base de clientes cadastrados, limites de crédito disponíveis e status de bloqueio comercial.'
      }));
    }

    // 9. NFSE / NOTA FISCAL DE SERVIÇO / RPS / ISSQN
    if (p.includes('nfse') || p.includes('nfs-e') || p.includes('servico') || p.includes('serviço') || p.includes('rps') || p.includes('issqn') || p.includes('tomador')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Consulta Analítica Completa de NFSe (Nota Fiscal de Serviços Eletrônica)
SELECT 
    nfse.id AS nfse_id,
    nfse.numero_rps,
    nfse.status_rps,
    nfse.data_emissao,
    nfse.total_valor_servico,
    nfse.aliquota_iss,
    nfse.iss_retido,
    tomador.tomador_razao_social,
    tomador.tomador_cnpj_cpf,
    item.discriminacao_servico,
    item.valor_servico
FROM nota_fiscal_servico_eletronica nfse
LEFT JOIN nota_fiscal_servico_eletronica_tomador tomador ON tomador.nfse_id = nfse.id
LEFT JOIN nota_fiscal_servico_eletronica_item item ON item.nfse_id = nfse.id
WHERE nfse.deleted_at IS NULL 
  AND nfse.empresa_id = 1
ORDER BY nfse.id DESC
LIMIT 50;\,
        tabelas_utilizadas: [
          "nota_fiscal_servico_eletronica",
          "nota_fiscal_servico_eletronica_item",
          "nota_fiscal_servico_eletronica_tomador",
          "nfse_aliquota_padrao",
          "nfse_codigo_servico_item",
          "contrato_servico"
        ],
        explicacao: 'Identificamos todas as tabelas oficiais do módulo de NFSe no schema: \
ota_fiscal_servico_eletronica\ (cabeçalho/RPS), \
ota_fiscal_servico_eletronica_item\ (itens e alíquotas de ISS), \
ota_fiscal_servico_eletronica_tomador\ (dados do tomador), \
fse_aliquota_padrao\, \
fse_codigo_servico_item\, \
fse_serie\ e vínculos com \contrato_servico\.'
      }));
    }

    // 10. MARKETPLACE / INTEGRAÇÕES / IFOOD / DELIVERY
    if (p.includes('market') || p.includes('ifood') || p.includes('delivery') || p.includes('integrac') || p.includes('ecom')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Consulta Analítica Completa de Integração com Marketplaces
SELECT 
    v.id AS venda_id,
    v.api_data_hora_venda AS data_venda,
    v.origem_venda,
    v.api_app_name AS canal_marketplace,
    v.marketplace_pedido_id AS pedido_externo_id,
    v.valor_total AS valor_total_venda,
    v.status AS status_venda,
    mv.marketplace_name,
    mp.status AS status_marketplace_pedido,
    mp.valor_total AS valor_pedido_marketplace
FROM venda v
LEFT JOIN marketplace_pedido mp ON v.marketplace_pedido_id = mp.id
LEFT JOIN marketplace_vinculado mv ON mp.marketplace_id = mv.marketplace_id
WHERE v.deleted_at IS NULL 
  AND v.empresa_id = 1
  AND (v.origem_venda LIKE '%MARKETPLACE%' OR v.marketplace_pedido_id IS NOT NULL OR v.api_app_name IS NOT NULL)
ORDER BY v.id DESC
LIMIT 50;\,
        tabelas_utilizadas: ['venda', 'marketplace_pedido', 'marketplace_vinculado', 'marketplace_config', 'produto_marketplace'],
        explicacao: 'Identificamos todas as tabelas oficiais do módulo de Marketplace no schema: \marketplace_pedido\, \marketplace_vinculado\, \marketplace_config\, \marketplace_produto\, \marketplace_categoria\ e os vínculos diretos na tabela \enda\ (\pi_app_name\, \marketplace_pedido_id\, \origem_venda\). A consulta acima cruza os pedidos de venda com os registros de integração externa.'
      }));
    }

    // 11. CONTINGÊNCIA SEFAZ / NOTA FISCAL ELETRÔNICA
    if (p.includes('conting') || p.includes('rejei') || (p.includes('erro') && p.includes('nota'))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \SELECT 
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
ORDER BY v.id DESC;\,
        tabelas_utilizadas: ['venda', 'nota_fiscal_eletronica', 'financeiro_parcela'],
        explicacao: 'Consulta com cruzamento analítico entre vendas e documentos em contingência com cálculo de diferenças.'
      }));
    }

    // 12. CAIXA / TURNOS DE OPERADORES
    if (p.includes('caixa') || p.includes('turno') || p.includes('sangria') || p.includes('suprimento')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Relatório de Controle de Turnos e Caixas de Operadores
SELECT 
    c.id AS caixa_id,
    c.descricao AS nome_caixa,
    t.id AS turno_id,
    u.nome AS operador,
    t.data_abertura,
    t.saldo_inicial,
    t.data_fechamento,
    t.saldo_final,
    t.total_sangrias,
    t.total_suprimentos,
    t.status AS status_turno
FROM caixa_turno t
INNER JOIN caixa c ON t.caixa_id = c.id
INNER JOIN usuario u ON t.usuario_id = u.id
WHERE t.deleted_at IS NULL 
  AND c.empresa_id = 1
ORDER BY t.data_abertura DESC
LIMIT 20;\,
        tabelas_utilizadas: ['caixa', 'caixa_turno', 'usuario'],
        explicacao: 'Auditoria completa de abertura, sangrias, suprimentos e fechamento de turnos dos operadores de caixa.'
      }));
    }

    // 13. RESTAURANTE / MESAS
    if (p.includes('restauran') || p.includes('mesa') || p.includes('comanda')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: \-- Monitoramento de Mesas e Comandas do Restaurante
SELECT 
    rm.id AS mesa_id,
    rm.numero_mesa,
    rm.status AS status_mesa,
    rm.consumo_total,
    rm.data_abertura,
    rm.quantidade_pessoas,
    u.nome AS garcom_responsavel
FROM restaurante_mesa rm
LEFT JOIN usuario u ON rm.garcom_usuario_id = u.id
WHERE rm.deleted_at IS NULL 
  AND rm.empresa_id = 1
ORDER BY rm.numero_mesa ASC;\,
        tabelas_utilizadas: ['restaurante_mesa', 'usuario'],
        explicacao: 'Visão operacional do módulo de restaurante com status de mesas ocupadas/livres e consumo em tempo real.'
      }));
    }

    // Resposta padrão analítica de vendas
    return res.status(200).json(sanitizeData({
      tipo_operacao: "SELECT",
      sql_validacao: "",
      sql_final: \SELECT 
    v.id AS venda_id, 
    v.api_data_hora_venda AS data_venda, 
    v.status, 
    v.valor_total, 
    v.total_desconto,
    v.total_pagamento
FROM venda v
WHERE v.deleted_at IS NULL AND v.empresa_id = 1
ORDER BY v.id DESC
LIMIT 10;\,
      tabelas_utilizadas: ['venda'],
      explicacao: 'Consulta base com as últimas vendas registradas aplicando filtros recomendados de empresa e exclusão lógica.'
    }));
  } catch (fatalErr) {
    console.error('Fatal API Error:', fatalErr);
    return res.status(200).json({
      tipo_operacao: "SELECT",
      sql_validacao: "",
      sql_final: \SELECT v.id, v.api_data_hora_venda, v.status, v.valor_total FROM venda v WHERE v.deleted_at IS NULL AND v.empresa_id = 1 ORDER BY v.id DESC LIMIT 10;\,
      tabelas_utilizadas: ["venda"],
      explicacao: "Consulta de contingência executada com segurança."
    });
  }
};

function sanitizeData(obj) {
  if (!obj || typeof obj !== 'object') return { error: "Erro de processamento" };
  const allowed = ['tipo_operacao', 'sql_validacao', 'sql_final', 'sql', 'tabelas_utilizadas', 'explicacao', 'message'];
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
      if (typeof obj[k] === 'string') {
        let val = obj[k];
        for (const pat of secretPatterns) {
          val = val.replace(pat, '[PROTEGIDO]');
        }
        clean[k] = val;
      } else {
        clean[k] = obj[k];
      }
    }
  }
  return clean;
}
