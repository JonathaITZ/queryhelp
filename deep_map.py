"""
Mapeador Profundo do Banco de Dados Softcomshop
Gera schema_complete.json, schema_relacionamentos.md e potira_models.py
"""
import os
import json
import pymysql
import pymysql.cursors

DB_CONFIG = {
    "host": "softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com",
    "port": 3306,
    "user": "patrick.morais",
    "password": "sq6j7dDW53pm",
    "database": "softcoms_softcomshop_lanchoneteerestaurantepotira",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
    "connect_timeout": 30
}

conn = pymysql.connect(**DB_CONFIG)
schema_dir = r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema"
os.makedirs(schema_dir, exist_ok=True)

print("Iniciando mapeamento profundo de tabelas, colunas, índices e relacionamentos...")

with conn.cursor() as cursor:
    # 1. Tabelas
    cursor.execute("""
        SELECT 
            TABLE_NAME, TABLE_TYPE, ENGINE, TABLE_ROWS, DATA_LENGTH, 
            INDEX_LENGTH, AUTO_INCREMENT, CREATE_TIME, TABLE_COLLATION, TABLE_COMMENT 
        FROM information_schema.TABLES 
        WHERE TABLE_SCHEMA = 'softcoms_softcomshop_lanchoneteerestaurantepotira'
        ORDER BY TABLE_NAME;
    """)
    tables_raw = cursor.fetchall()
    
    # 2. Colunas
    cursor.execute("""
        SELECT 
            TABLE_NAME, COLUMN_NAME, ORDINAL_POSITION, COLUMN_DEFAULT, 
            IS_NULLABLE, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, 
            NUMERIC_SCALE, COLUMN_TYPE, COLUMN_KEY, EXTRA, COLUMN_COMMENT 
        FROM information_schema.COLUMNS 
        WHERE TABLE_SCHEMA = 'softcoms_softcomshop_lanchoneteerestaurantepotira'
        ORDER BY TABLE_NAME, ORDINAL_POSITION;
    """)
    columns_raw = cursor.fetchall()

    # 3. Índices
    cursor.execute("""
        SELECT 
            TABLE_NAME, NON_UNIQUE, INDEX_NAME, SEQ_IN_INDEX, 
            COLUMN_NAME, COLLATION, CARDINALITY, SUB_PART, PACKED, 
            NULLABLE, INDEX_TYPE, COMMENT, INDEX_COMMENT 
        FROM information_schema.STATISTICS 
        WHERE TABLE_SCHEMA = 'softcoms_softcomshop_lanchoneteerestaurantepotira'
        ORDER BY TABLE_NAME, INDEX_NAME, SEQ_IN_INDEX;
    """)
    indexes_raw = cursor.fetchall()

    # 4. Chaves Estrangeiras e Regras Referenciais
    cursor.execute("""
        SELECT 
            k.TABLE_NAME, k.COLUMN_NAME, k.CONSTRAINT_NAME, 
            k.REFERENCED_TABLE_NAME, k.REFERENCED_COLUMN_NAME,
            r.UPDATE_RULE, r.DELETE_RULE, r.MATCH_OPTION
        FROM information_schema.KEY_COLUMN_USAGE k
        INNER JOIN information_schema.REFERENTIAL_CONSTRAINTS r
            ON k.CONSTRAINT_NAME = r.CONSTRAINT_NAME
            AND k.CONSTRAINT_SCHEMA = r.CONSTRAINT_SCHEMA
        WHERE k.TABLE_SCHEMA = 'softcoms_softcomshop_lanchoneteerestaurantepotira'
          AND k.REFERENCED_TABLE_NAME IS NOT NULL
        ORDER BY k.TABLE_NAME, k.COLUMN_NAME;
    """)
    fks_raw = cursor.fetchall()

conn.close()

# Estruturar os dados
tables_dict = {}
for t in tables_raw:
    t_name = t["TABLE_NAME"]
    tables_dict[t_name] = {
        "name": t_name,
        "type": t["TABLE_TYPE"],
        "engine": t["ENGINE"],
        "rows_estimated": t["TABLE_ROWS"],
        "data_length_bytes": t["DATA_LENGTH"],
        "index_length_bytes": t["INDEX_LENGTH"],
        "auto_increment": t["AUTO_INCREMENT"],
        "collation": t["TABLE_COLLATION"],
        "comment": t["TABLE_COMMENT"],
        "columns": [],
        "indexes": {},
        "foreign_keys": [],
        "referenced_by": []
    }

for c in columns_raw:
    t_name = c["TABLE_NAME"]
    if t_name in tables_dict:
        tables_dict[t_name]["columns"].append({
            "name": c["COLUMN_NAME"],
            "position": c["ORDINAL_POSITION"],
            "default": c["COLUMN_DEFAULT"],
            "nullable": c["IS_NULLABLE"] == "YES",
            "data_type": c["DATA_TYPE"],
            "max_length": c["CHARACTER_MAXIMUM_LENGTH"],
            "numeric_precision": c["NUMERIC_PRECISION"],
            "numeric_scale": c["NUMERIC_SCALE"],
            "full_type": c["COLUMN_TYPE"],
            "key": c["COLUMN_KEY"],
            "extra": c["EXTRA"],
            "comment": c["COLUMN_COMMENT"]
        })

