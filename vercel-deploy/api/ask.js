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

  // Motor Estrutural Local Seguro
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
