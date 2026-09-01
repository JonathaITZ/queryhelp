import urllib.request
import urllib.error
import json

secret = 'sb_secret_NooW3WtF3PabZJSzZZscxg_wXoYRmOo'

sql = """
CREATE TABLE IF NOT EXISTS public.chat_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id TEXT NOT NULL DEFAULT 'default-session',
    user_prompt TEXT NOT NULL,
    tipo_operacao TEXT DEFAULT 'SELECT',
    sql_validacao TEXT,
    sql_final TEXT,
    tabelas_utilizadas JSONB DEFAULT '[]'::jsonb,
    explicacao TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.saved_queries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    titulo TEXT NOT NULL,
    descricao TEXT,
    categoria TEXT DEFAULT 'Geral',
    tipo_operacao TEXT DEFAULT 'SELECT',
    sql_query TEXT NOT NULL,
    tabelas JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

ALTER TABLE public.chat_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.saved_queries ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Permitir insercao anon em chat_messages" ON public.chat_messages;
DROP POLICY IF EXISTS "Permitir leitura anon em saved_queries" ON public.saved_queries;

CREATE POLICY "Permitir insercao anon em chat_messages" ON public.chat_messages FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY "Permitir leitura anon em saved_queries" ON public.saved_queries FOR SELECT TO anon USING (true);
"""

endpoints = [
    ('https://api.supabase.com/v1/projects/qqgszvnjnvcxbqbxifve/database/query', {'query': sql}),
    ('https://qqgszvnjnvcxbqbxifve.supabase.co/pg/query', {'query': sql})
]

for ep, body in endpoints:
    try:
        req = urllib.request.Request(
            ep,
            data=json.dumps(body).encode('utf-8'),
            headers={
                'apikey': secret,
                'Authorization': f'Bearer {secret}',
                'Content-Type': 'application/json'
            }
        )
        with urllib.request.urlopen(req) as res:
            print(f"Sucesso em {ep}: {res.read().decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} em {ep}: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"Erro em {ep}: {e}")
