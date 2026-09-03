# 🖥️ DOCUMENTAÇÃO TÉCNICA: BANCO DE DADOS SOFTSHOP DESKTOP

> **Instância:** Microsoft SQL Server 2019 (Porta 5433)  
> **Base de Dados:** `BaseLavanderiaPandaNovo`  
> **Total de Tabelas:** 642 tabelas | 14.234 colunas | 696 Chaves Primárias | 231 Chaves Estrangeiras

---

## ⚠️ DIRETRIZES DE SINTAXE E ARQUITETURA (SQL SERVER / T-SQL)

1. **Identificadores com Espaços e Acentuação (Colchetes Obrigatórios):**
   - As tabelas e colunas do Softshop Desktop utilizam nomes em linguagem natural com espaços: `[Cadastro de Vendas]`, `[Vendas Efetuadas]`, `[Cadastro de Mercadorias]`, `[Cadastro de Clientes]`, `[contas a receber]`.
   - **Toda consulta T-SQL DEVE usar colchetes `[Nome da Tabela]` e `[Nome da Coluna]`**.

2. **Exclusão Lógica e Ativação no Softshop:**
   - No Softshop Desktop **NÃO EXISTE** a coluna `deleted_at`. O padrão é a coluna booleana `[Desativado] = 0` (ativo) / `1` (desativado) em cadastros, ou campos de status como `[Situação]` / `[Cancelada]`.

3. **Transações Defensivas no SQL Server:**
   - Operações de UPDATE/DELETE devem utilizar: `BEGIN TRANSACTION; ... COMMIT TRANSACTION;` (ou `ROLLBACK TRANSACTION;`).

---

## 🏢 MAPEAMENTO DETALHADO DOS PRINCIPAIS MÓDULOS

### 📌 Tabela: `[Cadastro de Vendas]`
- **Total de Linhas:** 491,472
- **Chaves Primárias (PK):** C, ó, d, i, g, o,  , d, a,  , V, e, n, d, a
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Nome do Cliente]` ➔ `[Cadastro de Clientes]([Código do Cliente])`
  - `[Vendedor]` ➔ `[cadastro de vendedores]([Código do Vendedor])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código da Venda]` | `int` | ✅ SIM | Coluna nativa |
| `[Data da Venda]` | `datetime` | NÃO | Coluna nativa |
| `[Horas]` | `datetime` | NÃO | Coluna nativa |
| `[Nome do Cliente]` | `int` | NÃO | Coluna nativa |
| `[Nº da Duplicata]` | `float` | NÃO | Coluna nativa |
| `[Obs]` | `varchar(255)` | NÃO | Coluna nativa |
| `[Vendedor]` | `int` | NÃO | Coluna nativa |
| `[Mensagem]` | `varchar(-1)` | NÃO | Coluna nativa |
| `[CFOP]` | `varchar(50)` | NÃO | Coluna nativa |
| `[descontar]` | `float` | NÃO | Coluna nativa |
| `[valor pago]` | `float` | NÃO | Coluna nativa |
| `[Cancelado]` | `bit` | NÃO | Coluna nativa |
| `[Descontar2]` | `float` | NÃO | Coluna nativa |
| `[finalizarvenda]` | `bit` | NÃO | Coluna nativa |
| `[OS]` | `int` | NÃO | Coluna nativa |
| `[lacrar]` | `bit` | NÃO | Coluna nativa |
| `[ValorEntrada]` | `float` | NÃO | Coluna nativa |
| `[FormaEntrada]` | `varchar(50)` | NÃO | Coluna nativa |
| `[TipoCartãoEntrada]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Parcelado]` | `int` | NÃO | Coluna nativa |
| `[FormaParcelado]` | `varchar(50)` | NÃO | Coluna nativa |
| `[DataPrimeiraParcela]` | `datetime` | NÃO | Coluna nativa |
| `[TipoCartãoParcelado]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Lancamento_Usuario]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Lancamento_DataHora]` | `datetime` | NÃO | Coluna nativa |
*... e mais 159 colunas disponíveis no schema.*

### 📌 Tabela: `[Vendas Efetuadas]`
- **Total de Linhas:** 1,911,454
- **Chaves Primárias (PK):** c, o, n, t, a, r
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Código da Mercadoria]` ➔ `[Cadastro de Mercadorias]([Código da Mercadoria])`
  - `[Código da Venda]` ➔ `[Cadastro de Vendas]([Código da Venda])`
  - `[Cores]` ➔ `[Confeccao_Cores]([Cor])`
  - `[Tam]` ➔ `[Confeccao_Tamanhos]([Tamanho])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código da Venda]` | `int` | NÃO | Coluna nativa |
