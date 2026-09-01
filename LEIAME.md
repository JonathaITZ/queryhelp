# 🚀 Manual de Acesso e Guia do Banco de Dados
## Projeto Especialista SQL & Engenharia de Dados
> **Autor e Responsável Técnico: Jonatha Dantas**  
> *Data: 31 de Agosto de 2026*

Este documento consolida o mapeamento integral, instruções de conexão, inventário de arquivos e credenciais da base de dados **`softcoms_softcomshop_lanchoneteerestaurantepotira`** (MySQL 8.0).ema mapeados, relacionamentos (FKs), modelos Python gerados, backups e o guia de utilização local para novos projetos.

---

## 📌 1. Dados de Conexão

| Parâmetro | Detalhes |
| :--- | :--- |
| **Ambiente / Host** | `softcomdb-mysql-hml.cluster-cyv0220iwox9.us-east-1.rds.amazonaws.com` |
| **Porta** | `3306` |
| **Driver / SGBD** | MySQL 8.0 / MariaDB |
| **Usuário** | `patrick.morais` |
| **Senha** | `sq6j7dDW53pm` |
| **Banco de Dados** | `softcoms_softcomshop_lanchoneteerestaurantepotira` |

### 🏢 Empresa Cadastrada na Base:
* **ID:** `1`
* **Razão Social:** `MATRIZ`
* **Nome Fantasia:** `LANCHONETE E RESTAURANTE POTIRA LTDA`
* **CNPJ:** `37.671.348/0001-10`
* **Cidade / UF:** Cláudio / MG

---

## 📊 2. Resumo da Estrutura Geral

* **Total de Tabelas:** `459`
* **Total de Colunas Mapeadas:** `6.600`
* **Total de Chaves Estrangeiras (Relacionamentos):** `518`
* **Total de Índices:** Mapeados integralmente com unicidade e sequenciamento.

---

## 📁 3. Arquivos do Mapeamento Completo para Novos Projetos

Todos os arquivos estão organizados no diretório:
`C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\`

| Arquivo | Conteúdo e Finalidade |
| :--- | :--- |
| **`DOCUMENTACAO_PROJETO.md`** | **Documentação Oficial de Autoria do Projeto (Jonatha Dantas)**: Registro formal de requisitos atendidos, arquitetura implementada e especificações técnicas. |
| **`REGRAS_DE_NEGOCIO.md`** | **Manual Completo de Regras de Negócio e Domínio** cobrindo ciclo de vida de clientes, vendas (balcão/mesas/delivery), emissão fiscal NFC-e/NF-e, parcelamento financeiro, fechamento de caixa e diretrizes de arquitetura para novos projetos. |
| **`schema_complete.json`** | Mapeamento profundo e integral em JSON com **todas as tabelas, colunas, tipos precisos, chaves primárias, índices, chaves estrangeiras, regras `ON DELETE`/`ON UPDATE` e referências inversas (`referenced_by`)**. Ideal para alimentar geradores de código, ferramentas de migração ou automações. |
| **`schema_relacionamentos.md`** | Tabela detalhada de todos os **518 relacionamentos** (chaves estrangeiras) ligando tabelas de origem, colunas, tabelas de destino e regras referenciais. |
| **`schema_quick_reference.md`** | Dicionário de dados navegável em Markdown com descrição coluna a coluna de todas as 459 tabelas. |
| **`iniciar_chat.bat` / `.ps1`** | **Iniciador em 1 Clique**: Abre o navegador automaticamente e inicia o servidor do Chat Especialista. |
| **`app_chat_sql.py`** | **Aplicação de Chat Especialista em Estrutura SQL (100% Desconectada do Banco)**: Opera exclusivamente sobre os metadados do schema e regras de negócio, sem conexão de rede com o banco e sem trafegar dados de clientes. |
| **`potira_models.py`** | Classes **Python (`dataclass`)** geradas para todas as tabelas da base com tipos tipados (`int`, `str`, `Decimal`, `datetime`, `Optional[...]`), prontas para uso em novos projetos. |
| **`../potira_db.py`** | Módulo e CLI para executar queries com formatação e consultas de schema offline. |
| **`../python/`** | Python 3.11 portátil configurado com `pymysql`, `cryptography` e `tabulate`. |
| **`../backup_potira_contingencias_20260831_170855.sql`** | Backup dos registros originais antes do ajuste de contingência. |

---

## 🚀 4. Como Usar o Mapeamento e o Python no seu Projeto

### 4.1. Importando os Modelos Gerados em Python:
```python
import sys
sys.path.append(r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema")
sys.path.append(r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch")

from potira_models import Venda, FinanceiroParcela, NotaFiscalEletronica
from potira_db import query

# Buscar dados já tipados
raw_vendas = query("SELECT * FROM venda ORDER BY id DESC LIMIT 5", print_table=False)
for v in raw_vendas:
    print(f"Venda ID: {v['id']} | Total: R$ {v['valor_total']} | Data: {v['api_data_hora_venda']}")
```

### 4.2. Consultando o JSON de Schema em Qualquer Linguagem:
O arquivo `schema_complete.json` pode ser lido em Python, Node.js, C#, PHP ou Go para inspecionar relacionamentos, gerar diagramas ER automaticamente ou construir ORMs customizados:
```python
import json

with open(r"C:\Users\dantas.jonatha\.gemini\antigravity\scratch\schema\schema_complete.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

# Listar todas as tabelas que se relacionam com 'venda'
for t in schema["tables"]:
    if t["name"] == "venda":
        print("Tabelas que 'venda' referencia:", [fk["referenced_table"] for fk in t["foreign_keys"]])
        print("Tabelas que referenciam 'venda':", [ref["from_table"] for ref in t["referenced_by"]])
```
