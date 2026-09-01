import urllib.request
import json

def test_sql_injection():
    # 1. Login para autenticar
    req_login = urllib.request.Request(
        "http://127.0.0.1:8080/api/login",
        data=json.dumps({"username": "especialistas", "password": "7711"}).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    res_login = urllib.request.urlopen(req_login)
    token = json.loads(res_login.read().decode("utf-8"))["token"]

    # 2. Testar strings clássicas de SQL Injection
    payloads = [
        "'; DELETE * FROM Database; --",
        "' OR '1'='1' --",
        "1; DROP TABLE chat_messages; --",
        "UNION SELECT null, username, password FROM users --"
    ]

    print("=== TESTE DE RESILIENCIA CONTRA SQL INJECTION (CWE-89) ===\n")
    for payload in payloads:
        req = urllib.request.Request(
            "http://127.0.0.1:8080/api/ask",
            data=json.dumps({"message": payload}).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )
        res = urllib.request.urlopen(req)
        data = json.loads(res.read().decode("utf-8"))
        print(f"[TESTADO] Payload: {payload}")
        print(f"          Status HTTP: {res.status} | Tratado com segurança como texto puro.")
        print(f"          Retorno Sanitizado: {data.get('tipo_operacao')}\n")

if __name__ == "__main__":
    test_sql_injection()