| `[Código da Mercadoria]` | `int` | NÃO | Coluna nativa |
| `[Quantidade]` | `float` | NÃO | Coluna nativa |
| `[Quantidade2]` | `float` | NÃO | Coluna nativa |
| `[Preço]` | `float` | NÃO | Coluna nativa |
| `[Desconto]` | `float` | NÃO | Coluna nativa |
| `[Produto]` | `varchar(255)` | NÃO | Coluna nativa |
| `[Atualizado]` | `bit` | NÃO | Coluna nativa |
| `[Preço Compra2]` | `float` | NÃO | Coluna nativa |
| `[Situação]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Printar]` | `bit` | NÃO | Coluna nativa |
| `[Comissão]` | `float` | NÃO | Coluna nativa |
| `[contar]` | `int` | ✅ SIM | Coluna nativa |
| `[Serial]` | `varchar(50)` | NÃO | Coluna nativa |
| `[CR_CodItem]` | `int` | NÃO | Coluna nativa |
| `[CR_Mercadoria]` | `varchar(50)` | NÃO | Coluna nativa |
| `[CR_BalancaCodigo]` | `varchar(50)` | NÃO | Coluna nativa |
| `[CR_BalancaPreco]` | `float` | NÃO | Coluna nativa |
| `[DataHoraDigitacao]` | `datetime` | NÃO | Coluna nativa |
| `[Pronto]` | `bit` | NÃO | Coluna nativa |
| `[TransferirSelecionar]` | `bit` | NÃO | Coluna nativa |
| `[PrecoBruto]` | `float` | NÃO | Coluna nativa |
| `[DescontoItem]` | `float` | NÃO | Coluna nativa |
| `[CR_PrecoTotal]` | `float` | NÃO | Coluna nativa |
| `[SM_IDITEMPEDIDO]` | `varchar(50)` | NÃO | Coluna nativa |
*... e mais 98 colunas disponíveis no schema.*