for idx in indexes_raw:
    t_name = idx["TABLE_NAME"]
    if t_name in tables_dict:
        idx_name = idx["INDEX_NAME"]
        if idx_name not in tables_dict[t_name]["indexes"]:
            tables_dict[t_name]["indexes"][idx_name] = {
                "name": idx_name,
                "unique": idx["NON_UNIQUE"] == 0,
                "type": idx["INDEX_TYPE"],
                "columns": []
            }
        tables_dict[t_name]["indexes"][idx_name]["columns"].append({
            "seq": idx["SEQ_IN_INDEX"],
            "column": idx["COLUMN_NAME"]
        })

for fk in fks_raw:
    t_name = fk["TABLE_NAME"]
    ref_t_name = fk["REFERENCED_TABLE_NAME"]
    fk_obj = {
        "constraint": fk["CONSTRAINT_NAME"],
        "column": fk["COLUMN_NAME"],
        "referenced_table": ref_t_name,
        "referenced_column": fk["REFERENCED_COLUMN_NAME"],
        "on_update": fk["UPDATE_RULE"],
        "on_delete": fk["DELETE_RULE"]
    }
    if t_name in tables_dict:
        tables_dict[t_name]["foreign_keys"].append(fk_obj)
    if ref_t_name in tables_dict:
        tables_dict[ref_t_name]["referenced_by"].append({
            "from_table": t_name,
            "from_column": fk["COLUMN_NAME"],
            "constraint": fk["CONSTRAINT_NAME"]
        })

# Salvar schema_complete.json
schema_complete = {
    "database": "softcoms_softcomshop_lanchoneteerestaurantepotira",
    "total_tables": len(tables_raw),
    "total_columns": len(columns_raw),
    "total_indexes": len(indexes_raw),
    "total_foreign_keys": len(fks_raw),
    "tables": list(tables_dict.values())
}

json_path = os.path.join(schema_dir, "schema_complete.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(schema_complete, f, indent=2, ensure_ascii=False)
print(f"Salvo schema_complete.json ({len(tables_raw)} tabelas, {len(columns_raw)} colunas, {len(fks_raw)} FKs)")

# Salvar schema_relacionamentos.md
rel_path = os.path.join(schema_dir, "schema_relacionamentos.md")
with open(rel_path, "w", encoding="utf-8") as f:
    f.write("# 🔗 Mapa Completo de Relacionamentos (Foreign Keys)\n\n")
    f.write(f"**Total de Chaves Estrangeiras:** {len(fks_raw)} | **Tabelas Relacionadas:** {len([t for t in tables_dict.values() if t['foreign_keys']])}\n\n")
    f.write("| Tabela Origem | Coluna Origem | ➔ | Tabela Destino | Coluna Destino | On Update | On Delete |\n")
    f.write("| :--- | :--- | :---: | :--- | :--- | :--- | :--- |\n")
    for fk in fks_raw:
        f.write(f"| `{fk['TABLE_NAME']}` | `{fk['COLUMN_NAME']}` | ➔ | `{fk['REFERENCED_TABLE_NAME']}` | `{fk['REFERENCED_COLUMN_NAME']}` | `{fk['UPDATE_RULE']}` | `{fk['DELETE_RULE']}` |\n")

print(f"Salvo schema_relacionamentos.md")

# Gerar arquivo de modelos Python para o projeto futuro (potira_models.py)
models_path = os.path.join(schema_dir, "potira_models.py")
with open(models_path, "w", encoding="utf-8") as f:
    f.write('"""\nModelos de dados gerados automaticamente a partir do schema de softcoms_softcomshop_lanchoneteerestaurantepotira\nProntos para uso em novos projetos Python / APIs.\n"""\n\n')
    f.write("from dataclasses import dataclass\nfrom typing import Optional, List, Dict, Any\nfrom datetime import datetime, date\nfrom decimal import Decimal\n\n")
    
    type_map = {
        "int": "int",
        "bigint": "int",
        "smallint": "int",
        "tinyint": "int",
        "varchar": "str",
        "char": "str",
        "text": "str",
        "longtext": "str",
        "mediumtext": "str",
        "decimal": "Decimal",
        "float": "float",
        "double": "float",
        "datetime": "datetime",
        "timestamp": "datetime",
        "date": "date",
        "time": "str",
        "enum": "str",
        "json": "Dict[str, Any]"
    }
    
    for t in tables_dict.values():
        class_name = "".join([part.capitalize() for part in t["name"].split("_") if part])
        if not class_name or class_name[0].isdigit():
            class_name = "Model_" + class_name
        
        f.write(f"@dataclass\nclass {class_name}:\n")
        f.write(f'    """Tabela: {t["name"]} (Linhas aprox: {t["rows_estimated"]})"""\n')
        
        if not t["columns"]:
            f.write("    pass\n\n")
            continue
            
        for c in t["columns"]:
            py_type = type_map.get(c["data_type"], "Any")
            if c["nullable"]:
                py_type = f"Optional[{py_type}] = None"
            f.write(f"    {c['name']}: {py_type}\n")
        f.write("\n")

print(f"Salvo potira_models.py com todas as classes mapeadas para novos projetos!")
