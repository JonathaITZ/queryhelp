-- ======================================================================
-- 🚀 SCRIPT COMPLETO DE TABELAS E ESTRUTURA NO SUPABASE
-- Projeto: Especialista SQL • by Jonatha Dantas
-- ======================================================================

-- 1. Tabela para armazenar todas as 459 Tabelas e 6.600 Campos do Banco
CREATE TABLE IF NOT EXISTS public.schema_tables (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_name TEXT UNIQUE NOT NULL,
    column_count INT NOT NULL,
    columns JSONB DEFAULT '[]'::jsonb,
    foreign_keys JSONB DEFAULT '[]'::jsonb,
    primary_keys JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Tabela de Histórico de Mensagens e Consultas Geradas
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

-- 3. Tabela de Consultas Salvas
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

-- 4. Habilitar RLS com Políticas de Segurança
ALTER TABLE public.schema_tables ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.chat_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.saved_queries ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Permitir leitura anon em schema_tables" ON public.schema_tables;
DROP POLICY IF EXISTS "Permitir insercao anon em chat_messages" ON public.chat_messages;
DROP POLICY IF EXISTS "Permitir leitura anon em saved_queries" ON public.saved_queries;

CREATE POLICY "Permitir leitura anon em schema_tables"
    ON public.schema_tables FOR SELECT TO anon USING (true);

CREATE POLICY "Permitir insercao anon em chat_messages"
    ON public.chat_messages FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY "Permitir leitura anon em saved_queries"
    ON public.saved_queries FOR SELECT TO anon USING (true);
