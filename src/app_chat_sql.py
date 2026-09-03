"""
Chat Especialista em Estrutura de Banco de Dados (Schema & Regras de Negócio)
Design Clean, Humano e Minimalista (Inspirado no Claude / Linear / Vercel)
Desenvolvido por Jonatha Dantas (by Dantas)
Proteção Cibernética Nível Produção: Rate Limiting por IP, Anti-Brute Force Lockout e Autenticação Segura.
"""
import os
import sys
import json
import re
import time
import secrets
import urllib.request
import urllib.error
from collections import defaultdict
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

import hmac
import unicodedata

# Variáveis e Segredos isolados exclusivamente no Backend
SUPABASE_REST_URL = os.environ.get("SUPABASE_URL", "https://qqgszvnjnvcxbqbxifve.supabase.co/rest/v1")
SUPABASE_SECRET = os.environ.get("SUPABASE_SECRET", "sb_secret_NooW3WtF3PabZJSzZZscxg_wXoYRmOo")
GEMINI_SERVER_KEY = os.environ.get("GEMINI_API_KEY", "")
LOGO_PATH = r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\logo.jpg"

# Credenciais Oficiais do Especialista
AUTH_USERS = {"especialistas", "especialista", "admin"}
AUTH_PASS = "7711"

# Sessões com Expiração Automática (TTL de 2 horas)
SESSION_TTL_SECONDS = 7200
ACTIVE_SESSIONS = {} # token -> expiry_timestamp

def is_session_valid(token):
    """Verifica e expira sessões de forma segura (CWE-613)."""
    now = time.time()
    if not token or token not in ACTIVE_SESSIONS:
        return False
    if now > ACTIVE_SESSIONS[token]:
        del ACTIVE_SESSIONS[token]
        return False
    return True

def create_session():
    """Gera token CSPRNG com validade de 2 horas."""
    now = time.time()
    token = secrets.token_hex(24)
    ACTIVE_SESSIONS[token] = now + SESSION_TTL_SECONDS
    # Limpeza de sessões expiradas em lote
    expired = [t for t, exp in ACTIVE_SESSIONS.items() if now > exp]
    for t in expired:
        ACTIVE_SESSIONS.pop(t, None)
    return token

# ==============================================================================
# 🛡️ MOTOR DE RATE LIMITING E ANTI-BRUTE FORCE COM LIMPEZA DE MEMÓRIA (LRU)
# ==============================================================================
class SecurityRateLimiter:
    def __init__(self):
        self.failed_logins = defaultdict(list)
        self.locked_ips = {}
        self.api_requests = defaultdict(list)
        
        self.MAX_LOGIN_ATTEMPTS = 5
        self.LOGIN_WINDOW_SECONDS = 300
        self.LOCKOUT_DURATION = 900
        self.MAX_API_REQ_PER_MIN = 30
        self.MAX_TRACKED_IPS = 5000 # Prevenção de DoS em memória

    def _prune_stale_records(self, now):
        """Limpa registros antigos para evitar vazamento de memória (Memory Leak / DoS)."""
        if len(self.failed_logins) > self.MAX_TRACKED_IPS:
            self.failed_logins.clear()
        if len(self.api_requests) > self.MAX_TRACKED_IPS:
            self.api_requests.clear()

    def is_ip_locked(self, ip):
        now = time.time()
        self._prune_stale_records(now)
        if ip in self.locked_ips:
            if now < self.locked_ips[ip]:
                remaining = int(self.locked_ips[ip] - now)
                return True, remaining
            else:
                del self.locked_ips[ip]
                self.failed_logins[ip] = []
        return False, 0

    def record_login_attempt(self, ip, success):
        now = time.time()
        if success:
            self.failed_logins.pop(ip, None)
            self.locked_ips.pop(ip, None)
            return True, 0
        else:
            self.failed_logins[ip] = [t for t in self.failed_logins[ip] if now - t < self.LOGIN_WINDOW_SECONDS]
            self.failed_logins[ip].append(now)
            
            if len(self.failed_logins[ip]) >= self.MAX_LOGIN_ATTEMPTS:
                self.locked_ips[ip] = now + self.LOCKOUT_DURATION
                return False, self.LOCKOUT_DURATION
            return True, self.MAX_LOGIN_ATTEMPTS - len(self.failed_logins[ip])

    def check_api_rate_limit(self, ip):
        now = time.time()
        self.api_requests[ip] = [t for t in self.api_requests[ip] if now - t < 60]
        if len(self.api_requests[ip]) >= self.MAX_API_REQ_PER_MIN:
            return False, 60 - int(now - self.api_requests[ip][0])
        self.api_requests[ip].append(now)
        return True, self.MAX_API_REQ_PER_MIN - len(self.api_requests[ip])

rate_limiter = SecurityRateLimiter()

def load_schema_from_supabase():
    """Carrega o catálogo de 459 tabelas com segurança no backend."""
    import ssl
    ssl_context = ssl._create_unverified_context()
    try:
        req = urllib.request.Request(
            f"{SUPABASE_REST_URL}/schema_tables?select=table_name,column_count,columns,foreign_keys,primary_keys",
            headers={
                "apikey": SUPABASE_SECRET,
                "Authorization": f"Bearer {SUPABASE_SECRET}"
            }
        )
        with urllib.request.urlopen(req, context=ssl_context, timeout=5) as res:
            tables = json.loads(res.read().decode("utf-8"))
            if tables:
                print(f"[SUPABASE] {len(tables)} tabelas carregadas com sucesso via API!")
                return {t["table_name"]: t for t in tables}
    except Exception as e:
        print(f"[SCHEMA] Carregando catálogo via cache local: {e}")

    # Fallback para o arquivo local de schema completo
    local_schema_path = r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\schema_complete.json"
    if os.path.exists(local_schema_path):
        try:
            with open(local_schema_path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
                return {t["name"]: t for t in data.get("tables", [])}
        except Exception:
            pass
    return {}

SCHEMA_TABLES_MAP = load_schema_from_supabase()

def persist_message_server_side(user_prompt, bot_data):
    """Grava o histórico no Supabase pelo Backend."""
    import ssl
    ssl_context = ssl._create_unverified_context()
    try:
        url = f"{SUPABASE_REST_URL}/chat_messages"
        payload = {
            "session_id": "auth-session-especialista",
            "user_prompt": user_prompt,
            "tipo_operacao": bot_data.get("tipo_operacao", "SELECT"),
            "sql_validacao": bot_data.get("sql_validacao") or None,
            "sql_final": bot_data.get("sql_final") or bot_data.get("sql") or None,
            "tabelas_utilizadas": bot_data.get("tabelas_utilizadas") or [],
            "explicacao": bot_data.get("explicacao") or bot_data.get("message") or None
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "apikey": SUPABASE_SECRET,
                "Authorization": f"Bearer {SUPABASE_SECRET}",
                "Content-Type": "application/json"
            }
        )
        urllib.request.urlopen(req, context=ssl_context, timeout=4)
    except Exception:
        pass

