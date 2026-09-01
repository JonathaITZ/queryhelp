"""
Mecanismo Inteligente de Busca Semântica e Geração de Consultas SQL
Sobre o Catálogo Completo de 459 Tabelas e 6.600 Campos
"""
import re

STOPWORDS = {
    "quero", "uma", "query", "querry", "consulta", "tabela", "tabelas", "traga", "todas", "todos",
    "com", "informacao", "informações", "relacionadas", "relacionada", "relacionados", "relacionado",
    "ao", "a", "o", "os", "as", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "para", "por", "que", "seja", "mostrar", "mostre", "ver", "quais", "qual", "como", "fazer",
    "gerar", "cria", "criar", "me", "de", "um", "uns", "umas"
}

def extract_keywords(prompt_text):
    # Limpa pontuação e acentos
    text = prompt_text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    tokens = text.split()
    meaningful = [t for t in tokens if t not in STOPWORDS and len(t) > 2]
    return meaningful

def search_schema_tables(schema_dict, keywords):
    scores = {}
    
    # Mapeamento de sinônimos e tópicos frequentes
    synonyms = {
        "marketplace": ["market", "ifood", "delivery", "integrac", "ecom", "origem", "canal"],
        "mercado": ["marketplace", "market"],
        "ifood": ["ifood", "delivery", "marketplace", "integrac"],
        "delivery": ["delivery", "ifood", "entregador", "mesa", "restaurante"],
        "fiscal": ["nfe", "nfce", "nota_fiscal", "icms", "pis", "cofins", "imposto", "tribut"],
        "nfe": ["nota_fiscal_eletronica", "nfe", "chave_nfe", "recibo_situacao"],
        "nfce": ["nfce", "nota_fiscal", "contingencia"],
        "financeiro": ["financeiro", "parcela", "pagamento", "caixa", "banco", "contas_receber", "contas_pagar"],
        "pagamento": ["forma_pagamento", "venda_cartao", "parcela", "financeiro"],
        "estoque": ["estoque", "produto_estoque", "almoxarifado", "movimentacao_estoque"],
        "produto": ["produto", "grade", "codigo_barra", "preco", "categoria", "grupo"],
        "cliente": ["cliente", "pessoa", "endereco", "contato"],
        "usuario": ["usuario", "funcionario", "permissao", "acesso", "log"],
        "venda": ["venda", "venda_item", "pedido", "faturamento"]
    }

    expanded_keywords = set(keywords)
    for kw in keywords:
        for root_term, syn_list in synonyms.items():
            if kw in root_term or root_term in kw:
                expanded_keywords.update(syn_list)

    for table_name, t_data in schema_dict.items():
        score = 0
        cols = t_data.get("columns", [])
        col_names = [c["name"].lower() if isinstance(c, dict) else str(c).lower() for c in cols]
        
        # 1. Match direto no nome da tabela
        for kw in expanded_keywords:
            if kw in table_name.lower():
                score += 15
            # Match em colunas
            matched_cols = [c for c in col_names if kw in c]
            score += len(matched_cols) * 3

        if score > 0:
            scores[table_name] = (score, t_data)

    sorted_tables = sorted(scores.items(), key=lambda x: x[1][0], reverse=True)
    return sorted_tables

# Teste com 'marketplace'
if __name__ == "__main__":
    import json
    with open(r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\schema_complete.json", "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    schema_map = {t["name"]: t for t in data["tables"]}
    
    prompt = "Quero uma querry que traga todas as tabelas com informação relacionadas ao marketplace"
    kws = extract_keywords(prompt)
    print("Keywords extraídas:", kws)
    results = search_schema_tables(schema_map, kws)
    print("Top tabelas encontradas:", [t[0] for t in results[:10]])
