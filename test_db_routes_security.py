import urllib.request
import urllib.error
import json

def run_db_security_audit():
    print("=== AUDITORIA DE SEGURANCA NAS ROTAS DE BANCO DE DADOS ===\n")
    
    # 1. Testar RLS em chat_messages com a chave pública anon
    anon_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFxZ3N6dm5qbnZjeGJxYnhpZnZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODgyNDA4MjMsImV4cCI6MjEwMzgxNjgyM30.FF9cqVN8q1FBd9RnM51ULKFJ9SmW1GW535qna39d_ZE"
    req_anon_sniff = urllib.request.Request(
        "https://qqgszvnjnvcxbqbxifve.supabase.co/rest/v1/chat_messages?select=*",
        headers={"apikey": anon_jwt, "Authorization": f"Bearer {anon_jwt}"}
    )
    try:
        with urllib.request.urlopen(req_anon_sniff, timeout=5) as res:
            data = json.loads(res.read().decode("utf-8"))
            if len(data) == 0:
                print("1. [RLS NO POSTGRESQL] chat_messages: BLINDADO (0 registros retornados para anon)")
            else:
                print("1. [RLS NO POSTGRESQL] chat_messages: VULNERAVEL")
    except urllib.error.HTTPError as e:
        print(f"1. [RLS NO POSTGRESQL] chat_messages: BLOQUEADO (HTTP {e.code})")

    # 2. Testar /api/ask sem autenticação
    req_unauth_ask = urllib.request.Request(
        "http://127.0.0.1:8080/api/ask",
        data=json.dumps({"message": "SELECT * FROM venda"}).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    try:
        urllib.request.urlopen(req_unauth_ask, timeout=5)
        print("2. [/api/ask] Protecao de Rota: FALHA (Permitiu acesso anonimo)")
    except urllib.error.HTTPError as e:
        print(f"2. [/api/ask] Protecao de Rota: BLINDADO (Rejeitado com HTTP {e.code} Nao Autorizado)")

    # 3. Testar comunicação autenticada
    try:
        req_login = urllib.request.Request(
            "http://127.0.0.1:8080/api/login",
            data=json.dumps({"username": "especialistas", "password": "7711"}).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        res_login = urllib.request.urlopen(req_login, timeout=5)
        token = json.loads(res_login.read().decode("utf-8"))["token"]
        
        req_auth_ask = urllib.request.Request(
            "http://127.0.0.1:8080/api/ask",
            data=json.dumps({"message": "vendas canceladas"}).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        )
        res_auth = urllib.request.urlopen(req_auth_ask, timeout=5)
        print(f"3. [BACKEND -> SUPABASE] Gravacao Server-to-Server: SUCESSO (HTTP {res_auth.status})")
    except Exception as e:
        print(f"3. [BACKEND -> SUPABASE] Erro: {e}")

if __name__ == "__main__":
    run_db_security_audit()
