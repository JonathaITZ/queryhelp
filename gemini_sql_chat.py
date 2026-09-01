"""
Chat Interativo Gemini -> SQL para o banco Softcomshop / Potira
Gera consultas SQL a partir de linguagem natural e permite executá-las no banco.
"""
import os
import sys
import json
import urllib.request
import urllib.error
import pymysql
import pymysql.cursors
from tabulate import tabulate

# Força UTF-8 no stdout
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DB_CONFIG = {
    "host": "softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com",
    "port": 3306,
    "user": "patrick.morais",
    "password": "sq6j7dDW53pm",
    "database": "softcoms_softcomshop_lanchoneteerestaurantepotira",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
    "connect_timeout": 10
}

SYSTEM_PROMPT = """
Você é o Especialista Sênior em SQL e Engenharia de Dados do banco MySQL 'softcoms_softcomshop_lanchoneteerestaurantepotira'.
Seu papel exclusivo é responder com a consulta SQL MySQL mais eficiente, correta e segura para atender à solicitação do usuário.

Diretrizes:
- SGBD: MySQL 8.0
- Sempre considere deleted_at IS NULL onde aplicável
- Sempre filtre por empresa_id = 1 (ou conforme solicitado)
- Utilize alias legíveis e formatação SQL limpa
- Responda OBRIGATORIAMENTE no formato JSON com duas chaves:
  "sql": "consulta SQL aqui",
  "explicacao": "breve explicação em português da lógica da query"
"""

def call_gemini_api(user_message, api_key):
    """Envia o prompt para a API do Google Gemini e extrai o SQL gerado."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "system_instruction": {
            "parts": [{"text": SYSTEM_PROMPT}]
        },
        "contents": [
            {
                "parts": [{"text": f"Gere uma consulta SQL MySQL para: {user_message}"}]
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
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            text = res_data["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(text)
    except urllib.error.HTTPError as e:
        print(f"\n[Erro na API do Gemini]: HTTP {e.code} - {e.read().decode('utf-8')}")
        return None
    except Exception as e:
        print(f"\n[Erro]: {e}")
        return None

def execute_query(sql):
    """Executa a consulta no banco de dados e exibe a tabela formatada."""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows:
                print("\n" + tabulate(rows, headers="keys", tablefmt="grid"))
                print(f"\nTotal de registros retornados: {len(rows)}")
            else:
                print("\n[Resultado]: A consulta não retornou nenhum registro.")
        conn.close()
    except Exception as e:
        print(f"\n[Erro ao executar no MySQL]: {e}")

def main():
    print("=" * 70)
    print("  🤖 Assistente Gemini Especialista em Consultas SQL - Softcomshop")
    print("=" * 70)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = input("\nInforme sua GEMINI_API_KEY (ou pressione ENTER se já estiver salva): ").strip()
        if not api_key:
            print("Chave API não informada. O assistente requer uma chave Gemini API para conectar.")
            return

    print("\nDigite sua pergunta em linguagem natural (ex: 'vendas em dinheiro', 'produtos mais vendidos').")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        try:
            pergunta = input("\n💬 Pergunta: ").strip()
            if not pergunta:
                continue
            if pergunta.lower() in ["sair", "exit", "quit"]:
                print("Até logo!")
                break
            
            print("\n⏳ Consultando o Gemini para gerar o SQL...")
            result = call_gemini_api(pergunta, api_key)
            if not result:
                continue
            
            sql = result.get("sql", "").strip()
            explicacao = result.get("explicacao", "").strip()
            
            print("\n📝 [SQL Gerado]:")
            print("-" * 50)
            print(sql)
            print("-" * 50)
            print(f"💡 [Explicação]: {explicacao}")
            
            executar = input("\nDeseja executar esta consulta no banco agora? (s/n): ").strip().lower()
            if executar in ["s", "sim", "y", "yes"]:
                execute_query(sql)
                
        except KeyboardInterrupt:
            print("\nEncerrado.")
            break

if __name__ == "__main__":
    main()