### 📌 Tabela: `[Cadastro de Mercadorias]`
- **Total de Linhas:** 572
- **Chaves Primárias (PK):** C, ó, d, i, g, o,  , d, a,  , M, e, r, c, a, d, o, r, i, a
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Fornecedor]` ➔ `[Fornecedores]([Fornecedor])`
  - `[Grupo]` ➔ `[grp]([GRP_DESCRI])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código da Mercadoria]` | `int` | ✅ SIM | Coluna nativa |
| `[Mercadoria]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Fabricante]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Preço C]` | `float` | NÃO | Coluna nativa |
| `[Preço de Venda]` | `float` | NÃO | Coluna nativa |
| `[Fornecedor]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Unidades em Estoque]` | `float` | NÃO | Coluna nativa |
| `[DataEstoque]` | `datetime` | NÃO | Coluna nativa |
| `[Medida]` | `varchar(50)` | NÃO | Coluna nativa |
| `[ICMS]` | `float` | NÃO | Coluna nativa |
| `[Frete]` | `float` | NÃO | Coluna nativa |
| `[IPI]` | `float` | NÃO | Coluna nativa |
| `[Preço Compra]` | `float` | NÃO | Coluna nativa |
| `[Prateleira]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Grupo]` | `varchar(255)` | NÃO | Coluna nativa |
| `[SubGrupo]` | `int` | NÃO | Coluna nativa |
| `[VendaA]` | `float` | NÃO | Coluna nativa |
| `[VendaB]` | `float` | NÃO | Coluna nativa |
| `[VendaC]` | `float` | NÃO | Coluna nativa |
| `[Isento ICMS]` | `bit` | NÃO | Coluna nativa |
| `[Máximo]` | `float` | NÃO | Coluna nativa |
| `[Desativado]` | `bit` | NÃO | Coluna nativa |
| `[Comissão2]` | `float` | NÃO | Coluna nativa |
| `[Cód Barra]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Cód Fabricante]` | `varchar(50)` | NÃO | Coluna nativa |
*... e mais 193 colunas disponíveis no schema.*

### 📌 Tabela: `[cadastro de mercadoriasLojas]`
- **Total de Linhas:** 610
- **Chaves Primárias (PK):** C, ó, d, i, g, o,  , d, a,  , M, e, r, c, a, d, o, r, i, a, L, o, j, a
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Código da Mercadoria]` ➔ `[Cadastro de Mercadorias]([Código da Mercadoria])`
  - `[Cores]` ➔ `[Confeccao_Cores]([Cor])`
  - `[Tam]` ➔ `[Confeccao_Tamanhos]([Tamanho])`
  - `[Loja]` ➔ `[Integrar_Lojas]([Loja])`
  - `[Loja]` ➔ `[Integrar_Lojas]([Loja])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código da Mercadoria]` | `int` | NÃO | Coluna nativa |
| `[Loja]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Estoque]` | `float` | NÃO | Coluna nativa |
| `[Entradas]` | `float` | NÃO | Coluna nativa |
| `[Saídas]` | `float` | NÃO | Coluna nativa |
| `[EntMov]` | `float` | NÃO | Coluna nativa |
| `[SaíMov]` | `int` | NÃO | Coluna nativa |
| `[Código da MercadoriaLoja]` | `int` | ✅ SIM | Coluna nativa |
| `[Devolucao]` | `int` | NÃO | Coluna nativa |
| `[Requisicao]` | `int` | NÃO | Coluna nativa |
| `[Tam]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Cores]` | `varchar(255)` | NÃO | Coluna nativa |
| `[CodBarras]` | `varchar(50)` | NÃO | Coluna nativa |
| `[PrecoGrade]` | `float` | NÃO | Coluna nativa |
| `[SMobile_Validades]` | `varchar(220)` | NÃO | Coluna nativa |
| `[SoftSync_Add]` | `bit` | NÃO | Coluna nativa |
| `[IdRestauranteSetor]` | `int` | NÃO | Coluna nativa |
| `[DescrRestauranteSetor]` | `varchar(50)` | NÃO | Coluna nativa |
| `[EstoqueReservado]` | `float` | NÃO | Coluna nativa |
| `[SS_CodigoProduto]` | `int` | NÃO | Coluna nativa |
| `[SS_CodigoProdutoUnicoGrade]` | `int` | NÃO | Coluna nativa |
| `[ECommerce_CodigoSite]` | `varchar(50)` | NÃO | Coluna nativa |
| `[DesativadoLoja]` | `bit` | NÃO | Coluna nativa |
| `[EstoqueMinimo]` | `float` | NÃO | Coluna nativa |
| `[Marketplace_Sincronizado]` | `bit` | NÃO | Coluna nativa |
*... e mais 2 colunas disponíveis no schema.*

