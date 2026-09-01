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

export default async function handler(req, res) {
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

  const SYSTEM_PROMPT = `
Você é o Especialista Sênior em Engenharia de Dados e Estrutura de Banco de Dados do sistema comercial Softcomshop (MySQL 8.0).
Sistema e plataforma projetados por Jonatha Dantas (by Dantas).

DIRETRIZES DE PRIVACIDADE E SEGURANÇA:
- NUNCA retorne senhas, chaves de API, tokens de conexão ou credenciais internas.
- Gere consultas SQL MySQL precisas, limpas e seguras considerando deleted_at IS NULL e empresa_id = 1.
- Quando a operação for de alteração (UPDATE) ou exclusão (DELETE/cancelar/apagar), forneça SEMPRE:
  1. \`sql_validacao\`: Um SELECT de conferência prévia com os mesmos filtros.
  2. \`sql_final\`: O comando definitivo envolvido em START TRANSACTION e COMMIT.

Para consultas normais de leitura (SELECT), deixe \`sql_validacao\` vazio "" e coloque o SQL em \`sql_final\`.

Responda OBRIGATORIAMENTE em JSON:
{
  "tipo_operacao": "SELECT" | "UPDATE" | "DELETE",
  "sql_validacao": "SELECT ... (se for alteração/exclusão)",
  "sql_final": "comando SQL definitivo",
  "tabelas_utilizadas": ["lista", "de", "tabelas"],
  "explicacao": "explicação concisa, natural e humana em português"
}
`;

  if (activeKey) {
    try {
      const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${encodeURIComponent(activeKey)}`;
      const payload = {
        system_instruction: { parts: [{ text: SYSTEM_PROMPT }] },
        contents: [{ parts: [{ text: `Gere a consulta SQL para: ${message}` }] }],
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
      // Falha isolada no servidor sem vazar detalhes para a resposta
      console.error('Fallback ativado.');
    }
  }

  // Motor Estrutural Local com Inteligência Semântica
  const p = message.toLowerCase();
  const isDelete = ["delet", "exclu", "apag", "remov", "drop", "limp"].some(k => p.includes(k));
  const isUpdate = ["updat", "atualiz", "alter", "modific", "cancel", "inativ", "bloque", "ajust", "troc", "mud"].some(k => p.includes(k));

  if (isDelete && (p.includes('venda') || p.includes('pedido'))) {
    return res.status(200).json(sanitizeData({
      tipo_operacao: "DELETE",
      sql_validacao: `-- 1. Consulta de Validação (Execute para conferir os registros antes de deletar)
SELECT id AS venda_id, status, valor_total, total_pagamento, cliente_id, nfe_id, api_data_hora_venda, deleted_at
FROM venda
WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;`,
      sql_final: `-- 2. Comando de Exclusão (Soft Delete com Transação)
START TRANSACTION;
UPDATE venda SET deleted_at = NOW(), status = 'CANCELADA', updated_at = NOW() WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;
COMMIT;`,
      tabelas_utilizadas: ['venda', 'venda_item', 'financeiro_parcela'],
      explicacao: 'Utilize a aba Validação para conferir a venda antes de aplicar o Soft Delete dentro da transação segura.'
    }));
  }

  // Resposta inteligente para Marketplace / Integrações / Canais
  if (p.includes('market') || p.includes('ifood') || p.includes('delivery') || p.includes('integrac') || p.includes('ecom')) {
    return res.status(200).json(sanitizeData({
      tipo_operacao: "SELECT",
      sql_validacao: "",
      sql_final: `-- Consulta Analítica Completa de Integração com Marketplaces
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
      explicacao: 'Identificamos todas as tabelas oficiais do módulo de Marketplace no schema: `marketplace_pedido`, `marketplace_vinculado`, `marketplace_config`, `marketplace_produto`, `marketplace_categoria` e os vínculos diretos na tabela `venda` (`api_app_name`, `marketplace_pedido_id`, `origem_venda`). A consulta acima cruza os pedidos de venda com os registros de integração externa.'
    }));
  }

  // Resposta para Contingência SEFAZ
  if (p.includes('conting') || p.includes('rejei') || (p.includes('erro') && p.includes('nota'))) {
    return res.status(200).json(sanitizeData({
      tipo_operacao: "SELECT",
      sql_validacao: "",
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
      explicacao: 'Consulta com cruzamento analítico entre vendas e documentos em contingência com cálculo de diferenças.'
    }));
  }

  return res.status(200).json(sanitizeData({
    tipo_operacao: "SELECT",
    sql_validacao: "",
    sql_final: `SELECT v.id AS venda_id, v.api_data_hora_venda AS data_venda, v.status, v.valor_total, v.total_pagamento
FROM venda v
WHERE v.deleted_at IS NULL AND v.empresa_id = 1
ORDER BY v.id DESC
LIMIT 10;`,
    tabelas_utilizadas: ['venda'],
    explicacao: 'Consulta base com as últimas vendas registradas aplicando filtros recomendados de empresa e exclusão lógica.'
  }));
}

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
