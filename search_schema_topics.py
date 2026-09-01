import json

with open(r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\schema_complete.json", "r", encoding="utf-8-sig") as f:
    data = json.load(f)

keywords = ["market", "ifood", "delivery", "integrac", "ecom", "origem", "loja_virtual", "app", "pedido", "canal"]
matching_tables = []

for t in data.get("tables", []):
    t_name = t["name"]
    col_names = [c["name"] for c in t.get("columns", [])]
    matched_cols = [c for c in col_names if any(k in c.lower() for k in keywords)]
    
    if any(k in t_name.lower() for k in keywords) or matched_cols:
        matching_tables.append({
            "table": t_name,
            "col_count": len(col_names),
            "matched_cols": matched_cols
        })

print(f"Total de tabelas relacionadas encontradas: {len(matching_tables)}")
for item in matching_tables:
    print(f"Tabela: {item['table']} -> Colunas: {item['matched_cols'][:6]}")