### 📌 Tabela: `[Cadastro de Clientes]`
- **Total de Linhas:** 3,536
- **Chaves Primárias (PK):** C, ó, d, i, g, o,  , d, o,  , C, l, i, e, n, t, e
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Area]` ➔ `[Cargas_Area]([Area])`
  - `[Loja]` ➔ `[Integrar_Lojas]([Loja])`
  - `[Loja]` ➔ `[Integrar_Lojas]([Loja])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código do Cliente]` | `int` | ✅ SIM | Coluna nativa |
| `[Razão Social]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Nome do Cliente]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Endereço]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Bairro]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Cidade]` | `varchar(50)` | NÃO | Coluna nativa |
| `[UF]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Fone Resid]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Datanasc]` | `datetime` | NÃO | Coluna nativa |
| `[Observações]` | `varchar(255)` | NÃO | Coluna nativa |
| `[CEP]` | `varchar(50)` | NÃO | Coluna nativa |
| `[CGC]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Inscrição Estadual]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Contato]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Tipo de Cliente]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Ponto de Referência]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Vendedor]` | `int` | NÃO | Coluna nativa |
| `[Dt Cadastro]` | `datetime` | NÃO | Coluna nativa |
| `[Pessoa]` | `varchar(50)` | NÃO | Coluna nativa |
| `[RG]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Desativado]` | `bit` | NÃO | Coluna nativa |
| `[endcob]` | `varchar(250)` | NÃO | Coluna nativa |
| `[bairrocob]` | `varchar(150)` | NÃO | Coluna nativa |
| `[cidcob]` | `varchar(50)` | NÃO | Coluna nativa |
| `[ufcob]` | `varchar(50)` | NÃO | Coluna nativa |
*... e mais 54 colunas disponíveis no schema.*

### 📌 Tabela: `[contas a receber]`
- **Total de Linhas:** 132,373
- **Chaves Primárias (PK):** R, e, g, i, s, t, r, o
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Código do Cliente]` ➔ `[Cadastro de Clientes]([Código do Cliente])`
  - `[Conta]` ➔ `[ContaBanco]([DescricaoConta])`
  - `[LojaOrigem]` ➔ `[Integrar_Lojas]([Loja])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Registro]` | `int` | ✅ SIM | Coluna nativa |
| `[Data da Venda]` | `datetime` | NÃO | Coluna nativa |
| `[Vendedor]` | `int` | NÃO | Coluna nativa |
| `[Bloquete]` | `int` | NÃO | Coluna nativa |
| `[Código do Cliente]` | `int` | NÃO | Coluna nativa |
| `[Nome do Cliente]` | `varchar(150)` | NÃO | Coluna nativa |
| `[Vencimento]` | `datetime` | NÃO | Coluna nativa |
| `[Valor da Parcela]` | `float` | NÃO | Coluna nativa |
| `[DataPag]` | `datetime` | NÃO | Coluna nativa |
| `[Valor Pago]` | `float` | NÃO | Coluna nativa |
| `[Pagto]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Numero]` | `int` | NÃO | Coluna nativa |
| `[Pedido]` | `bit` | NÃO | Coluna nativa |
| `[Dados do Cheque]` | `varchar(150)` | NÃO | Coluna nativa |
| `[Cartão]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Parcela]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Nota Fiscal]` | `int` | NÃO | Coluna nativa |
| `[Pagto2]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Taxa]` | `float` | NÃO | Coluna nativa |
| `[Destino]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Loja]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Observação]` | `varchar(255)` | NÃO | Coluna nativa |
| `[Conta]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Lacrar]` | `bit` | NÃO | Coluna nativa |
| `[Bordero]` | `bit` | NÃO | Coluna nativa |
*... e mais 82 colunas disponíveis no schema.*

