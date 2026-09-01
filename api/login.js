// Vercel Serverless Function: /api/login.js
// Desenvolvido por Jonatha Dantas (by Dantas)
// Autenticação Segura com Tokens Assinados HMAC-SHA256 (Stateless & Serverless-Ready)

const crypto = require('crypto');

const AUTH_USERS = ['especialistas', 'especialista', 'admin'];
const AUTH_PASS = '7711';
const JWT_SECRET = process.env.JWT_SECRET || 'QueryHelp-Secure-Key-by-Jonatha-Dantas-2026';

const loginAttempts = new Map();

function getClientIP(req) {
  const forwarded = req.headers ? req.headers['x-forwarded-for'] : null;
  if (forwarded) return forwarded.split(',')[0].trim();
  return (req.headers && req.headers['x-real-ip']) || (req.socket && req.socket.remoteAddress) || '127.0.0.1';
}

function checkRateLimit(ip) {
  const now = Date.now();
  let data = loginAttempts.get(ip) || { count: 0, lockedUntil: 0 };
  
  if (now < data.lockedUntil) {
    const remaining = Math.ceil((data.lockedUntil - now) / 1000);
    return { allowed: false, remaining };
  }

  return { allowed: true };
}

function recordAttempt(ip, success) {
  const now = Date.now();
  if (success) {
    loginAttempts.delete(ip);
    return;
  }
  let data = loginAttempts.get(ip) || { count: 0, lockedUntil: 0 };
  data.count += 1;
  if (data.count >= 5) {
    data.lockedUntil = now + (15 * 60 * 1000);
  }
  loginAttempts.set(ip, data);
}

function generateSignedToken(username) {
  const payload = JSON.stringify({
    user: username,
    exp: Date.now() + (24 * 60 * 60 * 1000)
  });
  const b64Payload = Buffer.from(payload).toString('base64url');
  const signature = crypto.createHmac('sha256', JWT_SECRET).update(b64Payload).digest('base64url');
  return `${b64Payload}.${signature}`;
}

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const clientIP = getClientIP(req);
    const rateCheck = checkRateLimit(clientIP);

    if (!rateCheck.allowed) {
      res.setHeader('Retry-After', String(rateCheck.remaining));
      return res.status(429).json({ 
        error: `Muitas tentativas incorretas. IP bloqueado temporariamente por ${Math.ceil(rateCheck.remaining / 60)} minuto(s).` 
      });
    }

    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (e) { body = {}; }
    } else if (!body) {
      body = {};
    }

    const u = String(body.username || '').replace(/\0/g, '').trim().toLowerCase();
    const p = String(body.password || '').replace(/\0/g, '').trim();

    const isUserValid = AUTH_USERS.includes(u);
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
      recordAttempt(clientIP, true);
      const token = generateSignedToken(u);
      return res.status(200).json({
        success: true,
        token: token,
        user: u
      });
    } else {
      recordAttempt(clientIP, false);
      return res.status(401).json({
        error: 'Credenciais incorretas. Usuário especialista e senha 7711.'
      });
    }
  } catch (err) {
    return res.status(500).json({ error: 'Erro interno no servidor de autenticação.' });
  }
};
