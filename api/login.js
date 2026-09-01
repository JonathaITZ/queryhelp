// Vercel Serverless Function: /api/login
// Desenvolvido por Jonatha Dantas (by Dantas)
// Seguranca: Anti-Brute Force por IP, Lockout de 15 Minutos e Rate Limiting

const crypto = require('crypto');

const AUTH_USER = 'especialista';
const AUTH_PASS = '7711';

// Cache em memoria para instancias serverless
const failedAttempts = new Map(); // ip -> [timestamps]
const lockedIPs = new Map();      // ip -> unlock_timestamp

const MAX_ATTEMPTS = 5;
const WINDOW_MS = 5 * 60 * 1000;   // 5 minutos
const LOCKOUT_MS = 15 * 60 * 1000; // 15 minutos

function getClientIP(req) {
  if (!req || !req.headers) return '127.0.0.1';
  const forwarded = req.headers['x-forwarded-for'];
  if (forwarded) {
    return forwarded.split(',')[0].trim();
  }
  return req.headers['x-real-ip'] || (req.socket && req.socket.remoteAddress) || '127.0.0.1';
}

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Referrer-Policy', 'no-referrer');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const clientIP = getClientIP(req);
    const now = Date.now();

    // 1. Verificar se o IP esta bloqueado
    if (lockedIPs.has(clientIP)) {
      const unlockTime = lockedIPs.get(clientIP);
      if (now < unlockTime) {
        const remainingSec = Math.ceil((unlockTime - now) / 1000);
        res.setHeader('Retry-After', String(remainingSec));
        return res.status(429).json({
          error: 'Muitas tentativas incorretas. Acesso bloqueado temporariamente. Tente novamente em ' + Math.ceil(remainingSec / 60) + ' min.'
        });
      } else {
        lockedIPs.delete(clientIP);
        failedAttempts.delete(clientIP);
      }
    }

    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch(e) { body = {}; }
    } else if (!body) {
      body = {};
    }

    const u = String(body.username || '').replace(/\0/g, '').trim().toLowerCase();
    const p = String(body.password || '').replace(/\0/g, '').trim();

    const isUserValid = ['especialistas', 'especialista', 'admin'].includes(u);
    
    // Comparacao em tempo constante (Timing-Safe)
    let isPassValid = false;
    try {
      const pBuf = Buffer.from(p);
      const authBuf = Buffer.from(AUTH_PASS);
      if (pBuf.length === authBuf.length) {
        isPassValid = crypto.timingSafeEqual(pBuf, authBuf);
      }
    } catch (e) {
      isPassValid = false;
    }

    if (isUserValid && isPassValid) {
      failedAttempts.delete(clientIP);
      lockedIPs.delete(clientIP);
      
      const token = crypto.randomBytes(24).toString('hex');
      return res.status(200).json({
        success: true,
        token: token,
        user: u
      });
    }

    // Falha: Registra tentativa
    let attempts = failedAttempts.get(clientIP) || [];
    attempts = attempts.filter(t => now - t < WINDOW_MS);
    attempts.push(now);
    failedAttempts.set(clientIP, attempts);

    if (attempts.length >= MAX_ATTEMPTS) {
      lockedIPs.set(clientIP, now + LOCKOUT_MS);
      res.setHeader('Retry-After', String(LOCKOUT_MS / 1000));
      return res.status(429).json({
        error: 'Limite de 5 tentativas excedido. IP bloqueado temporariamente por 15 minutos.'
      });
    }

    const remaining = MAX_ATTEMPTS - attempts.length;
    res.setHeader('X-RateLimit-Remaining', String(remaining));
    return res.status(401).json({
      error: 'Usuario ou senha incorretos. Tentativas restantes: ' + remaining + '.'
    });
  } catch(err) {
    return res.status(500).json({ error: 'Erro interno de autenticacao' });
  }
};
