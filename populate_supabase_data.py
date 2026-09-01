"""
Script de Carga de Dados no Supabase via REST API (Secret Key)
Desenvolvido por Jonatha Dantas (by Dantas)
"""
import urllib.request
import urllib.error
import json

SUPABASE_URL = "https://qqgszvnjnvcxbqbxifve.supabase.co/rest/v1"
SECRET_KEY = "sb_secret_NooW3WtF3PabZJSzZZscxg_wXoYRmOo"

DEFAULT_QUERIES = [
    {
        "titulo": "Auditoria de Vendas em Contingência (Rejeição 865 SEFAZ)",
        "descricao": "Identifica vendas em contingência e compara o total da venda com o total das parcelas financeiras para encontrar diferenças de centavos.",
        "categoria": "Fiscal / SEFAZ",
        "tipo_operacao": "SELECT",
        "sql_query": """SELECT 
    v.id AS venda_id,
    v.valor_total AS total_venda,
    v.total_pagamento AS total_pago_venda,
    COALESCE(SUM(fp.valor_parcela), 0) AS total_parcelas,
    ROUND(v.valor_total - COALESCE(SUM(fp.valor_parcela), 0), 4) AS diferenca_parcelas,
    nfe.id AS nfe_id,
    nfe.numero_nfe,
    nfe.recibo_situacao,
    nfe.mensagem_erro
FROM venda v
INNER JOIN nota_fiscal_eletronica nfe ON v.nfe_id = nfe.id
LEFT JOIN financeiro_parcela fp ON fp.venda_id = v.id AND fp.deleted_at IS NULL
WHERE nfe.recibo_situacao = 'CONTINGENCIA'
GROUP BY v.id, v.valor_total, v.total_pagamento, nfe.id, nfe.numero_nfe, nfe.recibo_situacao, nfe.mensagem_erro
ORDER BY v.id DESC;""",
        "tabelas": ["venda", "nota_fiscal_eletronica", "financeiro_parcela"]
    },
    {
        "titulo": "Cancelamento Seguro de Venda (Soft Delete com Transação)",
        "descricao": "Comando seguro em duas etapas para inativação lógica de venda preservando histórico e auditoria fiscal.",
        "categoria": "Vendas / DML",
        "tipo_operacao": "DELETE",
        "sql_query": """-- 1ª Etapa (Validação prévia):
SELECT id, status, valor_total, total_pagamento, api_data_hora_venda, deleted_at 
FROM venda WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;

-- 2ª Etapa (Execução com Transação):
START TRANSACTION;
UPDATE venda SET deleted_at = NOW(), status = 'CANCELADA', updated_at = NOW() 
WHERE id = 100 AND empresa_id = 1 AND deleted_at IS NULL;
COMMIT;""",
        "tabelas": ["venda"]
    },
    {
        "titulo": "Ranking dos Top 10 Produtos Mais Vendidos e Faturamento",
        "descricao": "Totaliza a quantidade comercializada e o faturamento real líquido por produto.",
        "categoria": "Estoque & Vendas",
        "tipo_operacao": "SELECT",
        "sql_query": """SELECT 
    p.id AS produto_id,
    p.nome AS produto_nome,
    p.referencia,
    SUM(vi.quantidade) AS total_quantidade_vendida,
    ROUND(SUM(vi.quantidade * vi.preco - COALESCE(vi.desconto_valor_item, 0) + COALESCE(vi.acrescimo_valor_item, 0)), 2) AS total_faturado
FROM venda_item vi
INNER JOIN venda v ON vi.venda_id = v.id
INNER JOIN produto p ON vi.produto_id = p.id
WHERE v.deleted_at IS NULL AND vi.deleted_at IS NULL
GROUP BY p.id, p.nome, p.referencia
ORDER BY total_quantidade_vendida DESC
LIMIT 10;""",
        "tabelas": ["venda", "venda_item", "produto"]
    },
    {
        "titulo": "Faturamento Agrupado por Forma de Pagamento (PIX, Cartão, Dinheiro)",
        "descricao": "Demonstrativo financeiro com quantidade de títulos e volume recebido por meio de pagamento.",
        "categoria": "Financeiro",
        "tipo_operacao": "SELECT",
        "sql_query": """SELECT 
    fp.id AS forma_pagamento_id,
    fp.nome AS forma_pagamento,
    fp.tipo,
    COUNT(p.id) AS qtd_parcelas,
    ROUND(SUM(p.valor_parcela), 2) AS total_parcelado,
    ROUND(SUM(p.valor_pago), 2) AS total_pago_recebido
FROM forma_pagamento fp
INNER JOIN financeiro_parcela p ON p.forma_pagamento_id = fp.id
WHERE p.deleted_at IS NULL AND p.cancelada = 0
GROUP BY fp.id, fp.nome, fp.tipo
ORDER BY total_pago_recebido DESC;""",
        "tabelas": ["forma_pagamento", "financeiro_parcela"]
    },
    {
        "titulo": "Relatório de Inadimplência e Contas a Receber Vencidas",
        "descricao": "Identifica títulos em aberto por cliente ordenados pela data de vencimento.",
        "categoria": "Financeiro / Cobrança",
        "tipo_operacao": "SELECT",
        "sql_query": """SELECT 
    fp.id AS parcela_id,
    fp.venda_id,
    c.nome AS cliente_nome,
    c.cpf_cnpj,
    fp.parcela,
    fp.vencimento,
    fp.valor_parcela,
    fp.valor_pago,
    ROUND(fp.valor_parcela - COALESCE(fp.valor_pago, 0), 2) AS saldo_devedor
FROM financeiro_parcela fp
INNER JOIN cliente c ON fp.cliente_id = c.id
WHERE fp.deleted_at IS NULL 
  AND fp.cancelada = 0 
  AND (fp.valor_parcela - COALESCE(fp.valor_pago, 0)) > 0.01
ORDER BY fp.vencimento ASC;""",
        "tabelas": ["financeiro_parcela", "cliente"]
    }
]

def check_and_populate():
    url = f"{SUPABASE_URL}/saved_queries"
    req = urllib.request.Request(
        url,
        data=json.dumps(DEFAULT_QUERIES).encode("utf-8"),
        headers={
            "apikey": SECRET_KEY,
            "Authorization": f"Bearer {SECRET_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }
    )
    try:
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode("utf-8"))
            print(f"Sucesso! {len(data)} consultas padrao foram inseridas no Supabase!")
            return True
    except urllib.error.HTTPError as e:
        print(f"Status HTTP {e.code}: {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"Erro: {e}")
        return False

if __name__ == "__main__":
    check_and_populate()