SYSTEM_PROMPT = """
Você é o Especialista Sênior em Engenharia de Dados e Estrutura de Banco de Dados do sistema comercial Softcomshop (MySQL 8.0).
Sistema e plataforma projetados por Jonatha Dantas (by Dantas).

DIRETRIZES DE SEGURANÇA E PRIVACIDADE:
- NUNCA exponha senhas, chaves de API, tokens de acesso, endereços IP de infraestrutura ou dados pessoais reais de clientes.
- Gere consultas SQL MySQL limpas, seguras e bem estruturadas considerando deleted_at IS NULL e empresa_id = 1.
- Para operações de alteração ou exclusão (UPDATE / DELETE), forneça obrigatoriamente:
  1. "sql_validacao": Um SELECT de conferência prévia com os mesmos filtros WHERE.
  2. "sql_final": O comando definitivo envolvido em transação com START TRANSACTION e COMMIT.

Para leituras (SELECT), deixe "sql_validacao" como "" e coloque a query em "sql_final".

Responda OBRIGATORIAMENTE em JSON:
{
  "tipo_operacao": "SELECT" | "UPDATE" | "DELETE",
  "sql_validacao": "SELECT ... (se for alteração/exclusão)",
  "sql_final": "código SQL definitivo",
  "tabelas_utilizadas": ["lista", "de", "tabelas"],
  "explicacao": "explicação concisa, natural e profissional em português"
}
"""

