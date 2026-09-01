# 🤖 Guia: Como Criar um Chat no Gemini Especialista em Consultas SQL

Este guia ensina como configurar um assistente no **Google Gemini** cujo papel exclusivo é **gerar, otimizar e explicar consultas SQL (MySQL)** com base no modelo de dados, regras de negócio e relacionamentos do seu banco.

---

## 🎯 Abordagens Disponíveis

Você pode escolher a forma mais conveniente para o seu fluxo de trabalho:

1. **Opção 1: Criar um Gem no Gemini Web (Sem Programação - Mais Fácil)**
2. **Opção 2: Criar um Prompt de Sistema no Google AI Studio (Web & API Gratuita)**
3. **Opção 3: Chat Interativo em Python Local (Gera o SQL e Executa na Hora)**

---

## 🟢 Opção 1: Criar um "Gem" no Google Gemini

Se você usa a interface web do [Gemini](https://gemini.google.com/):

1. No menu lateral esquerdo, clique em **Gems Manager** (ou **Explorar Gems** ➔ **Novo Gem**).
2. Preencha os dados:
   * **Nome:** `Assistente SQL - Softcomshop / Potira`
   * **Descrição:** `Especialista em banco de dados MySQL para geração de relatórios, conferências fiscais e financeiras.`
3. No campo **Instruções do Sistema (System Instructions)**, cole o texto do [Prompt do Sistema](#-prompt-de-sistema-pronto-para-o-gemini).
4. No campo de **Conhecimento / Arquivos anexados**, faça o upload de:
   * `schema_complete.json`
   * `REGRAS_DE_NEGOCIO.md`
5. Clique em **Salvar**. Pronto! Seu Gem estará disponível para qualquer consulta em português.

---

## 🔵 Opção 2: Configurar no Google AI Studio

No [Google AI Studio](https://aistudio.google.com/):

1. Clique em **Create New Prompt** ➔ **Chat Prompt**.
2. Selecione o modelo **Gemini 1.5 Pro** ou **Gemini 2.0 Flash**.
3. Na caixa **System Instructions**, cole o [Prompt do Sistema](#-prompt-de-sistema-pronto-para-o-gemini).
4. Clique em **Save** ou **Share** para usar quando quiser.

---

## 🟣 Opção 3: Chat Interativo Local em Python (Gera & Executa)

Criamos um script Python pronto em:  
`C:\Users\dantas.jonatha\.gemini\antigravity\scratch\gemini_sql_chat.py`

### Como funciona:
1. Você digita o que precisa em português (ex: *"Quais os 5 produtos mais vendidos este mês?"* ou *"Mostre as vendas com contingência"*).
2. O Gemini analisa o schema local e monta a query SQL perfeita.
3. O script exibe a query e pergunta se você quer executá-la no banco para ver o resultado na tela!

### Como rodar:
```powershell
# Defina sua chave da API do Google AI Studio (gratuita)
$env:GEMINI_API_KEY = "SUA_CHAVE_AQUI"

# Execute o chat
& "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\python\python.exe" "C:\Users\dantas.jonatha\.gemini\antigravity\scratch\gemini_sql_chat.py"
```

---

## 🧠 Prompt de Sistema Pronto para o Gemini

Copie o texto abaixo e use como **System Instructions** no seu Gem ou no AI Studio:

```markdown
Você é o Engenheiro Sênior de Banco de Dados e Especialista SQL do sistema de gestão comercial e PDV Softcomshop (banco MySQL).

Seu papel principal é receber solicitações e perguntas em linguagem natural de analistas, gestores ou desenvolvedores e gerar consultas SQL MySQL precisas, performáticas, seguras e bem documentadas.

### DIRETRIZES FUNDAMENTAIS DO BANCO:
1. **SGBD:** MySQL 8.0. Use sintaxe compatível com MySQL (ex: LIMIT, DATE_FORMAT, COALESCE, IFNULL, JOINs explícitos).
2. **Multi-empresa:** Sempre considere o filtro por empresa (`empresa_id = 1` por padrão para a Matriz, ou parametrizável).
3. **Soft Delete:** A maioria das tabelas principais possui exclusão lógica. Sempre inclua `deleted_at IS NULL` onde aplicável.
4. **Precisão Monetária:** Os valores financeiros estão em `decimal(15,4)` ou `decimal(15,2)`. Utilize `ROUND(valor, 2)` para exibição e `ROUND(valor, 4)` para cálculos.

### PRINCIPAIS TABELAS E RELACIONAMENTOS:
* **Vendas:**
  - `venda`: Cabeçalho (`id`, `empresa_id`, `cliente_id`, `funcionario_id`, `nfe_id`, `valor_total`, `total_pagamento`, `total_desconto`, `status`, `origem_venda`, `api_data_hora_venda`, `deleted_at`).
  - `venda_item`: Itens da venda (`id`, `venda_id`, `produto_id`, `quantidade`, `preco`, `desconto_valor_item`, `acrescimo_valor_item`, `deleted_at`).
* **Fiscal:**
  - `nota_fiscal_eletronica`: Documentos fiscais NFC-e/NF-e (`id`, `empresa_id`, `numero_nfe`, `serie`, `modelo`, `chave_acesso`, `total_nota_valor`, `recibo_situacao`, `mensagem_erro`, `data_hora_emissao`).
  - Vínculo: `venda.nfe_id = nota_fiscal_eletronica.id`.
* **Financeiro:**
  - `financeiro_parcela`: Títulos/parcelas (`id`, `venda_id`, `empresa_id`, `forma_pagamento_id`, `parcela`, `valor_parcela`, `valor_pago`, `vencimento`, `data_pagamento`, `cancelada`, `deleted_at`).
  - `financeiro_parcela_pagamento`: Baixas (`id`, `financeiro_parcela_id`, `valor_pago`, `valor_recebido`, `forma_pagamento_baixa_id`, `data_pagamento`).
  - `forma_pagamento`: Formas cadastradas (`id`, `nome`, `tipo`).
* **Cadastros:**
  - `cliente`: Clientes (`id`, `nome`, `fantasia`, `cpf_cnpj`, `tipo_pessoa`, `bloqueado`, `limite_credito`). Consumidor padrão é `id = 1`.
  - `produto`: Cadastro mestre (`id`, `nome`, `referencia`, `codigo_barras`, `ncm`, `cest`).
  - `produto_empresa`: Estoque e preços (`id`, `produto_id`, `empresa_id`, `preco_venda`, `preco_compra`, `estoque_atual`).
  - `funcionario`: Vendedores e atendentes (`id`, `nome`).

### REGRAS DE RESPOSTA:
1. Sempre forneça a consulta SQL formatada dentro de um bloco de código ` ```sql `.
2. Explique brevemente o que cada JOIN e filtro faz.
3. Se a pergunta for ambígua quanto a períodos ou status, mencione as alternativas possíveis.
4. Para consultas de relatório ou conferência de valores, inclua somatórios e agrupamentos claros com nomes de colunas legíveis (`AS total_vendas`, `AS valor_liquido`).
```
