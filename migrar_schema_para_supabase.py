"""
Migrador do Schema Completo (459 Tabelas e 6.600 Colunas) para o Supabase
Desenvolvido por Jonatha Dantas (by Dantas)
"""
import os
import json
import urllib.request
import urllib.error

SCHEMA_FILE = r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\schema_complete.json"
SUPABASE_URL = "https://qqgszvnjnvcxbqbxifve.supabase.co/rest/v1/schema_tables"
SECRET_KEY = "sb_secret_NooW3WtF3PabZJSzZZscxg_wXoYRmOo"

def migrate_all_tables():
    if not os.path.exists(SCHEMA_FILE):
        print("Arquivo de schema não encontrado.")
        return

    with open(SCHEMA_FILE, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    tables = data.get("tables", [])
    print(f"Total de tabelas a migrar para o Supabase: {len(tables)}")

    # Preparar payload em lotes de 50 tabelas para alta performance
    batch_size = 50
    total_migrated = 0

    for i in range(0, len(tables), batch_size):
        batch = tables[i:i + batch_size]
        payload = []
        for t in batch:
            payload.append({
                "table_name": t.get("name"),
                "column_count": len(t.get("columns", [])),
                "columns": t.get("columns", []),
                "foreign_keys": t.get("foreign_keys", []),
                "primary_keys": t.get("primary_keys", [])
            })

        req = urllib.request.Request(
            SUPABASE_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "apikey": SECRET_KEY,
                "Authorization": f"Bearer {SECRET_KEY}",
                "Content-Type": "application/json",
                "Prefer": "resolution=merge-duplicates"
            }
        )

        try:
            with urllib.request.urlopen(req) as res:
                total_migrated += len(batch)
                print(f"Progresso: {total_migrated}/{len(tables)} tabelas migradas com sucesso para o Supabase!")
        except urllib.error.HTTPError as e:
            print(f"Erro HTTP no lote {i}-{i+batch_size}: {e.code} - {e.read().decode('utf-8')}")
            return False
        except Exception as e:
            print(f"Erro no lote: {e}")
            return False

    print(f"\n Migração Concluída! Todas as {total_migrated} tabelas e seus campos agora estão 100% no Supabase!")
    return True

if __name__ == "__main__":
    migrate_all_tables()