### 📌 Tabela: `[contas a pagar]`
- **Total de Linhas:** 4,839
- **Chaves Primárias (PK):** R, e, g, i, s, t, r, o
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Categoria]` ➔ `[Categorias]([GRP_DESCRI])`
  - `[Histórico]` ➔ `[Fornecedores]([Fornecedor])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Registro]` | `int` | ✅ SIM | Coluna nativa |
| `[Histórico]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Categoria]` | `varchar(250)` | NÃO | Coluna nativa |
| `[SubCategoria]` | `int` | NÃO | Coluna nativa |
| `[NumeroDoc]` | `varchar(50)` | NÃO | Coluna nativa |
| `[DtEmissão]` | `datetime` | NÃO | Coluna nativa |
| `[Valor Nota]` | `float` | NÃO | Coluna nativa |
| `[Código da Compra]` | `int` | NÃO | Coluna nativa |
| `[Tipo Documento]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Lancamento_Usuario]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Lancamento_DataHora]` | `datetime` | NÃO | Coluna nativa |
| `[ObsLancamento]` | `varchar(-1)` | NÃO | Coluna nativa |
| `[LojaOrigem]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Parcelas]` | `int` | NÃO | Coluna nativa |
| `[PrimeiroVencimento]` | `datetime` | NÃO | Coluna nativa |
| `[RegistroConhecimento]` | `int` | NÃO | Coluna nativa |
| `[DiasIntervalo]` | `int` | NÃO | Coluna nativa |
| `[CodBarrasBoleto]` | `varchar(255)` | NÃO | Coluna nativa |
| `[ChaveNFe]` | `varchar(50)` | NÃO | Coluna nativa |
| `[TipoGNRE]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Multa]` | `float` | NÃO | Coluna nativa |
| `[Juros]` | `float` | NÃO | Coluna nativa |
| `[PlanoDeContasID]` | `int` | NÃO | Coluna nativa |
| `[IB_ConciliacaoNovo]` | `bit` | NÃO | Coluna nativa |
| `[Veiculo]` | `int` | NÃO | Coluna nativa |

### 📌 Tabela: `[ContasaPagarVencimentos]`
- **Total de Linhas:** 7,218
- **Chaves Primárias (PK):** O, r, d, e, m
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[Conta]` ➔ `[ContaBanco]([DescricaoConta])`
  - `[Registro]` ➔ `[contas a pagar]([Registro])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Registro]` | `int` | NÃO | Coluna nativa |
| `[Vencimento]` | `datetime` | NÃO | Coluna nativa |
| `[Valor2]` | `float` | NÃO | Coluna nativa |
| `[Parcela]` | `int` | NÃO | Coluna nativa |
| `[Data de Pagamento]` | `datetime` | NÃO | Coluna nativa |
| `[Valor Pago]` | `float` | NÃO | Coluna nativa |
| `[Forma Pagto]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[Nº Cheque]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[Conta]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Obs2]` | `nvarchar(255)` | NÃO | Coluna nativa |
| `[Ordem]` | `int` | ✅ SIM | Coluna nativa |
| `[Lacrar]` | `bit` | NÃO | Coluna nativa |
| `[Pago]` | `bit` | NÃO | Coluna nativa |
| `[Baixa_Usuario]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[Baixa_DataHora]` | `datetime` | NÃO | Coluna nativa |
| `[DuplicataPendenteCP]` | `bit` | NÃO | Coluna nativa |
| `[Chave_PagamentoCompras]` | `int` | NÃO | Coluna nativa |
| `[RegistroPendencia]` | `int` | NÃO | Coluna nativa |
| `[LinhaDigitavel]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[ChBanco]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[ChAgencia]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[ChConta]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[ChNumeroCheque]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[ChEmitente]` | `nvarchar(255)` | NÃO | Coluna nativa |
| `[MovimentacaoId]` | `int` | NÃO | Coluna nativa |
*... e mais 27 colunas disponíveis no schema.*