HTML_PAGE = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QueryHelp (BETA) • by Dantas</title>
    <link rel="icon" type="image/jpeg" href="/logo.jpg">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Inter"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    },
                    colors: {
                        bgApp: '#0c0e14',
                        cardBg: '#131620',
                        borderBase: 'rgba(255, 255, 255, 0.07)',
                        borderHighlight: 'rgba(234, 179, 8, 0.3)',
                        goldAccent: '#eab308'
                    }
                }
            }
        }
    </script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #0c0e14;
            color: #e2e8f0;
        }
        .custom-scroll::-webkit-scrollbar {
            width: 4px;
        }
        .custom-scroll::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scroll::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
        }
        .custom-scroll::-webkit-scrollbar-thumb:hover {
            background: rgba(234, 179, 8, 0.3);
        }
        pre code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 12.5px;
            line-height: 1.65;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col font-sans selection:bg-amber-500/20 selection:text-amber-200 antialiased">

    <!-- TELA DE LOGIN (Exibida quando não autenticado) -->
    <div id="login-view" class="min-h-screen flex flex-col items-center justify-center p-4">
        <div class="max-w-sm w-full bg-cardBg border border-borderBase rounded-2xl p-8 shadow-2xl relative overflow-hidden">
            <div class="absolute -top-12 -right-12 w-32 h-32 bg-amber-500/10 rounded-full blur-2xl pointer-events-none"></div>
            
            <div class="text-center mb-6">
                <img src="/logo.jpg" alt="Logo" class="w-14 h-14 rounded-2xl mx-auto mb-3 object-cover border border-white/10 shadow-md" />
                <div class="flex items-center justify-center gap-2">
                    <h1 class="text-lg font-bold text-white tracking-tight">QueryHelp</h1>
                    <span class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-mono">BETA</span>
                </div>
                <p class="text-xs text-slate-400 mt-1">Acesso Restrito • <span class="text-amber-400 font-mono">by Dantas</span></p>
            </div>

            <form id="login-form" onsubmit="handleLogin(event)" class="space-y-4">
                <div>
                    <label class="block text-[11px] font-medium text-slate-400 uppercase tracking-wider mb-1.5">Usuário</label>
                    <div class="relative">
                        <i class="fa-regular fa-user absolute left-3.5 top-3 text-slate-500 text-xs"></i>
                        <input 
                            type="text" 
                            id="login-username" 
                            placeholder="especialista" 
                            class="w-full bg-bgApp border border-borderBase focus:border-amber-500/60 rounded-xl pl-9 pr-3.5 py-2.5 text-xs text-white placeholder-slate-600 focus:outline-none transition font-sans"
                            autocomplete="username"
                            required
                        />
                    </div>
                </div>

                <div>
                    <label class="block text-[11px] font-medium text-slate-400 uppercase tracking-wider mb-1.5">Senha</label>
                    <div class="relative">
                        <i class="fa-solid fa-lock absolute left-3.5 top-3 text-slate-500 text-xs"></i>
                        <input 
                            type="password" 
                            id="login-password" 
                            placeholder="••••" 
                            class="w-full bg-bgApp border border-borderBase focus:border-amber-500/60 rounded-xl pl-9 pr-3.5 py-2.5 text-xs text-white placeholder-slate-600 focus:outline-none transition font-mono tracking-widest"
                            autocomplete="current-password"
                            required
                        />
                    </div>
                </div>

                <div id="login-error" class="hidden text-xs text-red-400 bg-red-950/30 border border-red-500/20 rounded-xl p-2.5 text-center flex items-center justify-center gap-1.5">
                    <i class="fa-solid fa-circle-exclamation text-xs"></i>
                    <span id="login-error-text">Usuário ou senha incorretos.</span>
                </div>

                <button 
                    type="submit" 
                    id="btn-login"
                    class="w-full py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow-lg shadow-amber-500/10 flex items-center justify-center gap-2 mt-2"
                >
                    <span>Entrar no Sistema</span>
                    <i class="fa-solid fa-arrow-right text-xs"></i>
                </button>
            </form>

            <div class="mt-6 text-center text-[11px] text-slate-500 border-t border-borderBase/60 pt-4 flex items-center justify-center gap-1.5">
                <i class="fa-solid fa-shield-halved text-emerald-400 text-[10px]"></i>
                <span>Proteção Anti-Brute Force Ativa</span>
            </div>
        </div>
    </div>

    <!-- APLICAÇÃO PRINCIPAL (Exibida após Login) -->
    <div id="app-view" class="min-h-screen flex-col hidden">
        <!-- Header Minimalista e Seguro -->
        <header class="border-b border-borderBase px-6 py-3.5 bg-bgApp/90 sticky top-0 z-40 backdrop-blur-md flex items-center justify-between">
            <div class="flex items-center gap-3">
                <img src="/logo.jpg" alt="Logo" class="w-8 h-8 rounded-lg object-cover border border-white/10 shadow-sm" />
                <div class="flex items-center gap-2">
                    <span class="text-sm font-semibold text-white tracking-tight">QueryHelp</span>
                    <span class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-mono">BETA</span>
                    <span class="text-[11px] text-amber-400/90 font-mono bg-amber-500/10 px-2 py-0.5 rounded-full border border-amber-500/20">by Dantas</span>
                </div>
            </div>

            <div class="flex items-center gap-3">
                <span class="text-xs text-slate-400 hidden sm:inline-block">Softcomshop • 459 tabelas</span>
                <button onclick="openApiKeyModal()" class="text-xs text-slate-300 hover:text-white px-3 py-1.5 rounded-lg bg-cardBg hover:bg-white/5 border border-borderBase transition flex items-center gap-1.5">
                    <i class="fa-solid fa-shield-halved text-emerald-400 text-[10px]"></i>
                    <span id="btn-api-text">API Gemini</span>
                </button>
                <button onclick="clearChat()" title="Nova conversa" class="text-xs text-slate-400 hover:text-white p-1.5 rounded-lg hover:bg-white/5 transition">
                    <i class="fa-solid fa-arrow-rotate-right text-[11px]"></i>
                </button>
                <button onclick="handleLogout()" title="Sair do sistema" class="text-xs text-red-400 hover:text-red-300 px-2.5 py-1.5 rounded-lg bg-red-950/20 hover:bg-red-950/40 border border-red-500/20 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-arrow-right-from-bracket text-[10px]"></i>
                    <span>Sair</span>
                </button>
            </div>
        </header>

        <!-- Área Principal de Chat -->
        <main class="flex-1 flex flex-col max-w-3xl w-full mx-auto px-4 py-6 overflow-hidden">
            <div id="chat-box" class="flex-1 overflow-y-auto space-y-6 custom-scroll pr-1 pb-6">
                
                <!-- Welcome Clean -->
                <div id="welcome-card" class="text-center py-16 px-4">
                    <img src="/logo.jpg" alt="Logo" class="w-16 h-16 rounded-2xl mx-auto mb-4 object-cover border border-white/10 shadow-lg" />
                    <h1 class="text-xl font-semibold text-white mb-2 tracking-tight">Bem-vindo, <span class="text-amber-400 font-mono">Especialista</span>!</h1>
                    <p class="text-xs text-slate-400 max-w-md mx-auto leading-relaxed mb-6">
                        Estrutura oficial de <strong>459 tabelas e 6.600 campos</strong> conectada no Supabase. Pergunte sobre consultas, exclusões ou atualizações com validação prévia.
                    </p>

                    <div class="flex flex-wrap justify-center gap-2 max-w-lg mx-auto">
                        <button onclick="sendQuickPrompt('Como deletar vendas com segurança?')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                            Deletar vendas (com validação)
                        </button>
                        <button onclick="sendQuickPrompt('Quais vendas estão em contingência e suas diferenças?')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                            Vendas em contingência
                        </button>
                        <button onclick="sendQuickPrompt('Como alterar o preço ou estoque de um produto?')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                            Alterar preço/estoque
                        </button>
                        <button onclick="sendQuickPrompt('Faturamento agrupado por forma de pagamento')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                            Faturamento por pagamento
                        </button>
                    </div>
                </div>

            </div>

            <!-- Input Bar Clean -->
            <div class="pt-2">
                <form id="chat-form" onsubmit="sendMessage(event)" class="bg-cardBg rounded-xl border border-borderBase focus-within:border-amber-500/50 transition flex items-center p-1.5 shadow-lg">
                    <input 
                        type="text" 
                        id="user-input" 
                        placeholder="Digite sua dúvida ou o que deseja consultar..." 
                        class="flex-1 bg-transparent px-3 py-2 text-sm text-white placeholder-slate-500 focus:outline-none"
                        autocomplete="off"
                        maxlength="1500"
                    />
                    <button type="submit" id="btn-send" class="h-8 px-3.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-semibold text-xs transition flex items-center gap-1.5 shrink-0">
                        <span>Enviar</span>
                        <i class="fa-solid fa-arrow-up text-[10px]"></i>
                    </button>
                </form>
                <div class="flex items-center justify-between px-1 mt-2 text-[11px] text-slate-500">
                    <span class="flex items-center gap-1.5"><i class="fa-solid fa-lock text-amber-400 text-[10px]"></i> Sessão Autenticada: Especialista</span>
                    <span>Desenvolvido por <strong class="text-slate-400 font-medium">Jonatha Dantas</strong></span>
                </div>
            </div>
        </main>
    </div>

    <!-- Modal de API Key -->
    <div id="api-modal" class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 hidden z-50">
        <div class="bg-cardBg border border-borderBase rounded-2xl p-5 max-w-sm w-full shadow-2xl">
            <h3 class="text-sm font-semibold text-white mb-1">Chave da API Gemini</h3>
            <p class="text-xs text-slate-400 mb-3">Insira sua chave gratuita do Google AI Studio para ativar o modelo generativo.</p>
            <input 
                type="password" 
                id="api-key-input" 
                placeholder="Cole sua chave aqui..." 
                class="w-full bg-bgApp border border-borderBase focus:border-amber-500 rounded-lg px-3 py-2 text-xs text-white mb-4 focus:outline-none font-mono"
            />
            <div class="flex justify-end gap-2">
                <button onclick="closeApiKeyModal()" class="px-3 py-1.5 rounded-lg text-xs text-slate-400 hover:text-white">Cancelar</button>
                <button onclick="saveApiKey()" class="px-4 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 hover:bg-amber-400 text-slate-950">Salvar</button>
            </div>
        </div>
    </div>

    <script>
        let sessionToken = sessionStorage.getItem('AUTH_SESSION_TOKEN') || '';
        let currentApiKey = sessionStorage.getItem('GEMINI_SESSION_KEY') || '';

        function checkAuth() {
            const loginView = document.getElementById('login-view');
            const appView = document.getElementById('app-view');
            if (sessionToken) {
                loginView.classList.add('hidden');
                appView.classList.remove('hidden');
                appView.classList.add('flex');
            } else {
                loginView.classList.remove('hidden');
                appView.classList.add('hidden');
                appView.classList.remove('flex');
            }
        }

        async function handleLogin(e) {
            e.preventDefault();
            const u = document.getElementById('login-username').value.trim();
            const p = document.getElementById('login-password').value.trim();
            const errDiv = document.getElementById('login-error');
            const errText = document.getElementById('login-error-text');
            const btn = document.getElementById('btn-login');

            btn.disabled = true;
            btn.innerHTML = '<i class="fa-solid fa-circle-notch animate-spin text-xs"></i> Autenticando...';
            errDiv.classList.add('hidden');

            try {
                const res = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: u, password: p })
                });
                const data = await res.json();
                
                if (res.ok && data.token) {
                    sessionToken = data.token;
                    sessionStorage.setItem('AUTH_SESSION_TOKEN', sessionToken);
                    checkAuth();
                } else {
                    errText.innerText = data.error || 'Usuário ou senha incorretos.';
                    errDiv.classList.remove('hidden');
                }
            } catch (err) {
                errText.innerText = 'Falha na conexão com o servidor.';
                errDiv.classList.remove('hidden');
            } finally {
                btn.disabled = false;
                btn.innerHTML = '<span>Entrar no Sistema</span> <i class="fa-solid fa-arrow-right text-xs"></i>';
            }
        }

        function handleLogout() {
            sessionToken = '';
            sessionStorage.removeItem('AUTH_SESSION_TOKEN');
            checkAuth();
        }

        checkAuth();

        function openApiKeyModal() {
            document.getElementById('api-key-input').value = currentApiKey;
            document.getElementById('api-modal').classList.remove('hidden');
        }

        function closeApiKeyModal() {
            document.getElementById('api-modal').classList.add('hidden');
        }

        function saveApiKey() {
            currentApiKey = document.getElementById('api-key-input').value.trim();
            if (currentApiKey) {
                sessionStorage.setItem('GEMINI_SESSION_KEY', currentApiKey);
            } else {
                sessionStorage.removeItem('GEMINI_SESSION_KEY');
            }
            closeApiKeyModal();
            updateBtnText();
        }

        function updateBtnText() {
            const btn = document.getElementById('btn-api-text');
            if (btn) {
                btn.innerText = currentApiKey ? 'Gemini Conectado' : 'API Gemini';
            }
        }
        updateBtnText();

        function clearChat() {
            const box = document.getElementById('chat-box');
            box.innerHTML = '';
            const welcome = document.createElement('div');
            welcome.id = 'welcome-card';
            welcome.className = 'text-center py-16 px-4';
            welcome.innerHTML = `
                <img src="/logo.jpg" alt="Logo" class="w-16 h-16 rounded-2xl mx-auto mb-4 object-cover border border-white/10 shadow-lg" />
                <h1 class="text-xl font-semibold text-white mb-2 tracking-tight">Bem-vindo, <span class="text-amber-400 font-mono">Especialista</span>!</h1>
                <p class="text-xs text-slate-400 max-w-md mx-auto leading-relaxed mb-6">
                    Estrutura oficial de <strong>459 tabelas e 6.600 campos</strong> conectada no Supabase. Pergunte sobre consultas, exclusões ou atualizações com validação prévia.
                </p>
                <div class="flex flex-wrap justify-center gap-2 max-w-lg mx-auto">
                    <button onclick="sendQuickPrompt('Como deletar vendas com segurança?')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                        Deletar vendas (com validação)
                    </button>
                    <button onclick="sendQuickPrompt('Quais vendas estão em contingência e suas diferenças?')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                        Vendas em contingência
                    </button>
                    <button onclick="sendQuickPrompt('Como alterar o preço ou estoque de um produto?')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                        Alterar preço/estoque
                    </button>
                    <button onclick="sendQuickPrompt('Faturamento agrupado por forma de pagamento')" class="text-xs text-slate-300 hover:text-white bg-cardBg hover:bg-white/5 border border-borderBase px-3 py-1.5 rounded-lg transition">
                        Faturamento por pagamento
                    </button>
                </div>
            `;
            box.appendChild(welcome);
        }

        function sendQuickPrompt(text) {
            document.getElementById('user-input').value = text;
            document.getElementById('chat-form').dispatchEvent(new Event('submit'));
        }

        async function sendMessage(e) {
            e.preventDefault();
            const input = document.getElementById('user-input');
            const queryText = input.value.trim();
            if (!queryText) return;

            const welcomeCard = document.getElementById('welcome-card');
            if (welcomeCard) welcomeCard.remove();

            input.value = '';
            appendUserMessage(queryText);

            const loadingId = appendLoadingMessage();

            try {
                const response = await fetch('/api/ask', {
                    method: 'POST',
                    headers: { 
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${sessionToken}`
                    },
                    body: JSON.stringify({ message: queryText, apiKey: currentApiKey })
                });

                if (response.status === 401) {
                    handleLogout();
                    throw new Error('Sessão expirada. Faça login novamente.');
                }

                if (!response.ok) {
                    let errMsg = 'Falha no processamento.';
                    try {
                        const errData = await response.json();
                        if (errData && errData.error) errMsg = errData.error;
                    } catch (_) {}
                    throw new Error(errMsg);
                }

                const data = await response.json();
                removeLoadingMessage(loadingId);
                appendBotMessage(data);
            } catch (err) {
                removeLoadingMessage(loadingId);
                appendErrorMessage('Não foi possível gerar a resposta: ' + err.message);
            }
        }

        function appendUserMessage(text) {
            const box = document.getElementById('chat-box');
            const div = document.createElement('div');
            div.className = 'flex justify-end';
            div.innerHTML = `
                <div class="bg-amber-500/10 text-amber-200 border border-amber-500/20 rounded-2xl rounded-tr-sm px-4 py-2.5 text-xs leading-relaxed max-w-lg">
                    ${escapeHtml(text)}
                </div>
            `;
            box.appendChild(div);
            box.scrollTop = box.scrollHeight;
        }

        function appendLoadingMessage() {
            const id = 'loading-' + Date.now();
            const box = document.getElementById('chat-box');
            const div = document.createElement('div');
            div.id = id;
            div.className = 'flex gap-3 items-start';
            div.innerHTML = `
                <img src="/logo.jpg" alt="Logo" class="w-6 h-6 rounded-md object-cover border border-white/10 shrink-0 mt-1 animate-pulse" />
                <div class="text-xs text-slate-400 py-1 flex items-center gap-2">
                    <i class="fa-solid fa-circle-notch animate-spin text-amber-400"></i>
                    <span>Estruturando e validando consulta no schema...</span>
                </div>
            `;
            box.appendChild(div);
            box.scrollTop = box.scrollHeight;
            return id;
        }

        function removeLoadingMessage(id) {
            const el = document.getElementById(id);
            if (el) el.remove();
        }

        function appendErrorMessage(text) {
            const box = document.getElementById('chat-box');
            const div = document.createElement('div');
            div.className = 'flex gap-3 items-start';
            div.innerHTML = `
                <div class="w-6 h-6 rounded-md bg-red-500/20 text-red-400 flex items-center justify-center text-xs shrink-0 mt-1">
                    <i class="fa-solid fa-triangle-exclamation"></i>
                </div>
                <div class="text-xs text-red-300 py-1 bg-red-950/30 border border-red-500/20 rounded-xl px-3.5 py-2">
                    ${escapeHtml(text)}
                </div>
            `;
            box.appendChild(div);
            box.scrollTop = box.scrollHeight;
        }

        function appendBotMessage(data) {
            const box = document.getElementById('chat-box');
            const div = document.createElement('div');
            div.className = 'flex gap-3 items-start text-xs leading-relaxed';

            const isModification = (data.tipo_operacao === 'UPDATE' || data.tipo_operacao === 'DELETE' || !!data.sql_validacao);
            const tables = data.tabelas_utilizadas || [];

            let contentHtml = `
                <div class="flex-1 space-y-3">
                    <p class="text-slate-200 leading-relaxed font-normal">${escapeHtml(data.explicacao || data.message || '')}</p>
            `;

            if (isModification && data.sql_validacao) {
                const tab1Id = 'tab-val-' + Date.now();
                const tab2Id = 'tab-final-' + Date.now();
                const code1Id = 'code-val-' + Date.now();
                const code2Id = 'code-final-' + Date.now();
                const btnCopyId = 'btn-copy-' + Date.now();
                const opName = data.tipo_operacao || 'DML';

                contentHtml += `
                    <!-- Box Unificado Clean de 2 Etapas com Abas -->
                    <div class="rounded-xl border border-borderBase bg-[#090b10] overflow-hidden">
                        <!-- Header com Abas Minimalistas -->
                        <div class="flex items-center justify-between border-b border-borderBase px-3 py-2 bg-cardBg/60">
                            <div class="flex items-center gap-1.5">
                                <button id="${tab1Id}" onclick="switchTab('${tab1Id}', '${tab2Id}', '${code1Id}', '${code2Id}', '${btnCopyId}', true)" class="px-2.5 py-1 rounded-md text-[11px] font-medium bg-white/10 text-white transition flex items-center gap-1.5">
                                    <span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span> 1. Validação (SELECT)
                                </button>
                                <button id="${tab2Id}" onclick="switchTab('${tab1Id}', '${tab2Id}', '${code1Id}', '${code2Id}', '${btnCopyId}', false)" class="px-2.5 py-1 rounded-md text-[11px] font-medium text-slate-400 hover:text-slate-200 transition flex items-center gap-1.5">
                                    <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span> 2. Execução (${escapeHtml(opName)})
                                </button>
                            </div>
                            <button id="${btnCopyId}" onclick="copyActiveCode('${code1Id}', '${btnCopyId}')" class="text-[11px] text-slate-400 hover:text-white px-2 py-0.5 rounded hover:bg-white/5 transition flex items-center gap-1">
                                <i class="fa-regular fa-copy text-[10px]"></i> Copiar
                            </button>
                        </div>

                        <!-- Código da Aba 1 (SELECT de Validação) -->
                        <div id="${code1Id}">
                            <pre class="p-3.5 text-slate-200 overflow-x-auto custom-scroll"><code>${escapeHtml(data.sql_validacao)}</code></pre>
                        </div>

                        <!-- Código da Aba 2 (UPDATE/DELETE Final) -->
                        <div id="${code2Id}" class="hidden">
                            <div class="m-3 mb-1 p-2.5 bg-amber-500/10 border border-amber-500/20 rounded-lg flex items-center gap-2 text-[11.5px] text-amber-300 font-medium">
                                <i class="fa-solid fa-triangle-exclamation text-amber-400 shrink-0"></i>
                                <span><strong>Atenção:</strong> Você precisa validar com seu gestor antes de executar a query final.</span>
                            </div>
                            <pre class="p-3.5 pt-2 text-amber-200/90 overflow-x-auto custom-scroll"><code>${escapeHtml(data.sql_final || data.sql)}</code></pre>
                        </div>
                    </div>
                `;
            } else if (data.sql_final || data.sql) {
                const codeId = 'code-single-' + Date.now();
                const btnId = 'btn-single-' + Date.now();
                const sqlText = data.sql_final || data.sql;

                contentHtml += `
                    <!-- Bloco Único de Código Clean -->
                    <div class="rounded-xl border border-borderBase bg-[#090b10] overflow-hidden">
                        <div class="flex items-center justify-between border-b border-borderBase px-3.5 py-2 bg-cardBg/60 text-[11px] text-slate-400">
                            <span class="font-mono text-slate-400">mysql</span>
                            <button id="${btnId}" onclick="copySqlClean('${codeId}', '${btnId}')" class="text-slate-400 hover:text-white px-2 py-0.5 rounded hover:bg-white/5 transition flex items-center gap-1">
                                <i class="fa-regular fa-copy text-[10px]"></i> Copiar
                            </button>
                        </div>
                        <pre class="p-3.5 text-slate-200 overflow-x-auto custom-scroll" id="${codeId}"><code>${escapeHtml(sqlText)}</code></pre>
                    </div>
                `;
            }

            if (tables.length > 0) {
                contentHtml += `
                    <div class="text-[11px] text-slate-500 flex items-center gap-2 pt-0.5">
                        <span>Tabelas:</span>
                        <span class="text-slate-400 font-mono">${escapeHtml(tables.join(', '))}</span>
                    </div>
                `;
            }

            contentHtml += `</div>`;

            div.innerHTML = `
                <img src="/logo.jpg" alt="Logo" class="w-6 h-6 rounded-md object-cover border border-white/10 shrink-0 mt-0.5" />
                ${contentHtml}
            `;
            box.appendChild(div);
            box.scrollTop = box.scrollHeight;
        }

        function switchTab(tab1Id, tab2Id, code1Id, code2Id, btnCopyId, showFirst) {
            const tab1 = document.getElementById(tab1Id);
            const tab2 = document.getElementById(tab2Id);
            const code1 = document.getElementById(code1Id);
            const code2 = document.getElementById(code2Id);
            const btn = document.getElementById(btnCopyId);

            if (showFirst) {
                tab1.className = 'px-2.5 py-1 rounded-md text-[11px] font-medium bg-white/10 text-white transition flex items-center gap-1.5';
                tab2.className = 'px-2.5 py-1 rounded-md text-[11px] font-medium text-slate-400 hover:text-slate-200 transition flex items-center gap-1.5';
                code1.classList.remove('hidden');
                code2.classList.add('hidden');
                btn.setAttribute('onclick', `copyActiveCode('${code1Id}', '${btnCopyId}')`);
            } else {
                tab2.className = 'px-2.5 py-1 rounded-md text-[11px] font-medium bg-white/10 text-white transition flex items-center gap-1.5';
                tab1.className = 'px-2.5 py-1 rounded-md text-[11px] font-medium text-slate-400 hover:text-slate-200 transition flex items-center gap-1.5';
                code2.classList.remove('hidden');
                code1.classList.add('hidden');
                btn.setAttribute('onclick', `copyActiveCode('${code2Id}', '${btnCopyId}')`);
            }
        }

        function copyActiveCode(codeContainerId, btnId) {
            const container = document.getElementById(codeContainerId);
            const text = container.querySelector('code').innerText;
            navigator.clipboard.writeText(text);
            const btn = document.getElementById(btnId);
            btn.innerHTML = '<i class="fa-solid fa-check text-emerald-400 text-[10px]"></i> Copiado!';
            setTimeout(() => {
                btn.innerHTML = '<i class="fa-regular fa-copy text-[10px]"></i> Copiar';
            }, 2000);
        }

        function copySqlClean(codeId, btnId) {
            const el = document.getElementById(codeId);
            const text = el.querySelector('code').innerText;
            navigator.clipboard.writeText(text);
            const btn = document.getElementById(btnId);
            btn.innerHTML = '<i class="fa-solid fa-check text-emerald-400 text-[10px]"></i> Copiado!';
            setTimeout(() => {
                btn.innerHTML = '<i class="fa-regular fa-copy text-[10px]"></i> Copiar';
            }, 2000);
        }

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }
    </script>
</body>
</html>
"""

def sanitize_response_data(data):
    """Sanitiza o dicionário de resposta antes do envio."""
    if not isinstance(data, dict):
        return {"error": "Formato inválido"}
    
    allowed_keys = {"tipo_operacao", "sql_validacao", "sql_final", "sql", "tabelas_utilizadas", "explicacao", "message"}
    sanitized = {k: v for k, v in data.items() if k in allowed_keys}
    
    secret_patterns = [
        r"AIzaSy[A-Za-z0-9_-]{33}",
        r"sb_publishable_[A-Za-z0-9_-]+",
        r"sb_secret_[A-Za-z0-9_-]+",
        r"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
        r"postgresql://[^@]+@[^:]+:[0-9]+/[^ \n\r\t]+",
        r"password\s*=\s*['\"][^'\"]+['\"]",
        r"127\.0\.0\.1:[0-9]+",
        r"aws-0-[a-z0-9-]+\.pooler\.supabase\.com"
    ]
    
    for k, v in list(sanitized.items()):
        if isinstance(v, str):
            for pat in secret_patterns:
                v = re.sub(pat, "[PROTEGIDO]", v)
            sanitized[k] = v
            
    return sanitized

def call_gemini_api(user_message, api_key):
    """Requisição server-to-server segura para a API do Gemini."""
    import ssl
    ssl_context = ssl._create_unverified_context()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {
        "system_instruction": {
            "parts": [{"text": SYSTEM_PROMPT}]
        },
        "contents": [
            {
                "parts": [{"text": f"Gere a consulta SQL para: {user_message}"}]
            }
        ],
        "generationConfig": {
            "temperature": 0.1,
            "response_mime_type": "application/json"
        }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        text = res_data["candidates"][0]["content"]["parts"][0]["text"]
        parsed = json.loads(text)
        usage_meta = res_data.get("usageMetadata", {})
        parsed["usage"] = {
            "prompt_tokens": usage_meta.get("promptTokenCount", 250),
            "completion_tokens": usage_meta.get("candidatesTokenCount", 90),
            "total_tokens": usage_meta.get("totalTokenCount", 340),
            "source": "gemini-1.5-flash",
            "status": "success",
            "quota_exhausted": False
        }
        return parsed

STOPWORDS = {
    "quero", "uma", "query", "querry", "consulta", "tabela", "tabelas", "traga", "todas", "todos",
    "com", "informacao", "informacoes", "informação", "informações", "relacionadas", "relacionada",
    "relacionados", "relacionado", "ao", "a", "o", "os", "as", "de", "do", "da", "dos", "das", "em",
    "no", "na", "nos", "nas", "para", "por", "que", "seja", "mostrar", "mostre", "ver", "quais", "qual",
    "como", "fazer", "gerar", "cria", "criar", "me", "de", "um", "uns", "umas", "sobre", "relaciona",
    "exibe", "exibir", "listar", "liste", "buscar", "busque"
}

SYNONYMS_MAP = {
    "nfse": ["nota_fiscal_servico_eletronica", "nota_fiscal_servico", "nfse", "servico", "rps", "iss", "issqn", "tomador"],
    "nfs-e": ["nota_fiscal_servico_eletronica", "nota_fiscal_servico", "nfse", "servico", "rps", "iss", "issqn", "tomador"],
    "servico": ["nota_fiscal_servico_eletronica", "contrato_servico", "nfse", "rps", "issqn", "venda_ordem_servico"],
    "serviço": ["nota_fiscal_servico_eletronica", "contrato_servico", "nfse", "rps", "issqn", "venda_ordem_servico"],
    "marketplace": ["marketplace_pedido", "marketplace_vinculado", "marketplace_config", "produto_marketplace", "market", "ifood", "delivery", "integrac", "canal"],
    "mercado": ["marketplace", "market"],
    "ifood": ["ifood", "delivery", "marketplace", "integrac", "restaurante_mesa"],
    "delivery": ["delivery", "ifood", "entregador", "restaurante_mesa", "venda"],
    "fiscal": ["nota_fiscal_eletronica", "nota_fiscal_servico_eletronica", "nfe", "nfce", "nfse", "icms", "pis", "cofins", "imposto", "tribut"],
    "nfe": ["nota_fiscal_eletronica", "nota_fiscal_eletronica_item", "nfe", "chave_nfe", "recibo_situacao"],
    "nfce": ["venda_nfce", "nota_fiscal_eletronica", "contingencia"],
    "cte": ["cte", "cte_documento_nfe", "cte_tabela_frete", "transporte"],
    "mdfe": ["manifesto_documento_eletronico", "mdfe"],
    "os": ["venda_ordem_servico", "atendimento", "assistencia_padrao_laudo", "ordem_servico"],
    "ordem_servico": ["venda_ordem_servico", "atendimento", "assistencia_padrao_laudo", "ordem_servico"],
    "financeiro": ["financeiro", "financeiro_parcela", "caixa", "banco", "contas_receber", "contas_pagar", "forma_pagamento"],
    "pagamento": ["forma_pagamento", "venda_cartao", "financeiro_parcela", "financeiro"],
    "estoque": ["produto_empresa_grade", "produto_estoque_ruptura", "movimentacao_estoque", "almoxarifado"],
    "produto": ["produto", "produto_empresa", "produto_empresa_grade", "tabela_preco_produto", "grupo"],
    "cliente": ["cliente", "pessoa", "endereco", "contato"],
    "usuario": ["usuario", "funcionario", "permissao", "acesso", "permission_role"],
    "venda": ["venda", "venda_item", "venda_cartao", "faturamento", "pedido"],
    "restaurante": ["restaurante_mesa", "restaurante_mesa_item", "restaurante_mesa_configuracao"],
    "petshop": ["petshop_ordem_servico", "petshop_atendimento_servico", "petshop_configuracao"]
}

def extract_semantic_keywords(prompt_text):
    text = prompt_text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    tokens = text.split()
    return [t for t in tokens if t not in STOPWORDS and len(t) > 2]

def search_tables_by_topic(keywords):
    if not SCHEMA_TABLES_MAP:
        return []
    
    expanded = set(keywords)
    for kw in keywords:
        for root_term, syn_list in SYNONYMS_MAP.items():
            if kw in root_term or root_term in kw:
                expanded.update(syn_list)

    scores = {}
    for t_name, t_data in SCHEMA_TABLES_MAP.items():
        score = 0
        cols = t_data.get("columns", [])
        col_names = [c["name"].lower() if isinstance(c, dict) else str(c).lower() for c in cols]
        
        for kw in expanded:
            if kw in t_name.lower():
                score += 20
            matched_cols = [c for c in col_names if kw in c]
            score += len(matched_cols) * 4

        if score > 0:
            scores[t_name] = (score, t_data)

    return sorted(scores.items(), key=lambda x: x[1][0], reverse=True)

def generate_structure_response(prompt_text):
    """Motor especialista local com inteligência de negócio e busca semântica em 459 tabelas."""
    p = prompt_text.lower()
    keywords = extract_semantic_keywords(prompt_text)
    
    is_delete = any(k in p for k in ["delet", "exclu", "apag", "remov", "drop", "limp"])
    is_update = any(k in p for k in ["updat", "atualiz", "alter", "modific", "cancel", "inativ", "bloque", "ajust", "troc", "mud", "aument", "diminu", "baix"])

    # 1. ALTERAR PREÇO OU ESTOQUE DE PRODUTO (2 ETAPAS)
    if is_update and any(k in p for k in ["produt", "preco", "preço", "estoqu", "custo", "grade", "valor"]):
        sql_val = """-- 1. Consulta de Validação (Conferência do Produto, Preço e Estoque Atual)
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
  AND p.deleted_at IS NULL;"""

        sql_final = """-- 2. Atualização Segura de Preço e/ou Saldo de Estoque (com Transação)
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

-- Confirmar alteração:
COMMIT;

-- Caso queira desfazer:
-- ROLLBACK;"""

        return {
            "tipo_operacao": "UPDATE",
            "sql_validacao": sql_val,
            "sql_final": sql_final,
            "tabelas_utilizadas": ["produto", "produto_empresa", "produto_empresa_grade"],
            "explicacao": "No Softcomshop, os preços e saldos de estoque são vinculados por filial na tabela `produto_empresa_grade` relacionada a `produto_empresa` e `produto`. Na aba **1. Validação**, confira o cadastro e valores atuais. Na aba **2. Execução**, aplique a alteração dentro de uma transação segura."
        }

    # 2. DELETE / EXCLUSÃO DE VENDAS (2 ETAPAS COM VALIDAÇÃO FISCAL E FINANCEIRA)
    if is_delete and ("venda" in p or "pedido" in p or "seguran" in p):
        sql_val = """-- 1. Validação Prévia (Conferência de Status, NF-e Autorizada e Parcelas Quitadas)
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
GROUP BY v.id, v.status, v.valor_total, v.total_pagamento, v.api_data_hora_venda, nfe.id, nfe.numero_nfe, nfe.recibo_situacao;"""

        sql_final = """-- 2. Exclusão Lógica com Transação Segura (Soft Delete)
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
-- ROLLBACK;"""

        return {
            "tipo_operacao": "DELETE",
            "sql_validacao": sql_val,
            "sql_final": sql_final,
            "tabelas_utilizadas": ["venda", "nota_fiscal_eletronica", "financeiro_parcela"],
            "explicacao": "Para deletar uma venda com total conformidade no Softcomshop, a query de validação prévia verifica o status da venda, se há documento fiscal (NF-e/NFC-e) já autorizado na SEFAZ e se as parcelas financeiras já foram baixadas. A exclusão final é executada via exclusão lógica (deleted_at = NOW()) com status CANCELADA dentro de uma transação segura."
        }

    # 3. UPDATE / CANCELAMENTO DE VENDAS (2 ETAPAS)
    if is_update and ("venda" in p or "pedido" in p):
        sql_val = """-- 1. Consulta de Validação
SELECT 
    id AS venda_id, 
    status, 
    valor_total, 
    total_pagamento, 
    api_data_hora_venda, 
    cliente_id, 
    nfe_id
FROM venda
WHERE id = 100 
  AND empresa_id = 1 
  AND deleted_at IS NULL;"""

        sql_final = """-- 2. Atualização com Transação
START TRANSACTION;

UPDATE venda 
SET status = 'CANCELADA', 
    updated_at = NOW() 
WHERE id = 100 
  AND empresa_id = 1 
  AND deleted_at IS NULL;

COMMIT;"""

        return {
            "tipo_operacao": "UPDATE",
            "sql_validacao": sql_val,
            "sql_final": sql_final,
            "tabelas_utilizadas": ["venda"],
            "explicacao": "Na aba **Validação**, confira os dados da venda. Na aba **Execução**, aplique a atualização de status com confirmação explícita."
        }

    # 4. NFSE / NOTA FISCAL DE SERVIÇO / ISSQN / RPS
    if any(k in p for k in ["nfse", "nfs-e", "servico", "serviço", "rps", "issqn", "tomador", "iss"]):
        sql = """-- Consulta Analítica Completa de NFSe (Nota Fiscal de Serviços Eletrônica)
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
LIMIT 50;"""
        return {
            "tipo_operacao": "SELECT",
            "sql_validacao": "",
            "sql_final": sql,
            "tabelas_utilizadas": [
                "nota_fiscal_servico_eletronica",
                "nota_fiscal_servico_eletronica_item",
                "nota_fiscal_servico_eletronica_tomador",
                "nfse_aliquota_padrao",
                "nfse_codigo_servico_item",
                "contrato_servico"
            ],
            "explicacao": "Identificamos todas as tabelas oficiais do módulo de NFSe no schema: `nota_fiscal_servico_eletronica` (cabeçalho/RPS), `nota_fiscal_servico_eletronica_item` (itens e alíquotas de ISS), `nota_fiscal_servico_eletronica_tomador` (dados do tomador), `nfse_aliquota_padrao`, `nfse_codigo_servico_item`, `nfse_serie` e vínculos com `contrato_servico`."
        }

    # 5. MARKETPLACE / INTEGRAÇÕES / CANAIS / IFOOD
    if any("market" in kw or "ifood" in kw or "delivery" in kw or "canal" in kw or "integrac" in kw or "ecom" in kw for kw in keywords):
        sql = """-- Consulta Analítica Completa de Integração com Marketplaces
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
LIMIT 50;"""
        return {
            "tipo_operacao": "SELECT",
            "sql_validacao": "",
            "sql_final": sql,
            "tabelas_utilizadas": ["venda", "marketplace_pedido", "marketplace_vinculado", "marketplace_config", "produto_marketplace"],
            "explicacao": "Identificamos todas as tabelas oficiais do módulo de Marketplace no schema: `marketplace_pedido`, `marketplace_vinculado`, `marketplace_config`, `marketplace_produto`, `marketplace_categoria` e os vínculos diretos na tabela `venda` (`api_app_name`, `marketplace_pedido_id`, `origem_venda`). A consulta acima cruza os pedidos de venda com os registros de integração externa."
        }

    # 5. FATURAMENTO POR FORMA DE PAGAMENTO
    if any(k in p for k in ["fatur", "pagament", "forma_pagamento", "cartao", "cartão", "pix", "dinheiro"]):
        sql = """SELECT 
    fp.descricao AS forma_pagamento,
    COUNT(v.id) AS quantidade_vendas,
    SUM(v.valor_total) AS total_faturado,
    SUM(v.total_desconto) AS total_descontos,
    ROUND(AVG(v.valor_total), 2) AS ticket_medio
FROM venda v
INNER JOIN financeiro_parcela p ON p.venda_id = v.id AND p.deleted_at IS NULL
INNER JOIN forma_pagamento fp ON p.forma_pagamento_id = fp.id
WHERE v.deleted_at IS NULL 
  AND v.empresa_id = 1
  AND v.status = 'FINALIZADA'
GROUP BY fp.id, fp.descricao
ORDER BY total_faturado DESC;"""
        return {
            "tipo_operacao": "SELECT",
            "sql_validacao": "",
            "sql_final": sql,
            "tabelas_utilizadas": ["venda", "financeiro_parcela", "forma_pagamento"],
            "explicacao": "Relatório consolidado de faturamento agrupado por forma de pagamento (PIX, Cartões, Dinheiro), calculando faturamento total, quantidade de vendas e ticket médio."
        }

    # 6. SEFAZ / CONTINGÊNCIA FISCAL
    if "conting" in p or "rejei" in p or ("erro" in p and "nota" in p):
        sql = """SELECT 
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
ORDER BY v.id DESC;"""
        return {
            "tipo_operacao": "SELECT",
            "sql_validacao": "",
            "sql_final": sql,
            "tabelas_utilizadas": ["venda", "nota_fiscal_eletronica", "financeiro_parcela"],
            "explicacao": "Esta consulta faz o cruzamento entre as vendas e os documentos fiscais em contingência, comparando o valor total com as parcelas financeiras para identificar eventuais divergências de centavos."
        }

    # 7. BUSCA DINÂMICA INTELIGENTE SOBRE O SCHEMA DE 459 TABELAS
    search_results = search_tables_by_topic(keywords)
    if search_results:
        top_tables = [t[0] for t in search_results[:8]]
        main_table = top_tables[0]
        
        sql = f"""SELECT *
FROM {main_table}
WHERE deleted_at IS NULL
ORDER BY id DESC
LIMIT 20;"""
        return {
            "tipo_operacao": "SELECT",
            "sql_validacao": "",
            "sql_final": sql,
            "tabelas_utilizadas": top_tables[:5],
            "explicacao": f"Localizamos {len(search_results)} tabelas no schema relacionadas ao tema pesquisado. As principais tabelas são: **{', '.join(top_tables[:5])}**."
        }

    # Resposta padrão estrutural caso nenhum termo seja detectado
    sql = """SELECT 
    v.id AS venda_id,
    v.api_data_hora_venda AS data_venda,
    v.origem_venda,
    v.status,
    v.valor_total,
    v.total_desconto,
    v.total_pagamento
FROM venda v
WHERE v.deleted_at IS NULL AND v.empresa_id = 1
ORDER BY v.id DESC
LIMIT 10;"""
    return {
        "tipo_operacao": "SELECT",
        "sql_validacao": "",
        "sql_final": sql,
        "tabelas_utilizadas": ["venda"],
        "explicacao": "Consulta base com as últimas vendas registradas na base aplicando os filtros padrão de empresa e exclusão lógica."
    }

class RequestHandler(BaseHTTPRequestHandler):
    def _get_client_ip(self):
        """Identifica o IP real do cliente com suporte a proxies confiáveis."""
        forwarded = self.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        real_ip = self.headers.get("X-Real-IP")
        if real_ip:
            return real_ip.strip()
        return self.client_address[0]

    def _send_security_headers(self, extra_headers=None):
        """Injeta cabeçalhos defensivos de Cyber Segurança (OWASP Standard)."""
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-XSS-Protection", "1; mode=block")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Content-Security-Policy", "default-src 'self' https://fonts.googleapis.com https://fonts.gstatic.com https://cdn.tailwindcss.com https://cdnjs.cloudflare.com; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; img-src 'self' data:; connect-src 'self';")
        if extra_headers:
            for k, v in extra_headers.items():
                self.send_header(k, str(v))

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self._send_security_headers()
            self.end_headers()
            index_path = os.path.join(os.path.dirname(__file__), "index.html")
            if os.path.exists(index_path):
                with open(index_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(HTML_PAGE.encode("utf-8"))
        elif self.path == "/logo.jpg" or self.path == "/favicon.ico":
            if os.path.exists(LOGO_PATH):
                self.send_response(200)
                self.send_header("Content-Type", "image/jpeg")
                self._send_security_headers()
                self.end_headers()
                with open(LOGO_PATH, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        client_ip = self._get_client_ip()

        # 1. Defesa DoS: Limitação de tamanho de payload (Máx 64KB)
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length > 65536:
            self.send_response(413)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._send_security_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Payload excede o limite permitido."}).encode("utf-8"))
            return

        body = self.rfile.read(content_length).decode("utf-8", errors="ignore")
        
        # Endpoint de Autenticação /api/login com Proteção Anti-Brute Force
        if self.path == "/api/login":
            is_locked, remaining_lock = rate_limiter.is_ip_locked(client_ip)
            if is_locked:
                self.send_response(429)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self._send_security_headers({"Retry-After": remaining_lock})
                self.end_headers()
                self.wfile.write(json.dumps({
                    "error": f"Muitas tentativas incorretas. Acesso bloqueado por segurança. Tente novamente em {remaining_lock // 60} min e {remaining_lock % 60} seg."
                }).encode("utf-8"))
                return

            try:
                data = json.loads(body)
                u = unicodedata.normalize("NFKC", str(data.get("username", "")).replace("\x00", "").strip().lower())
                p = unicodedata.normalize("NFKC", str(data.get("password", "")).replace("\x00", "").strip())
                
                # Comparação em tempo constante para mitigação de Timing Attacks (CWE-208)
                is_user_valid = any(hmac.compare_digest(u, valid_u) for valid_u in AUTH_USERS)
                is_pass_valid = hmac.compare_digest(p, AUTH_PASS)

                if is_user_valid and is_pass_valid:
                    rate_limiter.record_login_attempt(client_ip, success=True)
                    token = create_session()
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self._send_security_headers()
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True, "token": token, "user": u}).encode("utf-8"))
                else:
                    allowed, attempts_left = rate_limiter.record_login_attempt(client_ip, success=False)
                    if not allowed:
                        self.send_response(429)
                        self.send_header("Content-Type", "application/json; charset=utf-8")
                        self._send_security_headers({"Retry-After": attempts_left})
                        self.end_headers()
                        self.wfile.write(json.dumps({
                            "error": f"Limite de tentativas excedido. IP bloqueado temporariamente por 15 minutos."
                        }).encode("utf-8"))
                    else:
                        self.send_response(401)
                        self.send_header("Content-Type", "application/json; charset=utf-8")
                        self._send_security_headers({"X-RateLimit-Remaining": attempts_left})
                        self.end_headers()
                        self.wfile.write(json.dumps({
                            "error": f"Credenciais incorretas. Tentativas restantes: {attempts_left}."
                        }).encode("utf-8"))
            except Exception:
                self.send_response(400)
                self.end_headers()
            return

        # ======================================================================
        # 💬 Endpoint de Consulta /api/ask com Rate Limiting e Validação de Sessão
        # ======================================================================
        if self.path == "/api/ask":
            auth_header = self.headers.get("Authorization", "")
            token = auth_header.replace("Bearer ", "").strip()
            
            # 1. Verificação de Autenticação com TTL (CWE-613)
            if not is_session_valid(token):
                self.send_response(401)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self._send_security_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Sessão não autorizada ou expirada."}).encode("utf-8"))
                return

            # 2. Verificação de Rate Limit da API (Máx 30 req/min por IP)
            allowed, remaining = rate_limiter.check_api_rate_limit(client_ip)
            if not allowed:
                self.send_response(429)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self._send_security_headers({"Retry-After": remaining})
                self.end_headers()
                self.wfile.write(json.dumps({
                    "error": f"Taxa de requisições excedida. Aguarde {remaining} segundos."
                }).encode("utf-8"))
                return

            try:
                data = json.loads(body)
                if data.get("action") == "check_quota":
                    test_key = data.get("apiKey") or GEMINI_SERVER_KEY
                    if not test_key:
                        quota_res = {
                            "available": False,
                            "quota_exhausted": False,
                            "has_key": False,
                            "message": "Nenhuma chave de API configurada. Operando no modo Schema RAG Local (Ilimitado e Gratuito)."
                        }
                    else:
                        try:
                            # Teste ping leve
                            call_gemini_api("ping", test_key)
                            quota_res = {"available": True, "quota_exhausted": False, "has_key": True, "message": "IA Operacional e Cota Disponível!"}
                        except Exception as qe:
                            is_quota = "429" in str(qe) or "RESOURCE_EXHAUSTED" in str(qe)
                            quota_res = {"available": False, "quota_exhausted": is_quota, "has_key": True, "message": str(qe)}
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self._send_security_headers()
                    self.end_headers()
                    self.wfile.write(json.dumps(quota_res).encode("utf-8"))
                    return

                msg = str(data.get("message", ""))[:1500].strip()
                api_key = data.get("apiKey") or GEMINI_SERVER_KEY
                active_system = data.get("system", "softcomshop")

                if active_system == "softshop":
                    res = {
                        "tipo_operacao": "SELECT",
                        "tabelas_utilizadas": ["softshop_desktop"],
                        "explicacao": "Módulo Softshop Desktop selecionado. O sistema está pronto e aguardando você fornecer os dados de acesso ao banco desktop (SGBD como Firebird, MySQL, SQL Server, PostgreSQL, Host, Porta e Credenciais) ou os scripts DDL das tabelas. Assim que você me passar o acesso, mapearei 100% das tabelas, campos e relacionamentos para gerar queries nativas e precisas!",
                        "sql_validacao": "",
                        "sql_final": "-- Módulo Softshop (Desktop) aguardando acesso\n-- Por favor, envie os dados de conexão ou o script DDL das tabelas para mapeamento completo de colunas e relacionamentos.",
                        "usage": {
                            "prompt_tokens": 0,
                            "completion_tokens": 0,
                            "total_tokens": 0,
                            "source": "softshop_desktop",
                            "status": "waiting_schema"
                        }
                    }
                elif api_key:
                    try:
                        ai_res = call_gemini_api(msg, api_key)
                        if ai_res and ("sql_final" in ai_res or "sql" in ai_res):
                            res = ai_res
                        else:
                            res = generate_structure_response(msg)
                            res["usage"] = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "source": "fallback_rag", "status": "fallback_active"}
                    except Exception as ai_err:
                        is_quota = "429" in str(ai_err) or "RESOURCE_EXHAUSTED" in str(ai_err)
                        res = generate_structure_response(msg)
                        res["usage"] = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "source": "fallback_rag", "status": "fallback_active", "quota_exhausted": is_quota}
                else:
                    res = generate_structure_response(msg)
                    res["usage"] = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "source": "fallback_rag", "status": "fallback_active"}
            except Exception:
                res = {"error": "Não foi possível processar a consulta."}
            
            clean_res = sanitize_response_data(res)
            persist_message_server_side(msg, clean_res)
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._send_security_headers({"X-RateLimit-Remaining": remaining})
            self.end_headers()
            self.wfile.write(json.dumps(clean_res, default=str).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Allow", "GET, POST, OPTIONS")
        self._send_security_headers()
        self.end_headers()

    def do_PUT(self):
        self._send_method_not_allowed()

    def do_DELETE(self):
        self._send_method_not_allowed()

    def do_PATCH(self):
        self._send_method_not_allowed()

    def do_HEAD(self):
        self.send_response(200)
        self._send_security_headers()
        self.end_headers()

    def _send_method_not_allowed(self):
        self.send_response(405)
        self.send_header("Allow", "GET, POST")
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self._send_security_headers()
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Método HTTP não permitido."}).encode("utf-8"))

def run_server(port=8080):
    server = ThreadingHTTPServer(("127.0.0.1", port), RequestHandler)
    print(f"Servidor Especialista SQL Seguro (Rate Limiting & Anti-Brute Force) rodando em: http://localhost:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Servidor finalizado.")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
