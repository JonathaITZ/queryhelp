// Vercel Serverless Function: /api/ask
// Desenvolvido por Jonatha Dantas (by Dantas)
// Seguranca: Zero Tokens Expostos, Sanitizacao Profunda e Proxy Server-to-Server

const https = require('https');

const apiRateLimits = new Map();

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

function callGemini(message, apiKey) {
  return new Promise((resolve) => {
    try {
      const systemPrompt = "Voce e o Especialista Senior em Engenharia de Dados do Softcomshop (MySQL 8.0). Responda estritamente em JSON no formato: {\"tipo_operacao\": \"SELECT\"|\"UPDATE\"|\"DELETE\", \"sql_validacao\": \"...\", \"sql_final\": \"...\", \"tabelas_utilizadas\": [...], \"explicacao\": \"...\"}";
      const postData = JSON.stringify({
        system_instruction: { parts: [{ text: systemPrompt }] },
        contents: [{ parts: [{ text: "Gere a consulta SQL para: " + message }] }],
        generationConfig: { temperature: 0.1, response_mime_type: "application/json" }
      });

      const options = {
        hostname: "generativelanguage.googleapis.com",
        path: "/v1beta/models/gemini-1.5-flash:generateContent?key=" + encodeURIComponent(apiKey),
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Content-Length": Buffer.byteLength(postData)
        },
        timeout: 8000
      };

      const req = https.request(options, (res) => {
        let body = "";
        res.on("data", (d) => { body += d; });
        res.on("end", () => {
          try {
            const data = JSON.parse(body);
            if (data.candidates && data.candidates[0] && data.candidates[0].content && data.candidates[0].content.parts && data.candidates[0].content.parts[0]) {
              const parsed = JSON.parse(data.candidates[0].content.parts[0].text);
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
    const forwarded = req.headers ? req.headers["x-forwarded-for"] : null;
    const clientIP = forwarded ? forwarded.split(",")[0].trim() : ((req.headers && req.headers["x-real-ip"]) || (req.socket && req.socket.remoteAddress) || "127.0.0.1");

    if (!checkRateLimit(clientIP)) {
      res.setHeader("Retry-After", "60");
      return res.status(429).json({ error: "Muitas requisicoes. Aguarde 1 minuto." });
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

    if (activeKey) {
      const geminiRes = await callGemini(message, activeKey);
      if (geminiRes && (geminiRes.sql_final || geminiRes.sql)) {
        return res.status(200).json(sanitizeData(geminiRes));
      }
    }

    const p = message.toLowerCase();
    const isUpdate = p.includes("update") || p.includes("alterar") || p.includes("atualizar") || p.includes("mudar") || p.includes("modificar");
    const isDelete = p.includes("delete") || p.includes("excluir") || p.includes("apagar") || p.includes("cancelar") || p.includes("remover");

    // 1. ALTERAR PRECO OU ESTOQUE
    if (isUpdate && (p.includes("produt") || p.includes("preco") || p.includes("estoqu") || p.includes("grade") || p.includes("valor"))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "UPDATE",
        sql_validacao: "-- 1. Consulta de Validacao (Conferencia do Produto, Preco e Estoque Atual)\nSELECT \n    p.id AS produto_id,\n    p.nome AS produto_nome,\n    p.referencia,\n    peg.id AS grade_id,\n    peg.codigo_barra,\n    peg.descricao AS variacao_grade,\n    peg.preco_venda AS preco_atual,\n    peg.estoque AS estoque_atual,\n    peg.updated_at AS ultima_atualizacao\nFROM produto p\nINNER JOIN produto_empresa pe ON pe.produto_id = p.id\nINNER JOIN produto_empresa_grade peg ON peg.produto_empresa_id = pe.id\nWHERE (p.id = 10 OR p.codigo_barras = '7891234567890' OR p.nome LIKE '%NOME_PRODUTO%')\n  AND pe.empresa_id = 1\n  AND p.deleted_at IS NULL;",
        sql_final: "-- 2. Atualizacao Segura de Preco e/ou Saldo de Estoque (com Transacao)\nSTART TRANSACTION;\n\nUPDATE produto_empresa_grade peg\nINNER JOIN produto_empresa pe ON peg.produto_empresa_id = pe.id\nSET peg.preco_venda = 29.90,\n    peg.estoque = 150.00,\n    peg.updated_at = NOW()\nWHERE pe.produto_id = 10\n  AND pe.empresa_id = 1\n  AND peg.deleted_at IS NULL;\n\nCOMMIT;",
        tabelas_utilizadas: ["produto", "produto_empresa", "produto_empresa_grade"],
        explicacao: "No Softcomshop, os precos e saldos de estoque sao vinculados por filial na tabela produto_empresa_grade relacionada a produto_empresa e produto."
      }));
    }

    // 2. DELETE DE VENDAS
    if (isDelete && (p.includes("venda") || p.includes("pedido"))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "DELETE",
        sql_validacao: "-- 1. Consulta de Validacao\nSELECT id AS venda_id, status, valor_total, total_pagamento, cliente_id, nfe_id, api_data_hora_venda, deleted_at\nFROM venda\nWHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;",
        sql_final: "-- 2. Comando de Exclusao (Soft Delete com Transacao)\nSTART TRANSACTION;\nUPDATE venda SET deleted_at = NOW(), status = 'CANCELADA', updated_at = NOW() WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;\nCOMMIT;",
        tabelas_utilizadas: ["venda", "venda_item", "financeiro_parcela"],
        explicacao: "Utilize a aba Validacao para conferir a venda antes de aplicar o Soft Delete dentro da transacao segura."
      }));
    }

    // 3. FATURAMENTO POR FORMA DE PAGAMENTO
    if (p.includes("fatur") || p.includes("pagament") || p.includes("forma_pagamento") || p.includes("cartao") || p.includes("cartao") || p.includes("pix") || p.includes("dinheiro") || p.includes("recebimento")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Relatorio de Faturamento Agrupado por Forma de Pagamento\nSELECT \n    fp.descricao AS forma_pagamento,\n    COUNT(DISTINCT v.id) AS quantidade_vendas,\n    SUM(fp_parc.valor_parcela) AS total_faturado,\n    SUM(v.total_desconto) AS total_descontos,\n    ROUND(AVG(v.valor_total), 2) AS ticket_medio\nFROM venda v\nINNER JOIN financeiro_parcela fp_parc ON fp_parc.venda_id = v.id AND fp_parc.deleted_at IS NULL\nINNER JOIN forma_pagamento fp ON fp_parc.forma_pagamento_id = fp.id\nWHERE v.deleted_at IS NULL \n  AND v.empresa_id = 1\n  AND v.status = 'FINALIZADA'\nGROUP BY fp.id, fp.descricao\nORDER BY total_faturado DESC;",
        tabelas_utilizadas: ["venda", "financeiro_parcela", "forma_pagamento"],
        explicacao: "Relatorio consolidado de faturamento agrupado por forma de pagamento (PIX, Cartoes, Dinheiro, Boleto), calculando total faturado, quantidade de vendas e ticket medio com filtros padrao do Softcomshop."
      }));
    }

    // 4. CONTAS A RECEBER
    if (p.includes("receber") || p.includes("inadimpl") || p.includes("cobranc") || p.includes("duplicata")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Relatorio de Contas a Receber / Inadimplencia\nSELECT \n    c.id AS cliente_id,\n    c.nome_razao_social AS cliente_nome,\n    c.cpf_cnpj,\n    c.telefone,\n    cr.id AS titulo_id,\n    cr.numero_documento,\n    cr.valor_documento,\n    cr.data_vencimento,\n    DATEDIFF(CURRENT_DATE, cr.data_vencimento) AS dias_atraso,\n    cr.status\nFROM contas_receber cr\nINNER JOIN cliente c ON cr.cliente_id = c.id\nWHERE cr.deleted_at IS NULL \n  AND cr.empresa_id = 1\n  AND cr.status = 'ABERTO'\nORDER BY cr.data_vencimento ASC;",
        tabelas_utilizadas: ["contas_receber", "cliente"],
        explicacao: "Consulta analitica de titulos a receber com status em aberto, calculando dias de atraso e dados do cliente para cobranca."
      }));
    }

    // 5. CONTAS A PAGAR
    if (p.includes("pagar") || p.includes("fornecedor") || p.includes("despesa")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Relatorio de Contas a Pagar por Fornecedor\nSELECT \n    f.id AS fornecedor_id,\n    f.razao_social AS fornecedor,\n    f.cnpj_cpf,\n    cp.id AS titulo_id,\n    cp.numero_documento,\n    cp.valor_documento,\n    cp.data_vencimento,\n    cp.status\nFROM contas_pagar cp\nINNER JOIN fornecedor f ON cp.fornecedor_id = f.id\nWHERE cp.deleted_at IS NULL \n  AND cp.empresa_id = 1\nORDER BY cp.data_vencimento ASC;",
        tabelas_utilizadas: ["contas_pagar", "fornecedor"],
        explicacao: "Consulta analitica de obrigacoes financeiras a pagar vinculadas aos seus respectivos fornecedores com data de vencimento e status."
      }));
    }

    // 6. ESTOQUE CRITICO
    if (p.includes("ruptura") || p.includes("minimo") || (p.includes("estoqu") && (p.includes("baixo") || p.includes("falta") || p.includes("critico") || p.includes("zerad")))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Relatorio de Produtos com Estoque Abaixo do Minimo (Ruptura)\nSELECT \n    p.id AS produto_id,\n    p.nome AS produto_nome,\n    p.referencia,\n    peg.codigo_barra,\n    peg.estoque AS estoque_atual,\n    peg.estoque_minimo,\n    ROUND(peg.estoque_minimo - peg.estoque, 2) AS quantidade_repor,\n    peg.preco_venda,\n    f.razao_social AS fornecedor_padrao\nFROM produto p\nINNER JOIN produto_empresa pe ON pe.produto_id = p.id\nINNER JOIN produto_empresa_grade peg ON peg.produto_empresa_id = pe.id\nLEFT JOIN fornecedor f ON p.fornecedor_id = f.id\nWHERE pe.empresa_id = 1\n  AND peg.estoque <= peg.estoque_minimo\n  AND peg.deleted_at IS NULL\n  AND p.deleted_at IS NULL\nORDER BY (peg.estoque_minimo - peg.estoque) DESC;",
        tabelas_utilizadas: ["produto", "produto_empresa", "produto_empresa_grade", "fornecedor"],
        explicacao: "Identificacao de itens em ruptura ou estoque critico por filial (produto_empresa_grade), calculando a sugestao de compra para reposicao."
      }));
    }

    // 7. CURVA ABC
    if (p.includes("abc") || p.includes("mais vendid") || p.includes("ranking") || p.includes("top produt") || p.includes("campeoes")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Relatorio de Ranking / Curva ABC de Produtos Mais Vendidos\nSELECT \n    p.id AS produto_id,\n    p.nome AS produto_nome,\n    p.referencia,\n    SUM(vi.quantidade) AS total_quantidade_vendida,\n    SUM(vi.valor_total) AS faturamento_total_bruto,\n    SUM(vi.total_desconto) AS total_descontos,\n    ROUND(SUM(vi.valor_total) - SUM(vi.total_desconto), 2) AS faturamento_liquido\nFROM venda_item vi\nINNER JOIN venda v ON vi.venda_id = v.id\nINNER JOIN produto p ON vi.produto_id = p.id\nWHERE v.deleted_at IS NULL \n  AND v.status = 'FINALIZADA'\n  AND v.empresa_id = 1\nGROUP BY p.id, p.nome, p.referencia\nORDER BY faturamento_liquido DESC\nLIMIT 20;",
        tabelas_utilizadas: ["venda", "venda_item", "produto"],
        explicacao: "Ranking dos 20 produtos de maior faturamento liquido e volume de vendas, com base no historico de vendas finalizadas do sistema."
      }));
    }

    // 8. CLIENTES
    if (p.includes("client") || p.includes("limite") || p.includes("bloqueio") || p.includes("crediario")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Relatorio Geral de Clientes, Limites e Status\nSELECT \n    c.id AS cliente_id,\n    c.nome_razao_social AS cliente_nome,\n    c.cpf_cnpj,\n    c.telefone,\n    c.email,\n    c.limite_credito,\n    c.bloqueado,\n    c.motivo_bloqueio,\n    c.created_at AS data_cadastro\nFROM cliente c\nWHERE c.deleted_at IS NULL \n  AND c.empresa_id = 1\nORDER BY c.nome_razao_social ASC\nLIMIT 50;",
        tabelas_utilizadas: ["cliente"],
        explicacao: "Consulta de base de clientes cadastrados, limites de credito disponiveis e status de bloqueio comercial."
      }));
    }

    // 9. NFSE
    if (p.includes("nfse") || p.includes("nfs-e") || p.includes("servico") || p.includes("rps") || p.includes("issqn") || p.includes("tomador")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Consulta Analitica Completa de NFSe (Nota Fiscal de Servicos Eletronica)\nSELECT \n    nfse.id AS nfse_id,\n    nfse.numero_rps,\n    nfse.status_rps,\n    nfse.data_emissao,\n    nfse.total_valor_servico,\n    nfse.aliquota_iss,\n    nfse.iss_retido,\n    tomador.tomador_razao_social,\n    tomador.tomador_cnpj_cpf,\n    item.discriminacao_servico,\n    item.valor_servico\nFROM nota_fiscal_servico_eletronica nfse\nLEFT JOIN nota_fiscal_servico_eletronica_tomador tomador ON tomador.nfse_id = nfse.id\nLEFT JOIN nota_fiscal_servico_eletronica_item item ON item.nfse_id = nfse.id\nWHERE nfse.deleted_at IS NULL \n  AND nfse.empresa_id = 1\nORDER BY nfse.id DESC\nLIMIT 50;",
        tabelas_utilizadas: [
          "nota_fiscal_servico_eletronica",
          "nota_fiscal_servico_eletronica_item",
          "nota_fiscal_servico_eletronica_tomador"
        ],
        explicacao: "Identificamos todas as tabelas oficiais do modulo de NFSe no schema: nota_fiscal_servico_eletronica, nota_fiscal_servico_eletronica_item e tomador."
      }));
    }

    // 10. MARKETPLACE
    if (p.includes("market") || p.includes("ifood") || p.includes("delivery") || p.includes("integrac") || p.includes("ecom")) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "-- Consulta Analitica Completa de Integracao com Marketplaces\nSELECT \n    v.id AS venda_id,\n    v.api_data_hora_venda AS data_venda,\n    v.origem_venda,\n    v.api_app_name AS canal_marketplace,\n    v.marketplace_pedido_id AS pedido_externo_id,\n    v.valor_total AS valor_total_venda,\n    v.status AS status_venda,\n    mv.marketplace_name,\n    mp.status AS status_marketplace_pedido,\n    mp.valor_total AS valor_pedido_marketplace\nFROM venda v\nLEFT JOIN marketplace_pedido mp ON v.marketplace_pedido_id = mp.id\nLEFT JOIN marketplace_vinculado mv ON mp.marketplace_id = mv.marketplace_id\nWHERE v.deleted_at IS NULL \n  AND v.empresa_id = 1\n  AND (v.origem_venda LIKE '%MARKETPLACE%' OR v.marketplace_pedido_id IS NOT NULL OR v.api_app_name IS NOT NULL)\nORDER BY v.id DESC\nLIMIT 50;",
        tabelas_utilizadas: ["venda", "marketplace_pedido", "marketplace_vinculado", "marketplace_config", "produto_marketplace"],
        explicacao: "Identificamos todas as tabelas oficiais do modulo de Marketplace no schema: marketplace_pedido, marketplace_vinculado e os vinculos diretos na tabela venda."
      }));
    }

    // 11. CONTINGENCIA
    if (p.includes("conting") || p.includes("rejei") || (p.includes("erro") && p.includes("nota"))) {
      return res.status(200).json(sanitizeData({
        tipo_operacao: "SELECT",
        sql_validacao: "",
        sql_final: "SELECT \n    v.id AS venda_id,\n    v.valor_total AS total_venda,\n    v.total_pagamento AS total_pago_venda,\n    COALESCE(SUM(fp.valor_parcela), 0) AS total_parcelas,\n    ROUND(v.valor_total - COALESCE(SUM(fp.valor_parcela), 0), 4) AS diferenca_parcelas,\n    nfe.id AS nfe_id,\n    nfe.numero_nfe,\n    nfe.recibo_situacao,\n    nfe.mensagem_erro\nFROM venda v\nINNER JOIN nota_fiscal_eletronica nfe ON v.nfe_id = nfe.id\nLEFT JOIN financeiro_parcela fp ON fp.venda_id = v.id AND fp.deleted_at IS NULL\nWHERE nfe.recibo_situacao = 'CONTINGENCIA'\nGROUP BY v.id, v.valor_total, v.total_pagamento, nfe.id, nfe.numero_nfe, nfe.recibo_situacao, nfe.mensagem_erro\nORDER BY v.id DESC;",
        tabelas_utilizadas: ["venda", "nota_fiscal_eletronica", "financeiro_parcela"],
        explicacao: "Consulta com cruzamento analitico entre vendas e documentos em contingencia com calculo de diferencas."
      }));
    }

    // Resposta padrao
    return res.status(200).json(sanitizeData({
      tipo_operacao: "SELECT",
      sql_validacao: "",
      sql_final: "SELECT \n    v.id AS venda_id, \n    v.api_data_hora_venda AS data_venda, \n    v.status, \n    v.valor_total, \n    v.total_desconto,\n    v.total_pagamento\nFROM venda v\nWHERE v.deleted_at IS NULL AND v.empresa_id = 1\nORDER BY v.id DESC\nLIMIT 10;",
      tabelas_utilizadas: ["venda"],
      explicacao: "Consulta base com as ultimas vendas registradas aplicando filtros recomendados de empresa e exclusao logica."
    }));
  } catch (fatalErr) {
    return res.status(200).json({
      tipo_operacao: "SELECT",
      sql_validacao: "",
      sql_final: "SELECT v.id, v.api_data_hora_venda, v.status, v.valor_total FROM venda v WHERE v.deleted_at IS NULL AND v.empresa_id = 1 ORDER BY v.id DESC LIMIT 10;",
      tabelas_utilizadas: ["venda"],
      explicacao: "Consulta de contingencia executada com seguranca."
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