### 📌 Tabela: `[pagamento]`
- **Total de Linhas:** 6
- **Chaves Primárias (PK):** G, R, P, _, D, E, S, C, R, I
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[GRP_COD]` | `int` | NÃO | Coluna nativa |
| `[GRP_DESCRI]` | `nvarchar(250)` | ✅ SIM | Coluna nativa |
| `[Ordem]` | `int` | NÃO | Coluna nativa |
| `[DescricaoCaixa]` | `varchar(50)` | NÃO | Coluna nativa |
| `[GerarReceber]` | `bit` | NÃO | Coluna nativa |
| `[Avista]` | `bit` | NÃO | Coluna nativa |
| `[Parcelado]` | `bit` | NÃO | Coluna nativa |
| `[PagarComissao]` | `bit` | NÃO | Coluna nativa |
| `[NivelUsuario]` | `bit` | NÃO | Coluna nativa |
| `[Limite]` | `bit` | NÃO | Coluna nativa |
| `[MostrarCaixaBolete]` | `bit` | NÃO | Coluna nativa |
| `[NaoMostrarNoTotalizadorCaixa]` | `bit` | NÃO | Coluna nativa |
| `[FormaECF]` | `varchar(50)` | NÃO | Coluna nativa |
| `[ParcelasLimite]` | `int` | NÃO | Coluna nativa |
| `[NFCe_tPag]` | `varchar(50)` | NÃO | Coluna nativa |
| `[PDV_DescricaoPagamento]` | `varchar(50)` | NÃO | Coluna nativa |
| `[PDV_Exibir]` | `bit` | NÃO | Coluna nativa |
| `[PDV_POS]` | `bit` | NÃO | Coluna nativa |
| `[PDV_TEF]` | `bit` | NÃO | Coluna nativa |
| `[PDV_GerarReceber]` | `bit` | NÃO | Coluna nativa |
| `[PDV_CadastrarCheque]` | `bit` | NÃO | Coluna nativa |
| `[PDV_ValeGerar]` | `bit` | NÃO | Coluna nativa |
| `[PDV_ValeUtilizar]` | `bit` | NÃO | Coluna nativa |
| `[RelatorioEvolucao]` | `bit` | NÃO | Coluna nativa |
| `[ModuloAppEspecifico]` | `varchar(50)` | NÃO | Coluna nativa |
*... e mais 16 colunas disponíveis no schema.*

### 📌 Tabela: `[Somatorio_Caixa]`
- **Total de Linhas:** 5,291
- **Chaves Primárias (PK):** S, e, q
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[fk_name]` ➔ `Somatorio_Caixa$FK_Somatorio_Caixa_Integrar_Lojas`
  - `[column]` ➔ `LojaOrigem`
  - `[references_table]` ➔ `Integrar_Lojas`
  - `[references_column]` ➔ `Loja`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código do Cliente]` | `int` | NÃO | Coluna nativa |
| `[data inicial]` | `datetime` | NÃO | Coluna nativa |
| `[data final]` | `datetime` | NÃO | Coluna nativa |
| `[PrimeiroVencimento]` | `datetime` | NÃO | Coluna nativa |
| `[Parcelas]` | `int` | NÃO | Coluna nativa |
| `[Pagamento]` | `nvarchar(50)` | NÃO | Coluna nativa |
| `[Seq]` | `int` | ✅ SIM | Coluna nativa |
| `[Lacrar]` | `bit` | NÃO | Coluna nativa |
| `[DataOperacao]` | `datetime` | NÃO | Coluna nativa |
| `[LojaOrigem]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Nome do Cliente]` | `nvarchar(255)` | NÃO | Coluna nativa |
| `[ListaPedidos]` | `nvarchar(255)` | NÃO | Coluna nativa |

### 📌 Tabela: `[NotaFiscal_Cabecalho]`
- **Total de Linhas:** 5,119
- **Chaves Primárias (PK):** R, e, g, i, s, t, r, o
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[fk_name]` ➔ `NotaFiscal_Cabecalho$FK_NotaFiscal_Cabecalho_Integrar_Lojas`
  - `[column]` ➔ `LojaOrigem`
  - `[references_table]` ➔ `Integrar_Lojas`
  - `[references_column]` ➔ `Loja`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Registro]` | `int` | ✅ SIM | Coluna nativa |
| `[CFOP]` | `int` | NÃO | Coluna nativa |
| `[Numero]` | `int` | NÃO | Coluna nativa |
| `[Cancelado]` | `bit` | NÃO | Coluna nativa |
| `[DataEmissao]` | `datetime` | NÃO | Coluna nativa |
| `[DataSaida]` | `datetime` | NÃO | Coluna nativa |
| `[HoraSaida]` | `datetime` | NÃO | Coluna nativa |
| `[PercentualICMS]` | `float` | NÃO | Coluna nativa |
| `[Observacao]` | `varchar(-1)` | NÃO | Coluna nativa |
| `[Impresso]` | `bit` | NÃO | Coluna nativa |
| `[Tabela]` | `varchar(50)` | NÃO | Coluna nativa |
| `[IniciarRegistro]` | `bit` | NÃO | Coluna nativa |
| `[Remetente_Codigo]` | `int` | NÃO | Coluna nativa |
| `[Remetente_Nome]` | `varchar(150)` | NÃO | Coluna nativa |
| `[Remetente_CPF]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Remetente_Endereco]` | `varchar(150)` | NÃO | Coluna nativa |
| `[Remetente_Bairro]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Remetente_CEP]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Remetente_Cidade]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Remetente_Fone]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Remetente_UF]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Remetente_InscricaoEstadual]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Remetente_Fonte]` | `bit` | NÃO | Coluna nativa |
| `[Calculo_ValorFrete]` | `float` | NÃO | Coluna nativa |
| `[Calculo_ValorSeguro]` | `float` | NÃO | Coluna nativa |
*... e mais 228 colunas disponíveis no schema.*

### 📌 Tabela: `[Bloquetes]`
- **Total de Linhas:** 130,071
- **Chaves Primárias (PK):** S, e, q, u, e, n, c, i, a
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[fk_name]` ➔ `Bloquetes$FK_Bloquetes_Cadastro_de_Vendas`
  - `[column]` ➔ `Código da Venda`
  - `[references_table]` ➔ `Cadastro de Vendas`
  - `[references_column]` ➔ `Código da Venda`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código da Venda]` | `int` | NÃO | Coluna nativa |
| `[Vencimento]` | `datetime` | NÃO | Coluna nativa |
| `[Valor da Parcela]` | `float` | NÃO | Coluna nativa |
| `[Bloquete]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Banco]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Pagto]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Parcelas]` | `int` | NÃO | Coluna nativa |
| `[Sequencia]` | `int` | ✅ SIM | Coluna nativa |
| `[Valor da Parcela2]` | `float` | NÃO | Coluna nativa |
| `[Prazo]` | `float` | NÃO | Coluna nativa |
| `[CACHE_ID]` | `varchar(100)` | NÃO | Coluna nativa |
| `[SMobile_Chave]` | `varchar(100)` | NÃO | Coluna nativa |
| `[Cache_Enviado]` | `bit` | NÃO | Coluna nativa |
| `[TpIntegra]` | `int` | NÃO | Coluna nativa |
| `[Rede]` | `varchar(50)` | NÃO | Coluna nativa |
| `[MFeCodigoNSUAdquirente]` | `varchar(255)` | NÃO | Coluna nativa |
| `[MFeCodigoAutorizacaoAdquirente]` | `varchar(255)` | NÃO | Coluna nativa |
| `[MFeInstituicaoFinanceira]` | `varchar(255)` | NÃO | Coluna nativa |
| `[MFeBandeiraCartao]` | `varchar(255)` | NÃO | Coluna nativa |
| `[MFeCodigoNSUSefaz]` | `varchar(255)` | NÃO | Coluna nativa |
| `[MFeAutorizacaoOnline]` | `bit` | NÃO | Coluna nativa |
| `[MFePOSID]` | `int` | NÃO | Coluna nativa |
| `[MFeIDFechamento]` | `varchar(255)` | NÃO | Coluna nativa |
| `[POS_Habilitar]` | `bit` | NÃO | Coluna nativa |
| `[Bandeira]` | `varchar(50)` | NÃO | Coluna nativa |
*... e mais 5 colunas disponíveis no schema.*

### 📌 Tabela: `[cadastro de vendedores]`
- **Total de Linhas:** 51
- **Chaves Primárias (PK):** C, ó, d, i, g, o,  , d, o,  , V, e, n, d, e, d, o, r
- **Relacionamentos (Chaves Estrangeiras / JOINs):**
  - `[LojaOrigem]` ➔ `[Integrar_Lojas]([Loja])`
  - `[IdPermissoesPerfil]` ➔ `[Permissoes_Perfis]([Id])`
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código do Vendedor]` | `int` | ✅ SIM | Coluna nativa |
| `[Nome]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Endereço]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Bairro]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Cidade]` | `varchar(50)` | NÃO | Coluna nativa |
| `[UF]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Fone Resid]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Datanasc]` | `datetime` | NÃO | Coluna nativa |
| `[Observações]` | `varchar(-1)` | NÃO | Coluna nativa |
| `[CEP]` | `varchar(50)` | NÃO | Coluna nativa |
| `[CGC]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Inscrição Estadual]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Ponto de Referência]` | `varchar(-1)` | NÃO | Coluna nativa |
| `[Senha]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Desativado]` | `bit` | NÃO | Coluna nativa |
| `[Comissao4]` | `float` | NÃO | Coluna nativa |
| `[HoraEntradaLimite]` | `datetime` | NÃO | Coluna nativa |
| `[HoraSaidaLimite]` | `datetime` | NÃO | Coluna nativa |
| `[Acesso]` | `varchar(50)` | NÃO | Coluna nativa |
| `[LojaOrigem]` | `varchar(50)` | NÃO | Coluna nativa |
| `[CodigoFuncao]` | `int` | NÃO | Coluna nativa |
| `[Restaurante_TipoViaImpressao]` | `int` | NÃO | Coluna nativa |
| `[CodigoAutenticacao]` | `varchar(50)` | NÃO | Coluna nativa |
| `[SS_CodigoVendedor]` | `varchar(50)` | NÃO | Coluna nativa |
| `[DescontoMaximo]` | `float` | NÃO | Coluna nativa |
*... e mais 19 colunas disponíveis no schema.*

