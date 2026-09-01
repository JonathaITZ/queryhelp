"""
Módulo utilitário Python para interação ágil e direta com o banco de dados
softcoms_softcomshop_lanchoneteerestaurantepotira
"""
import sys
import os
import json
import pymysql
import pymysql.cursors
from tabulate import tabulate

# Força UTF-8 no stdout do Windows
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

def get_connection():
    return pymysql.connect(**DB_CONFIG)

def query(sql, params=None, print_table=True):
    """Executa uma consulta SELECT e retorna lista de dicionários."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            results = cursor.fetchall()
            if print_table:
                if results:
                    print(tabulate(results, headers="keys", tablefmt="grid"))
                    print(f"\nTotal de registros: {len(results)}")
                else:
                    print("Nenhum registro encontrado.")
            return results
    finally:
        conn.close()

def execute(sql, params=None):
    """Executa um comando INSERT/UPDATE/DELETE e retorna linhas afetadas."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            affected = cursor.execute(sql, params)
            conn.commit()
            print(f"Comando executado com sucesso. Linhas afetadas: {affected}")
            return affected
    except Exception as e:
        conn.rollback()
        print(f"Erro na execução (Rollback executado): {e}")
        raise e
    finally:
        conn.close()

def describe_table(table_name):
    """Exibe a estrutura de uma tabela a partir do schema local mapeado."""
    schema_path = r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\schema.json"
    with open(schema_path, "r", encoding="utf-8-sig") as f:
        schema = json.load(f)
    
    found = False
    for t in schema["Tables"]:
        if t["Name"].lower() == table_name.lower():
            found = True
            print(f"\n[TABELA] {t['Name']} ({t['Type']})")
            print(f"Linhas estimadas: {t['Rows']} | Colunas: {len(t['Columns'])}")
            cols = []
            for c in t["Columns"]:
                cols.append({
                    "#": c["Position"],
                    "Coluna": c["Name"],
                    "Tipo": c["FullType"],
                    "Nulo": "SIM" if c["Nullable"] else "NAO",
                    "Chave": c["Key"] if c["Key"] else "-",
                    "Padrao": c["Default"] if c["Default"] is not None else "NULL",
                    "Extra": c["Extra"] if c["Extra"] else "-"
                })
            print(tabulate(cols, headers="keys", tablefmt="grid"))
            break
    
    if not found:
        print(f"Tabela '{table_name}' nao encontrada no schema mapeado.")

def search_columns(keyword):
    """Busca tabelas que contenham colunas com determinada palavra-chave."""
    schema_path = r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\schema.json"
    with open(schema_path, "r", encoding="utf-8-sig") as f:
        schema = json.load(f)
    
    matches = []
    kw = keyword.lower()
    for t in schema["Tables"]:
        for c in t["Columns"]:
            if kw in c["Name"].lower():
                matches.append({
                    "Tabela": t["Name"],
                    "Coluna": c["Name"],
                    "Tipo": c["FullType"],
                    "Chave": c["Key"]
                })
    
    if matches:
        print(f"\n[BUSCA] Colunas encontradas contendo '{keyword}':")
        print(tabulate(matches, headers="keys", tablefmt="grid"))
        print(f"\nTotal: {len(matches)} colunas encontradas.")
    else:
        print(f"Nenhuma coluna contendo '{keyword}' foi encontrada.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "describe" and len(sys.argv) > 2:
            describe_table(sys.argv[2])
        elif cmd == "search" and len(sys.argv) > 2:
            search_columns(sys.argv[2])
        elif cmd == "query" and len(sys.argv) > 2:
            query(" ".join(sys.argv[2:]))
        else:
            print("Uso:")
            print("  python potira_db.py describe <tabela>")
            print("  python potira_db.py search <termo_coluna>")
            print("  python potira_db.py query <sql_query>")
    else:
        print("Testando conexao via Python...")
        query("SELECT id, nome, fantasia, cnpj FROM empresa LIMIT 1;")
