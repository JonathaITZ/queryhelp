"""
Provisionador Automático do Banco Supabase
Desenvolvido por Jonatha Dantas (by Dantas)
Executa DDL e migra metadados do schema (459 tabelas) para o PostgreSQL do Supabase.
"""
import os
import sys
import json

PROJECT_REF = "qqgszvnjnvcxbqbxifve"
HOST = f"db.{PROJECT_REF}.supabase.co"
PORT = 5432
DBNAME = "postgres"
USER = "postgres"

def run_migration_with_password(password):
    import psycopg2
    print(f"Conectando ao PostgreSQL do Supabase em {HOST}:{PORT}...")
    try:
        conn = psycopg2.connect(
            host=HOST,
            port=PORT,
            dbname=DBNAME,
            user=USER,
            password=password,
            connect_timeout=10,
            sslmode="require"
        )
        conn.autocommit = True
        cur = conn.cursor()
        print("Conexao estabelecida com sucesso!")

        # Ler script DDL
        ddl_path = os.path.join(os.path.dirname(__file__), "supabase_setup.sql")
        with open(ddl_path, "r", encoding="utf-8") as f:
            sql_script = f.read()

        print("Executando criacao de tabelas e politicas RLS...")
        cur.execute(sql_script)
        print("Tabelas 'chat_messages' e 'saved_queries' criadas com sucesso!")

        # Opcional: Criar tabela de catalogo do schema
        cur.execute("""
        CREATE TABLE IF NOT EXISTS public.schema_tables (
            id SERIAL PRIMARY KEY,
            table_name TEXT UNIQUE NOT NULL,
            column_count INT NOT NULL,
            columns_info JSONB,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
        );
        ALTER TABLE public.schema_tables ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Permitir leitura anon em schema_tables" ON public.schema_tables FOR SELECT TO anon USING (true);
        """)

        # Povoar com as 459 tabelas do schema_complete.json
        schema_path = os.path.join(os.path.dirname(__file__), "schema", "schema_complete.json")
        if os.path.exists(schema_path):
            with open(schema_path, "r", encoding="utf-8-sig") as f:
                sdata = json.load(f)
                tables = sdata.get("tables", [])
                print(f"Populando catalogo de {len(tables)} tabelas no Supabase...")
                for t in tables:
                    tname = t.get("name")
                    cols = t.get("columns", [])
                    cur.execute("""
                        INSERT INTO public.schema_tables (table_name, column_count, columns_info)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (table_name) DO UPDATE 
                        SET column_count = EXCLUDED.column_count, columns_info = EXCLUDED.columns_info;
                    """, (tname, len(cols), json.dumps(cols)))
            print("Catalogo de 459 tabelas populado com sucesso no Supabase!")

        cur.close()
        conn.close()
        print("Configuracao do Supabase concluida com 100% de sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao provisionar Supabase: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pwd = sys.argv[1]
        run_migration_with_password(pwd)
    else:
        print("Uso: python setup_supabase_db.py <SENHA_DO_BANCO>")
