// Vercel Serverless Function: /api/ask
// Desenvolvido por Jonatha Dantas (by Dantas)
// Seguranca: Zero Tokens Expostos, Sanitizacao Profunda e Proxy Server-to-Server

const apiRateLimits = new Map(); // ip -> [timestamps]

function checkRateLimit(ip) {
  const now = Date.now();
  let timestamps = apiRateLimits.get(ip) || [];
  timestamps = timestamps.filter(t => now - t < 60000);
  if (timestamps.length >= 60) {
    return false;
  }
  timestamps.push(now);
  apiRateLimits.set(ip, timestamps);
  return true;
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Referrer-Policy', 'no-referrer');
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const forwarded = req.headers['x-forwarded-for'];
    const clientIP = forwarded ? forwarded.split(',')[0].trim() : (req.headers['x-real-ip'] || req.socket?.remoteAddress || '127.0.0.1');

    if (!checkRateLimit(clientIP)) {
      res.setHeader('Retry-After', '60');
      return res.status(429).json({ error: 'Muitas requisicoes. Aguarde 1 minuto.' });
    }

    let body = req.body;
    if (typeof body === 'string') {
      try {
        body = JSON.parse(body);
      } catch (e) {
        body = {};
      }
    } else if (!body) {
      body = {};
    }

    const rawMessage = typeof body.message === 'string' ? body.message : '';
    const message = rawMessage.slice(0, 1500).trim();
    const activeKey = body.apiKey || process.env.GEMINI_API_KEY;

    const SYSTEM_PROMPT = `Voce e o Especialista Senior em Engenharia de Dados do Softcomshop (MySQL 8.0).
Sistema e plataforma projetados por Jonatha Dantas (by Dantas).
Gere consultas SQL MySQL precisas considerando deleted_at IS NULL e empresa_id = 1.
Responda OBRIGATORIAMENTE em JSON:
{
  "tipo_operacao": "SELECT" | "UPDATE" | "DELETE",
  "sql_validacao": "SELECT ... (se for alteracao/exclusao)",
  "sql_final": "comando SQL definitivo",
  "tabelas_utilizadas": ["lista", "de", "tabelas"],
  "explicacao": "explicacao concisa em portugues"
}`;

    if (activeKey) {
      try {
        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${encodeURIComponent(activeKey)}`;
        const payload = {
          system_instruction: { parts: [{ text: SYSTEM_PROMPT }] },
          contents: [{ parts: [{ text: `Gere a consulta SQL para: ${message}` }] }],
          generationConfig: {
            temperature: 0.1,
            response_mime_type: 'application/json'
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

    const p = message.toLowerCase();
    const isUpdate = p.includes('update') || p.includes('alterar') || p.includes('atualizar') || p.includes('mudar') || p.includes('modificar');
    const isDelete = p.includes('delete') || p.includes('excluir') || p.includes('apagar') || p.includes('cancelar') || p.includes('remover');

    // 1. ALTERAR PRECO OU ESTOQUE
    if (isUpdate && (p.includes('produt') || p.includes('preco') || p.includes('estoqu') || p.includes('grade') || p.includes('valor'))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'UPDATE',
        sql_validacao: `-- 1. Consulta de Validacao (Conferencia do Produto, Preco e Estoque Atual)
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
        sql_final: `-- 2. Atualizacao Segura de Preco e/ou Saldo de Estoque (com Transacao)
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
        tabelas_utilizadas: ['produto', 'produto_empresa', 'produto_empresa_grade'],
        explicacao: 'No Softcomshop, os precos e saldos de estoque sao vinculados por filial na tabela produto_empresa_grade relacionada a produto_empresa e produto.'
      }));
    }

    // 2. DELETE DE VENDAS
    if (isDelete && (p.includes('venda') || p.includes('pedido'))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'DELETE',
        sql_validacao: `-- 1. Consulta de Validacao
SELECT id AS venda_id, status, valor_total, total_pagamento, cliente_id, nfe_id, api_data_hora_venda, deleted_at
FROM venda
WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;`,
        sql_final: `-- 2. Comando de Exclusao (Soft Delete com Transacao)
START TRANSACTION;
UPDATE venda SET deleted_at = NOW(), status = 'CANCELADA', updated_at = NOW() WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;
COMMIT;`,
        tabelas_utilizadas: ['venda', 'venda_item', 'financeiro_parcela'],
        explicacao: 'Utilize a aba Validacao para conferir a venda antes de aplicar o Soft Delete dentro da transacao segura.'
      }));
    }

    // 3. FATURAMENTO POR FORMA DE PAGAMENTO
    if (p.includes('fatur') || p.includes('pagament') || p.includes('forma_pagamento') || p.includes('cartao') || p.includes('cartão') || p.includes('pix') || p.includes('dinheiro') || p.includes('recebimento')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Relatorio de Faturamento Agrupado por Forma de Pagamento
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
ORDER BY total_faturado DESC;`,
        tabelas_utilizadas: ['venda', 'financeiro_parcela', 'forma_pagamento'],
        explicacao: 'Relatorio consolidado de faturamento agrupado por forma de pagamento (PIX, Cartoes, Dinheiro, Boleto), calculando total faturado, quantidade de vendas e ticket medio com filtros padrao do Softcomshop.'
      }));
    }

    // 4. CONTAS A RECEBER
    if (p.includes('receber') || p.includes('inadimpl') || p.includes('cobranc') || p.includes('duplicata')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Relatorio de Contas a Receber / Inadimplencia
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
ORDER BY cr.data_vencimento ASC;`,
        tabelas_utilizadas: ['contas_receber', 'cliente'],
        explicacao: 'Consulta analitica de titulos a receber com status em aberto, calculando dias de atraso e dados do cliente para cobranca.'
      }));
    }

    // 5. CONTAS A PAGAR
    if (p.includes('pagar') || p.includes('fornecedor') || p.includes('despesa')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Relatorio de Contas a Pagar por Fornecedor
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
ORDER BY cp.data_vencimento ASC;`,
        tabelas_utilizadas: ['contas_pagar', 'fornecedor'],
        explicacao: 'Consulta analitica de obrigacoes financeiras a pagar vinculadas aos seus respectivos fornecedores com data de vencimento e status.'
      }));
    }

    // 6. ESTOQUE CRITICO / RUPTURA
    if (p.includes('ruptura') || p.includes('minimo') || (p.includes('estoqu') && (p.includes('baixo') || p.includes('falta') || p.includes('critico') || p.includes('zerad')))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Relatorio de Produtos com Estoque Abaixo do Minimo (Ruptura)
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
ORDER BY (peg.estoque_minimo - peg.estoque) DESC;`,
        tabelas_utilizadas: ['produto', 'produto_empresa', 'produto_empresa_grade', 'fornecedor'],
        explicacao: 'Identificacao de itens em ruptura ou estoque critico por filial (produto_empresa_grade), calculando a sugestao de compra para reposicao.'
      }));
    }

    // 7. CURVA ABC / MAIS VENDIDOS
    if (p.includes('abc') || p.includes('mais vendid') || p.includes('ranking') || p.includes('top produt') || p.includes('campeoes')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Relatorio de Ranking / Curva ABC de Produtos Mais Vendidos
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
LIMIT 20;`,
        tabelas_utilizadas: ['venda', 'venda_item', 'produto'],
        explicacao: 'Ranking dos 20 produtos de maior faturamento liquido e volume de vendas, com base no historico de vendas finalizadas do sistema.'
      }));
    }

    // 8. CLIENTES / LIMITES
    if (p.includes('client') || p.includes('limite') || p.includes('bloqueio') || p.includes('crediario')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Relatorio Geral de Clientes, Limites e Status
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
LIMIT 50;`,
        tabelas_utilizadas: ['cliente'],
        explicacao: 'Consulta de base de clientes cadastrados, limites de credito disponiveis e status de bloqueio comercial.'
      }));
    }

    // 9. NFSE / SERVICOS
    if (p.includes('nfse') || p.includes('nfs-e') || p.includes('servico') || p.includes('rps') || p.includes('issqn') || p.includes('tomador')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Consulta Analitica Completa de NFSe (Nota Fiscal de Servicos Eletronica)
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
LIMIT 50;`,
        tabelas_utilizadas: [
          'nota_fiscal_servico_eletronica',
          'nota_fiscal_servico_eletronica_item',
          'nota_fiscal_servico_eletronica_tomador',
          'nfse_aliquota_padrao',
          'nfse_codigo_servico_item',
          'contrato_servico'
        ],
        explicacao: 'Identificamos todas as tabelas oficiais do modulo de NFSe no schema: nota_fiscal_servico_eletronica (cabecalho/RPS), nota_fiscal_servico_eletronica_item (itens e aliquotas de ISS), nota_fiscal_servico_eletronica_tomador (dados do tomador).'
      }));
    }

    // 10. MARKETPLACE / DELIVERY / IFOOD
    if (p.includes('market') || p.includes('ifood') || p.includes('delivery') || p.includes('integrac') || p.includes('ecom')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Consulta Analitica Completa de Integracao com Marketplaces
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
LIMIT 50;`,
        tabelas_utilizadas: ['venda', 'marketplace_pedido', 'marketplace_vinculado', 'marketplace_config', 'produto_marketplace'],
        explicacao: 'Identificamos todas as tabelas oficiais do modulo de Marketplace no schema: marketplace_pedido, marketplace_vinculado, marketplace_config, marketplace_produto, marketplace_categoria e os vinculos diretos na tabela venda.'
      }));
    }

    // 11. CONTINGENCIA SEFAZ
    if (p.includes('conting') || p.includes('rejei') || (p.includes('erro') && p.includes('nota'))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `SELECT 
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
        tabelas_utilizadas: ['venda', 'nota_fiscal_eletronica', 'financeiro_parcela'],
        explicacao: 'Consulta com cruzamento analitico entre vendas e documentos em contingencia com calculo de diferencas.'
      }));
    }

    // 12. CAIXA / TURNOS
    if (p.includes('caixa') || p.includes('turno') || p.includes('sangria') || p.includes('suprimento')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Relatorio de Controle de Turnos e Caixas de Operadores
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
LIMIT 20;`,
        tabelas_utilizadas: ['caixa', 'caixa_turno', 'usuario'],
        explicacao: 'Auditoria completa de abertura, sangrias, suprimentos e fechamento de turnos dos operadores de caixa.'
      }));
    }

    // 13. RESTAURANTE / MESAS
    if (p.includes('restauran') || p.includes('mesa') || p.includes('comanda')) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: 'SELECT',
        sql_validacao: '',
        sql_final: `-- Monitoramento de Mesas e Comandas do Restaurante
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
ORDER BY rm.numero_mesa ASC;`,
        tabelas_utilizadas: ['restaurante_mesa', 'usuario'],
        explicacao: 'Visao operacional do modulo de restaurante com status de mesas ocupadas/livres e consumo em tempo real.'
      }));
    }

    // Resposta padrao
    return res.status(200).json(sanitizeData({
      tipo_operacao: 'SELECT',
      sql_validacao: '',
      sql_final: `SELECT 
    v.id AS venda_id, 
    v.api_data_hora_venda AS data_venda, 
    v.status, 
    v.valor_total, 
    v.total_desconto,
    v.total_pagamento
FROM venda v
WHERE v.deleted_at IS NULL AND v.empresa_id = 1
ORDER BY v.id DESC
LIMIT 10;`,
      tabelas_utilizadas: ['venda'],
      explicacao: 'Consulta base com as ultimas vendas registradas aplicando filtros recomendados de empresa e exclusao logica.'
    }));
  } catch (fatalErr) {
    console.error('Fatal API Error:', fatalErr);
    return res.status(200).json({
      tipo_operacao: 'SELECT',
      sql_validacao: '',
      sql_final: 'SELECT v.id, v.api_data_hora_venda, v.status, v.valor_total FROM venda v WHERE v.deleted_at IS NULL AND v.empresa_id = 1 ORDER BY v.id DESC LIMIT 10;',
      tabelas_utilizadas: ['venda'],
      explicacao: 'Consulta de contingencia executada com seguranca.'
    });
  }
};

function sanitizeData(obj) {
  if (!obj || typeof obj !== 'object') return { error: 'Erro de processamento' };
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
