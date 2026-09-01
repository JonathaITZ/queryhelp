"""
Pesquisa aprofundada dos fluxos de Clientes, Vendas, Fiscal e Financeiro
"""
import sys
sys.path.append(r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch")
from potira_db import query

print("=== 1. STATUS E ORIGENS DE VENDA ===")
query("""
SELECT status, origem_venda, tipo_lancamento, COUNT(*) as total
FROM venda
GROUP BY status, origem_venda, tipo_lancamento;
""")

print("\n=== 2. EXEMPLO DE FLUXO COMPLETO DE UMA VENDA FINALIZADA ===")
venda_ex = query("""
SELECT id, empresa_id, cliente_id, funcionario_id, nfe_id, valor_total, total_pagamento, total_desconto, total_acrescimo, status, origem_venda, api_data_hora_venda
FROM venda
WHERE id = 57;
""")

print("\n--- 2.1 Itens da Venda 57 ---")
query("""
SELECT id, venda_id, produto_id, quantidade, preco_unitario, preco_total, desconto_valor, acrescimo_valor
FROM venda_item
WHERE venda_id = 57;
""")

print("\n--- 2.2 Parcela Financeira da Venda 57 ---")
query("""
SELECT id, venda_id, forma_pagamento_id, parcela, valor_parcela, valor_pago, vencimento, data_pagamento, cancelada
FROM financeiro_parcela
WHERE venda_id = 57;
""")

print("\n--- 2.3 Pagamento da Parcela da Venda 57 ---")
query("""
SELECT id, financeiro_parcela_id, forma_pagamento_baixa_id, valor_pago, valor_recebido, data_pagamento, api_device_id
FROM financeiro_parcela_pagamento
WHERE financeiro_parcela_id = 121;
""")

print("\n--- 2.4 Nota Fiscal Vinculada (NFC-e) da Venda 57 ---")
query("""
SELECT id, numero_nfe, serie, modelo, total_produto_valor, total_desconto_valor, total_nota_valor, recibo_situacao, codigo_status, mensagem_erro
FROM nota_fiscal_eletronica
WHERE id = 57;
""")

print("\n=== 3. FORMAS DE PAGAMENTO UTILIZADAS NA BASE ===")
query("""
SELECT fp.id, fp.nome, fp.tipo, COUNT(p.id) as qtd_usos
FROM forma_pagamento fp
LEFT JOIN financeiro_parcela p ON p.forma_pagamento_id = fp.id
GROUP BY fp.id, fp.nome, fp.tipo
ORDER BY qtd_usos DESC
LIMIT 10;
""")

print("\n=== 4. PERFIL DE CLIENTES CADASTRADOS ===")
query("""
SELECT id, nome, fantasia, cpf_cnpj, tipo_pessoa, tipo_cliente, created_at
FROM cliente
ORDER BY id ASC
LIMIT 5;
""")