### 📌 Tabela: `[Fornecedores]`
- **Total de Linhas:** 472
- **Chaves Primárias (PK):** F, o, r, n, e, c, e, d, o, r
- **Colunas de Destaque:**
| Coluna | Tipo | PK | Descrição / Papel |
|---|---|---|---|
| `[Código do Fornecedor]` | `int` | NÃO | Coluna nativa |
| `[Fornecedor]` | `varchar(250)` | ✅ SIM | Coluna nativa |
| `[Endereço]` | `varchar(250)` | NÃO | Coluna nativa |
| `[Bairro]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Cidade]` | `varchar(50)` | NÃO | Coluna nativa |
| `[UF]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Fone1]` | `varchar(150)` | NÃO | Coluna nativa |
| `[Fone2]` | `varchar(50)` | NÃO | Coluna nativa |
| `[CEP]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Observações]` | `varchar(255)` | NÃO | Coluna nativa |
| `[Contato]` | `varchar(250)` | NÃO | Coluna nativa |
| `[CGC/CPF]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Insc Estadual]` | `varchar(50)` | NÃO | Coluna nativa |
| `[E-mail]` | `varchar(255)` | NÃO | Coluna nativa |
| `[Representante]` | `varchar(150)` | NÃO | Coluna nativa |
| `[Fones]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Lancamento_Usuario]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Lancamento_DataHora]` | `datetime` | NÃO | Coluna nativa |
| `[ErroIE]` | `varchar(50)` | NÃO | Coluna nativa |
| `[ErroCNPJ]` | `varchar(50)` | NÃO | Coluna nativa |
| `[cCidade]` | `int` | NÃO | Coluna nativa |
| `[cPais]` | `int` | NÃO | Coluna nativa |
| `[TipoPessoa]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Leilao_Usuario]` | `varchar(50)` | NÃO | Coluna nativa |
| `[Leilao_Senha]` | `varchar(50)` | NÃO | Coluna nativa |
*... e mais 15 colunas disponíveis no schema.*
