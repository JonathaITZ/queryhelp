"""
Modelos de dados gerados automaticamente a partir do schema de softcoms_softcomshop_lanchoneteerestaurantepotira
Prontos para uso em novos projetos Python / APIs.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from decimal import Decimal

@dataclass
class AgendaEvento:
    """Tabela: agenda_evento (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    tipo_evento: Optional[str] = None
    titulo: Optional[str] = None
    data_hora_inicio: Optional[datetime] = None
    data_hora_termino: Optional[datetime] = None
    repeticao: Optional[str] = None
    data_termino_repeticao: Optional[date] = None
    funcionario_id: Optional[int] = None
    localizacao: Optional[str] = None
    observacoes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    data_realizacao: Optional[datetime] = None
    dia_inteiro: int
    atendimento_id: Optional[int] = None
    avulso: int
    evento_repeticao_id: Optional[int] = None
    cliente_id: Optional[int] = None

@dataclass
class AgendaEventoArquivo:
    """Tabela: agenda_evento_arquivo (Linhas aprox: 0)"""
    id: int
    parent_id: int
    description: Optional[str] = None
    filename: str
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    extension: str
    link: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class AgendaEventoAtendimento:
    """Tabela: agenda_evento_atendimento (Linhas aprox: 0)"""
    id: int
    agenda_evento_id: int
    atendimento_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class AgendaEventoParticipanteInterno:
    """Tabela: agenda_evento_participante_interno (Linhas aprox: 0)"""
    id: int
    agenda_evento_id: int
    funcionario_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Assistencia:
    """Tabela: assistencia (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    tipo_atendimento: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    status: Optional[str] = None
    tecnico_responsavel_id: Optional[int] = None
    nome_solicitante: Optional[str] = None
    previsao_laudo: Optional[datetime] = None
    data_saida: Optional[datetime] = None
    tipo_assistencia: str
    valor_pago_pela_otica: Optional[Decimal] = None

@dataclass
class AssistenciaOticaItens:
    """Tabela: assistencia_otica_itens (Linhas aprox: 0)"""
    id: int
    produto_id: Optional[int] = None
    produto_empresa_grade_id: Optional[int] = None
    assistencia_id: int
    descricao_item: Optional[str] = None
    quantidade: Decimal
    preco: Decimal
    desconto_valor_item: Decimal
    acrescimo_valor_item: Decimal
    percentual_desconto: Optional[Decimal] = None
    percentual_acrescimo: Optional[Decimal] = None
    tipo_item: Optional[str] = None
    receita_id: Optional[int] = None
    garantia: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class AssistenciaOticaReceitas:
    """Tabela: assistencia_otica_receitas (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    assistencia_id: int
    medico_id: Optional[int] = None
    paciente_id: Optional[int] = None
    tipo_lente: str
    lente_direita: Optional[int] = None
    lente_esquerda: Optional[int] = None
    valor_lente_direita: Decimal
    valor_lente_esquerda: Decimal
    validade_receita: Optional[date] = None
    armacao_propria: int
    altura: Decimal
    ponte_aro: Decimal
    maior_diagonal: Decimal
    distancia_pupilar: Decimal
    previsao_entrega: Optional[date] = None
    armacao_id: Optional[int] = None
    laboratorio_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    paciente_nome: Optional[str] = None
    convenio_id: Optional[int] = None
    observacao: Optional[str] = None

@dataclass
class AssistenciaOticaReceitasConfiguracoes:
    """Tabela: assistencia_otica_receitas_configuracoes (Linhas aprox: 0)"""
    id: int
    receita_id: int
    esferico_od_longe: Optional[Decimal] = None
    esferico_oe_longe: Optional[Decimal] = None
    esferico_od_perto: Optional[Decimal] = None
    esferico_oe_perto: Optional[Decimal] = None
    cilindrico_od_longe: Optional[Decimal] = None
    cilindrico_oe_longe: Optional[Decimal] = None
    cilindrico_od_perto: Optional[Decimal] = None
    cilindrico_oe_perto: Optional[Decimal] = None
    eixo_od_longe: Optional[Decimal] = None
    eixo_oe_longe: Optional[Decimal] = None
    eixo_od_perto: Optional[Decimal] = None
    eixo_oe_perto: Optional[Decimal] = None
    dnp_od_longe: Optional[Decimal] = None
    dnp_oe_longe: Optional[Decimal] = None
    dnp_od_perto: Optional[Decimal] = None
    dnp_oe_perto: Optional[Decimal] = None
    co_od_longe: Optional[Decimal] = None
    co_oe_longe: Optional[Decimal] = None
    co_od_perto: Optional[Decimal] = None
    co_oe_perto: Optional[Decimal] = None
    adicao: Optional[Decimal] = None
    deleted_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

@dataclass
class AssistenciaPadraoEquipamento:
    """Tabela: assistencia_padrao_equipamento (Linhas aprox: 0)"""
    id: int
    assistencia_id: int
    equipamento_id: int
    marca_id: Optional[int] = None
    modelo: Optional[str] = None
    num_serie: Optional[str] = None
    defeito: Optional[str] = None
    acessorios: Optional[str] = None
    observacao: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class AssistenciaPadraoLaudo:
    """Tabela: assistencia_padrao_laudo (Linhas aprox: 0)"""
    id: int
    assistencia_id: int
    laudo_tecnico: Optional[str] = None
    servico_realizado: Optional[str] = None
    data_finalizacao: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Atendimento:
    """Tabela: atendimento (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    atendimento_lista_id: int
    ordem: int
    data_atendimento: Optional[datetime] = None
    data_conclusao_lista: Optional[datetime] = None
    tipo_atendimento: Optional[str] = None
    tipo_atendimento_kanban: str
    observacao: Optional[str] = None
    cliente_id: Optional[int] = None
    atendente_id: Optional[int] = None
    ordem_servico_id: Optional[int] = None
    venda_id: Optional[int] = None
    assistencia_id: Optional[int] = None
    receita_id: Optional[int] = None
    orcamento_id: Optional[int] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    data_cancelamento: Optional[datetime] = None

@dataclass
class AtendimentoConfig:
    """Tabela: atendimento_config (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    multiplos_cards: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    manutencao_equipamentos: int

@dataclass
class AtendimentoLista:
    """Tabela: atendimento_lista (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    nome: str
    cor_hex: Optional[str] = None
    ordem: int
    manter_cards: int
    ativar_mensagem: int
    mensagem_id: Optional[int] = None
    ativo: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class AtendimentoListaNotificacaoControle:
    """Tabela: atendimento_lista_notificacao_controle (Linhas aprox: 0)"""
    id: int
    atendimento_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class AtestadosTermos:
    """Tabela: atestados_termos (Linhas aprox: 11)"""
    id: int
    nome: str
    tipo: str
    texto: Optional[str] = None
    padrao: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Auditoria:
    """Tabela: auditoria (Linhas aprox: 0)"""
    id: int
    usuario: str
    data_hora: datetime
    api_device_id: str
    acao: str
    empresa_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class AutopecaChecklist:
    """Tabela: autopeca_checklist (Linhas aprox: 0)"""
    id: int
    orcamento_autopecas_id: int
    finalizado: int
    observacoes: Optional[str] = None

@dataclass
class AutopecaChecklistRespostas:
    """Tabela: autopeca_checklist_respostas (Linhas aprox: 0)"""
    id: int
    autopeca_checklist_id: int
    autopecas_checklist_item_id: int
    resposta: Optional[str] = None

@dataclass
class AutopecasChecklistCategoria:
    """Tabela: autopecas_checklist_categoria (Linhas aprox: 0)"""
    id: int
    nome: str
    ordenacao: int
    empresa_id: int
    visivel: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class AutopecasChecklistItem:
    """Tabela: autopecas_checklist_item (Linhas aprox: 0)"""
    id: int
    autopecas_checklist_categoria_id: int
    nome: str
    tipo_resposta: str
    ordenacao: int
    permitir_foto: int
    obrigatorio: int
    valor_padrao: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class AzureKeys:
    """Tabela: azure_keys (Linhas aprox: 0)"""
    id: int
    description: Optional[str] = None
    type: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    company_id: int
    portal_360_tenant_id: Optional[str] = None
    portal_360_company_id: Optional[str] = None
    portal_360_usuario: Optional[str] = None
    portal_360_senha: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ambiente_teste: int
    softconnect_company_id: Optional[str] = None
    softconnect_device_id: Optional[str] = None
    notification_company_id: Optional[str] = None
    notification_days: Optional[str] = None
    notification_sending_start_time: Optional[str] = None
    notification_sending_end_time: Optional[str] = None
    nfse_nacional: Optional[int] = None

@dataclass
class Bairro:
    """Tabela: bairro (Linhas aprox: 14)"""
    id: int
    nome: str
    taxa_entrega: Decimal
    cobrar_taxa_entrega: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Balanco:
    """Tabela: balanco (Linhas aprox: 0)"""
    id: int
    data_balanco: date
    responsavel_id: int
    observacao: Optional[str] = None
    empresa_id: int
    status_balanco: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class BalancoItem:
    """Tabela: balanco_item (Linhas aprox: 26)"""
    id: int
    produto_id: int
    balanco_id: int
    produto_empresa_grade_id: int
    quantidade: Decimal
    estoque: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Banco:
    """Tabela: banco (Linhas aprox: None)"""
    id: int
    codigo: str
    nome: str
    image: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Bandeira:
    """Tabela: bandeira (Linhas aprox: 28)"""
    id: int
    codigo: str
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class BoxPrisma:
    """Tabela: box_prisma (Linhas aprox: 0)"""
    nome: str
    id: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class CacheLocks:
    """Tabela: cache_locks (Linhas aprox: 0)"""
    key: str
    owner: str
    expiration: int

@dataclass
class CaixaFuncoes:
    """Tabela: caixa_funcoes (Linhas aprox: 0)"""
    id: int
    data_caixa: Optional[date] = None
    data_abertura: Optional[datetime] = None
    data_fechamento: Optional[datetime] = None
    api_device_id: str
    turno: int
    operador_id: Optional[int] = None
    usuario_abertura_id: Optional[int] = None
    usuario_fechamento_id: Optional[int] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    device_client_id: Optional[str] = None

@dataclass
class CaixaFuncoesDigitacao:
    """Tabela: caixa_funcoes_digitacao (Linhas aprox: 0)"""
    id: int
    caixa_funcoes_id: int
    caixa_data: Optional[date] = None
    caixa_turno: Optional[str] = None
    caixa_usuario_id: Optional[int] = None
    forma_pagamento_id: int
    valor: Decimal
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class CaixaFuncoesDigitacaoBandeiras:
    """Tabela: caixa_funcoes_digitacao_bandeiras (Linhas aprox: 0)"""
    id: int
    caixa_funcoes_id: Optional[int] = None
    caixa_usuario_id: int
    caixa_data: date
    caixa_turno: str
    bandeira: str
    valor: Decimal
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class CartaoAlias:
    """Tabela: cartao_alias (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class CartaoCredito:
    """Tabela: cartao_credito (Linhas aprox: 11)"""
    id: int
    nome: str
    dia: int
    taxa_admin: Decimal
    empresa_id: Optional[int] = None
    bandeira: str
    credenciadora_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    bandeira_nome: str
    parcelas: int
    alias_cartao: Optional[str] = None
    alias: str
    tipo: str

@dataclass
class CentroCusto:
    """Tabela: centro_custo (Linhas aprox: 0)"""
    id: int
    nome: str
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class Cfop:
    """Tabela: cfop (Linhas aprox: 0)"""
    id: int
    codigo: int
    nome: Optional[str] = None
    aliquota_icms: Decimal
    operacao: Optional[str] = None
    cfop_equivalente: Optional[int] = None
    nao_escriturar: int
    devolucao: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ChecklistPhotos:
    """Tabela: checklist_photos (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    parent_id: Optional[int] = None
    orcamento_id: Optional[int] = None
    filename: str
    link: str
    extension: Optional[str] = None
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None
    observacoes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Cheque:
    """Tabela: cheque (Linhas aprox: 0)"""
    id: int
    parcela_id: Optional[int] = None
    parcela_repasse_id: Optional[int] = None
    banco_numero: str
    numero: str
    emitente: str
    data_vencimento: date
    valor: Decimal
    data_baixa: Optional[date] = None
    motivo_devolucao_id: Optional[int] = None
    data_devolucao: Optional[date] = None
    tipo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ChequeMotivo:
    """Tabela: cheque_motivo (Linhas aprox: 0)"""
    id: int
    codigo: int
    descricao: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ChequeMovimento:
    """Tabela: cheque_movimento (Linhas aprox: 0)"""
    id: int
    cheque_id: int
    empresa_id: Optional[int] = None
    fornecedor_id: Optional[int] = None
    data_movimento: date
    tipo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Cliente:
    """Tabela: cliente (Linhas aprox: 1)"""
    id: int
    pessoa: str
    cpf_cnpj: Optional[str] = None
    inscricao_estadual: Optional[str] = None
    inscricao_municipal: Optional[str] = None
    rg: Optional[str] = None
    nome: str
    razao_social: str
    data_fundacao: Optional[date] = None
    data_nascimento: Optional[date] = None
    area_id: Optional[int] = None
    funcionario_id: Optional[int] = None
    tipo_cliente_id: int
    tipo_preco: str
    foto: Optional[str] = None
    bloqueado: Optional[int] = None
    desativado: int
    observacao: Optional[str] = None
    api_guid: Optional[str] = None
    permitir_excluir: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    contribuinte_icms: Optional[int] = None
    indicador_finalidade: Optional[str] = None
    detalhe_financeiro: Optional[str] = None
    limite_credito: Decimal
    tabela_preco_id: Optional[int] = None
    id_estrangeiro: Optional[str] = None
    codigo_pais: Optional[str] = None
    cliente_administradora_id: Optional[int] = None
    nome_pais: Optional[str] = None

@dataclass
class ClienteCondicaoPagamento:
    """Tabela: cliente_condicao_pagamento (Linhas aprox: 0)"""
    id: int
    cliente_id: Optional[int] = None
    condicao_pagamento_padrao_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ClienteCondicaoPagamentoParents:
    """Tabela: cliente_condicao_pagamento_parents (Linhas aprox: 0)"""
    id: int
    cliente_condicao_pagamento_id: Optional[int] = None
    condicao_pagamento_id: Optional[int] = None

@dataclass
class ClienteConvenio:
    """Tabela: cliente_convenio (Linhas aprox: 0)"""
    id: int
    cliente_id: int
    produto_id: int
    valor: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ClienteCredito:
    """Tabela: cliente_credito (Linhas aprox: 0)"""
    id: int
    cliente_id: int
    venda_id: Optional[int] = None
    operacao: str
    data_operacao: date
    valor: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    api_device_id: Optional[str] = None
    utilizado: int
    usuario_id: Optional[int] = None

@dataclass
class ClienteImagens:
    """Tabela: cliente_imagens (Linhas aprox: 0)"""
    id: int
    description: Optional[str] = None
    file_name: str
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    extension: str
    link: Optional[str] = None
    imagem_principal: int
    cliente_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ClienteOcorrencia:
    """Tabela: cliente_ocorrencia (Linhas aprox: 0)"""
    id: int
    cliente_id: int
    usuario_atendente_id: int
    usuario_agendado_id: int
    data_cadastro: date
    motivo: str
    data_retorno: Optional[date] = None
    hora_marcada: Optional[str] = None
    realizado: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_termino: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ClienteTagClassificacao:
    """Tabela: cliente_tag_classificacao (Linhas aprox: 0)"""
    id: int
    cliente_id: Optional[int] = None
    tag_classificacao_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ClienteVeiculo:
    """Tabela: cliente_veiculo (Linhas aprox: 0)"""
    id: int
    cliente_id: int
    placa: str
    modelo: Optional[str] = None
    combustivel: Optional[str] = None
    ano_fabricacao: Optional[str] = None
    ano_modelo: Optional[int] = None
    cor: Optional[str] = None
    renavam: Optional[str] = None
    chassi: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    marca_id: int
    quilometragem: Optional[int] = None
    observacoes: Optional[str] = None

@dataclass
class CnpjsAutorizados:
    """Tabela: cnpjs_autorizados (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    cnpj: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class CobrancaParcelas:
    """Tabela: cobranca_parcelas (Linhas aprox: 0)"""
    id: str
    financeiro_parcela_id: int
    recipient_account_agreement_id: str
    status: str
    status_dispatch: str
    dispatch_number: Optional[str] = None
    payer_type_document: str
    payer_document: str
    payer_name: str
    payer_postal_code: str
    payer_street: str
    payer_number: str
    payer_state: str
    payer_city: str
    payer_neighborhood: str
    our_number: str
    document_number: Optional[str] = None
    installment: Optional[str] = None
    due_date: date
    issue_date: datetime
    amount: Decimal
    fine: Decimal
    interest: Decimal
    discount: Decimal
    pix_qrcode: Optional[str] = None
    ticket_typed_line: Optional[str] = None
    paid: Optional[str] = None
    historic: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CobrancaWebhooks:
    """Tabela: cobranca_webhooks (Linhas aprox: 0)"""
    id: int
    payload: str
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class CodigoAnp:
    """Tabela: codigo_anp (Linhas aprox: None)"""
    id: int
    codigo: str
    descricao: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Comissoes:
    """Tabela: comissoes (Linhas aprox: 0)"""
    id: int
    nome: str
    valor: Decimal
    tipo: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Compra:
    """Tabela: compra (Linhas aprox: 62)"""
    id: int
    empresa_id: int
    chave_acesso: Optional[str] = None
    numero_nfe: int
    modelo: Optional[str] = None
    serie: str
    tipo_operacao: Optional[int] = None
    tipo_emissao: Optional[int] = None
    finalidade: int
    indicador_finalidade: str
    indicador_presencial: Optional[str] = None
    data_hora_emissao: Optional[datetime] = None
    data_hora_entrada: Optional[datetime] = None
    natureza: Optional[str] = None
    codigo_natureza: Optional[int] = None
    cfop_id: Optional[int] = None
    cobranca_numero_fatura: Optional[str] = None
    cobranca_valor_original: Optional[Decimal] = None
    cobranca_valor_desconto: Optional[Decimal] = None
    cobranca_valor_liquido: Optional[Decimal] = None
    total_frete_valor: Decimal
    total_seguro_valor: Decimal
    total_valor_outras_despesas: Decimal
    total_desconto_percentual: Decimal
    total_desconto_valor: Decimal
    total_icms_base_calculo: Optional[Decimal] = None
    total_icms_valor: Optional[Decimal] = None
    total_icmsst_base_calculo: Optional[Decimal] = None
    total_icmsst_valor: Optional[Decimal] = None
    total_produto_valor: Optional[Decimal] = None
    total_ipi_valor: Optional[Decimal] = None
    total_pis_valor: Optional[Decimal] = None
    total_cofins_valor: Optional[Decimal] = None
    total_nota_valor: Optional[Decimal] = None
    total_tributos_valor: Optional[Decimal] = None
    total_icmsdesoneracao_valor: Optional[Decimal] = None
    total_icms_uf_destino_valor: Optional[Decimal] = None
    total_icms_uf_remetente_valor: Optional[Decimal] = None
    total_fcp_uf_destino_valor: Optional[Decimal] = None
    indicador_forma_pagamento: Optional[str] = None
    informacoes_adicionais_complementares: Optional[str] = None
    informacoes_adicionais_fisco: Optional[str] = None
    identificador_local_destino: Optional[int] = None
    codigo_nota_fiscal: Optional[str] = None
    chave_dv: Optional[int] = None
    data_hora_contingencia: Optional[datetime] = None
    justificativa_contingencia: Optional[str] = None
    ambiente: Optional[int] = None
    xml: Optional[str] = None
    xml_recibo_emissao: Optional[str] = None
    xml_cancelamento: Optional[str] = None
    justificativa_cancelamento: Optional[str] = None
    recibo_situacao: Optional[str] = None
    lote_emissao: Optional[str] = None
    numero_recibo: Optional[str] = None
    numero_protocolo_autorizacao: Optional[str] = None
    data_hora_protocolo_autorizacao: Optional[datetime] = None
    inutilizado_em: Optional[datetime] = None
    rateavel: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    transportador_modalidade_frete: Optional[str] = None
    importacao: int
    fundo_combate_pobreza: Decimal
    nfe_id: Optional[int] = None
    atualizar_valor_compra: int
    subserie: Optional[str] = None
    codigo_grupo_tensao: Optional[str] = None
    tipo_ligacao: Optional[str] = None
    valor_pis: Optional[Decimal] = None
    valor_cofins: Optional[Decimal] = None
    valor_fornecido: Optional[Decimal] = None
    valor_servico_nao_tributado: Optional[Decimal] = None
    valor_terceiros: Optional[Decimal] = None
    base_icms_energia: Optional[Decimal] = None
    aliq_icms_energia: Optional[Decimal] = None
    valor_icms_energia: Optional[Decimal] = None
    icms_desonerado_totalizer: int

@dataclass
class CompraDestinatario:
    """Tabela: compra_destinatario (Linhas aprox: 62)"""
    id: int
    compra_id: int
    destinatario_cpf_cnpj: str
    destinatario_id_estrangeiro: Optional[str] = None
    destinatario_nome: str
    destinatario_endereco: str
    destinatario_numero: str
    destinatario_complemento: Optional[str] = None
    destinatario_bairro: str
    destinatario_codigo_cidade: str
    destinatario_nome_cidade: str
    destinatario_uf: Optional[str] = None
    destinatario_cep: Optional[str] = None
    destinatario_codigo_pais: str
    destinatario_nome_pais: Optional[str] = None
    destinatario_telefone: Optional[str] = None
    destinatario_indicador_ie: str
    destinatario_ie: Optional[str] = None
    destinatario_inscricao_suframa: Optional[str] = None
    destinatario_inscricao_municipal: Optional[str] = None
    destinatario_email: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class CompraEmitente:
    """Tabela: compra_emitente (Linhas aprox: 62)"""
    id: int
    compra_id: int
    cliente_id: int
    fornecedor_id: int
    codigo_uf: str
    emitente_cnpj: str
    emitente_nome: str
    emitente_fantasia: Optional[str] = None
    emitente_endereco: Optional[str] = None
    emitente_numero: Optional[str] = None
    emitente_complemento: Optional[str] = None
    emitente_bairro: Optional[str] = None
    emitente_codigo_cidade: Optional[str] = None
    emitente_nome_cidade: Optional[str] = None
    emitente_uf: Optional[str] = None
    emitente_cep: Optional[str] = None
    emitente_telefone: Optional[str] = None
    emitente_inscricao_estadual: Optional[str] = None
    emitente_email: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class CompraItem:
    """Tabela: compra_item (Linhas aprox: 347)"""
    id: int
    compra_id: int
    produto_id: int
    tipo_especifico: Optional[str] = None
    codigo_produto: Optional[str] = None
    codigo_ean: Optional[str] = None
    produto_nome: str
    ncm: Optional[str] = None
    cst_csosn: Optional[str] = None
    unidade_comercial: Optional[str] = None
    pedido_compra_numero_compra: Optional[str] = None
    pedido_compra_numero_pedido: Optional[str] = None
    quantidade_comercial: Optional[Decimal] = None
    valor_unitario_comercial: Optional[Decimal] = None
    valor_total_produto: Optional[Decimal] = None
    icms_percentual_reducao_base: Optional[Decimal] = None
    icmsst_valor: Optional[Decimal] = None
    icmsst_retido_base_calculo: Optional[Decimal] = None
    icmsst_retido_valor: Optional[Decimal] = None
    icms_desoneracao_motivo: Optional[Decimal] = None
    icms_desoneracao_valor: Optional[Decimal] = None
    icms_operacao_valor: Optional[Decimal] = None
    icms_diferimento_percentual: Optional[Decimal] = None
    icms_diferimento_valor: Optional[Decimal] = None
    icms_valor: Optional[Decimal] = None
    ipi_valor: Optional[Decimal] = None
    ipi_aliquota: Optional[Decimal] = None
    ipi_enquadramento: Optional[Decimal] = None
    tributos_federais: Optional[Decimal] = None
    tributos_estaduais: Optional[Decimal] = None
    tributos_municipais: Optional[Decimal] = None
    total_tributos: Optional[Decimal] = None
    cest: Optional[str] = None
    especifico: Optional[str] = None
    cfop: Optional[str] = None
    cfop_item_id: int
    icms_aliquota: Optional[Decimal] = None
    icmsst_mva: Optional[Decimal] = None
    icmsst_percentual_reducao_base: Optional[Decimal] = None
    icmsst_aliquota: Optional[Decimal] = None
    pis_cst: Optional[str] = None
    pis_base_calculo: Optional[Decimal] = None
    pis_aliquota: Optional[Decimal] = None
    pis_valor: Optional[Decimal] = None
    cofins_cst: Optional[str] = None
    cofins_aliquota: Optional[Decimal] = None
    cofins_valor: Optional[Decimal] = None
    icmsdifal_base_calculo_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_fcp_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_icms_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_icms_interestadual: Optional[Decimal] = None
    icmsdifal_percentual_provisorio_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_fcp_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_icms_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_icms_uf_remetente: Optional[Decimal] = None
    ipi_cst: Optional[str] = None
    icmsst_base_calculo: Optional[Decimal] = None
    ipi_base_calculo: Optional[Decimal] = None
    icms_base_calculo: Optional[Decimal] = None
    icms_aliquota_credito_simples_nacional: Optional[Decimal] = None
    icms_valor_credito_simples_nacional: Optional[Decimal] = None
    rateavel: int
    unidade_tributavel: Optional[str] = None
    quantidade_tributavel: Optional[Decimal] = None
    valor_unitario_tributavel: Optional[Decimal] = None
    valor_total_frete: Optional[Decimal] = None
    valor_total_seguro: Optional[Decimal] = None
    valor_total_desconto: Optional[Decimal] = None
    valor_total_outras_despesas: Optional[Decimal] = None
    indicador_total: int
    origem: int
    icms_modalidade_base_calculo: Optional[Decimal] = None
    icmsst_modalidade_base_calculo: Optional[Decimal] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    unidade_medida_xml: Optional[str] = None
    quantidade_xml: Optional[Decimal] = None
    fator_conversao: Optional[Decimal] = None
    fcp_st_percentual: Decimal
    fcp_st_valor: Decimal
    lote_numero: Optional[str] = None
    lote_quantidade: Decimal
    lote_data_fabricacao: Optional[date] = None
    lote_data_validade: Optional[date] = None
    lote_codigo_agregacao: Optional[str] = None

@dataclass
class CompraItemGrade:
    """Tabela: compra_item_grade (Linhas aprox: 267)"""
    id: int
    compra_item_id: int
    produto_empresa_grade_id: int
    quantidade: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class CompraObservacao:
    """Tabela: compra_observacao (Linhas aprox: 0)"""
    id: int
    compra_id: int
    observacao_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Condutor:
    """Tabela: condutor (Linhas aprox: 0)"""
    id: int
    nome: str
    cpf: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ConfiguracaoBancaria:
    """Tabela: configuracao_bancaria (Linhas aprox: 0)"""
    id: int
    conta_id: int
    nome: str
    banco_nome: str
    codigo_banco: str
    cnab: str
    logo: Optional[str] = None
    agencia: str
    agencia_dv: str
    conta: str
    conta_dv: str
    mora_multa: float
    juros: float
    carteira: str
    sequencial_nosso_numero: int
    moeda: int
    aceite: str
    especie: str
    convenio: Optional[str] = None
    cip: Optional[str] = None
    emissao: Optional[str] = None
    codigo_cliente: Optional[str] = None
    carteira_dv: Optional[str] = None
    ios: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    protesto: Optional[int] = None
    devolucao: Optional[int] = None
    codigo_multa: int
    codigo_juros: int

@dataclass
class ConfiguracaoBancariaOcorrencia:
    """Tabela: configuracao_bancaria_ocorrencia (Linhas aprox: 0)"""
    id: int
    financeiro_parcela_id: int
    boleto_bancario_id: int
    numero_ocorrencia: str
    remessa: Optional[int] = None
    ocorrencia_retorno: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ConsignacaoDevolucao:
    """Tabela: consignacao_devolucao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    observacao: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    venda_id: Optional[int] = None
    finalizada: int

@dataclass
class ConsignacaoDevolucaoItem:
    """Tabela: consignacao_devolucao_item (Linhas aprox: 0)"""
    id: int
    consignacao_devolucao_id: int
    produto_id: int
    produto_empresa_grade_id: int
    quantidade: Optional[Decimal] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    requisicao_item_id: int
    quantidade_venda: Decimal

@dataclass
class ConsignacaoRequisicao:
    """Tabela: consignacao_requisicao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    fator_id: Optional[int] = None
    observacao: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    cancelada: int
    tipo_preco_id: Optional[int] = None

@dataclass
class ConsignacaoRequisicaoItem:
    """Tabela: consignacao_requisicao_item (Linhas aprox: 0)"""
    id: int
    consignacao_requisicao_id: int
    produto_id: int
    produto_empresa_grade_id: int
    preco: Optional[Decimal] = None
    quantidade: Optional[Decimal] = None
    preco_compra: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Conta:
    """Tabela: conta (Linhas aprox: 3)"""
    id: int
    empresa_id: int
    nome: str
    tipo: str
    saldo_inicial: Optional[Decimal] = None
    data_saldo_inicial: Optional[date] = None
    observacao: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    pattern: int
    permitir_excluir: int
    visible: int
    ativo: int

@dataclass
class ContaBanco:
    """Tabela: conta_banco (Linhas aprox: 0)"""
    id: int
    conta_id: Optional[int] = None
    banco_id: int
    agencia: str
    agencia_dv: str
    conta_corrente: str
    conta_corrente_dv: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    recipient_id: Optional[str] = None
    account_id: Optional[str] = None
    agreement_id: Optional[str] = None
    recipient_code: Optional[str] = None
    format_recipient_code: Optional[str] = None
    wallet_code: Optional[str] = None
    wallet_variation: Optional[str] = None
    last_dispatch: int
    last_our_number: str
    format_our_number: Optional[str] = None
    message_1: Optional[str] = None
    message_2: Optional[str] = None
    accept_code: Optional[str] = None
    species_code: Optional[str] = None
    fine_code: Optional[str] = None
    fine_amount: Decimal
    interest_code: Optional[str] = None
    interest_amount: Decimal
    low_code: Optional[str] = None
    low_days: Optional[str] = None
    occurrence_code: Optional[str] = None
    protest_code: Optional[str] = None
    protest_days: Optional[str] = None
    discount_code: Optional[str] = None
    discount_amount: Optional[Decimal] = None
    instruction_one: Optional[str] = None
    instruction_two: Optional[str] = None
    factor_due: Optional[int] = None
    company_code: Optional[str] = None
    layout_print: Optional[str] = None
    integration_type: Optional[str] = None
    url_webhook: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    posto: Optional[str] = None
    type_key_pix: Optional[str] = None
    key_pix: Optional[str] = None

@dataclass
class ContaCartao:
    """Tabela: conta_cartao (Linhas aprox: 0)"""
    id: int
    conta_id: Optional[int] = None
    cartao_credito_id: int
    conta_baixa_id: Optional[int] = None
    dia_fechamento: int
    dia_vencimento: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ContaSoftcompay:
    """Tabela: conta_softcompay (Linhas aprox: 0)"""
    id: int
    senha_supervisor: int
    ambiente_teste: int
    client_id: str
    client_secret: str
    bank_id: str
    comerciante_id: str
    juros_tipo: Optional[int] = None
    juros: Decimal
    multa_tipo: Optional[int] = None
    multa: Decimal
    abatimento_tipo: Optional[int] = None
    abatimento: Decimal
    dias_apos_vencimento: Optional[int] = None
    conta_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Contador:
    """Tabela: contador (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    nome: str
    cpf: str
    cnpj: Optional[str] = None
    crc: str
    fone: Optional[str] = None
    fax: Optional[str] = None
    email: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Contato:
    """Tabela: contato (Linhas aprox: 0)"""
    id: int
    tipo: str
    cliente_id: Optional[int] = None
    fornecedor_id: Optional[int] = None
    funcionario_id: Optional[int] = None
    transportador_id: Optional[int] = None
    indicador_id: Optional[int] = None
    nome: Optional[str] = None
    ddd: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    nascimento: Optional[date] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ativar_notificacao: int

@dataclass
class ContratoModelo:
    """Tabela: contrato_modelo (Linhas aprox: 0)"""
    id: int
    descricao: str
    texto: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class ContratoServico:
    """Tabela: contrato_servico (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    nfse_id: Optional[int] = None
    dia_cobranca: int
    termino_vigencia: str
    data_termino: Optional[date] = None
    data_encerramento: Optional[date] = None
    usuario_encerramento_id: Optional[int] = None
    motivo_encerramento: Optional[str] = None
    status: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class ContratoServicoItem:
    """Tabela: contrato_servico_item (Linhas aprox: 0)"""
    id: int
    contrato_servico_id: int
    produto_id: int
    produto_empresa_grade_id: int
    descricao: Optional[str] = None
    quantidade: Decimal
    preco: Decimal
    desconto_valor_item: Decimal
    acrescimo_valor_item: Decimal
    percentual_desconto: Optional[Decimal] = None
    percentual_acrescimo: Optional[Decimal] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class Cotacao:
    """Tabela: cotacao (Linhas aprox: 0)"""
    id: int
    data_cotacao: date
    hora_cotacao: datetime
    empresa_id: int
    fornecedor_id: int
    funcionario_id: int
    transportadora_id: int
    tipo_frete: str
    meses_reposicao: int
    numero_pedido: Optional[str] = None
    condicao_pagamento: Optional[str] = None
    garantia: Optional[str] = None
    chegada: Optional[date] = None
    observacao: Optional[str] = None
    nao_mostrar_preco: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CotacaoItem:
    """Tabela: cotacao_item (Linhas aprox: 0)"""
    id: int
    cotacao_id: int
    produto_id: int
    produto_empresa_grade_id: int
    preco: Optional[Decimal] = None
    quantidade: Optional[Decimal] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Credenciadora:
    """Tabela: credenciadora (Linhas aprox: 1)"""
    id: int
    nome: str
    cnpj: Optional[str] = None
    empresa_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    inscricao_estadual: Optional[str] = None
    suframa: Optional[str] = None
    ponto_venda: Optional[str] = None
    conta_banco_id: Optional[int] = None

@dataclass
class Cte:
    """Tabela: cte (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    serie: str
    numero: int
    chave_acesso: Optional[str] = None
    data_emissao: datetime
    tipo_servico: int
    tipo_cte: int
    tipo_impressao: int
    forma_emissao: int
    ambiente: int
    cfop: str
    natureza_operacao: str
    tomador: int
    uf_envio: str
    municipio_envio: str
    cod_municipio_envio: str
    uf_inicio: str
    municipio_inicio: str
    cod_municipio_inicio: str
    uf_fim: str
    municipio_fim: str
    cod_municipio_fim: str
    rota_envio_use_empresa: int
    rota_inicio_use_remetente: int
    indicador_globalizado: Optional[int] = None
    retira_no_destino: Optional[int] = None
    detalhe_retirada: Optional[str] = None
    chave_cte_referenciado: Optional[str] = None
    tabela_frete_id: Optional[int] = None
    valor_total_prestacao: Decimal
    valor_a_receber: Decimal
    valor_total_cte: Decimal
    status: int
    response_codigo_status: Optional[int] = None
    response_motivo: Optional[str] = None
    response_protocolo: Optional[str] = None
    response_data_recebimento: Optional[datetime] = None
    response_transmitido_em: Optional[datetime] = None
    response_xml_resposta: Optional[str] = None
    response_xml_link: Optional[str] = None
    response_pdf_link: Optional[str] = None
    response_cte_id: Optional[str] = None
    observacoes: Optional[str] = None
    caracteristica_servico: Optional[str] = None
    caracteristica_transporte: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteCarga:
    """Tabela: cte_carga (Linhas aprox: 0)"""
    id: int
    cte_id: int
    produto_predominante: str
    outras_caracteristicas: Optional[str] = None
    valor_carga: Decimal
    valor_averbacao: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteCartaCorrecao:
    """Tabela: cte_carta_correcao (Linhas aprox: 0)"""
    id: int
    cte_id: int
    sequencial: int
    correcao_json: str
    protocolo: Optional[str] = None
    codigo_status: Optional[int] = None
    motivo: Optional[str] = None
    data_registro: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteComponenteFrete:
    """Tabela: cte_componente_frete (Linhas aprox: 0)"""
    id: int
    cte_id: int
    nome_componente: str
    valor: Decimal
    ordem: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteDocumentoNfe:
    """Tabela: cte_documento_nfe (Linhas aprox: 0)"""
    id: int
    cte_id: int
    chave_nfe: str
    pin: Optional[str] = None
    data_prevista: Optional[date] = None
    origem: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteDocumentoOutro:
    """Tabela: cte_documento_outro (Linhas aprox: 0)"""
    id: int
    cte_id: int
    tipo_documento: str
    descricao: Optional[str] = None
    numero: Optional[str] = None
    data_emissao: Optional[date] = None
    valor: Optional[Decimal] = None
    subtipo: str
    forma_emissao: Optional[str] = None
    chave_acesso: Optional[str] = None
    cnpj_emitente_anterior: Optional[str] = None
    uf_emitente_anterior: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteEmpresaConfig:
    """Tabela: cte_empresa_config (Linhas aprox: 0)"""
    empresa_id: int
    serie: str
    proximo_numero: int
    cfop_id: Optional[int] = None
    ambiente: int
    forma_emissao: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteEvento:
    """Tabela: cte_evento (Linhas aprox: 0)"""
    id: int
    cte_id: int
    tipo: str
    descricao: Optional[str] = None
    codigo_status: Optional[int] = None
    protocolo: Optional[str] = None
    pdf_link: Optional[str] = None
    xml_link: Optional[str] = None
    payload_json: Optional[str] = None
    response_json: Optional[str] = None
    data_registro: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteIcms:
    """Tabela: cte_icms (Linhas aprox: 0)"""
    id: int
    cte_id: int
    cst: str
    perc_reducao_bc: Optional[Decimal] = None
    base_calculo: Optional[Decimal] = None
    aliquota: Optional[Decimal] = None
    valor_icms: Optional[Decimal] = None
    valor_credito: Optional[Decimal] = None
    bc_st_retido: Optional[Decimal] = None
    valor_st_retido: Optional[Decimal] = None
    aliquota_st_retido: Optional[Decimal] = None
    ind_sn: Optional[int] = None
    difal_ativo: Optional[int] = None
    difal_bc_uf_fim: Optional[Decimal] = None
    difal_aliq_uf_fim: Optional[Decimal] = None
    difal_aliq_interestadual: Optional[Decimal] = None
    difal_valor_uf_ini: Optional[Decimal] = None
    difal_valor_uf_fim: Optional[Decimal] = None
    cst_ibs_cbs: Optional[str] = None
    cod_class_trib: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteModalRodoviario:
    """Tabela: cte_modal_rodoviario (Linhas aprox: 0)"""
    id: int
    cte_id: int
    transportador_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteOcc:
    """Tabela: cte_occ (Linhas aprox: 0)"""
    id: int
    cte_id: int
    serie: Optional[str] = None
    numero: int
    cnpj_emitente: str
    inscricao_estadual: Optional[str] = None
    data_emissao: date
    uf_emitente: str
    codigo_interno: Optional[str] = None
    telefone: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteParticipante:
    """Tabela: cte_participante (Linhas aprox: 0)"""
    id: int
    cte_id: int
    cliente_id: Optional[int] = None
    papel: str
    tipo_documento: str
    cpf_cnpj: str
    razao_social: str
    nome: Optional[str] = None
    tipo_contribuinte: int
    inscricao_estadual: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    end_logradouro: str
    end_numero: str
    end_complemento: Optional[str] = None
    end_bairro: str
    end_cep: str
    end_municipio: str
    end_cod_municipio: str
    end_uf: str
    end_pais: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteQuantidade:
    """Tabela: cte_quantidade (Linhas aprox: 0)"""
    id: int
    cte_id: int
    unidade: str
    tipo_medida: str
    quantidade: Decimal
    ordem: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteTabelaFrete:
    """Tabela: cte_tabela_frete (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    nome: str
    uf_origem: str
    uf_destino: str
    peso_minimo: Optional[Decimal] = None
    peso_maximo: Optional[Decimal] = None
    data_inicio_vigencia: date
    data_fim_vigencia: Optional[date] = None
    ativa: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class CteTabelaFreteComponente:
    """Tabela: cte_tabela_frete_componente (Linhas aprox: 0)"""
    id: int
    tabela_frete_id: int
    nome: str
    valor: Decimal
    ordem: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class DocumentoFiscalCsc:
    """Tabela: documento_fiscal_csc (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    token: str
    token_id: str
    padrao: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Empresa:
    """Tabela: empresa (Linhas aprox: 1)"""
    id: int
    empresa_email_id: Optional[int] = None
    cnpj: str
    inscricao_estadual: Optional[str] = None
    inscricao_estadual_st: Optional[str] = None
    inscricao_municipal: Optional[str] = None
    nome: str
    fantasia: str
    razao_social: str
    ddd: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    habilitar_emitir_nfe: str
    sms_usuario: Optional[str] = None
    sms_senha: Optional[str] = None
    suporte_codigo: int
    suporte_senha: str
    preco_atacado: str
    nome_impressao: str
    mensagem_pedido: Optional[str] = None
    habilitar_mensagem_pedido: int
    nfe_ambiente: str
    nfe_layout: str
    nfe_serie: int
    nfe_tipoemissao_id: int
    nfe_codigo_uf: int
    nuvem_nfe_empresa_id: Optional[int] = None
    certificado_nome: Optional[str] = None
    logomarca: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    troca_prazo: Optional[int] = None
    troca_mensagem: Optional[str] = None
    mfe_chave_validador: Optional[str] = None
    softcom_service_guid: Optional[str] = None
    tipo_inventario: str
    formacao_preco: str
    cartao_cadastro_proprio: int
    timezone: str

@dataclass
class EmpresaBalancaConfiguracao:
    """Tabela: empresa_balanca_configuracao (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    tam_codigo: Optional[str] = None
    info_impressao: Optional[str] = None
    ativar: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class EmpresaEmail:
    """Tabela: empresa_email (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    alias: Optional[str] = None
    driver: Optional[str] = None
    host: Optional[str] = None
    port: Optional[str] = None
    encryption: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class EmpresaMfeAdquirente:
    """Tabela: empresa_mfe_adquirente (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    credenciadora_id: int
    adquirente_descricao: Optional[str] = None
    cnpj_adquirente: Optional[str] = None
    chave_requisicao: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class EmpresaMfePos:
    """Tabela: empresa_mfe_pos (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    credenciadora_id: int
    descricao: Optional[str] = None
    serial: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class EmpresaVendaConfiguracao:
    """Tabela: empresa_venda_configuracao (Linhas aprox: 1)"""
    id: int
    empresa_id: int
    tipo_comissao: str
    nome_destinatario_impressao: str
    agrupar_pagamentos_impressao: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    taxa_servico: Decimal

@dataclass
class Endereco:
    """Tabela: endereco (Linhas aprox: 16)"""
    id: int
    tipo: str
    empresa_id: Optional[int] = None
    funcionario_id: Optional[int] = None
    cliente_id: Optional[int] = None
    fornecedor_id: Optional[int] = None
    transportador_id: Optional[int] = None
    contador_id: Optional[int] = None
    indicador_id: Optional[int] = None
    cep: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    ponto_referencia: Optional[str] = None
    bairro: Optional[str] = None
    cidade_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    credenciadora_id: Optional[int] = None
    laboratorio_id: Optional[int] = None

@dataclass
class Equipamento:
    """Tabela: equipamento (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class EtiquetaConfiguracao:
    """Tabela: etiqueta_configuracao (Linhas aprox: 10)"""
    id: int
    empresa_id: int
    nome: str
    observacao: Optional[str] = None
    tipo_papel: str
    papel_altura: Decimal
    papel_largura: Decimal
    margem_superior: Decimal
    margem_inferior: Decimal
    margem_esquerda: Decimal
    margem_direita: Decimal
    etiqueta_altura: Decimal
    etiqueta_largura: Decimal
    quantidade_colunas: Decimal
    espacamento_colunas: Decimal
    espacamento_linhas: Decimal
    padrao: int
    ativa: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    tipo: str

@dataclass
class EtiquetaItem:
    """Tabela: etiqueta_item (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    produto_empresa_grade_id: int
    quantidade: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Fabricante:
    """Tabela: fabricante (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FailedJobs:
    """Tabela: failed_jobs (Linhas aprox: 0)"""
    id: int
    connection: str
    queue: str
    payload: str
    exception: str
    failed_at: datetime

@dataclass
class FatorAcrescimoConfiguracao:
    """Tabela: fator_acrescimo_configuracao (Linhas aprox: 0)"""
    id: int
    nome: str
    percentual: Decimal
    ativo: int
    empresa_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class Financeiro:
    """Tabela: financeiro (Linhas aprox: 116)"""
    id: int
    empresa_id: int
    data_lancamento: date
    categoria_id: int
    documento: Optional[str] = None
    historico: str
    fornecedor_id: Optional[int] = None
    cliente_id: Optional[int] = None
    contrato_servico_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    valor: Decimal
    tipo_documento_id: Optional[int] = None
    origem: Optional[str] = None
    device_id: Optional[str] = None
    usuario_lancamento_id: Optional[int] = None
    api_device_id: Optional[str] = None
    repeticao: str
    repeticao_tipo: str
    repeticao_quantidade: int
    repeticao_intervalo: int
    termino_vigencia: str
    data_termino_vigencia: Optional[date] = None
    lancamento_troco: int
    transferencia_grupo_id: Optional[str] = None

@dataclass
class FinanceiroCategoria:
    """Tabela: financeiro_categoria (Linhas aprox: 2)"""
    id: int
    code: str
    name: str
    tag: str
    parent_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    fixed: int
    root: int
    color: str
    permitir_excluir: int
    nao_exibir_dre: int
    descricao_original: Optional[str] = None
    segmento: Optional[str] = None
    conta_dre_id: Optional[int] = None
    ativo: int

@dataclass
class FinanceiroCategoriaContaDre:
    """Tabela: financeiro_categoria_conta_dre (Linhas aprox: 32)"""
    id: int
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FinanceiroCategoriaSegmento:
    """Tabela: financeiro_categoria_segmento (Linhas aprox: None)"""
    id: int
    code: str
    name: str
    tag: str
    parent_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    fixed: int
    root: int
    color: str
    permitir_excluir: int
    nao_exibir_dre: int
    descricao_original: Optional[str] = None
    segmento: Optional[str] = None
    conta_dre_id: Optional[int] = None
    ativo: int

@dataclass
class FinanceiroCentroCusto:
    """Tabela: financeiro_centro_custo (Linhas aprox: 0)"""
    financeiro_parcela_id: int
    centro_custo_id: int
    percentual: Decimal
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class FinanceiroCondicaoPagamento:
    """Tabela: financeiro_condicao_pagamento (Linhas aprox: 0)"""
    id: int
    description: str
    forma_pagamento_id: int
    discount: Decimal
    active: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FinanceiroCondicaoPagamentoParcela:
    """Tabela: financeiro_condicao_pagamento_parcela (Linhas aprox: 0)"""
    id: int
    financeiro_condicao_pagamento_id: int
    order: int
    days: int
    acrescimo: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FinanceiroExtratoBancario:
    """Tabela: financeiro_extrato_bancario (Linhas aprox: 0)"""
    id: int
    tipo: str
    data: date
    valor: Decimal
    operacao: str
    banco: Optional[str] = None
    banco_codigo: Optional[str] = None
    banco_agencia: Optional[str] = None
    banco_agencia_dv: Optional[str] = None
    banco_conta: Optional[str] = None
    banco_conta_dv: Optional[str] = None
    credenciadora: Optional[str] = None
    bandeira: Optional[str] = None
    bandeira_tipo: Optional[str] = None
    identificador_transacao: str
    numero_checagem: str
    descricao: Optional[str] = None
    conciliado: int
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FinanceiroParcela:
    """Tabela: financeiro_parcela (Linhas aprox: 116)"""
    id: int
    compra_id: Optional[int] = None
    venda_id: Optional[int] = None
    financeiro_id: Optional[int] = None
    transferencia_id: Optional[int] = None
    fornecedor_id: Optional[int] = None
    cliente_id: Optional[int] = None
    contrato_servico_id: Optional[int] = None
    documento: Optional[str] = None
    forma_pagamento_id: int
    conta_id: Optional[int] = None
    cartao_credito_id: Optional[int] = None
    venda_cartao_id: Optional[int] = None
    api_codigo_pagamento: Optional[str] = None
    api_nome_pagamento: Optional[str] = None
    parcela: Optional[str] = None
    cheque_agenciabancaria_id: Optional[int] = None
    cheque_agencia: Optional[str] = None
    cheque_conta: Optional[str] = None
    cheque_numero: Optional[str] = None
    cheque_emitente: Optional[str] = None
    cheque_devolucao_data: Optional[date] = None
    cheque_devolucao_motivo: Optional[int] = None
    vencimento: date
    valor_parcela: Decimal
    tarifa: Optional[Decimal] = None
    duplicata_pendente: int
    banco_id: Optional[int] = None
    forma_pagamento_baixa_id: Optional[int] = None
    financeira_id: Optional[int] = None
    data_pagamento: Optional[date] = None
    valor_pago: Optional[Decimal] = None
    data_caixa: Optional[date] = None
    observacao: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    acrescimo: Optional[Decimal] = None
    desconto: Optional[Decimal] = None
    cancelada: int
    parcela_vinculada: Optional[int] = None
    operacao: Optional[str] = None
    empresa_id: Optional[int] = None
    user_id: Optional[int] = None
    motivo_cancelamento: Optional[str] = None
    cheque_banco: Optional[str] = None
    data_cancelamento: Optional[datetime] = None
    guid: Optional[str] = None
    pos_habilitar: Optional[int] = None
    tp_integra: Optional[int] = None
    api_cobranca_id: Optional[str] = None
    api_cobranca_agreemente_id: Optional[str] = None
    codigo_autorizacao: Optional[str] = None
    cnpj_instituicao_financeira: Optional[str] = None
    cartao_credito_taxa_admin: Optional[Decimal] = None
    tipo_debito_id: Optional[int] = None
    conciliacao_extrato_bancario: int
    caixa_funcoes_id: Optional[int] = None
    financeiro_condicao_pagamento_id: Optional[int] = None
    condicao_pagamento_id: Optional[int] = None

@dataclass
class FinanceiroParcelaArquivo:
    """Tabela: financeiro_parcela_arquivo (Linhas aprox: 0)"""
    id: int
    parent_id: int
    description: Optional[str] = None
    filename: str
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    extension: str
    link: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FinanceiroParcelaPagamento:
    """Tabela: financeiro_parcela_pagamento (Linhas aprox: 23)"""
    id: int
    valor_pago: Decimal
    acrescimo: Decimal
    desconto: Decimal
    conta_id: Optional[int] = None
    forma_pagamento_baixa_id: int
    financeiro_parcela_id: int
    data_pagamento: date
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    user_baixa_id: Optional[int] = None
    api_device_id: Optional[str] = None
    valor_recebido: Decimal
    caixa_funcoes_id: Optional[int] = None
    caixa_turno: Optional[str] = None

@dataclass
class FinanceiroParcelaPix:
    """Tabela: financeiro_parcela_pix (Linhas aprox: 0)"""
    id: int
    financeiro_parcela_id: int
    conta_id: int
    key_alias_id: str
    amount: Decimal
    qrcode_type: str
    expiration: int
    duedate: date
    vencimento: date
    days_after_duedate: int
    description: Optional[str] = None
    transaction_id: Optional[str] = None
    transaction_type: Optional[str] = None
    transaction_status: Optional[str] = None
    transaction_qrcode: Optional[str] = None
    transaction_link: Optional[str] = None
    transaction_all: Optional[str] = None
    transaction_data_pagamento: Optional[date] = None
    transaction_valor_pago: Optional[Decimal] = None
    transaction_comprovante: Optional[str] = None
    response_id: Optional[str] = None
    bank_tax_id: Optional[str] = None
    end_to_end: Optional[str] = None
    estorno_all: Optional[str] = None
    estorno_comprovante: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FinanceiroParcelaPixBilling:
    """Tabela: financeiro_parcela_pix_billing (Linhas aprox: 0)"""
    id: int
    financeiro_parcela_pix_id: int
    payer_name: str
    payer_taxid: str
    payer_email: str
    payer_address_street: str
    payer_address_city: str
    payer_address_state: str
    payer_address_postalcode: str
    interest_modality: Optional[int] = None
    interest_value: Optional[Decimal] = None
    fine_modality: Optional[int] = None
    fine_value: Optional[Decimal] = None
    discount_modality: Optional[int] = None
    discount_value: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FinanceiroTroco:
    """Tabela: financeiro_troco (Linhas aprox: 0)"""
    id: int
    valor: float
    caixa_usuario_id: Optional[int] = None
    caixa_data: Optional[date] = None
    caixa_turno: Optional[int] = None
    caixa_funcoes_id: Optional[int] = None
    tipo: str
    device_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class FormaPagamento:
    """Tabela: forma_pagamento (Linhas aprox: 28)"""
    id: int
    nome: str
    tipo: str
    permitir_excluir: int
    codigo_nfce: str
    credenciadora_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ordem: Optional[int] = None
    codigo_transacao_sitef: Optional[str] = None
    carteira_digital: int
    pdv_pos: int
    integrar_api: int
    permitir_alterar: int
    exibir_pagamento: int
    pre_venda: int
    saldo_caixa: int
    atalho_numero: Optional[int] = None

@dataclass
class Fornecedor:
    """Tabela: fornecedor (Linhas aprox: 14)"""
    id: int
    pessoa: str
    cpf_cnpj: Optional[str] = None
    inscricao_estadual: Optional[str] = None
    inscricao_municipal: Optional[str] = None
    nome: str
    razao_social: str
    representante: Optional[str] = None
    ddd: Optional[str] = None
    telefone: Optional[str] = None
    site: Optional[str] = None
    observacao: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    funcionario_id: Optional[int] = None

@dataclass
class FornecedorBoleto:
    """Tabela: fornecedor_boleto (Linhas aprox: 0)"""
    id: int
    fornecedor_id: int
    banco: str
    codigo_boleto: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Funcionario:
    """Tabela: funcionario (Linhas aprox: 2)"""
    id: int
    empresa_id: int
    cpf: Optional[str] = None
    rg: Optional[str] = None
    nome: str
    usuario_id: Optional[int] = None
    funcao_id: int
    setor_id: Optional[int] = None
    data_admissao: Optional[date] = None
    data_demissao: Optional[date] = None
    desconto_percentual: Optional[Decimal] = None
    comissao: Optional[Decimal] = None
    desativado: int
    observacao: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    supervisor: int
    numero_cartao_supervisor: Optional[str] = None
    veterinario: Optional[int] = None
    crmv: Optional[str] = None
    numero_mapa: Optional[str] = None
    numero_sipeagro: Optional[str] = None

@dataclass
class GestaoEstoqueConfiguracao:
    """Tabela: gestao_estoque_configuracao (Linhas aprox: 0)"""
    id: int
    tipo: str
    empresa_id: Optional[int] = None
    dados: Optional[str] = None
    filtro_ultimos_meses: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class GestaoEstoqueConsolidadoMensal:
    """Tabela: gestao_estoque_consolidado_mensal (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    data_competencia: Optional[date] = None
    estoque_volume_medio: Optional[Decimal] = None
    quantidade_produtos_disponiveis: Optional[Decimal] = None
    quantidade_produtos_vendidos: Optional[Decimal] = None
    quantidade_volumes_vendidos: Optional[Decimal] = None
    media_diaria_venda: Optional[Decimal] = None
    quantidade_ruptura: Optional[Decimal] = None
    valor_compra: Optional[Decimal] = None
    valor_venda: Optional[Decimal] = None
    quantidade_baixa_demanda: Optional[Decimal] = None
    porcentagem_positivacao_produtos: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Grupo:
    """Tabela: grupo (Linhas aprox: 4)"""
    id: int
    parent_id: Optional[int] = None
    nome: str
    editavel: Optional[str] = None
    vender: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    imagem: Optional[str] = None
    armacao: int
    lente: int
    restaurante_familia_id: Optional[int] = None
    habilitar_acompanhamento: Optional[int] = None
    acompanhamento_grupo_id: Optional[int] = None
    qtd_max: Optional[int] = None
    self_service: Optional[int] = None
    perguntar_adicionais: Optional[int] = None
    nao_enviar_comanda: Optional[int] = None
    cobrar_taxa_servico: Optional[int] = None
    adicional: Optional[int] = None
    marketplace_created_at: Optional[datetime] = None
    marketplace_updated_at: Optional[datetime] = None
    marketplace_code: Optional[str] = None
    restaurante_setor_id: Optional[int] = None
    hub_code: Optional[str] = None
    hub_name: Optional[str] = None
    hub_name_full: Optional[str] = None
    ativo: int
    comissao: Decimal
    hortifruit: int
    restricao_idade: int

@dataclass
class GrupoAdicional:
    """Tabela: grupo_adicional (Linhas aprox: 0)"""
    id: int
    grupo_id: int
    grupo_adicional_id: int
    quantidade_limite: int
    ordem: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class GrupoMarketplace:
    """Tabela: grupo_marketplace (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    descricao: str
    habilitar: int
    grupo_id: int
    marketplace_vinculado_id: Optional[int] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    hub_code: Optional[str] = None
    hub_name: Optional[str] = None

@dataclass
class Indicador:
    """Tabela: indicador (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cpf_cnpj: Optional[str] = None
    inscricao_estadual: Optional[str] = None
    inscricao_municipal: Optional[str] = None
    pessoa: str
    nome: str
    razao_social: str
    observacao: Optional[str] = None
    comissao: Decimal
    desativado: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class IntegracaoLog:
    """Tabela: integracao_log (Linhas aprox: 0)"""
    id: int
    data: Optional[datetime] = None
    tipo_integracao: str
    origem: str
    origem_id: Optional[str] = None
    mensagem: str
    requisicao_id: Optional[str] = None
    endpoint: Optional[str] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Laboratorio:
    """Tabela: laboratorio (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cnpj: Optional[str] = None
    nome: str
    responsavel: Optional[str] = None
    telefone: Optional[str] = None
    observacao: Optional[str] = None
    desativado: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronico:
    """Tabela: manifesto_documento_eletronico (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    versao: str
    chave_acesso: str
    tipo_ambiente: int
    tipo_emitente: int
    tipo_transporte: Optional[int] = None
    modelo: str
    serie: str
    numero_mdfe: int
    codigo_chave_acesso: str
    digito_verificador: int
    modal: int
    modalidade_transporte: int
    data_hora_emissao: Optional[datetime] = None
    tipo_emissao: int
    processo_emissao: int
    versao_processo: str
    carregamento_uf: str
    descarregamento_uf: str
    numero_lacre: Optional[str] = None
    total_quantidade_cte: Decimal
    total_quantidade_nfe: Decimal
    total_quantidade_mdfe: Decimal
    total_carga_valor: Decimal
    total_carga_quantidade: Decimal
    total_codigo_unidade: str
    unidade_medida: str
    data_hora_encerramento: Optional[datetime] = None
    validado: Optional[int] = None
    informacao_fisco: Optional[str] = None
    informacao_complementar_contribuinte: Optional[str] = None
    xml: Optional[str] = None
    cancelamento_xml: Optional[str] = None
    recibo_situacao: str
    recibo_numero: Optional[str] = None
    lote_numero: Optional[str] = None
    data_inutilizacao: Optional[datetime] = None
    recibo_xml: Optional[str] = None
    recibo_protocolo: Optional[str] = None
    encerramento_xml: Optional[str] = None
    encerramento_protocolo: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    rntrc_emitente: Optional[str] = None
    canal_verde: Optional[int] = None
    carregamento_posterior: Optional[int] = None

@dataclass
class ManifestoDocumentoEletronicoAutorizadoXml:
    """Tabela: manifesto_documento_eletronico_autorizado_xml (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    autorizado_cpf: Optional[str] = None
    autorizado_cnpj: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoCargaDescarga:
    """Tabela: manifesto_documento_eletronico_carga_descarga (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    carregamento_codigo_cidade: Optional[str] = None
    carregamento_nome: Optional[str] = None
    descarregamento_codigo_cidade: Optional[str] = None
    descarregamento_nome: Optional[str] = None
    ordem: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoDocumento:
    """Tabela: manifesto_documento_eletronico_documento (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    carga_descarga_id: int
    documento_tipo: Optional[str] = None
    documento_chave_acesso: str
    documento_segundo_codigo_barra: Optional[str] = None
    documento_indicador_reentrega: int
    documento_quantidade_rateada: Optional[Decimal] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    manifesto_documento_eletronico_inclusao_id: Optional[int] = None

@dataclass
class ManifestoDocumentoEletronicoDocumentoUnidadeTransporte:
    """Tabela: manifesto_documento_eletronico_documento_unidade_transporte (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    manifesto_documento_eletronico_documento_id: int
    unidade_transporte_id: Optional[int] = None
    unidade_transporte_tipo_unidade: Optional[int] = None
    unidade_transporte_identificacao: Optional[str] = None
    unidade_transporte_quantidade_rateada: Optional[Decimal] = None
    unidade_carga_tipo_unidade: Optional[int] = None
    unidade_carga_identificacao: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoEmitente:
    """Tabela: manifesto_documento_eletronico_emitente (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    codigo_uf: str
    emitente_cnpj: str
    emitente_nome: str
    emitente_fantasia: Optional[str] = None
    emitente_endereco: Optional[str] = None
    emitente_numero: Optional[str] = None
    emitente_complemento: Optional[str] = None
    emitente_bairro: Optional[str] = None
    emitente_codigo_cidade: Optional[str] = None
    emitente_nome_cidade: Optional[str] = None
    emitente_uf: Optional[str] = None
    emitente_cep: Optional[str] = None
    emitente_telefone: Optional[str] = None
    emitente_inscricao_estadual: Optional[str] = None
    emitente_email: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoInclusao:
    """Tabela: manifesto_documento_eletronico_inclusao (Linhas aprox: 0)"""
    id: int
    mdfe_id: int
    sequencia: int
    xml_evento: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoLacre:
    """Tabela: manifesto_documento_eletronico_lacre (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    unidade_transporte_id: Optional[int] = None
    lacre_numero: Optional[str] = None
    veiculo_lacre_numero: Optional[str] = None
    documento_transporte_lacre_numero: Optional[str] = None
    documento_carga_lacre_numero: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoPagamentoFreteLancamentos:
    """Tabela: manifesto_documento_eletronico_pagamento_frete_lancamentos (Linhas aprox: 0)"""
    id: int
    tipo: str
    tipo_pagamento: str
    numero_parcela: Optional[str] = None
    vencimento: Optional[date] = None
    valor: Decimal
    tipo_componente: Optional[str] = None
    descricao_componente: str
    manifesto_documento_eletronico_pagamento_frete_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoPagamentosFrete:
    """Tabela: manifesto_documento_eletronico_pagamentos_frete (Linhas aprox: 0)"""
    id: int
    responsavel: str
    cpf_cnpj: str
    valor_contrato: Decimal
    banco_id: int
    banco_agencia: str
    banco_cnpj: str
    tipo_pagamento: str
    manifesto_documento_eletronico_id: int
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoPercurso:
    """Tabela: manifesto_documento_eletronico_percurso (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    percurso_sigla_uf: str
    percurso_data_hora_inicio: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoProdutoPredominante:
    """Tabela: manifesto_documento_eletronico_produto_predominante (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    tipo_carga: str
    produto: str
    ncm: Optional[str] = None
    codigo_barras: Optional[str] = None
    carregamento_cep: Optional[str] = None
    carregamento_latitude: Optional[float] = None
    carregamento_longitude: Optional[float] = None
    descarregamento_cep: Optional[str] = None
    descarregamento_latitude: Optional[float] = None
    descarregamento_longitude: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoResponsavelTecnico:
    """Tabela: manifesto_documento_eletronico_responsavel_tecnico (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    cnpj: str
    contato: str
    email: str
    fone: str
    id_csrt: Optional[str] = None
    hash_csrt: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoSeguro:
    """Tabela: manifesto_documento_eletronico_seguro (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    seguro_responsavel: str
    seguro_cnpj: Optional[str] = None
    seguro_cpf: Optional[str] = None
    seguro_nome_seguradora: Optional[str] = None
    seguro_cnpj_seguradora: Optional[str] = None
    seguro_numero_apolice: Optional[str] = None
    seguro_numero_averbacao: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoVeiculo:
    """Tabela: manifesto_documento_eletronico_veiculo (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    veiculo_tipo: Optional[str] = None
    veiculo_codigo_veiculo: Optional[str] = None
    veiculo_placa: Optional[str] = None
    veiculo_renavam: Optional[str] = None
    veiculo_tara: Optional[str] = None
    veiculo_capacidade_kg: Optional[str] = None
    veiculo_capacidade_m3: Optional[str] = None
    veiculo_proprietario_cpf: Optional[str] = None
    veiculo_proprietario_cnpj: Optional[str] = None
    veiculo_proprietario_rntrc: Optional[str] = None
    veiculo_proprietario_nome: Optional[str] = None
    veiculo_proprietario_inscricao_estadual: Optional[str] = None
    veiculo_proprietario_uf: Optional[str] = None
    veiculo_proprietario_tipo: Optional[int] = None
    veiculo_tipo_rodado: Optional[str] = None
    veiculo_tipo_carroceria: Optional[str] = None
    veiculo_uf_licenciado: Optional[str] = None
    veiculo_codigo_agendamento_portuario: Optional[str] = None
    agencia_reguladora_rntrc: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoVeiculoAgencia:
    """Tabela: manifesto_documento_eletronico_veiculo_agencia (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    veiculo_id: Optional[int] = None
    agencia_tipo: Optional[str] = None
    agencia_codigo: Optional[str] = None
    agencia_cpf: Optional[str] = None
    agencia_cnpj: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoVeiculoAgenciaValePedagio:
    """Tabela: manifesto_documento_eletronico_veiculo_agencia_vale_pedagio (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    veiculo_id: int
    agencia_id: int
    vale_pedagio_cnpj_fornecedora: Optional[str] = None
    vale_pedagio_cnpj_pg: Optional[str] = None
    vale_pedagio_cpf_pg: Optional[str] = None
    vale_pedagio_numero_comprovante: str
    vale_pedagio_valor: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoVeiculoCondutor:
    """Tabela: manifesto_documento_eletronico_veiculo_condutor (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    veiculo_id: int
    veiculo_condutor_nome: str
    veiculo_condutor_cpf: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ManifestoDocumentoEletronicoVeiculoPerigoso:
    """Tabela: manifesto_documento_eletronico_veiculo_perigoso (Linhas aprox: 0)"""
    id: int
    manifesto_documento_eletronico_id: int
    documento_id: int
    perigoso_numero_onu: str
    perigoso_nome_embarque: Optional[str] = None
    perigoso_classe_risco: Optional[str] = None
    perigoso_grupo_embalagem: Optional[str] = None
    perigoso_quantidade_total_produto: str
    perigoso_quantidade_volume_tipo: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class MarcaEquipamento:
    """Tabela: marca_equipamento (Linhas aprox: 0)"""
    id: int
    equipamento_id: int
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class MarcaVeiculo:
    """Tabela: marca_veiculo (Linhas aprox: 47)"""
    id: int
    marca: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class MarketplaceCategoria:
    """Tabela: marketplace_categoria (Linhas aprox: 0)"""
    id: int
    merchant_marketplace_id: Optional[str] = None
    category_id: str
    category_name: str
    category_code: Optional[str] = None
    category_availability: str
    grupo_id: Optional[int] = None
    empresa_id: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class MarketplaceConfig:
    """Tabela: marketplace_config (Linhas aprox: 1)"""
    id: int
    funcionario_id: Optional[int] = None
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ultima_sincronizacao_cadastro: Optional[datetime] = None
    tempo_sinc_cadastro: int
    ultima_sincronizacao_venda: Optional[datetime] = None
    tempo_sinc_venda: int
    ultima_sincronizacao_estoque: Optional[datetime] = None
    tempo_sinc_estoque: int

@dataclass
class MarketplaceGestorProduto:
    """Tabela: marketplace_gestor_produto (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    produto_empresa_grade_id: Optional[int] = None
    grupo_id: Optional[int] = None
    categoria_id: Optional[int] = None
    marketplace_id: Optional[str] = None
    integrar: Optional[str] = None
    status: Optional[str] = None
    atualizar_categoria_id: Optional[int] = None
    atualizar_disponibilidade: Optional[str] = None
    atualizar_integrar: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class MarketplaceGestorProdutoItem:
    """Tabela: marketplace_gestor_produto_item (Linhas aprox: 0)"""
    id: int
    marketplace_gestor_produto_id: int
    produto_id: Optional[int] = None
    produto_empresa_grade_id: int
    categoria_item_id: Optional[int] = None
    disponibilidade: str
    integrar: int
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class MarketplaceGrupoEmpresa:
    """Tabela: marketplace_grupo_empresa (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    grupo_id: int
    marketplace_code: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class MarketplaceHubSaleschannel:
    """Tabela: marketplace_hub_saleschannel (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    codigo: str
    nome: str
    possui_anuncio: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    seller_id: Optional[str] = None

@dataclass
class MarketplacePagamentoConversao:
    """Tabela: marketplace_pagamento_conversao (Linhas aprox: 8)"""
    id: int
    forma_pagamento_marketplace: str
    forma_pagamento_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class MarketplacePedido:
    """Tabela: marketplace_pedido (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    marketplace_id: str
    merchant_marketplace_id: str
    order_id: str
    order_number: str
    order_date: datetime
    notes: Optional[str] = None
    status: str
    invoice_number: Optional[str] = None
    discount: Decimal
    shipping_cost: Decimal
    total: Decimal
    customer_name: str
    customer_document: str
    customer: str
    shipping: str
    invoice_issue_date: Optional[datetime] = None
    done_date: Optional[datetime] = None
    items: str
    payments: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class MarketplaceProduto:
    """Tabela: marketplace_produto (Linhas aprox: 0)"""
    id: int
    merchant_marketplace_id: Optional[str] = None
    product_code: Optional[str] = None
    product_id: str
    product_name: str
    product_sku: Optional[str] = None
    product_gtin: Optional[str] = None
    product_availability: Optional[str] = None
    product_measure: Optional[str] = None
    product_grid: int
    product_stock_active: int
    product_stock_min: Decimal
    product_stock: Decimal
    product_price: Decimal
    product_description: Optional[str] = None
    product_promotion_price: Decimal
    product_promotion_start: Optional[date] = None
    product_promotion_validity: Optional[date] = None
    category_id: Optional[str] = None
    category_code: Optional[str] = None
    category_name: Optional[str] = None
    produto_empresa_id: Optional[int] = None
    empresa_id: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class MarketplaceProdutoGrade:
    """Tabela: marketplace_produto_grade (Linhas aprox: 0)"""
    id: int
    merchant_marketplace_id: Optional[str] = None
    product_grid_id: str
    product_grid_code: Optional[str] = None
    product_grid_name: Optional[str] = None
    product_grid_sku: Optional[str] = None
    product_grid_gtin: Optional[str] = None
    product_grid_availability: Optional[str] = None
    product_grid_price: Decimal
    product_grid_specifications: Optional[str] = None
    product_id: Optional[str] = None
    product_name: Optional[str] = None
    produto_empresa_grade_id: Optional[int] = None
    empresa_id: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class MarketplaceVinculado:
    """Tabela: marketplace_vinculado (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    merchant_marketplace_id: str
    name: str
    active: int
    marketplace_id: str
    marketplace_name: str
    marketplace_crypto_data: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    is_hub: int

@dataclass
class MdfeSerie:
    """Tabela: mdfe_serie (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    serie: int
    numeracao_inicial: int
    padrao: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    ambiente: Optional[int] = None
    tipo_serie: Optional[str] = None
    oauth_client_id: Optional[str] = None

@dataclass
class Medico:
    """Tabela: medico (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    nome: str
    crm: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class MenuFavorito:
    """Tabela: menu_favorito (Linhas aprox: 0)"""
    id: int
    user_id: int
    nome: str
    ordem: int
    url: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    data: Optional[str] = None

@dataclass
class MeuLucroVisaoGeral:
    """Tabela: meu_lucro_visao_geral (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    data_competencia: Optional[date] = None
    config_lucro_pretendido: Optional[Decimal] = None
    config_saldo_caixa: Optional[Decimal] = None
    config_quantidade_funcionario: Optional[int] = None
    config_tamanho_estrutura: Optional[Decimal] = None
    config_despesa_fixa_folha_pagamento: Optional[Decimal] = None
    config_despesa_fixa_pro_labore: Optional[Decimal] = None
    config_despesa_fixa_aluguel: Optional[Decimal] = None
    config_despesa_fixa_outras: Optional[Decimal] = None
    config_despesa_variavel_imposto: Optional[Decimal] = None
    config_despesa_variavel_taxa_antecipacao: Optional[Decimal] = None
    config_despesa_variavel_comissao: Optional[Decimal] = None
    config_despesa_variavel_custo_mercadoria_vendida: Optional[Decimal] = None
    config_despesa_variavel_custo_mercadoria_vendida_sistema: int
    config_despesa_variavel_margem_lucro_bruto: Decimal
    config_despesa_variavel_outras_despesas: Optional[Decimal] = None
    config_categoria_receita_id: Optional[int] = None
    config_categoria_despesa_id: Optional[int] = None
    config_emprestimo_financiamento_manual: int
    config_valor_emprestimo_entrada: Decimal
    config_valor_emprestimo_saida: Decimal
    ind_faturamento_por_funcionario: Optional[Decimal] = None
    ind_faturamento_por_m2: Optional[Decimal] = None
    ind_prazo_medio_pagamento: Optional[Decimal] = None
    ind_prazo_medio_recebimento: Optional[Decimal] = None
    ind_ticket_medio: Optional[Decimal] = None
    ind_custo_por_mercadoria: Optional[Decimal] = None
    ind_lucro_por_funcionario: Optional[Decimal] = None
    ind_lucro_por_m2: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ind_faturamento: Decimal
    ind_faturamento_mes_anterior: Decimal
    ind_recebimentos_vendas: Decimal
    ind_pagamento_fornecedores: Decimal
    ind_outras_despesas: Decimal
    ind_entradas_financiamentos: Decimal
    ind_pagamentos_financiamentos: Decimal
    ind_lucro_prejuizo_acumulado: Decimal
    ind_quantidade_pedidos: int
    ind_valor_taxas_cartao: Decimal
    ind_percentual_taxas_cartao: Decimal
    ind_impostos: Decimal
    ind_receita_liquida: Decimal
    ind_custo_mercadoria: Decimal
    ind_taxa_cartao: Decimal
    ind_comissao: Decimal
    ind_custos_fixos: Decimal
    ind_margem_lucro: Decimal
    ind_margem_contribuicao: Decimal
    ind_lucro_liquido: Decimal
    ind_saldo_fco: Decimal
    ind_saldo_fcf: Decimal
    ind_saldo_final: Decimal

@dataclass
class Migrations:
    """Tabela: migrations (Linhas aprox: 1299)"""
    migration: str
    batch: int

@dataclass
class Modulo:
    """Tabela: modulo (Linhas aprox: 41)"""
    id: int
    versao_atual: str
    modulo: str
    descricao: str
    visivel: int
    separado: int
    versao: str
    nivel: int
    ativo: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    parametrizacao_fiscal: str
    segmento_assistencia: Optional[str] = None

@dataclass
class ModuloConfiguracao:
    """Tabela: modulo_configuracao (Linhas aprox: 6)"""
    id: int
    modulo_id: int
    configuracao: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    alias: Optional[str] = None

@dataclass
class Movimentacao:
    """Tabela: movimentacao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    data_operacao: date
    operacao: str
    tipo_ajuste_id: Optional[int] = None
    empresa_destino_id: Optional[int] = None
    observacao: Optional[str] = None
    tipo_destinatario: str
    fornecedor_id: Optional[int] = None
    cliente_id: Optional[int] = None
    finalidade_codigo: int
    cfop_codigo: Optional[int] = None
    chave_nfe: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    balanco_id: Optional[int] = None
    producao_id: Optional[int] = None
    caixa_funcoes_id: Optional[int] = None
    nfe_id: Optional[int] = None

@dataclass
class MovimentacaoItem:
    """Tabela: movimentacao_item (Linhas aprox: 26)"""
    id: int
    movimentacao_id: int
    produto_id: int
    produto_empresa_grade_id: int
    produto_empresa_grade_destino_id: Optional[int] = None
    quantidade: Decimal
    preco: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfceCfop:
    """Tabela: nfce_cfop (Linhas aprox: 9)"""
    id: int
    codigo: int
    natureza: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfceSerie:
    """Tabela: nfce_serie (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    serie: int
    numeracao_inicial: int
    padrao: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    ambiente: Optional[int] = None
    tipo_serie: Optional[str] = None
    oauth_client_id: Optional[str] = None
    numero: Optional[str] = None

@dataclass
class NfeCest:
    """Tabela: nfe_cest (Linhas aprox: None)"""
    id: int
    codigo: str
    ncm: Optional[str] = None
    descricao: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeCidade:
    """Tabela: nfe_cidade (Linhas aprox: 5640)"""
    id: int
    cidade_uf: str
    c_cidade: int
    cidade: str
    c_uf: int
    short_uf: str
    full_uf: str
    c_pais: str
    pais: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeClassificacaoTributaria:
    """Tabela: nfe_classificacao_tributaria (Linhas aprox: None)"""
    id: int
    cst: str
    cst_descricao: str
    cclass_trib: str
    cclass_trib_nome: str
    cclass_trib_descricao: str
    ibs_percentual_red: Decimal
    cbs_percentual_red: Decimal
    ind_nfe: int
    ind_nfce: int
    ind_nfse: int
    ind_cte: int
    vigencia_data_inicio: Optional[date] = None
    vigencia_data_fim: Optional[date] = None
    data_atualizacao: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ind_g_ibs_cbs: int
    ind_g_ibs_cbs_mono: int
    ind_g_red: int
    ind_g_dif: int

@dataclass
class NfeCodigoGenero:
    """Tabela: nfe_codigo_genero (Linhas aprox: 100)"""
    id: int
    codigo: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeCofins:
    """Tabela: nfe_cofins (Linhas aprox: 33)"""
    id: int
    codigo: str
    nome: str
    tipo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeCst:
    """Tabela: nfe_cst (Linhas aprox: 25)"""
    id: int
    cst: str
    natureza: str
    nome: Optional[str] = None
    crt: int
    deleted_at: Optional[datetime] = None
    nfce: Optional[int] = None
    crt_mei: int
    cst_substituicao: str

@dataclass
class NfeEspecifico:
    """Tabela: nfe_especifico (Linhas aprox: 4)"""
    id: int
    codigo: str
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeFinalidade:
    """Tabela: nfe_finalidade (Linhas aprox: 0)"""
    id: int
    codigo: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeGrupo:
    """Tabela: nfe_grupo (Linhas aprox: 110)"""
    id: int
    nome: str
    cst_relacionado: Optional[str] = None
    cst_relacionado2: Optional[str] = None
    sub_grupo: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeGrupoTensao:
    """Tabela: nfe_grupo_tensao (Linhas aprox: 14)"""
    id: int
    codigo: str
    descricao: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeIbpt:
    """Tabela: nfe_ibpt (Linhas aprox: 0)"""
    id: int
    ncm: int
    aliquota_federal: Decimal
    aliquota_estadual: Decimal
    aliquota_municipal: Decimal
    aliquota_federal_texto: Optional[str] = None
    aliquota_estadual_texto: Optional[str] = None
    aliquota_municipal_texto: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeIcmsAliquota:
    """Tabela: nfe_icms_aliquota (Linhas aprox: None)"""
    id: int
    uf_origem_id: int
    uf_origem_sigla: str
    uf_destino_id: int
    uf_destino_sigla: str
    aliquota: Decimal
    ano_base: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeIcmsSt:
    """Tabela: nfe_icms_st (Linhas aprox: 4)"""
    id: int
    codigo: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeInformacoesAdicionais:
    """Tabela: nfe_informacoes_adicionais (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    texto: Optional[str] = None
    tipo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    padrao: int

@dataclass
class NfeMensagemHumanizada:
    """Tabela: nfe_mensagem_humanizada (Linhas aprox: 4)"""
    id: int
    ws_id: Optional[str] = None
    codigo_app: Optional[str] = None
    codigo_erro: Optional[str] = None
    codigo_faq: Optional[str] = None
    mensagem: Optional[str] = None
    link: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NfeModbaseicms:
    """Tabela: nfe_modbaseicms (Linhas aprox: 7)"""
    id: int
    codigo: int
    descricao: str
    descricao_st: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeMotivoDesoneracao:
    """Tabela: nfe_motivo_desoneracao (Linhas aprox: 45)"""
    id: int
    cst_codigo: str
    codigo: int
    motivo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeNatureza:
    """Tabela: nfe_natureza (Linhas aprox: None)"""
    id: int
    natureza: str
    cfop: str
    operacao: str
    descricao: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    nfce: int
    cfop_substituicao: Optional[int] = None

@dataclass
class NfeOrigem:
    """Tabela: nfe_origem (Linhas aprox: 9)"""
    id: int
    codigo: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfePais:
    """Tabela: nfe_pais (Linhas aprox: None)"""
    id: int
    cpais: int
    xpais: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfePis:
    """Tabela: nfe_pis (Linhas aprox: 34)"""
    id: int
    codigo: str
    nome: str
    tipo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeSerie:
    """Tabela: nfe_serie (Linhas aprox: 1)"""
    id: int
    empresa_id: int
    serie: str
    numeracao_inicial: int
    padrao: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ambiente: Optional[int] = None
    tipo_serie: Optional[str] = None
    oauth_client_id: Optional[str] = None

@dataclass
class NfeSituacaoIpi:
    """Tabela: nfe_situacao_ipi (Linhas aprox: 14)"""
    id: int
    codigo: str
    nome: str
    destacar_ipi: int
    tipo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeTipoEmissao:
    """Tabela: nfe_tipo_emissao (Linhas aprox: 0)"""
    id: int
    codigo: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeTipoItem:
    """Tabela: nfe_tipo_item (Linhas aprox: 12)"""
    id: int
    nome: str
    tipo: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfeTipoServico:
    """Tabela: nfe_tipo_servico (Linhas aprox: None)"""
    id: int
    codigo: int
    nome: str
    aliquota: Optional[Decimal] = None
    item_lista_servico: Optional[Decimal] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    c_cidade: str
    descricao: str

@dataclass
class NfseAliquotaPadrao:
    """Tabela: nfse_aliquota_padrao (Linhas aprox: 1)"""
    id: int
    iss: Decimal
    pis: Decimal
    cssl: Decimal
    cofins: Decimal
    inss: Decimal
    ir: Decimal
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfseCodigoServicoItem:
    """Tabela: nfse_codigo_servico_item (Linhas aprox: 531)"""
    id: int
    codigo: str
    codigo_numerico: str
    descricao: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    ambiente_nacional: int

@dataclass
class NfseExigibilidadeIss:
    """Tabela: nfse_exigibilidade_iss (Linhas aprox: 7)"""
    id: int
    descricao: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfseNatureza:
    """Tabela: nfse_natureza (Linhas aprox: 6)"""
    id: int
    descricao: str
    cfop: str
    operacao: str
    percentual_icms: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfseRegimeEspecialTributacao:
    """Tabela: nfse_regime_especial_tributacao (Linhas aprox: 7)"""
    id: int
    descricao: str
    tipo: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NfseSerie:
    """Tabela: nfse_serie (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    serie: int
    numeracao_inicial: int
    padrao: int
    ambiente: int
    tipo_serie: str
    oauth_client_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronica:
    """Tabela: nota_fiscal_eletronica (Linhas aprox: 76)"""
    id: int
    empresa_id: int
    versao: Optional[str] = None
    chave_acesso: Optional[str] = None
    codigo_nota_fiscal: Optional[str] = None
    natureza: str
    indicador_forma_pagamento: Optional[int] = None
    modelo: Optional[str] = None
    serie: Optional[str] = None
    numero_nfe: int
    data_hora_emissao: Optional[datetime] = None
    data_hora_saida: Optional[datetime] = None
    tipo_operacao: Optional[int] = None
    identificador_local_destino: Optional[int] = None
    tipo_emissao: Optional[int] = None
    chave_dv: Optional[int] = None
    ambiente: Optional[int] = None
    xml: Optional[str] = None
    xml_recibo_emissao: Optional[str] = None
    xml_cancelamento: Optional[str] = None
    justificativa_cancelamento: Optional[str] = None
    recibo_situacao: Optional[str] = None
    lote_emissao: Optional[str] = None
    numero_recibo: Optional[str] = None
    numero_protocolo_autorizacao: Optional[str] = None
    data_hora_protocolo_autorizacao: Optional[datetime] = None
    inutilizado_em: Optional[datetime] = None
    rateavel: int
    finalidade: int
    indicador_finalidade: str
    indicador_presencial: Optional[str] = None
    indicador_intermediador: int
    codigo_natureza: Optional[int] = None
    data_hora_contingencia: Optional[datetime] = None
    justificativa_contingencia: Optional[str] = None
    cobranca_numero_fatura: Optional[str] = None
    cobranca_valor_original: Optional[Decimal] = None
    cobranca_valor_desconto: Optional[Decimal] = None
    cobranca_valor_liquido: Optional[Decimal] = None
    total_frete_valor: Decimal
    total_seguro_valor: Decimal
    total_valor_outras_despesas: Decimal
    total_desconto_percentual: Decimal
    total_desconto_valor: Decimal
    total_icms_base_calculo: Optional[Decimal] = None
    total_icms_valor: Optional[Decimal] = None
    total_icmsst_base_calculo: Optional[Decimal] = None
    total_icmsst_valor: Optional[Decimal] = None
    total_produto_valor: Optional[Decimal] = None
    total_ipi_valor: Optional[Decimal] = None
    total_pis_valor: Optional[Decimal] = None
    total_cofins_valor: Optional[Decimal] = None
    total_nota_valor: Optional[Decimal] = None
    total_tributos_valor: Optional[Decimal] = None
    total_icmsdesoneracao_valor: Optional[Decimal] = None
    total_icms_uf_destino_valor: Optional[Decimal] = None
    total_icms_uf_remetente_valor: Optional[Decimal] = None
    total_fcp_uf_destino_valor: Optional[Decimal] = None
    total_icms_fundo_combate_pobreza_valor: Optional[Decimal] = None
    total_icmsst_fundo_combate_pobreza_valor: Optional[Decimal] = None
    total_issqn_valor_servico: Optional[Decimal] = None
    total_issqn_valor_base_calculo: Optional[Decimal] = None
    total_issqn_valor_iss: Optional[Decimal] = None
    total_issqn_valor_pis: Optional[Decimal] = None
    total_issqn_valor_cofins: Optional[Decimal] = None
    total_issqn_valor_deducao: Optional[Decimal] = None
    total_issqn_valor_outro: Optional[Decimal] = None
    total_issqn_valor_desconto_incondicionado: Optional[Decimal] = None
    total_issqn_data_competencia: Optional[date] = None
    total_issqn_regime_tributario: Optional[str] = None
    total_issqn_valor_desconto_condicionado: Optional[Decimal] = None
    total_issqn_valor_iss_retencao: Optional[Decimal] = None
    informacoes_adicionais_complementares: Optional[str] = None
    informacoes_adicionais_fisco: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    digest_value: Optional[str] = None
    codigo_status: Optional[str] = None
    mensagem_erro: Optional[str] = None
    sat_equipamento_serie: Optional[str] = None
    sat_assinatura_qr_code: Optional[str] = None
    compra_id: Optional[int] = None
    duplicidade: int
    confirmacao_duplicidade: int
    chave_acesso_anterior_duplicidade: Optional[str] = None
    memoria_fiscal: int
    operacao_tipo: Optional[str] = None
    movimentar_estoque: int

@dataclass
class NotaFiscalEletronicaAutorizado:
    """Tabela: nota_fiscal_eletronica_autorizado (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    cpf_cnpj: str
    nome: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaCartaCorrecao:
    """Tabela: nota_fiscal_eletronica_carta_correcao (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    chave_acesso: Optional[str] = None
    tipo_ambiente: int
    sequencial: Optional[int] = None
    correcao: Optional[str] = None
    retorno_sefaz: Optional[str] = None
    data_hora_registro: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaCobranca:
    """Tabela: nota_fiscal_eletronica_cobranca (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    numero_duplicata: Optional[str] = None
    vencimento: Optional[date] = None
    valor_duplicata: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaDestinatario:
    """Tabela: nota_fiscal_eletronica_destinatario (Linhas aprox: 48)"""
    id: int
    nota_fiscal_eletronica_id: int
    destinatario_cpf_cnpj: str
    destinatario_id_estrangeiro: Optional[str] = None
    destinatario_nome: str
    destinatario_endereco: Optional[str] = None
    destinatario_numero: Optional[str] = None
    destinatario_complemento: Optional[str] = None
    destinatario_bairro: Optional[str] = None
    destinatario_codigo_cidade: Optional[str] = None
    destinatario_nome_cidade: Optional[str] = None
    destinatario_uf: Optional[str] = None
    destinatario_cep: Optional[str] = None
    destinatario_codigo_pais: Optional[str] = None
    destinatario_nome_pais: Optional[str] = None
    destinatario_telefone: Optional[str] = None
    destinatario_indicador_ie: Optional[str] = None
    destinatario_ie: Optional[str] = None
    destinatario_inscricao_suframa: Optional[str] = None
    destinatario_inscricao_municipal: Optional[str] = None
    destinatario_email: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    destinatario_id: Optional[int] = None
    destinatario_tipo: Optional[str] = None

@dataclass
class NotaFiscalEletronicaEmitente:
    """Tabela: nota_fiscal_eletronica_emitente (Linhas aprox: 48)"""
    id: int
    nota_fiscal_eletronica_id: int
    emitente_cnpj: str
    emitente_nome: str
    emitente_fantasia: Optional[str] = None
    emitente_endereco: Optional[str] = None
    emitente_numero: Optional[str] = None
    emitente_complemento: Optional[str] = None
    emitente_bairro: Optional[str] = None
    emitente_codigo_cidade: Optional[str] = None
    emitente_nome_cidade: Optional[str] = None
    emitente_uf: Optional[str] = None
    emitente_codigo_uf: Optional[int] = None
    emitente_cep: Optional[str] = None
    emitente_codigo_pais: Optional[str] = None
    emitente_nome_pais: Optional[str] = None
    emitente_telefone: Optional[str] = None
    emitente_inscricao_estadual: Optional[str] = None
    emitente_inscricao_estadual_st: Optional[str] = None
    emitente_inscricao_municipal: Optional[str] = None
    emitente_cnae: Optional[str] = None
    emitente_codigo_regime_tributario: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaEspecificoArmamento:
    """Tabela: nota_fiscal_eletronica_especifico_armamento (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_item_id: int
    especifico_tipo_arma: str
    especifico_numero_serie_arma: str
    especifico_numero_serie_cano: str
    especifico_descricao: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaEspecificoCombustivel:
    """Tabela: nota_fiscal_eletronica_especifico_combustivel (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_item_id: int
    especifico_codigo_produto: str
    especifico_descricao_produto: str
    especifico_percentual_glp: Optional[Decimal] = None
    especifico_percentual_gas_natural_importado: Optional[Decimal] = None
    especifico_valor_partida: Optional[Decimal] = None
    especifico_percentual_gas_natural: Optional[Decimal] = None
    especifico_codif: Optional[str] = None
    especifico_quantidade_combustivel: Optional[Decimal] = None
    especifico_uf_consumo: str
    especifico_quantidade_bc_cide: Optional[Decimal] = None
    especifico_aliquota_cide: Optional[Decimal] = None
    especifico_valor_cide: Optional[Decimal] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    percentual_bio: Decimal
    aliquota_ad_rem: Decimal
    aliquota_ad_rem_icms_reten: Decimal
    aliquota_ad_rem_icms_ret: Decimal
    percentual_reducao_ad_rem: Decimal
    motivo_reducao_ad_rem: Optional[int] = None
    quantidade_base_calculo_tributada: Decimal
    quantidade_retida_base_calculo_tributada: Decimal

@dataclass
class NotaFiscalEletronicaEspecificoMedicamento:
    """Tabela: nota_fiscal_eletronica_especifico_medicamento (Linhas aprox: 0)"""
    id: int
    especifico_codigo_anvisa: str
    especifico_motivo_isencao: Optional[str] = None
    nota_fiscal_eletronica_item_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaEspecificoMedicamentoRastro:
    """Tabela: nota_fiscal_eletronica_especifico_medicamento_rastro (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_item_id: int
    especifico_numero_lote: str
    especifico_quantidade_lote: Decimal
    especifico_data_fabricacao: date
    especifico_data_validade: date
    especifico_preco_maximo: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaEspecificoPapel:
    """Tabela: nota_fiscal_eletronica_especifico_papel (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_item_id: int
    especifico_numero_recopi: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaEspecificoVeiculo:
    """Tabela: nota_fiscal_eletronica_especifico_veiculo (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_item_id: int
    especifico_tipo_operacao: str
    especifico_chassi: str
    especifico_cor_codigo: str
    especifico_cor_descricao: str
    especifico_potencia_motor: str
    especifico_cilindrada: str
    especifico_peso_liquido: str
    especifico_peso_bruto: str
    especifico_numero_serie: str
    especifico_tipo_combustivel: str
    especifico_numero_motor: str
    especifico_capacidade_maxima_tracao: str
    especifico_distancia_eixo: str
    especifico_ano_modelo: int
    especifico_ano_fabricacao: int
    especifico_tipo_pintura: str
    especifico_tipo_veiculo: str
    especifico_especie_veiculo: str
    especifico_condicao_vin: str
    especifico_condicao_veiculo: str
    especifico_codigo_marca_modelo: str
    especifico_codigo_cor_denatran: str
    especifico_lotacao_capacidade: str
    especifico_tipo_restricao: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaExportacao:
    """Tabela: nota_fiscal_eletronica_exportacao (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    uf_saida_pais: str
    localizacao: str
    localizacao_despacho: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaFormaPagamento:
    """Tabela: nota_fiscal_eletronica_forma_pagamento (Linhas aprox: 48)"""
    id: int
    nota_fiscal_eletronica_id: int
    pagamento_tipo: str
    pagamento_valor: Optional[Decimal] = None
    pagamento_tipo_integracao: Optional[str] = None
    pagamento_cnpj_credenciadora: Optional[str] = None
    pagamento_bandeira_operadora: Optional[str] = None
    pagamento_numero_autorizacao: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    pagamento_valor_troco: Optional[Decimal] = None
    pagamento_descricao: Optional[str] = None

@dataclass
class NotaFiscalEletronicaInutilizacao:
    """Tabela: nota_fiscal_eletronica_inutilizacao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    modelo: str
    numero_inicial: Optional[int] = None
    numero_final: Optional[int] = None
    serie: Optional[int] = None
    justificativa: Optional[str] = None
    tipo_ambiente: int
    retorno_sefaz: Optional[str] = None
    data_hora_registro: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaItem:
    """Tabela: nota_fiscal_eletronica_item (Linhas aprox: 196)"""
    id: int
    nota_fiscal_eletronica_id: int
    produto_empresa_grade_id: int
    produto_id: int
    servico: int
    tipo_especifico: Optional[str] = None
    codigo_produto: Optional[str] = None
    codigo_ean: Optional[str] = None
    produto_nome: str
    ncm: Optional[str] = None
    cest: Optional[str] = None
    cfop: Optional[str] = None
    unidade_comercial: Optional[str] = None
    pedido_compra_numero_compra: Optional[str] = None
    pedido_compra_numero_pedido: Optional[str] = None
    quantidade_comercial: Optional[Decimal] = None
    valor_unitario_comercial: Optional[Decimal] = None
    valor_total_produto: Optional[Decimal] = None
    unidade_tributavel: Optional[str] = None
    quantidade_tributavel: Optional[Decimal] = None
    valor_unitario_tributavel: Optional[Decimal] = None
    valor_total_frete: Optional[Decimal] = None
    valor_total_seguro: Optional[Decimal] = None
    valor_total_desconto: Optional[Decimal] = None
    valor_total_outras_despesas: Optional[Decimal] = None
    indicador_total: int
    origem: str
    cst_csosn: Optional[str] = None
    icms_modalidade_base_calculo: Optional[str] = None
    icms_base_calculo: Optional[Decimal] = None
    icms_aliquota_credito_simples_nacional: Optional[Decimal] = None
    icms_valor_credito_simples_nacional: Optional[Decimal] = None
    rateavel: int
    icms_percentual_reducao_base: Optional[Decimal] = None
    icms_aliquota: Optional[Decimal] = None
    icms_aliquota_automatica: int
    icms_valor: Optional[Decimal] = None
    icmsst_modalidade_base_calculo: Optional[str] = None
    icmsst_base_calculo: Optional[Decimal] = None
    icmsst_percentual_reducao_base: Optional[Decimal] = None
    icmsst_mva: Optional[Decimal] = None
    icmsst_aliquota: Optional[Decimal] = None
    icmsst_valor: Optional[Decimal] = None
    icmsst_retido_base_calculo: Optional[Decimal] = None
    icmsst_retido_valor: Optional[Decimal] = None
    icms_aliquota_suportada_consumidor: Decimal
    icms_desoneracao_motivo: Optional[str] = None
    icms_desoneracao_valor: Optional[Decimal] = None
    icms_operacao_valor: Optional[Decimal] = None
    icms_diferimento_percentual: Optional[Decimal] = None
    icms_diferimento_valor: Optional[Decimal] = None
    ipi_cst: Optional[str] = None
    ipi_base_calculo: Optional[Decimal] = None
    ipi_aliquota: Optional[Decimal] = None
    ipi_devolucao: Optional[Decimal] = None
    ipi_valor: Optional[Decimal] = None
    ipi_enquadramento: Optional[str] = None
    tributos_federais: Optional[Decimal] = None
    tributos_estaduais: Optional[Decimal] = None
    tributos_municipais: Optional[Decimal] = None
    total_tributos: Optional[Decimal] = None
    especifico: Optional[str] = None
    pis_cst: Optional[str] = None
    pis_base_calculo: Optional[Decimal] = None
    pis_aliquota: Optional[Decimal] = None
    pis_valor: Optional[Decimal] = None
    cofins_cst: Optional[str] = None
    cofins_aliquota: Optional[Decimal] = None
    cofins_valor: Optional[Decimal] = None
    icmsdifal_base_calculo_uf_destino: Optional[Decimal] = None
    icmsdifal_base_calculo_fcp_destino: Optional[Decimal] = None
    icmsdifal_percentual_fcp_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_icms_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_icms_interestadual: Optional[Decimal] = None
    icmsdifal_percentual_provisorio_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_fcp_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_icms_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_icms_uf_remetente: Optional[Decimal] = None
    natureza: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    informacoes_adicionais_produto: Optional[str] = None
    codigo_beneficio_fiscal: Optional[str] = None
    icmsst_base_calculo_destino: Optional[Decimal] = None
    icmsst_valor_destino: Optional[Decimal] = None
    peso: Optional[Decimal] = None
    icms_st_modalidade_base: Optional[str] = None
    icms_st_mva: Optional[Decimal] = None
    icms_st_aliquota: Optional[Decimal] = None
    icms_st_reducao: Optional[Decimal] = None
    icms_valor_pauta: Optional[Decimal] = None
    icmsst_valor_base_calculo_fundo_combate_pobreza: Optional[Decimal] = None
    icmsst_percentual_fundo_combate_pobreza: Optional[Decimal] = None
    icmsst_valor_fundo_combate_pobreza: Optional[Decimal] = None
    imposto_manual: int
    zerar_icms: int
    ibs_cbs_cst: str
    ibs_cbs_cclass_trib: str
    ibs_aliquota: Decimal
    cbs_aliquota: Decimal
    ibs_percentual_red: Decimal
    cbs_percentual_red: Decimal
    ibs_cbs_cst_id: Optional[int] = None
    agro_numero_receituario: Optional[str] = None
    agro_cpf_responsavel: Optional[str] = None
    icms_desoneracao_codigo: Optional[str] = None
    icms_original_normal_aliquota: Decimal
    icms_original_aliquota: Decimal
    somar_ipi_icmsst_base: int

@dataclass
class NotaFiscalEletronicaItemCombustivelOrigem:
    """Tabela: nota_fiscal_eletronica_item_combustivel_origem (Linhas aprox: 0)"""
    id: int
    indicador_importacao: int
    codigo_uf_origem: str
    percentual_originario_uf: Decimal
    nota_fiscal_eletronica_item_id: int
    nota_fiscal_eletronica_especifico_combustivel_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaItemIssqn:
    """Tabela: nota_fiscal_eletronica_item_issqn (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_item_id: int
    issqn_valor_base_calculo: Decimal
    issqn_valor_aliquota: Decimal
    issqn_valor_issqn: Decimal
    issqn_codigo_municipio_fato_gerador: str
    issqn_item_lista_servico: str
    issqn_valor_deducao: Optional[Decimal] = None
    issqn_valor_outro: Optional[Decimal] = None
    issqn_valor_desconto_incondicionado: Optional[Decimal] = None
    issqn_valor_desconto_condicionado: Optional[Decimal] = None
    issqn_valor_retencao_iss: Optional[Decimal] = None
    issqn_indicador_exigibilidade_iss: str
    issqn_codigo_servico: Optional[str] = None
    issqn_codigo_municipio: Optional[str] = None
    issqn_codigo_pais: Optional[str] = None
    issqn_numero_processo: Optional[str] = None
    issqn_indicador_incentivo_fiscal: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaLocalEntrega:
    """Tabela: nota_fiscal_eletronica_local_entrega (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    local_entrega_cpf_cnpj: Optional[str] = None
    local_entrega_endereco: Optional[str] = None
    local_entrega_numero: Optional[str] = None
    local_entrega_complemento: Optional[str] = None
    local_entrega_bairro: Optional[str] = None
    local_entrega_codigo_cidade: Optional[str] = None
    local_entrega_nome_cidade: Optional[str] = None
    local_entrega_uf: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    local_entrega_nome: Optional[str] = None
    local_entrega_cep: Optional[str] = None
    local_entrega_pais: Optional[str] = None
    local_entrega_codigo_pais: Optional[str] = None
    local_entrega_telefone: Optional[str] = None
    local_entrega_email: Optional[str] = None
    local_entrega_inscricao_estadual: Optional[str] = None
    local_entrega_motivo_isencao: Optional[str] = None

@dataclass
class NotaFiscalEletronicaLocalRetirada:
    """Tabela: nota_fiscal_eletronica_local_retirada (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    local_retirada_cpf_cnpj: Optional[str] = None
    local_retirada_endereco: Optional[str] = None
    local_retirada_numero: Optional[str] = None
    local_retirada_complemento: Optional[str] = None
    local_retirada_bairro: Optional[str] = None
    local_retirada_codigo_cidade: Optional[str] = None
    local_retirada_nome_cidade: Optional[str] = None
    local_retirada_cidade_uf: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    local_retirada_nome: Optional[str] = None
    local_retirada_cep: Optional[str] = None
    local_retirada_pais: Optional[str] = None
    local_retirada_codigo_pais: Optional[str] = None
    local_retirada_telefone: Optional[str] = None
    local_retirada_email: Optional[str] = None
    local_retirada_inscricao_estadual: Optional[str] = None

@dataclass
class NotaFiscalEletronicaReferenciada:
    """Tabela: nota_fiscal_eletronica_referenciada (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    numero: str
    chave_acesso: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaResponsavelTecnico:
    """Tabela: nota_fiscal_eletronica_responsavel_tecnico (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    cnpj: str
    contato: str
    email: str
    fone: str
    id_csrt: Optional[str] = None
    hash_csrt: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalEletronicaTransportador:
    """Tabela: nota_fiscal_eletronica_transportador (Linhas aprox: 48)"""
    id: int
    nota_fiscal_eletronica_id: int
    transportador_nome: Optional[str] = None
    transportador_cpf_cnpj: Optional[str] = None
    transportador_ie: Optional[str] = None
    transportador_uf: Optional[str] = None
    transportador_endereco: Optional[str] = None
    transportador_nome_cidade: Optional[str] = None
    transportador_modalidade_frete: int
    transportador_placa: Optional[str] = None
    transportador_placa_uf: Optional[str] = None
    transportador_rntc: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    volume_manual: int

@dataclass
class NotaFiscalEletronicaVolume:
    """Tabela: nota_fiscal_eletronica_volume (Linhas aprox: 0)"""
    id: int
    nota_fiscal_eletronica_id: int
    volumes_quantidade: Optional[int] = None
    volumes_especie: Optional[str] = None
    volumes_marca: Optional[str] = None
    volumes_numero: Optional[str] = None
    volumes_peso_bruto: Optional[Decimal] = None
    volumes_peso_liquido: Optional[Decimal] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotaFiscalServicoEletronica:
    """Tabela: nota_fiscal_servico_eletronica (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    serie: str
    ambiente: int
    numero_rps: Optional[str] = None
    status_rps: int
    data_emissao: Optional[datetime] = None
    data_competencia: Optional[date] = None
    total_valor_servico: Optional[Decimal] = None
    total_valor_deducoes: Optional[Decimal] = None
    total_valor_outras_retencoes: Optional[Decimal] = None
    total_valor_desconto_incondicionado: Optional[Decimal] = None
    total_valor_desconto_condicionado: Optional[Decimal] = None
    iss_retido: int
    simples_nacional: int
    aliquota_iss: Optional[Decimal] = None
    aliquota_pis: Optional[Decimal] = None
    aliquota_cofins: Optional[Decimal] = None
    aliquota_ir: Optional[Decimal] = None
    aliquota_inss: Optional[Decimal] = None
    aliquota_csll: Optional[Decimal] = None
    nfse_exigibilidade_iss_id: Optional[int] = None
    nfse_regime_especial_tributacao_id: Optional[int] = None
    total_base_calculo: Optional[Decimal] = None
    valor_liquido_nfse: Optional[Decimal] = None
    total_iss: Optional[Decimal] = None
    total_iss_retido: Optional[Decimal] = None
    total_pis: Optional[Decimal] = None
    total_cofins: Optional[Decimal] = None
    total_ir: Optional[Decimal] = None
    total_inss: Optional[Decimal] = None
    total_csll: Optional[Decimal] = None
    response_status: Optional[str] = None
    response_status_descricao: Optional[str] = None
    response_validacao: Optional[str] = None
    response_xml: Optional[str] = None
    response_xml_link: Optional[str] = None
    response_pdf_link: Optional[str] = None
    response_nfse_id: Optional[str] = None
    api_requisicao_data_hora: Optional[datetime] = None
    api_requisicao_contador: int
    nfse_json: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    com_tomador: int

@dataclass
class NotaFiscalServicoEletronicaItem:
    """Tabela: nota_fiscal_servico_eletronica_item (Linhas aprox: 0)"""
    id: int
    nfse_id: int
    produto_id: Optional[int] = None
    produto_empresa_grade_id: Optional[int] = None
    servico_codigo_cidade: Optional[str] = None
    servico_nome_cidade: Optional[str] = None
    servico_uf: Optional[str] = None
    servico_codigo_pais: Optional[str] = None
    servico_nome_pais: Optional[str] = None
    nfse_codigo_servico_item_id: Optional[int] = None
    codigo_numerico_servico_item: Optional[str] = None
    codigo_tributacao_municipal: Optional[str] = None
    descricao_servico: Optional[str] = None
    base_calculo: Optional[Decimal] = None
    valor_servico: Optional[Decimal] = None
    valor_deducoes: Optional[Decimal] = None
    valor_outras_retencoes: Optional[Decimal] = None
    valor_desconto_incondicionado: Optional[Decimal] = None
    valor_desconto_condicionado: Optional[Decimal] = None
    aliquota_iss: Optional[Decimal] = None
    aliquota_pis: Optional[Decimal] = None
    aliquota_cofins: Optional[Decimal] = None
    aliquota_ir: Optional[Decimal] = None
    aliquota_inss: Optional[Decimal] = None
    aliquota_csll: Optional[Decimal] = None
    valor_iss: Optional[Decimal] = None
    valor_iss_retido: Optional[Decimal] = None
    valor_pis: Optional[Decimal] = None
    valor_cofins: Optional[Decimal] = None
    valor_ir: Optional[Decimal] = None
    valor_inss: Optional[Decimal] = None
    valor_csll: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    tributos_federais: Optional[Decimal] = None
    tributos_estaduais: Optional[Decimal] = None
    tributos_municipais: Optional[Decimal] = None
    descricao_tributos: Optional[str] = None
    nbs_cnae: Optional[str] = None

@dataclass
class NotaFiscalServicoEletronicaTomador:
    """Tabela: nota_fiscal_servico_eletronica_tomador (Linhas aprox: 0)"""
    id: int
    nfse_id: int
    cliente_id: Optional[int] = None
    nome: Optional[str] = None
    cpf_cnpj: Optional[str] = None
    inscricao_municipal: Optional[str] = None
    cep: Optional[str] = None
    codigo_cidade: Optional[str] = None
    nome_cidade: Optional[str] = None
    uf: Optional[str] = None
    codigo_pais: Optional[str] = None
    nome_pais: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Notificacao:
    """Tabela: notificacao (Linhas aprox: 0)"""
    id: int
    tipo: str
    mensagem: str
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotificacaoEnvio:
    """Tabela: notificacao_envio (Linhas aprox: 0)"""
    id: int
    notificacao_template_id: Optional[int] = None
    data_hora_geracao: Optional[datetime] = None
    data_hora_envio: Optional[datetime] = None
    origem_pessoa_id: Optional[int] = None
    origem_registro_id: Optional[int] = None
    destino_fone: Optional[str] = None
    destino_email: Optional[str] = None
    retorno: Optional[str] = None
    mensagem: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    mensagem_id: Optional[str] = None
    error: Optional[str] = None
    data_erro: Optional[datetime] = None

@dataclass
class NotificacaoMensagem:
    """Tabela: notificacao_mensagem (Linhas aprox: 0)"""
    id: int
    assunto: str
    canal: str
    titulo: str
    tipo: Optional[str] = None
    mensagem: str
    enviar_link_pesquisa: int
    permitir_excluir: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotificacaoMensagemArquivo:
    """Tabela: notificacao_mensagem_arquivo (Linhas aprox: 0)"""
    id: int
    parent_id: int
    description: Optional[str] = None
    filename: str
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    extension: str
    link: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NotificacaoPosVenda:
    """Tabela: notificacao_pos_venda (Linhas aprox: 0)"""
    id: int
    produto_empresa_grade_id: int
    grupo_id: Optional[int] = None
    mensagem_id: Optional[int] = None
    dias: int
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    whatsapp: int
    email: int
    todos_produtos: int

@dataclass
class NotificacaoTemplate:
    """Tabela: notificacao_template (Linhas aprox: 40)"""
    id: int
    tipo_notificacao: Optional[str] = None
    tipo_pessoa: Optional[str] = None
    tipo_envio: Optional[str] = None
    origem_registro_tabela: Optional[str] = None
    mensagem_titulo: Optional[str] = None
    mensagem_template: Optional[str] = None
    envio_automatico: Optional[int] = None
    possui_anexo: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    titulo: Optional[str] = None

@dataclass
class NotificacaoUsuario:
    """Tabela: notificacao_usuario (Linhas aprox: 0)"""
    id: int
    notificacao_id: int
    usuario_id: int
    lido_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NuvemNfe:
    """Tabela: nuvem_nfe (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    chave_nfe: str
    nfe_id: Optional[int] = None
    numero_protocolo: Optional[str] = None
    numero_nfe: Optional[str] = None
    serie: Optional[str] = None
    cnpj_emitente: Optional[str] = None
    x_nome_emitente: Optional[str] = None
    inscricao_estadual: Optional[str] = None
    data_hora_emissao: Optional[datetime] = None
    valor_nota_fiscal: Optional[Decimal] = None
    tipo_amb_consulta: Optional[int] = None
    cnpj_consulta: Optional[str] = None
    data_consulta: Optional[datetime] = None
    tipo_destino: Optional[str] = None
    resumido_nsu: Optional[str] = None
    resumido_schema: Optional[str] = None
    resumido_xml: Optional[str] = None
    processamento_nsu: Optional[str] = None
    processamento_schema: Optional[str] = None
    processamento_xml: Optional[str] = None
    status_nfe: Optional[str] = None
    codigo_manifestacao: Optional[str] = None
    codigo_situacao_nfe: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class NuvemNfeEmissao:
    """Tabela: nuvem_nfe_emissao (Linhas aprox: 1)"""
    id: int
    empresa_id: int
    ambiente_nuvem: int
    ambiente_nfe: int
    codigo_status_emissao_nfe: int
    ambiente_mdfe: int
    codigo_status_emissao_mdfe: int
    ambiente_nfce: int
    codigo_status_emissao_nfce: int
    regime_tributario: int
    aliquota_credito: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    nfce_solicitar_cpf_cnpj_valor: Optional[Decimal] = None
    nome_nota_fiscal: str
    nome_destinatario: str
    icms_desoneracao: int
    contingencia_nfce: int
    ultima_sincronizacao_contingencia: Optional[datetime] = None
    contingencia_nfe: int
    ambiente_nfse: int
    regime_especial_nfse: Optional[str] = None
    ultimo_rps_nfse: Optional[str] = None
    exigibilidade_iss: int
    competencia_nota_automatica_nfse: str
    exibir_pagamento: int
    memoria_fiscal: int
    exigibilidade_casas_decimais: int
    cfop_id: Optional[int] = None
    nfe_pdv_emissao: int
    deduzir_icms_base_pis_cofins: int

@dataclass
class NuvemNfeEmpresa:
    """Tabela: nuvem_nfe_empresa (Linhas aprox: 0)"""
    id: int
    maximo_nsu: Optional[int] = None
    ultimo_nsu: Optional[int] = None
    ultimo_tipo_amb: Optional[int] = None
    ultima_data_consulta: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    empresa_id: int

@dataclass
class NuvemNfeEventos:
    """Tabela: nuvem_nfe_eventos (Linhas aprox: 0)"""
    id: int
    evento_id: Optional[int] = None
    chave_nfe: Optional[str] = None
    numero_protocolo: Optional[str] = None
    tipo_evento: Optional[str] = None
    x_evento: Optional[str] = None
    numero_sequencial_evento: Optional[int] = None
    data_hora_registro_evento: Optional[datetime] = None
    tipo_amb_consulta: Optional[int] = None
    cnpj_consulta: Optional[str] = None
    data_consulta: Optional[datetime] = None
    resumido_nsu: Optional[str] = None
    resumido_schema: Optional[str] = None
    resumido_xml: Optional[str] = None
    processamento_nsu: Optional[str] = None
    processamento_schema: Optional[str] = None
    processamento_xml: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class OauthAccessTokens:
    """Tabela: oauth_access_tokens (Linhas aprox: 2)"""
    access_token: str
    refresh_token: Optional[str] = None
    client_id: str
    user_id: Optional[str] = None
    scope: Optional[str] = None
    expires: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class OauthAuthorizationCodes:
    """Tabela: oauth_authorization_codes (Linhas aprox: 0)"""
    authorization_code: str
    client_id: str
    user_id: Optional[str] = None
    redirect_uri: Optional[str] = None
    expires: datetime
    scope: Optional[str] = None

@dataclass
class OauthClients:
    """Tabela: oauth_clients (Linhas aprox: 5)"""
    client_id: str
    client_secret: str
    name: str
    device_id: str
    redirect_uri: Optional[str] = None
    grant_types: Optional[str] = None
    scope: Optional[str] = None
    user_id: Optional[str] = None
    empresa_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    visivel: Optional[int] = None
    previous_device_id: Optional[str] = None
    tipo_dispositivo: Optional[str] = None
    configuracao_dispositivo: Optional[str] = None

@dataclass
class OauthJwt:
    """Tabela: oauth_jwt (Linhas aprox: 0)"""
    client_id: str
    subject: Optional[str] = None
    public_key: Optional[str] = None

@dataclass
class OauthRefreshTokens:
    """Tabela: oauth_refresh_tokens (Linhas aprox: 0)"""
    refresh_token: str
    client_id: str
    user_id: Optional[str] = None
    expires: datetime
    scope: Optional[str] = None

@dataclass
class OauthScopes:
    """Tabela: oauth_scopes (Linhas aprox: 0)"""
    scope: Optional[str] = None
    is_default: Optional[int] = None

@dataclass
class OauthUsers:
    """Tabela: oauth_users (Linhas aprox: 2)"""
    username: str
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

@dataclass
class Observacao:
    """Tabela: observacao (Linhas aprox: 0)"""
    id: int
    codigo: int
    nome: str
    tipo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Orcamento:
    """Tabela: orcamento (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    venda_id: Optional[int] = None
    cliente_id: int
    cliente_nome: str
    cpf_cnpj: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    condicao_pagamento: Optional[str] = None
    garantia: Optional[str] = None
    validade: Optional[str] = None
    status: Optional[str] = None
    funcionario_id: int
    observacao: Optional[str] = None
    desconto_valor: Decimal
    desconto_percentual: Optional[Decimal] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    cep: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[str] = None
    cidade_id: Optional[int] = None
    bairro: Optional[str] = None
    previsao_entrega: Optional[str] = None
    cancelada: int
    servico_descricao: Optional[str] = None
    complemento: Optional[str] = None
    responsavel: Optional[str] = None
    tipo_lancamento: Optional[str] = None
    prazo_entrega: Optional[str] = None
    proposta_objetivo: Optional[str] = None
    contrato_vigencia: Optional[str] = None
    contrato_data_inicio: Optional[date] = None
    contrato_data_termino: Optional[date] = None
    contrato_forma_pagamento_id: Optional[int] = None
    contrato_conta_id: Optional[int] = None
    contrato_dia_vencimento: Optional[int] = None
    contrato_cobranca_automatica: Optional[int] = None
    contrato_emissao_nota_automatica: Optional[int] = None
    data_validade: Optional[date] = None
    contrato_data_primeiro_vencimento: Optional[str] = None
    tipo_preco_id: Optional[int] = None
    contrato_cartao_id: Optional[int] = None
    tipo_debito_id: Optional[int] = None
    frete: Optional[str] = None

@dataclass
class OrcamentoAutopecas:
    """Tabela: orcamento_autopecas (Linhas aprox: 0)"""
    id: int
    orcamento_id: int
    cliente_veiculo_id: Optional[int] = None
    quilometragem: Optional[int] = None
    funcionario_id: Optional[int] = None
    solicitacao_cliente: Optional[str] = None
    observacoes_tecnicas: Optional[str] = None
    status: Optional[str] = None
    ordem: Optional[int] = None
    ordem_servico: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    combustivel: Optional[str] = None
    box_prisma_id: Optional[int] = None

@dataclass
class OrcamentoItem:
    """Tabela: orcamento_item (Linhas aprox: 0)"""
    id: int
    orcamento_id: int
    produto_id: int
    produto_empresa_grade_id: int
    descricao_item: Optional[str] = None
    quantidade: Decimal
    preco: Decimal
    preco_compra: Decimal
    preco_caixa: Decimal
    quantidade_caixa: Decimal
    desconto_valor_item: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    acrescimo_valor_item: Decimal
    percentual_desconto: Optional[Decimal] = None
    percentual_acrescimo: Optional[Decimal] = None
    desabilita_rateio: int
    essencial: int

@dataclass
class OrcamentoItemProfissional:
    """Tabela: orcamento_item_profissional (Linhas aprox: 0)"""
    id: int
    orcamento_item_id: int
    funcionario_id: Optional[int] = None
    rateio: Decimal
    comissao: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class OrdemFornecimento:
    """Tabela: ordem_fornecimento (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    fornecedor_id: Optional[int] = None
    fornecedor_nome: Optional[str] = None
    telefone: Optional[str] = None
    tipo_frete: Optional[str] = None
    data_previsao_chegada: Optional[datetime] = None
    data_envio_email: Optional[datetime] = None
    pedido_fornecedor: Optional[str] = None
    pagamento: Optional[str] = None
    observacao: Optional[str] = None
    periodo_vendas: Optional[str] = None
    data_periodo_de: Optional[datetime] = None
    data_periodo_ate: Optional[datetime] = None
    prazo_medio: int
    compra_para: int
    estoque_seguranca: int
    grupos_lista: str
    fabricantes_lista: str
    fornecedores_lista: str
    produtos_sem_movimentacao: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    recebida: int
    data_hora_recebimento: Optional[datetime] = None
    funcionario_recebimento_id: Optional[int] = None

@dataclass
class OrdemFornecimentoItem:
    """Tabela: ordem_fornecimento_item (Linhas aprox: 0)"""
    id: int
    ordem_fornecimento_id: Optional[int] = None
    produto_id: int
    produto_empresa_grade_id: int
    quantidade: Decimal
    preco_compra: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class OrigemVenda:
    """Tabela: origem_venda (Linhas aprox: None)"""
    id: int
    nome: str
    descricao: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PasswordResets:
    """Tabela: password_resets (Linhas aprox: 0)"""
    email: str
    token: str
    created_at: datetime

@dataclass
class PermissionRole:
    """Tabela: permission_role (Linhas aprox: 705)"""
    id: int
    permission_id: int
    role_id: int

@dataclass
class Permissions:
    """Tabela: permissions (Linhas aprox: 503)"""
    id: int
    permission_title: str
    permission_slug: str
    permission_description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    permission_module: str
    integrar_api: int

@dataclass
class PetshopAlbumFotoClinica:
    """Tabela: petshop_album_foto_clinica (Linhas aprox: 0)"""
    id: int
    nome: str
    animal_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopAnamnese:
    """Tabela: petshop_anamnese (Linhas aprox: 0)"""
    id: int
    animal_id: Optional[int] = None
    tipo: Optional[str] = None
    retorno: Optional[int] = None
    data_atendimento: Optional[datetime] = None
    motivo: Optional[str] = None
    exame_fisico: Optional[str] = None
    diagnostico: Optional[str] = None
    tratamento: Optional[str] = None
    proximos_passos: Optional[str] = None
    observacoes_internas: Optional[str] = None
    created_at: Optional[datetime] = None
    nome_usuario_funcionario: str
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopAnexoExame:
    """Tabela: petshop_anexo_exame (Linhas aprox: 0)"""
    id: int
    parent_id: int
    description: Optional[str] = None
    filename: str
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    extension: str
    link: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopAnimal:
    """Tabela: petshop_animal (Linhas aprox: 0)"""
    id: int
    cliente_id: int
    especie_id: int
    raca_id: Optional[int] = None
    pelagem_id: Optional[int] = None
    porte_id: Optional[int] = None
    nome: str
    sexo: str
    data_nascimento: Optional[date] = None
    anos: Optional[int] = None
    meses: Optional[int] = None
    peso: Decimal
    alergia: Optional[str] = None
    temperamento: Optional[str] = None
    numero_pedigree: Optional[str] = None
    chip: Optional[str] = None
    observacao: Optional[str] = None
    esterelizacao: str
    status: str
    imagem: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    desativar: int
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    consumo_racao: Optional[Decimal] = None

@dataclass
class PetshopAnimalImagem:
    """Tabela: petshop_animal_imagem (Linhas aprox: 0)"""
    id: int
    parent_id: int
    observacoes: Optional[str] = None
    description: Optional[str] = None
    filename: str
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    extension: str
    link: Optional[str] = None
    clinica: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    album_foto_clinica_id: Optional[int] = None

@dataclass
class PetshopAtendimento:
    """Tabela: petshop_atendimento (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    animal_id: int
    tipo_atendimento_id: Optional[int] = None
    duracao: int
    horario: Optional[str] = None
    turno: str
    funcionario_id: Optional[int] = None
    data_atendimento: date
    observacao: Optional[str] = None
    status: str
    created_at: Optional[datetime] = None
    nome_usuario_funcionario: str
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    avulso: int
    inicio_atendimento: Optional[datetime] = None
    inicio_espera: Optional[datetime] = None
    doenca_pre_existente: Optional[str] = None
    problema_auditivo: Optional[str] = None
    doenca_pele: Optional[str] = None

@dataclass
class PetshopAtendimentoAtestadosTermos:
    """Tabela: petshop_atendimento_atestados_termos (Linhas aprox: 0)"""
    id: int
    animal_id: Optional[int] = None
    texto: Optional[str] = None
    nome: str
    tipo: str
    data_atendimento: date
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    nome_usuario_funcionario: str

@dataclass
class PetshopAtendimentoChecklist:
    """Tabela: petshop_atendimento_checklist (Linhas aprox: 0)"""
    id: int
    atendimento_id: int
    tipo_condicao_animal_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopAtendimentoServico:
    """Tabela: petshop_atendimento_servico (Linhas aprox: 0)"""
    id: int
    tipo_atendimento_id: Optional[int] = None
    produto_empresa_grade_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopConfiguracao:
    """Tabela: petshop_configuracao (Linhas aprox: 1)"""
    id: int
    gerar_atendimento_servico: int
    tipo_registro_tempo: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopContratoPacote:
    """Tabela: petshop_contrato_pacote (Linhas aprox: 0)"""
    id: int
    parent_id: Optional[int] = None
    venda_id: Optional[int] = None
    animal_id: int
    data_validade: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopContratoPacoteItem:
    """Tabela: petshop_contrato_pacote_item (Linhas aprox: 0)"""
    id: int
    contrato_pacote_id: int
    pacote_item_id: int
    quantidade: Decimal
    quantidade_retirada: Decimal
    valor: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopEspecie:
    """Tabela: petshop_especie (Linhas aprox: 2)"""
    id: int
    nome: str
    created_at: Optional[datetime] = None
    desativar: int
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopExame:
    """Tabela: petshop_exame (Linhas aprox: 0)"""
    id: int
    nome: Optional[str] = None
    observacoes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    petshop_exame_cabecalho_id: int

@dataclass
class PetshopExameCabecalho:
    """Tabela: petshop_exame_cabecalho (Linhas aprox: 0)"""
    id: int
    animal_id: Optional[int] = None
    observacoes: Optional[str] = None
    created_at: Optional[datetime] = None
    nome_usuario_funcionario: str
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    data_solicitacao: Optional[date] = None

@dataclass
class PetshopLaboratorio:
    """Tabela: petshop_laboratorio (Linhas aprox: 0)"""
    id: int
    nome: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopLancamentoVacina:
    """Tabela: petshop_lancamento_vacina (Linhas aprox: 0)"""
    id: int
    animal_id: Optional[int] = None
    vacina_protocolo_id: Optional[int] = None
    data_inicio: Optional[date] = None
    data_interrupcao: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopModeloPrescricao:
    """Tabela: petshop_modelo_prescricao (Linhas aprox: 0)"""
    id: int
    nome: Optional[str] = None
    tipo: Optional[str] = None
    tipo_farmacia: Optional[str] = None
    created_at: Optional[datetime] = None
    desativar: int
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopMotivoSuspeita:
    """Tabela: petshop_motivo_suspeita (Linhas aprox: 0)"""
    id: int
    petshop_exame_cabecalho_id: int
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopOrdemServico:
    """Tabela: petshop_ordem_servico (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    venda_id: Optional[int] = None
    animal_id: int
    atendimento_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopOrdemServicoItem:
    """Tabela: petshop_ordem_servico_item (Linhas aprox: 0)"""
    id: int
    produto_id: int
    produto_empresa_grade_id: int
    ordem_servico_id: int
    funcionario_id: Optional[int] = None
    atendimento_id: Optional[int] = None
    horario: Optional[str] = None
    turno: str
    contrato_pacote_item_id: Optional[int] = None
    quantidade: Decimal
    preco: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopPacote:
    """Tabela: petshop_pacote (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    descricao: str
    controlar_validade: int
    validade_dias: Optional[int] = None
    ativa: int
    desconto_valor: Decimal
    desconto_percentual: Decimal
    acrescimo_valor: Decimal
    acrescimo_percentual: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopPacoteItem:
    """Tabela: petshop_pacote_item (Linhas aprox: 0)"""
    id: int
    pacote_id: int
    produto_id: int
    produto_empresa_grade_id: int
    preco: Decimal
    quantidade: Decimal
    preco_compra: Decimal
    desconto_valor_item: Decimal
    acrescimo_valor_item: Decimal
    percentual_desconto: Decimal
    percentual_acrescimo: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopPelagem:
    """Tabela: petshop_pelagem (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopPeso:
    """Tabela: petshop_peso (Linhas aprox: 0)"""
    id: int
    animal_id: Optional[int] = None
    peso: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    data_registro: date
    nome_usuario_funcionario: str
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    observacao: Optional[str] = None

@dataclass
class PetshopPorte:
    """Tabela: petshop_porte (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopPosologia:
    """Tabela: petshop_posologia (Linhas aprox: 0)"""
    id: int
    modelo_prescricao_id: Optional[int] = None
    referencia: Optional[str] = None
    dosagem: Optional[str] = None
    medida: Optional[str] = None
    duracao: Optional[str] = None
    frequencia: Optional[str] = None
    via: Optional[str] = None
    quantidade: Optional[str] = None
    descricao_final: Optional[str] = None
    quantidade_duracao: Optional[int] = None
    frequencia_duracao: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopRaca:
    """Tabela: petshop_raca (Linhas aprox: 0)"""
    id: int
    nome: str
    especie_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopReceita:
    """Tabela: petshop_receita (Linhas aprox: 0)"""
    id: int
    animal_id: Optional[int] = None
    tipo_prescricao: Optional[str] = None
    observacoes: Optional[str] = None
    created_at: Optional[datetime] = None
    nome_usuario_funcionario: str
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    data: date

@dataclass
class PetshopReceitaPrescricao:
    """Tabela: petshop_receita_prescricao (Linhas aprox: 0)"""
    id: int
    receita_id: int
    nome: str
    dosagem: Optional[str] = None
    medida: Optional[str] = None
    frequencia: Optional[str] = None
    frequencia_duracao: Optional[int] = None
    duracao: Optional[str] = None
    tipo_farmacia: Optional[str] = None
    via: Optional[str] = None
    quantidade: Optional[str] = None
    descricao_final: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    duracao_periodo: Optional[int] = None

@dataclass
class PetshopTipoAtendimento:
    """Tabela: petshop_tipo_atendimento (Linhas aprox: 3)"""
    id: int
    nome_atendimento: Optional[str] = None
    duracao: Optional[str] = None
    cor: Optional[str] = None
    created_at: Optional[datetime] = None
    desativar: int
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopTipoCondicaoAnimal:
    """Tabela: petshop_tipo_condicao_animal (Linhas aprox: 8)"""
    id: int
    descricao: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopVacina:
    """Tabela: petshop_vacina (Linhas aprox: 0)"""
    id: int
    descricao: Optional[str] = None
    grupo: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    desativar: int
    respeitar_intervalo: int

@dataclass
class PetshopVacinaLaboratorio:
    """Tabela: petshop_vacina_laboratorio (Linhas aprox: 0)"""
    id: int
    vacina_id: Optional[int] = None
    laboratorio_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopVacinaProtocolo:
    """Tabela: petshop_vacina_protocolo (Linhas aprox: 0)"""
    id: int
    vacina_id: Optional[int] = None
    especie_id: Optional[int] = None
    nome: Optional[str] = None
    aplicacao: Optional[str] = None
    intervalo: Optional[int] = None
    vem_apos: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PetshopVacinaProtocoloAplicacao:
    """Tabela: petshop_vacina_protocolo_aplicacao (Linhas aprox: 0)"""
    id: int
    lancamento_vacina_id: Optional[int] = None
    data_programacao: Optional[date] = None
    data_aplicacao: Optional[datetime] = None
    laboratorio_id: Optional[int] = None
    laboratorio_nome: Optional[str] = None
    lote: Optional[str] = None
    data_cancelamento: Optional[datetime] = None
    created_at: Optional[datetime] = None
    nome_usuario_funcionario: str
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PivotNfe:
    """Tabela: pivot_nfe (Linhas aprox: 0)"""
    id: int
    venda_id: Optional[int] = None
    nota_fiscal_eletronica_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Categoria:
    """Tabela: portal_360_categoria (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    grupo_id: int
    portal_360_category_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Cliente:
    """Tabela: portal_360_cliente (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    portal_360_customer_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    portal_360_contact_id: Optional[str] = None
    portal_360_address_id: Optional[str] = None

@dataclass
class Portal360ClienteContato:
    """Tabela: portal_360_cliente_contato (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    contato_id: Optional[int] = None
    portal_360_customer_id: Optional[str] = None
    portal_360_contact_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360ClienteEndereco:
    """Tabela: portal_360_cliente_endereco (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    endereco_id: Optional[int] = None
    portal_360_customer_id: Optional[str] = None
    portal_360_address_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360ClienteRecebivel:
    """Tabela: portal_360_cliente_recebivel (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    cliente_id: int
    parcela_id: int
    portal_360_customer_id: Optional[str] = None
    portal_360_receivable_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Config:
    """Tabela: portal_360_config (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    ultima_sincronizacao_cadastro: Optional[datetime] = None
    ultima_sincronizacao_vendas: Optional[datetime] = None
    ultima_sincronizacao_clientes: Optional[datetime] = None
    ultima_sincronizacao_estoque: Optional[datetime] = None
    ultima_sincronizacao_recebiveis: Optional[datetime] = None
    tempo_sinc_cadastro: Optional[int] = None
    tempo_sinc_venda: Optional[int] = None
    tempo_sinc_estoque: Optional[int] = None
    tasks_ativo: int
    log_webhook_ativo: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360FormaPagamentoConversao:
    """Tabela: portal_360_forma_pagamento_conversao (Linhas aprox: 6)"""
    id: int
    forma_pagamento_portal360: Optional[str] = None
    forma_pagamento_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Marca:
    """Tabela: portal_360_marca (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    fabricante_id: Optional[int] = None
    portal_360_brand_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360PaymentTerm:
    """Tabela: portal_360_payment_term (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    financeiro_condicao_pagamento_id: int
    portal_360_payment_term_id: Optional[str] = None
    sync_hash: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Pedido:
    """Tabela: portal_360_pedido (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    portal_360_order_id: Optional[str] = None
    order_number: Optional[str] = None
    order_date: Optional[datetime] = None
    customer: Optional[str] = None
    customer_name: Optional[str] = None
    customer_document: Optional[str] = None
    portal_360_seller_id: Optional[str] = None
    items: Optional[str] = None
    payments: Optional[str] = None
    order_payload: Optional[str] = None
    observations: Optional[str] = None
    status: Optional[str] = None
    total: Optional[Decimal] = None
    discount: Optional[Decimal] = None
    shipping_cost: Optional[Decimal] = None
    venda_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Produto:
    """Tabela: portal_360_produto (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    produto_empresa_id: int
    portal_360_product_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Promocao:
    """Tabela: portal_360_promocao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    promocao_id: Optional[int] = None
    portal_360_promotion_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Venda:
    """Tabela: portal_360_venda (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    venda_id: Optional[int] = None
    portal_360_order_id: Optional[str] = None
    numero: Optional[str] = None
    data: Optional[datetime] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Vendedor:
    """Tabela: portal_360_vendedor (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    funcionario_id: Optional[int] = None
    portal_360_seller_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Portal360Webhook:
    """Tabela: portal_360_webhook (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    portal_360_webhook_id: Optional[str] = None
    group: Optional[str] = None
    group_event: Optional[str] = None
    signature_version: int
    url_callback: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Producao:
    """Tabela: producao (Linhas aprox: 0)"""
    id: int
    tipo_producao: str
    status: str
    observacao: Optional[str] = None
    producao_produto_id: int
    producao_produto_empresa_grade_id: int
    producao_quantidade: Decimal
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ProducaoItem:
    """Tabela: producao_item (Linhas aprox: 0)"""
    id: int
    producao_id: int
    produto_id: int
    produto_empresa_grade_id: int
    quantidade: Decimal
    preco: Decimal
    peso: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Produto:
    """Tabela: produto (Linhas aprox: 104)"""
    id: int
    referencia: Optional[str] = None
    codigo_barras: Optional[str] = None
    nome: str
    api_guid: Optional[str] = None
    grupo_id: int
    fabricante_id: Optional[int] = None
    especifico_id: int
    tipo_especifico: Optional[str] = None
    similar_id: Optional[int] = None
    observacao: Optional[str] = None
    informacao_adicional: Optional[str] = None
    unidade_medida: Optional[str] = None
    peso: Optional[Decimal] = None
    altura: Decimal
    largura: Decimal
    comprimento: Decimal
    garantia: Optional[str] = None
    especificacao: Optional[str] = None
    preco_compra: Decimal
    preco_venda: Decimal
    margem_lucro: Decimal
    tipo_margem_lucro: Optional[str] = None
    vender: Optional[int] = None
    controlar_estoque: Optional[int] = None
    desativado: Optional[int] = None
    genero: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    habilitar_grade: Optional[int] = None
    order_attributes: Optional[str] = None
    ncm: Optional[str] = None
    origem: Optional[str] = None
    cest: Optional[str] = None
    percentual_comissao_produto: Decimal
    servico: Optional[int] = None
    tipo_produto: str
    agrupar_pedido: int
    detalhe: Optional[str] = None
    quantidade_caixa: Optional[Decimal] = None
    codigo_barras_caixa: Optional[str] = None
    taxa_entrega: int
    habilitar_acompanhamento: int
    self_service: Optional[int] = None
    perguntar_adicionais: Optional[int] = None
    cobrar_taxa_entrega: Optional[int] = None
    nao_enviar_comanda: Optional[int] = None
    cobrar_taxa_servico: int
    controlar_estoque_composicao: int
    taxa_adicional_delivery: int
    tipo_combo: int
    tipo_faturamento: int
    preco_a_partir_de: Decimal
    agrupar_impressao_item_combo: int
    modo_preparo: Optional[str] = None
    kds_tempo_preparo: Optional[int] = None
    item_complementar: int
    localizacao: Optional[str] = None
    comissao_id: Optional[int] = None
    embalagem_id: Optional[int] = None
    ifood_id: Optional[str] = None

@dataclass
class ProdutoCombo:
    """Tabela: produto_combo (Linhas aprox: 0)"""
    id: int
    produto_id: Optional[int] = None
    descricao: str
    quantidade_minima: int
    quantidade_maxima: int
    ordem: int
    habilitar_pizza: int
    tipo_calculo_preco: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    ifood_grupo_id: Optional[str] = None

@dataclass
class ProdutoComboItem:
    """Tabela: produto_combo_item (Linhas aprox: 0)"""
    id: int
    produto_combo_id: int
    produto_id: Optional[int] = None
    codigo_pdv: Optional[str] = None
    preco_venda: Decimal
    quantidade: Decimal
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    ifood_item_id: Optional[str] = None

@dataclass
class ProdutoComposicao:
    """Tabela: produto_composicao (Linhas aprox: 0)"""
    id: int
    produto_id: int
    materia_prima_id: int
    quantidade: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    produto_empresa_grade_id: Optional[int] = None

@dataclass
class ProdutoEmpresa:
    """Tabela: produto_empresa (Linhas aprox: 111)"""
    id: int
    produto_id: int
    empresa_id: int
    regra_fiscal_id: Optional[int] = None
    tributos_federais: Decimal
    tributos_estaduais: Decimal
    tributos_municipais: Decimal
    data_validade_ibpt: Optional[date] = None
    fundo_combate_pobreza: Decimal
    preco_compra: Decimal
    icms_compra: Decimal
    icms_fronteira: Decimal
    ipi: Decimal
    frete: Decimal
    encargo_financeiro: Decimal
    custo_fixo: Decimal
    imposto_federal: Decimal
    icms_venda: Decimal
    comissao: Decimal
    marketing: Decimal
    outro_custo: Decimal
    preco_custo: Decimal
    margem_sugerida: Decimal
    preco_sugerido: Decimal
    preco_venda: Decimal
    preco_a: Decimal
    preco_b: Decimal
    preco_c: Decimal
    estoque_minimo: Decimal
    localizacao: Optional[str] = None
    alteracao_preco: Optional[date] = None
    promocao_preco: Decimal
    promocao_validade: Optional[date] = None
    promocao_quantidade_tipo: Optional[str] = None
    promocao_multiplos: Optional[int] = None
    promocao_quantidade_bonificada: Optional[int] = None
    balanca: int
    balanca_validade_dias: Optional[int] = None
    balanca_tara: int
    sku_atributo: Optional[str] = None
    aliquota_issqn: Optional[Decimal] = None
    item_lista_servico: Optional[str] = None
    indicador_exigibilidade: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    preco_d: Decimal
    preco_e: Decimal
    codigo_beneficio_fiscal: Optional[str] = None
    embalagem: Decimal
    codigo_tributacao_municipal: Optional[str] = None
    nfse_codigo_servico_item_id: Optional[int] = None
    codigo_numerico_servico_item: Optional[str] = None
    data_atualizacao_preco: Optional[datetime] = None
    marketplace_created_at: Optional[datetime] = None
    marketplace_updated_at: Optional[datetime] = None
    marketplace_code: Optional[str] = None
    especifico_id: Optional[int] = None
    nbs_cnae: Optional[str] = None
    status_fiscal: int
    codigo_imendes: Optional[str] = None

@dataclass
class ProdutoEmpresaGrade:
    """Tabela: produto_empresa_grade (Linhas aprox: 78)"""
    id: int
    produto_empresa_id: int
    sku: str
    sku_atributo: str
    codigo_barra: str
    descricao: str
    preco_venda: Decimal
    estoque: Decimal
    estoque_minimo: Optional[Decimal] = None
    validade: Optional[date] = None
    fabricacao: Optional[date] = None
    ativo: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    softshop_grade: Optional[str] = None
    marketplace_created_at: Optional[datetime] = None
    marketplace_updated_at: Optional[datetime] = None
    marketplace_code: Optional[str] = None
    lote_codigo_agregacao: Optional[str] = None
    curva_abc: Optional[str] = None
    data_atualizacao_curva_abc: Optional[datetime] = None

@dataclass
class ProdutoEmpresaVinculoFiscal:
    """Tabela: produto_empresa_vinculo_fiscal (Linhas aprox: 77)"""
    id: int
    produto_empresa_id: int
    vinculo_fiscal_id: int
    empresa_id: Optional[int] = None

@dataclass
class ProdutoEspecificoArmamento:
    """Tabela: produto_especifico_armamento (Linhas aprox: 0)"""
    id: int
    especifico_tipo_arma: str
    especifico_numero_serie_arma: str
    especifico_numero_serie_cano: str
    especifico_: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ProdutoEspecificoCombustivel:
    """Tabela: produto_especifico_combustivel (Linhas aprox: 0)"""
    id: int
    especifico_codigo_produto: str
    especifico_descricao_produto: str
    especifico_percentual_glp: Optional[Decimal] = None
    especifico_percentual_gas_natural_importado: Optional[Decimal] = None
    especifico_valor_partida: Optional[Decimal] = None
    especifico_percentual_gas_natural: Optional[Decimal] = None
    especifico_codif: Optional[str] = None
    especifico_quantidade_combustivel: Optional[Decimal] = None
    especifico_uf_consumo: Optional[str] = None
    especifico_quantidade_bc_cide: Optional[Decimal] = None
    especifico_aliquota_cide: Optional[Decimal] = None
    especifico_valor_cide: Optional[Decimal] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    percentual_bio: Decimal
    aliquota_ad_rem: Decimal
    aliquota_ad_rem_icms_reten: Decimal
    aliquota_ad_rem_icms_ret: Decimal
    percentual_reducao_ad_rem: Decimal
    motivo_reducao_ad_rem: Optional[int] = None

@dataclass
class ProdutoEspecificoCombustivelOrigem:
    """Tabela: produto_especifico_combustivel_origem (Linhas aprox: 0)"""
    id: int
    indicador_importacao: int
    codigo_uf_origem: str
    percentual_originario_uf: Decimal
    produto_especifico_combustivel_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ProdutoEspecificoMedicamento:
    """Tabela: produto_especifico_medicamento (Linhas aprox: 0)"""
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    especifico_codigo_anvisa: str
    especifico_motivo_isencao: Optional[str] = None

@dataclass
class ProdutoEspecificoPapel:
    """Tabela: produto_especifico_papel (Linhas aprox: 0)"""
    id: int
    especifico_numero_recopi: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ProdutoEspecificoVeiculo:
    """Tabela: produto_especifico_veiculo (Linhas aprox: 0)"""
    id: int
    especifico_tipo_operacao: str
    especifico_chassi: str
    especifico_cor_codigo: str
    especifico_cor_descricao: str
    especifico_potencia_motor: str
    especifico_cilindrada: str
    especifico_peso_liquido: str
    especifico_peso_bruto: str
    especifico_numero_serie: str
    especifico_tipo_combustivel: str
    especifico_numero_motor: str
    especifico_capacidade_maxima_tracao: str
    especifico_distancia_eixo: str
    especifico_ano_modelo: int
    especifico_ano_fabricacao: int
    especifico_tipo_pintura: str
    especifico_tipo_veiculo: str
    especifico_especie_veiculo: str
    especifico_condicao_vin: str
    especifico_condicao_veiculo: str
    especifico_codigo_marca_modelo: str
    especifico_codigo_cor_denatran: str
    especifico_lotacao_capacidade: str
    especifico_tipo_restricao: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ProdutoEstoqueRuptura:
    """Tabela: produto_estoque_ruptura (Linhas aprox: 0)"""
    id: int
    estoque: Decimal
    data_ruptura: date
    produto_id: int
    produto_empresa_grade_id: int
    venda_id: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class ProdutoFornecedor:
    """Tabela: produto_fornecedor (Linhas aprox: 72)"""
    id: int
    produto_empresa_id: int
    codigo_fornecedor: str
    cnpj_fornecedor: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ProdutoImagem:
    """Tabela: produto_imagem (Linhas aprox: 0)"""
    id: int
    parent_id: int
    description: Optional[str] = None
    filename: str
    thumbnail: Optional[str] = None
    mid_file: Optional[str] = None
    extension: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    link: Optional[str] = None
    use_default: Optional[int] = None
    produto_empresa_id: Optional[int] = None

@dataclass
class ProdutoMarketplace:
    """Tabela: produto_marketplace (Linhas aprox: 0)"""
    id: int
    produto_empresa_id: int
    disponibilidade: str
    descricao: str
    preco: Decimal
    preco_personalizado: int
    habilitar: int
    link_carrinho: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    habilitar_estoque: int
    quantidade_por_pedido: Decimal
    promocao_preco: Decimal
    promocao_data_inicial: Optional[date] = None
    promocao_data_final: Optional[date] = None
    estoque_ruptura: Decimal
    produto_personalizado: int
    produto_descricao: Optional[str] = None
    grupo_id: Optional[int] = None
    marketplace_vinculado_id: Optional[int] = None
    status_api: Optional[str] = None
    personalizar_canais_venda: int

@dataclass
class ProdutoMarketplaceAnuncio:
    """Tabela: produto_marketplace_anuncio (Linhas aprox: 0)"""
    id: int
    produto_empresa_id: int
    tipo: str
    titulo: str
    descricao: str
    habilitar: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class ProdutoMarketplaceHubSaleschannel:
    """Tabela: produto_marketplace_hub_saleschannel (Linhas aprox: 0)"""
    id: int
    produto_empresa_id: int
    saleschannel_codigo: str
    preco: Decimal
    promocao_preco: Decimal
    promocao_data_inicial: Optional[date] = None
    promocao_data_final: Optional[date] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class ProdutoOrganizarEstoque:
    """Tabela: produto_organizar_estoque (Linhas aprox: 65)"""
    produto_id: int
    produto_empresa_grade_id: int
    venda: Decimal
    compra: Decimal
    ajuste_entrada: Decimal
    ajuste_saida: Decimal
    transferencia_entrada: Decimal
    transferencia_saida: Decimal
    requisicao: Decimal
    devolucao: Decimal
    composicao: Decimal
    nfe_entrada: Decimal
    nfe_saida: Decimal
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ProdutoRelacionado:
    """Tabela: produto_relacionado (Linhas aprox: 0)"""
    id: int
    produto_id: int
    produto_relacionado_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ProdutoRestauranteSetor:
    """Tabela: produto_restaurante_setor (Linhas aprox: 0)"""
    id: int
    produto_id: int
    restaurante_setor_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class Promocao:
    """Tabela: promocao (Linhas aprox: 0)"""
    id: int
    descricao: str
    data_hora_inicio: datetime
    data_hora_fim: datetime
    ativa: Optional[int] = None
    segunda: Optional[int] = None
    terca: Optional[int] = None
    quarta: Optional[int] = None
    quinta: Optional[int] = None
    sexta: Optional[int] = None
    sabado: Optional[int] = None
    domingo: Optional[int] = None
    hora_inicio: Optional[str] = None
    hora_fim: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    modulo: Optional[str] = None

@dataclass
class PromocaoEmpresa:
    """Tabela: promocao_empresa (Linhas aprox: 0)"""
    id: int
    promocao_id: int
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class PromocaoItem:
    """Tabela: promocao_item (Linhas aprox: 0)"""
    id: int
    produto_id: int
    produto_empresa_grade_id: int
    promocao_id: int
    percentual_promocao: Optional[Decimal] = None
    tipo_promocao: Optional[str] = None
    quantidade: Optional[Decimal] = None
    quantidade_bonificada: Optional[Decimal] = None
    valor_promocional_unidade: Optional[Decimal] = None
    descricao_promocional_quantidade: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Reajuste:
    """Tabela: reajuste (Linhas aprox: 0)"""
    id: int
    tipo: str
    data_inicial: Optional[datetime] = None
    data_final: Optional[datetime] = None
    numero_nota: Optional[str] = None
    imposto_compra: Decimal
    imposto_venda: Decimal
    icms_compra: Decimal
    icms_fronteira_compra: Decimal
    ipi_compra: Decimal
    frete_compra: Decimal
    embalagem_compra: Decimal
    encargos_compra: Decimal
    custo_fixo_venda: Decimal
    impostos_federais_venda: Decimal
    icms_venda: Decimal
    comissao_venda: Decimal
    marketing_venda: Decimal
    outros_venda: Decimal
    margem_lucro: Decimal
    produto_id: Optional[int] = None
    fabricante_id: Optional[int] = None
    fornecedor_id: Optional[int] = None
    grupo_id: Optional[int] = None
    tabela_preco_id: Optional[int] = None
    operacao: str
    reajuste: Decimal
    status: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ReajusteItem:
    """Tabela: reajuste_item (Linhas aprox: 2)"""
    id: int
    reajuste_id: int
    produto_empresa_id: int
    imposto_compra: Decimal
    imposto_venda: Decimal
    custo_produto: Decimal
    ponto_equilibrio: Decimal
    margem_lucro: Decimal
    preco_compra: Decimal
    preco_venda: Decimal
    reajuste: Decimal
    preco_reajuste: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Recebimento:
    """Tabela: recebimento (Linhas aprox: 0)"""
    id: str
    dispositivo_id: str
    transacao_descricao: str
    transacao_tipo: str
    operacao_tipo: str
    transacao_id: str
    transacao_data_utc: str
    valor: Decimal
    parcelas: Optional[int] = None
    restricoes: Optional[str] = None
    doc: Optional[str] = None
    outras_informacoes: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class RecebimentoAutorizacao:
    """Tabela: recebimento_autorizacao (Linhas aprox: 0)"""
    id: str
    recebimento_id: str
    numero_terminal: Optional[str] = None
    forma_pagamento: Optional[str] = None
    comprovante_tipo: Optional[str] = None
    comprovante_cliente: Optional[str] = None
    comprovante_estabelecimento: Optional[str] = None
    nsu: str
    host: str
    auto: Optional[str] = None
    bin: Optional[str] = None
    bandeira: Optional[str] = None
    bandeira_tipo: Optional[str] = None
    cnpj_credenciadora: Optional[str] = None
    codigo_autorizacao: Optional[str] = None
    cartao_validade: Optional[str] = None
    cartao_titular: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class RecebimentoStatus:
    """Tabela: recebimento_status (Linhas aprox: 0)"""
    id: str
    recebimento_id: str
    mensagem: str
    data_hora: date
    operador: str
    status: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Recibo:
    """Tabela: recibo (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    nome: str
    cnpj: Optional[str] = None
    valor: Decimal
    servico_realizado: str
    data_recibo: date
    user_lancamento_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    parcela_pagamento_id: Optional[int] = None

@dataclass
class RegistroBloqueado:
    """Tabela: registro_bloqueado (Linhas aprox: 0)"""
    id: int
    table_name: str
    field_where: str
    value_where: str
    bloqueado: int
    created_at: datetime
    updated_at: datetime

@dataclass
class RegraFiscal:
    """Tabela: regra_fiscal (Linhas aprox: 0)"""
    id: int
    ncm_codigo: str
    origem_codigo: int
    cst_codigo: str
    modalidade_base_codigo: int
    percentual_icms: Decimal
    percentual_reducao: Decimal
    percentual_diferimento: Decimal
    desoneracao_icms_codigo: Optional[int] = None
    modalidade_base_st_codigo: int
    percentual_icms_st: Decimal
    aliquota_icms_st: Decimal
    percentual_reducao_st: Decimal
    ipi_cst_codigo: str
    ipi_aliquota: Decimal
    ipi_enquadramento: Optional[str] = None
    pis_cst_codigo: int
    pis_aliquota: Decimal
    cofins_cst_codigo: int
    cofins_aliquota: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RelatorioPersonalizado:
    """Tabela: relatorio_personalizado (Linhas aprox: 0)"""
    id: int
    nome: str
    parent: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RelatorioPersonalizadoColunas:
    """Tabela: relatorio_personalizado_colunas (Linhas aprox: 0)"""
    id: int
    relatorio_personalizado_id: int
    nome: str
    cabecalho_id: str
    ativar: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RelatorioPersonalizadoConfig:
    """Tabela: relatorio_personalizado_config (Linhas aprox: 0)"""
    id: int
    user_id: Optional[int] = None
    nome_relatorio: str
    filtros: Optional[str] = None
    colunas: Optional[str] = None
    ativar_notificacao: int
    email: Optional[str] = None
    telefone: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RelatorioPersonalizadoFiltros:
    """Tabela: relatorio_personalizado_filtros (Linhas aprox: 0)"""
    id: int
    relatorio_personalizado_id: int
    label: str
    filtro_id: str
    valor: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RelatorioPersonalizadoNotificacaoConfiguracao:
    """Tabela: relatorio_personalizado_notificacao_configuracao (Linhas aprox: 0)"""
    id: int
    relatorio_personalizado_id: int
    ativar_notificacao: int
    frequencia: str
    horario: str
    destino_email: str
    destino_fone: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RelatorioUltimosAcessados:
    """Tabela: relatorio_ultimos_acessados (Linhas aprox: 4)"""
    id: int
    parent: str
    payload: str
    usuario_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class ResponsavelTecnicoConfiguracao:
    """Tabela: responsavel_tecnico_configuracao (Linhas aprox: 4)"""
    id: int
    ambiente: str
    uf: str
    modelo: str
    cnpj: str
    contato: str
    email: str
    fone: str
    id_csrt: Optional[str] = None
    csrt: Optional[str] = None
    sync: datetime

@dataclass
class RestauranteAmbiente:
    """Tabela: restaurante_ambiente (Linhas aprox: 0)"""
    id: int
    nome: str
    padrao: int
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RestauranteConfiguracaoImpressoras:
    """Tabela: restaurante_configuracao_impressoras (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    ambiente_id: int
    setor_id: int
    impressora_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RestauranteFamilia:
    """Tabela: restaurante_familia (Linhas aprox: 0)"""
    id: int
    nome: str
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class RestauranteGrupoObservacao:
    """Tabela: restaurante_grupo_observacao (Linhas aprox: 0)"""
    id: int
    grupo_id: int
    restaurante_observacao_id: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class RestauranteImpressora:
    """Tabela: restaurante_impressora (Linhas aprox: 9)"""
    id: int
    nome: str
    caminho: Optional[str] = None
    empresa_id: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class RestauranteMesa:
    """Tabela: restaurante_mesa (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    id_auxiliar: Optional[int] = None
    codigo_mesa: str
    mesa_fechada: int
    data_hora_abertura: Optional[datetime] = None
    cliente_id: int
    cliente_nome: Optional[str] = None
    numero_agrupamento: Optional[int] = None
    tele_entrega: int
    desconto: Decimal
    atendente_id: int
    atendente_nome: Optional[str] = None
    dados_entrega: Optional[str] = None
    numero_comanda: Optional[str] = None
    data_hora_ultimo_item: Optional[datetime] = None
    lacrar: int
    nao_cobrar_10_porcento: int
    cpf_cliente: Optional[str] = None
    indicador_id: Optional[int] = None
    indicador_nome: Optional[str] = None
    ponto_referencia: Optional[str] = None
    delivery: Optional[int] = None
    entregador_id: Optional[int] = None
    pedido_pronto: Optional[int] = None
    cliente_vem_retirar: Optional[int] = None
    data_preparacao_pedido: Optional[date] = None
    impresso_conferencia: Optional[int] = None
    fechamento_tipo_pagamento: Optional[int] = None
    fechamento_valor_pago: Decimal
    quantidade_comandas: Optional[int] = None
    quantidade_pessoas: Optional[int] = None
    solicitado_conferencia: int
    solicitado_conferencia_atendente_id: Optional[int] = None
    excluido: int
    desconto_valor_promocao: Decimal
    numero_nfce: Optional[int] = None
    tipo_preco_venda: Optional[str] = None
    catraca_bloqueada: int
    pedido_origem: Optional[str] = None
    pedido_confirmado: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RestauranteMesaAdiantamento:
    """Tabela: restaurante_mesa_adiantamento (Linhas aprox: 0)"""
    id: int
    restaurante_mesa_id: int
    descricao: Optional[str] = None
    valor_pago: Optional[float] = None
    valor_digitado: Optional[float] = None
    numero_documento: Optional[str] = None
    prazo: Optional[float] = None
    vencimento: Optional[date] = None
    nome_cartao: Optional[str] = None
    numero_parcelas: Optional[str] = None
    cache_enviado: int
    chave_smobile: Optional[str] = None
    tp_integra: Optional[float] = None
    rede: Optional[str] = None
    cliente_nome: Optional[str] = None
    cancelado: int
    pdv_tef: int
    pdv_pos: int
    cache_id: Optional[str] = None
    cartao_via_cliente: Optional[str] = None
    cartao_via_estabelecimento: Optional[str] = None
    impresso: int
    tp_cred: Optional[str] = None
    bandeira: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RestauranteMesaConfiguracao:
    """Tabela: restaurante_mesa_configuracao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    intervalo_comanda_inicial: int
    intervalo_comanda_final: int
    intervalo_mesa_inicial: int
    intervalo_mesa_final: int
    impressao_async: int
    registro_delivery: int
    utilizar_comanda: int
    utilizar_mesa: int
    utilizar_teclado_numerico: int
    impressao_por_usuario: int
    habilitar_cobranca_10_porcento: int
    bloquear_mesa_apos_conferencia: int
    versao_banco: int
    bloquear_conta_parcial: int
    mesa_ociosa: Optional[str] = None
    filtrar_mesa_garcom: int
    classificacao_listagem: Optional[str] = None
    impressao_setores: Optional[str] = None
    impressao_config: Optional[str] = None
    exibir_servico_opcional: int
    solicitar_senha_transferencia_itens: int
    solicitar_senha_cancelar_delivery: int
    solicitar_senha_remover_taxa_servico: int
    solicitar_senha_juntar_mesa: int
    solicitar_senha_cancelar_item: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RestauranteMesaItem:
    """Tabela: restaurante_mesa_item (Linhas aprox: 0)"""
    id: int
    api_guid: Optional[str] = None
    adicional_mesa_item_id: Optional[int] = None
    restaurante_mesa_id: int
    produto_id: int
    produto_empresa_grade_id: int
    quantidade: Decimal
    preco: Decimal
    cancelado: int
    numero_mesa_origem: Optional[int] = None
    descricao: Optional[str] = None
    selecionado: int
    remover: int
    pronto: int
    data_hora_registro: Optional[datetime] = None
    cozinha: int
    observacao: Optional[str] = None
    atendente_item_id: Optional[int] = None
    atendente_item_nome: Optional[str] = None
    acomp: Optional[str] = None
    nao_agrupar: int
    quantidade_cancelada: Decimal
    codigo_pesquisa: Optional[str] = None
    bar: Optional[int] = None
    data_hora_pronto: Optional[datetime] = None
    data_hora_painel_chamada: Optional[datetime] = None
    impresso: int
    comanda_item: Optional[int] = None
    couvert: int
    cobrar_servico: int
    delivery: int
    cancelamento_usuario: Optional[str] = None
    cancelamento_data_hora: Optional[datetime] = None
    cancelamento_motivo: Optional[str] = None
    mesa_origem_id: Optional[int] = None
    setor: Optional[str] = None
    sem_desconto_convenio: int
    restaurante_setor_id: Optional[int] = None
    cliente_item_nome: Optional[str] = None
    lancamento_guid: Optional[str] = None
    lancamento_origem: Optional[str] = None
    lancamento_confirmado: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RestauranteMesaItemAcompanhamento:
    """Tabela: restaurante_mesa_item_acompanhamento (Linhas aprox: 0)"""
    id: int
    api_guid: Optional[str] = None
    restaurante_mesa_item_id: int
    numero_mesa: int
    produto_id: int
    produto_empresa_grade_id: int
    quantidade: Decimal
    descricao: Optional[str] = None
    produto_combo_item_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class RestauranteObservacao:
    """Tabela: restaurante_observacao (Linhas aprox: 0)"""
    id: int
    descricao: str
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class RestauranteSetor:
    """Tabela: restaurante_setor (Linhas aprox: 0)"""
    id: int
    empresa_id: Optional[int] = None
    nome: str
    impressora: Optional[str] = None
    painel_cozinha: int
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    kds_painel: Optional[str] = None

@dataclass
class RoleUser:
    """Tabela: role_user (Linhas aprox: 3)"""
    id: int
    role_id: int
    user_id: int
    empresa_id: int
    favorita: int

@dataclass
class Roles:
    """Tabela: roles (Linhas aprox: 2)"""
    id: int
    role_title: str
    role_slug: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    profile: str

@dataclass
class ServicoIssqn:
    """Tabela: servico_issqn (Linhas aprox: None)"""
    id: int
    codigo: str
    nome: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class Similar:
    """Tabela: similar (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    aplicacao: str

@dataclass
class SkuAtributo:
    """Tabela: sku_atributo (Linhas aprox: 19)"""
    id: int
    parent_id: Optional[int] = None
    nome: str
    restrito: Optional[int] = None
    cor: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    hub_code: Optional[str] = None
    hub_name: Optional[str] = None

@dataclass
class Softcomintro:
    """Tabela: softcomintro (Linhas aprox: 0)"""
    id: int
    intro: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedConfiguracoes:
    """Tabela: sped_configuracoes (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    geral_exibir_escolha_perfil: int
    geral_gerar_c170_mod55: int
    geral_gerar_c170_mod65: int
    geral_perfil_de_escrituracao: str
    geral_atividade_empresa: str
    icms_permitir_apurar_credito: int
    icms_permitir_apurar_debito: int
    icms_nfe_propria_data_imposto: str
    icms_entradas_adicionar_st: str
    icms_codigo_receita_e116: str
    ipi_entradas_adicionar_ipi: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    fiscal_1601_regime: int
    geral_natureza_juridica: int
    geral_situacao_especial: Optional[int] = None
    geral_atividade: int
    geral_incidencia_tributaria: int
    geral_apropriacao_creditos: int
    geral_tipo_contribuicao_apurada: int
    geral_criterio_escrituracao: int
    geral_indicador_escrituracao: int
    valores_gerar_bc_aliqzero: int
    valores_personalizar_bc_compras: int
    valores_bc_en_desconto: int
    valores_bc_en_icmscte: int
    valores_bc_en_seguro: int
    valores_bc_en_frete: int
    valores_bc_en_icmsst: int
    valores_bc_en_ipi: int
    valores_bc_en_outrasdespesas: int
    valores_personalizar_base_vendas: int
    valores_bc_sd_desconto: int
    valores_bc_sd_icms: int
    valores_bc_sd_seguro: int
    valores_bc_sd_frete: int
    valores_bc_sd_icmsst: int
    valores_bc_sd_ipi: int
    valores_bc_sd_outrasdespesas: int

@dataclass
class SpedDownload:
    """Tabela: sped_download (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    access_key: str
    data_inicio: date
    data_fim: date
    data_sync: datetime
    download: int

@dataclass
class SpedE111AjusteApuracao:
    """Tabela: sped_e111_ajuste_apuracao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    data_referencia: date
    tipo_ajuste: str
    codigo_ajuste: Optional[str] = None
    descricao_ajuste: Optional[str] = None
    valor_ajuste: Decimal
    mes_referencia: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedE113AjusteApuracaoDocumentos:
    """Tabela: sped_e113_ajuste_apuracao_documentos (Linhas aprox: 0)"""
    id: int
    e111_ajuste_id: int
    fornecedor_id: int
    modelo_documento: str
    serie_documento: str
    numero_documento: int
    data_documento: date
    codigo_item: int
    valor_ajuste: Decimal
    chave_acesso: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedE115ValoresDeclaratorios:
    """Tabela: sped_e115_valores_declaratorios (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    data_referencia: date
    codigo_ajuste: str
    descricao_ajuste: Optional[str] = None
    valor_ajuste: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedInventarioBase:
    """Tabela: sped_inventario_base (Linhas aprox: 0)"""
    id: int
    produto_id: int
    produto_empresa_id: int
    produto_empresa_grade_id: int
    nome: str
    data: date
    quantidade: Decimal
    created_at: datetime
    updated_at: datetime

@dataclass
class SpedIpiAjusteApuracao:
    """Tabela: sped_ipi_ajuste_apuracao (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    data_referencia: date
    tipo_ajuste: str
    codigo_ajuste: str
    descricao_ajuste: Optional[str] = None
    valor_ajuste: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedPlanoContas:
    """Tabela: sped_plano_contas (Linhas aprox: 0)"""
    id: int
    data_inclusao: datetime
    codigo: Optional[str] = None
    descricao: Optional[str] = None
    tipo: Optional[str] = None
    natureza: Optional[str] = None
    nivel: int
    codigo_referencial: Optional[str] = None
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class SpedPlanoContasCfop:
    """Tabela: sped_plano_contas_cfop (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    sped_plano_conta_id: int
    cfop: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class SpedTabela454:
    """Tabela: sped_tabela_4_5_4 (Linhas aprox: 9)"""
    id: int
    codigo: str
    descricao: str
    cd: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedTabela511:
    """Tabela: sped_tabela_5_1_1 (Linhas aprox: None)"""
    id: int
    codigo: str
    descricao: str
    cd: str
    tipo_icms: str
    uf: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedTabela52:
    """Tabela: sped_tabela_5_2 (Linhas aprox: 20)"""
    id: int
    codigo: str
    descricao: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class SpedTabelaE115CodigoApuracao:
    """Tabela: sped_tabela_e115_codigo_apuracao (Linhas aprox: 1197)"""
    id: int
    codigo: str
    descricao: str
    uf: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class TaNoMenuCategoria:
    """Tabela: ta_no_menu_categoria (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    grupo_id: Optional[str] = None
    category_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class TaNoMenuConfig:
    """Tabela: ta_no_menu_config (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    ultima_sincronizacao_cadastro: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TaNoMenuProduto:
    """Tabela: ta_no_menu_produto (Linhas aprox: 0)"""
    id: int
    produto_id: Optional[int] = None
    product_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    empresa_id: int

@dataclass
class TaNoMenuPromocao:
    """Tabela: ta_no_menu_promocao (Linhas aprox: 0)"""
    id: int
    promocao_id: int
    promotion_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class TaNoMenuPromocaoItem:
    """Tabela: ta_no_menu_promocao_item (Linhas aprox: 0)"""
    id: int
    promocao_id: int
    produto_empresa_grade_id: Optional[int] = None
    promotion_item_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class TaNoMenuVariation:
    """Tabela: ta_no_menu_variation (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    produto_combo_id: int
    variation_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class TaNoMenuVariationAdditional:
    """Tabela: ta_no_menu_variation_additional (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    grupo_id: int
    produto_id: Optional[int] = None
    variation_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class TaNoMenuVariationAdditionalItem:
    """Tabela: ta_no_menu_variation_additional_item (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    grupo_adicional_id: int
    produto_id: Optional[int] = None
    produto_adicional_id: Optional[int] = None
    variation_item_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class TaNoMenuVariationItem:
    """Tabela: ta_no_menu_variation_item (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    produto_combo_id: int
    produto_id: Optional[int] = None
    variation_item_code: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class TabelaPreco:
    """Tabela: tabela_preco (Linhas aprox: 4)"""
    id: int
    descricao: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class TabelaPrecoProduto:
    """Tabela: tabela_preco_produto (Linhas aprox: 0)"""
    id: int
    tabela_preco_id: int
    produto_empresa_id: Optional[int] = None
    preco: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class TagClassificacao:
    """Tabela: tag_classificacao (Linhas aprox: 0)"""
    id: int
    descricao: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TelescopeEntries:
    """Tabela: telescope_entries (Linhas aprox: 0)"""
    sequence: int
    uuid: str
    batch_id: str
    family_hash: Optional[str] = None
    should_display_on_index: int
    type: str
    content: str
    created_at: Optional[datetime] = None

@dataclass
class TelescopeEntriesTags:
    """Tabela: telescope_entries_tags (Linhas aprox: 0)"""
    entry_uuid: str
    tag: str

@dataclass
class TelescopeMonitoring:
    """Tabela: telescope_monitoring (Linhas aprox: 0)"""
    tag: str

@dataclass
class TipoAjuste:
    """Tabela: tipo_ajuste (Linhas aprox: 3)"""
    id: int
    nome: str
    permitir_excluir: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoArea:
    """Tabela: tipo_area (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoCliente:
    """Tabela: tipo_cliente (Linhas aprox: 2)"""
    id: int
    nome: str
    permitir_excluir: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoConvenio:
    """Tabela: tipo_convenio (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoDebito:
    """Tabela: tipo_debito (Linhas aprox: 0)"""
    id: int
    descricao: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoDocumento:
    """Tabela: tipo_documento (Linhas aprox: 3)"""
    id: int
    nome: str
    deleted_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    permitir_excluir: int

@dataclass
class TipoEnergiaGrupotensao:
    """Tabela: tipo_energia_grupotensao (Linhas aprox: 0)"""
    id: int
    codigo: str
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoEnergiaLigacao:
    """Tabela: tipo_energia_ligacao (Linhas aprox: 0)"""
    id: int
    codigo: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoFator:
    """Tabela: tipo_fator (Linhas aprox: 0)"""
    id: int
    nome: str
    percentual: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoFrete:
    """Tabela: tipo_frete (Linhas aprox: 0)"""
    id: int
    codigo: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoFuncao:
    """Tabela: tipo_funcao (Linhas aprox: 3)"""
    id: int
    nome: str
    permitir_excluir: int
    atendente: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoJustificativa:
    """Tabela: tipo_justificativa (Linhas aprox: 6)"""
    id: int
    descricao: str
    rotina: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoModelo:
    """Tabela: tipo_modelo (Linhas aprox: 0)"""
    id: int
    codigo: str
    nome: str
    operacao: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoNcm:
    """Tabela: tipo_ncm (Linhas aprox: None)"""
    id: int
    codigo: str
    nome: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoSetor:
    """Tabela: tipo_setor (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoSimilar:
    """Tabela: tipo_similar (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TipoUnidadeMedida:
    """Tabela: tipo_unidade_medida (Linhas aprox: 3)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class TransferenciaBancaria:
    """Tabela: transferencia_bancaria (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    data_operacao: date
    banco_origem_id: int
    banco_destino_id: int
    forma_pagamento_id: int
    historico: str
    valor: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Transportador:
    """Tabela: transportador (Linhas aprox: 0)"""
    id: int
    empresa_id: int
    pessoa: str
    cpf_cnpj: Optional[str] = None
    inscricao_estadual: Optional[str] = None
    rg: Optional[str] = None
    nome: str
    razao_social: str
    observacao: Optional[str] = None
    veiculo_placa: Optional[str] = None
    veiculo_uf: Optional[str] = None
    rntrc: Optional[str] = None
    tipo_transportador: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class TributosPorUf:
    """Tabela: tributos_por_uf (Linhas aprox: 0)"""
    id: int
    uf_destino: str
    ncm: Optional[str] = None
    ncm_descricao: Optional[str] = None
    fcp_aliquota: Decimal
    fcp_st_aliquota: Decimal
    empresa_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Troca:
    """Tabela: troca (Linhas aprox: 0)"""
    id: int
    devolucao_id: Optional[int] = None
    nfe_devolucao_id: Optional[int] = None
    venda_id: Optional[int] = None
    movimentacao_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    api_guid_nova_venda: Optional[str] = None
    venda_origem_funcionario_id: Optional[int] = None
    cliente_id: Optional[int] = None
    caixa_turno: Optional[int] = None
    caixa_operador_id: Optional[int] = None

@dataclass
class Users:
    """Tabela: users (Linhas aprox: 3)"""
    id: int
    name: str
    email: str
    password: str
    remember_token: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    default: int

@dataclass
class Veiculo:
    """Tabela: veiculo (Linhas aprox: 0)"""
    id: int
    placa: str
    renavam: Optional[str] = None
    tara: str
    capacidade_kg: Optional[str] = None
    capacidade_m: Optional[str] = None
    prorietario_tipo_pessoa: Optional[str] = None
    proprietario_cpf_cnpj: Optional[str] = None
    proprietario_rntrc: Optional[str] = None
    proprietario_nome: Optional[str] = None
    proprietario_inscricao_estadual: Optional[str] = None
    proprietario_uf: Optional[str] = None
    proprietario_tipo: Optional[str] = None
    tipo_rodado: str
    tipo_carroceria: str
    uf_licenciado: str
    reboque: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    codigo_veiculo: Optional[str] = None
    codigo_agendamento_portuario: Optional[str] = None

@dataclass
class VeiculoMarca:
    """Tabela: veiculo_marca (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VeiculoModelo:
    """Tabela: veiculo_modelo (Linhas aprox: 0)"""
    id: int
    nome: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Venda:
    """Tabela: venda (Linhas aprox: 95)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    nfe_id: Optional[int] = None
    nfse_id: Optional[int] = None
    observacao: Optional[str] = None
    api_cliente_cpf: Optional[str] = None
    api_cliente_nome: Optional[str] = None
    api_faturar: Optional[str] = None
    api_status: Optional[str] = None
    api_app_name: Optional[str] = None
    api_data_hora_venda: Optional[datetime] = None
    desconto_valor: Decimal
    desconto_percentual: Decimal
    acrescimo_valor: Decimal
    acrescimo_percentual: Decimal
    percentual_comissao_venda: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    api_guid: str
    api_device_id: str
    cancelada: int
    usuario_lancamento_id: Optional[int] = None
    bloqueada: int
    parent_guid: Optional[str] = None
    usuario_cancelamento_id: Optional[int] = None
    data_hora_cancelamento: Optional[datetime] = None
    numero_documento: Optional[str] = None
    numero_caixa: Optional[str] = None
    tipo_preco_id: Optional[int] = None
    integracao_delivery: Optional[str] = None
    entregador_id: Optional[int] = None
    tipo_entrega: str
    observacao_retirada: Optional[str] = None
    previsao_entrega: Optional[date] = None
    cliente_endereco_id: Optional[int] = None
    pedido_entregador_id: Optional[int] = None
    assistencia_id: Optional[int] = None
    caixa_funcoes_id: Optional[int] = None
    caixa_turno: Optional[int] = None
    caixa_data: Optional[date] = None
    indicador_id: Optional[int] = None
    marketplace_pedido_id: Optional[int] = None
    atendente_mesa: Optional[str] = None
    comissao_entregador: Optional[Decimal] = None
    comissao_indicador: Optional[Decimal] = None
    numero_mesa: Optional[str] = None
    numero_comanda: Optional[str] = None
    origem_venda: Optional[str] = None
    quantidade_pessoas: Optional[int] = None
    quantidade_comandas: Optional[int] = None
    tipo_lancamento: str
    orcamento_id: Optional[int] = None
    orcamento_competencia: Optional[date] = None
    numero_pre_venda: Optional[str] = None
    api_data_hora_lancamento: Optional[datetime] = None
    valor_total: Decimal
    total_pagamento: Decimal
    total_desconto: Decimal
    total_acrescimo: Decimal
    status: str
    data_hora_venda: Optional[datetime] = None
    fator_acrescimo_id: Optional[int] = None

@dataclass
class VendaAcoes:
    """Tabela: venda_acoes (Linhas aprox: 0)"""
    id: int
    venda_id: int
    impresso: int
    nota_fiscal: int
    boleto: int
    pix: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VendaBloqueio:
    """Tabela: venda_bloqueio (Linhas aprox: 0)"""
    id: int
    venda_id: int
    funcionario_id: Optional[int] = None
    observacao: Optional[str] = None
    motivo_bloqueio: str
    bloqueio: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VendaCartao:
    """Tabela: venda_cartao (Linhas aprox: 89)"""
    id: int
    valor_recebido: Decimal
    tipo_integracao_cartao: Optional[str] = None
    nome_credenciadora_cartao: Optional[str] = None
    cnpj_credenciadora_cartao: Optional[str] = None
    tipo_bandeira_cartao: Optional[str] = None
    codigo_autorizacao_cartao: Optional[str] = None
    recibo_aid: Optional[str] = None
    recibo_arqc: Optional[str] = None
    recibo_autorizacao: Optional[str] = None
    recibo_cnpj: Optional[str] = None
    recibo_nome_loja: Optional[str] = None
    recibo_cv: Optional[str] = None
    recibo_nsu: Optional[str] = None
    recibo_nome_cliente: Optional[str] = None
    recibo_numero_terminal: Optional[str] = None
    recibo_nome_emissor: Optional[str] = None
    recibo_tipo_operacao: Optional[str] = None
    recibo_valor: Decimal
    recibo_valor_parcela: Decimal
    recibo_parcelas: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    mfe_codigo_nsu_adquirente: Optional[str] = None
    mfe_codigo_autorizacao_adquirente: Optional[str] = None
    mfe_instituicao_financeira: Optional[str] = None
    mfe_bandeira_cartao: Optional[str] = None
    mfe_codigo_nsu_sefaz: Optional[str] = None
    mfe_autorizacao_online: Optional[int] = None
    mfe_pos_id: Optional[int] = None
    mfe_id_fechamento: Optional[str] = None
    caixa_funcoes_id: Optional[int] = None
    conciliacao_maquina_id: Optional[str] = None
    conciliacao_id: Optional[str] = None
    conciliacao_status: Optional[str] = None
    conciliacao_confirmacao: int
    conciliacao_nsu: Optional[str] = None
    conciliacao_data: Optional[datetime] = None
    geracao_automatica: int
    conciliacao_bandeira: Optional[str] = None
    conciliacao_bandeira_codigo: Optional[str] = None
    conciliacao_modalidade: Optional[str] = None

@dataclass
class VendaEnderecoEntrega:
    """Tabela: venda_endereco_entrega (Linhas aprox: 0)"""
    id: int
    venda_id: int
    cep: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class VendaItem:
    """Tabela: venda_item (Linhas aprox: 192)"""
    id: int
    venda_id: int
    produto_id: int
    produto_empresa_grade_id: int
    descricao_item: Optional[str] = None
    preco: Decimal
    quantidade: Decimal
    preco_compra: Decimal
    desconto_valor_item: Decimal
    acrescimo_valor_item: Decimal
    comissao: Optional[Decimal] = None
    vinculo_nfe: str
    desabilita_rateio: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    codigo_beneficio_fiscal: Optional[str] = None
    percentual_desconto: Optional[Decimal] = None
    percentual_acrescimo: Optional[Decimal] = None
    tipo_promocao: Optional[str] = None
    descricao_promocao: Optional[str] = None
    quantidade_promocao: Decimal
    quantidade_bonificada_promocao: Decimal
    valor_unidade_promocao: Decimal
    promocao_aplicada: int
    preco_original: Decimal
    existe_tabela_preco: int
    tabela_preco_valor: Decimal
    peso: Optional[Decimal] = None
    atendente_item: Optional[int] = None
    comissao_atendente: Optional[Decimal] = None
    cobrar_taxa_servico: Optional[int] = None
    guid: Optional[str] = None
    parent_guid: Optional[str] = None
    tipo_faturamento: int
    valor_desconto_promocao: Decimal
    comissao_atendente_lancamento: Optional[Decimal] = None
    comissao_carta_produto: Optional[Decimal] = None
    comissao_carta_produto_tipo: Optional[str] = None

@dataclass
class VendaItemAnimal:
    """Tabela: venda_item_animal (Linhas aprox: 0)"""
    id: int
    venda_item_id: int
    animal_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class VendaItemComposicao:
    """Tabela: venda_item_composicao (Linhas aprox: 0)"""
    id: int
    venda_id: int
    venda_item_id: Optional[int] = None
    venda_item_produto_id: int
    produto_id: int
    produto_empresa_grade_id: int
    quantidade: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VendaNfce:
    """Tabela: venda_nfce (Linhas aprox: 0)"""
    id: int
    venda_id: int
    nfce_nro: int
    nfce_protocolo: Optional[str] = None
    nfce_serie: Optional[str] = None
    nfce_chave: Optional[str] = None
    nfce_data: Optional[str] = None
    nfce_digestvalue: Optional[str] = None
    nfce_cstat: Optional[str] = None
    nfce_tipoemissao: Optional[str] = None
    nfce_msgerro: Optional[str] = None
    nfce_datahora_contingencia: Optional[datetime] = None
    nfce_motivo_contingencia: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VendaNotaReferenciada:
    """Tabela: venda_nota_referenciada (Linhas aprox: 0)"""
    id: int
    venda_id: int
    nota_fiscal_eletronica_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class VendaOrdemServico:
    """Tabela: venda_ordem_servico (Linhas aprox: 0)"""
    id: int
    venda_id: int
    status: Optional[str] = None
    nome_solicitante: Optional[str] = None
    tecnico_responsavel: Optional[str] = None
    data_previsao_entrega: Optional[datetime] = None
    atendimento_externo: Optional[int] = None
    data_atendimento: Optional[date] = None
    hora_marcada: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fim: Optional[str] = None
    equipamento_id: Optional[int] = None
    marca_equipamento_id: Optional[int] = None
    equipamento_modelo: Optional[str] = None
    equipamento_numero_serie: Optional[str] = None
    equipamento_defeito: Optional[str] = None
    equipamento_acessorios: Optional[str] = None
    laudo_tecnico: Optional[str] = None
    servico_realizado: Optional[str] = None
    observacoes_internas: Optional[str] = None
    data_hora_finalizacao: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VendaOrdemServicoContato:
    """Tabela: venda_ordem_servico_contato (Linhas aprox: 0)"""
    id: int
    ordem_servico_id: Optional[int] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VendaStatusHistorico:
    """Tabela: venda_status_historico (Linhas aprox: 0)"""
    id: int
    venda_id: int
    status: str
    observacao: Optional[str] = None
    funcionario_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VendaVeiculo:
    """Tabela: venda_veiculo (Linhas aprox: 0)"""
    venda_id: int
    veiculo_id: Optional[int] = None
    placa: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    cor: Optional[str] = None
    combustivel: Optional[str] = None
    ano_fabricacao: Optional[str] = None
    renavam: Optional[str] = None
    chassi: Optional[str] = None
    km: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class Vendas-laravelCreateFinanceiroParcelaDadosCartaoTable:
    """Tabela: vendas-laravel_create_financeiro_parcela_dados_cartao_table (Linhas aprox: 0)"""
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

@dataclass
class ViewMemoriaFinanceiroAgrupada:
    """Tabela: view_memoria_financeiro_agrupada (Linhas aprox: None)"""
    financeiro_id: int
    financeiro_empresa_id: int
    financeiro_data_lancamento: date
    financeiro_documento: Optional[str] = None
    financeiro_historico: str
    financeiro_fornecedor_id: Optional[int] = None
    financeiro_cliente_id: Optional[int] = None
    financeiro_contrato_servico_id: Optional[int] = None
    financeiro_created_at: datetime
    financeiro_updated_at: Optional[datetime] = None
    financeiro_deleted_at: Optional[datetime] = None
    financeiro_valor: Decimal
    financeiro_tipo_documento_id: Optional[int] = None
    financeiro_origem: Optional[str] = None
    financeiro_device_id: Optional[str] = None
    financeiro_usuario_lancamento_id: Optional[int] = None
    financeiro_api_device_id: Optional[str] = None
    financeiro_repeticao: str
    financeiro_repeticao_tipo: str
    financeiro_repeticao_quantidade: int
    financeiro_repeticao_intervalo: int
    financeiro_termino_vigencia: str
    financeiro_data_termino_vigencia: Optional[date] = None
    financeiro_caixa_operador_id: Optional[int] = None
    financeiro_empresa_nome: str
    financeiro_empresa_nome_fantasia: str
    financeiro_empresa_razao_social: str
    financeiro_categoria_id: int
    categoria_nome: Optional[str] = None
    categoria_codigo: Optional[str] = None
    categoria_conta_dre_id: Optional[int] = None
    categoria_tag: Optional[str] = None
    categoria_tipo: Optional[str] = None
    parcela_id: int
    parcela_compra_id: Optional[int] = None
    parcela_venda_id: Optional[int] = None
    parcela_financeiro_id: Optional[int] = None
    parcela_transferencia_id: Optional[int] = None
    parcela_fornecedor_id: Optional[int] = None
    parcela_cliente_id: Optional[int] = None
    parcela_contrato_servico_id: Optional[int] = None
    parcela_documento: Optional[str] = None
    parcela_conta_id: Optional[int] = None
    parcela_cartao_credito_id: Optional[int] = None
    parcela_venda_cartao_id: Optional[int] = None
    parcela_api_codigo_pagamento: Optional[str] = None
    parcela_api_nome_pagamento: Optional[str] = None
    parcela_numero: Optional[str] = None
    parcela_vencimento: date
    parcela_tarifa: Optional[Decimal] = None
    parcela_duplicata_pendente: int
    parcela_banco_id: Optional[int] = None
    parcela_financeira_id: Optional[int] = None
    parcela_data_caixa: Optional[date] = None
    parcela_observacao: Optional[str] = None
    parcela_created_at: datetime
    parcela_updated_at: Optional[datetime] = None
    parcela_deleted_at: Optional[datetime] = None
    parcela_cancelada: int
    parcela_parcela_vinculada: Optional[int] = None
    parcela_operacao: Optional[str] = None
    parcela_empresa_id: Optional[int] = None
    parcela_user_id: Optional[int] = None
    parcela_motivo_cancelamento: Optional[str] = None
    parcela_cheque_banco: Optional[str] = None
    parcela_data_cancelamento: Optional[datetime] = None
    parcela_guid: Optional[str] = None
    parcela_pos_habilitar: Optional[int] = None
    parcela_tp_integra: Optional[int] = None
    parcela_api_cobranca_id: Optional[str] = None
    parcela_api_cobranca_agreemente_id: Optional[str] = None
    parcela_codigo_autorizacao: Optional[str] = None
    parcela_cnpj_instituicao_financeira: Optional[str] = None
    parcela_cartao_credito_taxa_admin: Optional[Decimal] = None
    parcela_tipo_debito_id: Optional[int] = None
    parcela_conciliacao_extrato_bancario: int
    cartao_nome: Optional[str] = None
    cartao_taxa_admin: Optional[Decimal] = None
    parcela_forma_pagamento_id: int
    parcela_forma_pagamento_nome: Optional[str] = None
    parcela_forma_pagamento_tipo: Optional[str] = None
    parcela_forma_pagamento_exibir: Optional[int] = None
    parcela_forma_pagamento_saldo_caixa: Optional[int] = None
    parcela_forma_pagamento_codigo_nfce: Optional[str] = None
    parcela_forma_pagamento_ordem: Optional[int] = None
    valor_pago_parcela: Decimal
    valor_pago_liquido_parcela: Decimal
    acrescimo_parcela: Decimal
    desconto_parcela: Decimal
    valor_parcela: Decimal
    valor_parcela_corrigido: Optional[Decimal] = None
    valor_pendente: Optional[Decimal] = None

@dataclass
class ViewMemoriaFinanceiroPagamento:
    """Tabela: view_memoria_financeiro_pagamento (Linhas aprox: None)"""
    financeiro_parcela_id: int
    valor_pago: Optional[Decimal] = None
    acrescimo: Optional[Decimal] = None
    desconto: Optional[Decimal] = None
    valor_total: Optional[Decimal] = None

@dataclass
class ViewMemoriaFinanceiroTodas:
    """Tabela: view_memoria_financeiro_todas (Linhas aprox: None)"""
    financeiro_id: int
    financeiro_empresa_id: int
    financeiro_data_lancamento: date
    financeiro_documento: Optional[str] = None
    financeiro_historico: str
    financeiro_fornecedor_id: Optional[int] = None
    financeiro_cliente_id: Optional[int] = None
    financeiro_contrato_servico_id: Optional[int] = None
    financeiro_created_at: datetime
    financeiro_updated_at: Optional[datetime] = None
    financeiro_deleted_at: Optional[datetime] = None
    financeiro_valor: Decimal
    financeiro_tipo_documento_id: Optional[int] = None
    financeiro_origem: Optional[str] = None
    financeiro_device_id: Optional[str] = None
    financeiro_usuario_lancamento_id: Optional[int] = None
    financeiro_api_device_id: Optional[str] = None
    financeiro_repeticao: str
    financeiro_repeticao_tipo: str
    financeiro_repeticao_quantidade: int
    financeiro_repeticao_intervalo: int
    financeiro_termino_vigencia: str
    financeiro_data_termino_vigencia: Optional[date] = None
    financeiro_caixa_operador_id: Optional[int] = None
    financeiro_empresa_nome: str
    financeiro_empresa_nome_fantasia: str
    financeiro_empresa_razao_social: str
    financeiro_categoria_id: int
    categoria_nome: Optional[str] = None
    categoria_codigo: Optional[str] = None
    categoria_conta_dre_id: Optional[int] = None
    categoria_tag: Optional[str] = None
    categoria_tipo: Optional[str] = None
    parcela_id: int
    parcela_compra_id: Optional[int] = None
    parcela_venda_id: Optional[int] = None
    parcela_financeiro_id: Optional[int] = None
    parcela_transferencia_id: Optional[int] = None
    parcela_fornecedor_id: Optional[int] = None
    parcela_cliente_id: Optional[int] = None
    parcela_contrato_servico_id: Optional[int] = None
    parcela_documento: Optional[str] = None
    parcela_conta_id: Optional[int] = None
    parcela_cartao_credito_id: Optional[int] = None
    parcela_venda_cartao_id: Optional[int] = None
    parcela_api_codigo_pagamento: Optional[str] = None
    parcela_api_nome_pagamento: Optional[str] = None
    parcela_numero: Optional[str] = None
    parcela_vencimento: date
    parcela_tarifa: Optional[Decimal] = None
    parcela_duplicata_pendente: int
    parcela_banco_id: Optional[int] = None
    parcela_financeira_id: Optional[int] = None
    parcela_data_caixa: Optional[date] = None
    parcela_observacao: Optional[str] = None
    parcela_created_at: datetime
    parcela_updated_at: Optional[datetime] = None
    parcela_deleted_at: Optional[datetime] = None
    parcela_cancelada: int
    parcela_parcela_vinculada: Optional[int] = None
    parcela_operacao: Optional[str] = None
    parcela_empresa_id: Optional[int] = None
    parcela_user_id: Optional[int] = None
    parcela_motivo_cancelamento: Optional[str] = None
    parcela_cheque_banco: Optional[str] = None
    parcela_data_cancelamento: Optional[datetime] = None
    parcela_guid: Optional[str] = None
    parcela_pos_habilitar: Optional[int] = None
    parcela_tp_integra: Optional[int] = None
    parcela_api_cobranca_id: Optional[str] = None
    parcela_api_cobranca_agreemente_id: Optional[str] = None
    parcela_codigo_autorizacao: Optional[str] = None
    parcela_cnpj_instituicao_financeira: Optional[str] = None
    parcela_cartao_credito_taxa_admin: Optional[Decimal] = None
    parcela_tipo_debito_id: Optional[int] = None
    parcela_conciliacao_extrato_bancario: int
    cartao_nome: Optional[str] = None
    cartao_taxa_admin: Optional[Decimal] = None
    parcela_forma_pagamento_id: int
    parcela_forma_pagamento_nome: Optional[str] = None
    parcela_forma_pagamento_tipo: Optional[str] = None
    parcela_forma_pagamento_exibir: Optional[int] = None
    parcela_forma_pagamento_saldo_caixa: Optional[int] = None
    parcela_forma_pagamento_codigo_nfce: Optional[str] = None
    parcela_forma_pagamento_ordem: Optional[int] = None
    valor_pago_parcela: Decimal
    valor_pago_liquido_parcela: Decimal
    acrescimo_parcela: Decimal
    desconto_parcela: Decimal
    valor_parcela: Decimal
    valor_parcela_corrigido: Optional[Decimal] = None
    valor_pendente: Optional[Decimal] = None
    pagamento_id: Optional[int] = None
    pagamento_valor_pago: Optional[Decimal] = None
    pagamento_acrescimo: Optional[Decimal] = None
    pagamento_desconto: Optional[Decimal] = None
    pagamento_valor_pago_liquido: Optional[Decimal] = None
    pagamento_conta_id: Optional[int] = None
    pagamento_conta_nome: Optional[str] = None
    pagamento_conta_tipo: Optional[str] = None
    pagamento_financeiro_parcela_id: Optional[int] = None
    pagamento_data_pagamento: Optional[date] = None
    data_hora_pagamento: Optional[str] = None
    pagamento_created_at: Optional[datetime] = None
    pagamento_updated_at: Optional[datetime] = None
    pagamento_deleted_at: Optional[datetime] = None
    pagamento_user_baixa_id: Optional[int] = None
    pagamento_api_device_id: Optional[str] = None
    pagamento_valor_recebido: Optional[Decimal] = None
    pagamento_caixa_funcoes_id: Optional[int] = None
    pagamento_caixa_turno: Optional[str] = None
    pagamento_forma_pagamento_baixa_id: Optional[int] = None
    pagamento_forma_pagamento_nome: Optional[str] = None
    pagamento_forma_pagamento_tipo: Optional[str] = None
    pagamento_forma_pagamento_exibir: Optional[int] = None
    pagamento_forma_pagamento_saldo_caixa: Optional[int] = None
    pagamento_forma_pagamento_codigo_nfce: Optional[str] = None
    pagamento_forma_pagamento_ordem: Optional[int] = None

@dataclass
class ViewMemoriaNfEntrada:
    """Tabela: view_memoria_nf_entrada (Linhas aprox: None)"""
    id: int
    origem: str
    empresa_id: int
    data_hora_emissao: Optional[datetime] = None
    data_hora_entrada: Optional[datetime] = None
    numero_nfe: int
    modelo: Optional[str] = None
    serie: Optional[str] = None
    ambiente: Optional[int] = None
    destinatario_nome: str
    destinatario_cpf_cnpj: str
    xml_recibo_emissao: Optional[str] = None
    numero_protocolo_autorizacao: Optional[str] = None
    xml_cancelamento: Optional[str] = None
    recibo_situacao: Optional[str] = None
    cancelada: int
    denegada: int
    chave_acesso: Optional[str] = None
    tipo_emissao: Optional[int] = None
    deleted_at: Optional[datetime] = None
    cfop: Optional[str] = None
    cfop_natureza: str
    pis_cst: Optional[str] = None
    cofins_cst: Optional[str] = None
    produto_id: int
    quantidade_tributavel: Optional[Decimal] = None
    valor_unitario_tributavel: Optional[Decimal] = None
    valor_total_desconto: Decimal
    valor_total_frete: Decimal
    valor_total_outras_despesas: Decimal
    icms_base_calculo: Decimal
    icms_valor: Decimal
    icmsst_valor: Decimal
    fcp_st_valor: Decimal
    ipi_valor: Decimal
    pis_valor: Decimal
    cofins_valor: Decimal

@dataclass
class ViewMemoriaNfSaida:
    """Tabela: view_memoria_nf_saida (Linhas aprox: None)"""
    id: int
    empresa_id: int
    numero_nfe: int
    modelo: Optional[str] = None
    serie: Optional[str] = None
    ambiente: Optional[int] = None
    data_hora_emissao: Optional[datetime] = None
    data_hora_saida: Optional[datetime] = None
    recibo_situacao: Optional[str] = None
    cancelada: int
    denegada: int
    numero_recibo: Optional[str] = None
    status: str
    numero_protocolo_autorizacao: Optional[str] = None
    xml_recibo_emissao: Optional[str] = None
    xml_cancelamento: Optional[str] = None
    chave_acesso: Optional[str] = None
    tipo_emissao: Optional[int] = None
    xml: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    destinatario_cpf_cnpj: str
    destinatario_nome: str
    destinatario_endereco: Optional[str] = None
    destinatario_numero: Optional[str] = None
    destinatario_complemento: Optional[str] = None
    destinatario_bairro: Optional[str] = None
    destinatario_codigo_cidade: Optional[str] = None
    destinatario_nome_cidade: Optional[str] = None
    destinatario_uf: Optional[str] = None
    destinatario_cep: Optional[str] = None
    destinatario_codigo_pais: Optional[str] = None
    destinatario_nome_pais: Optional[str] = None
    destinatario_telefone: Optional[str] = None
    destinatario_indicador_ie: Optional[str] = None
    destinatario_ie: Optional[str] = None
    destinatario_inscricao_suframa: Optional[str] = None
    destinatario_inscricao_municipal: Optional[str] = None
    destinatario_email: Optional[str] = None
    produto_id: int
    codigo_ean: Optional[str] = None
    produto_nome: str
    ncm: Optional[str] = None
    cst_csosn: Optional[str] = None
    unidade_comercial: Optional[str] = None
    quantidade_comercial: Optional[Decimal] = None
    valor_unitario_comercial: Optional[Decimal] = None
    valor_total_produto: Optional[Decimal] = None
    icms_percentual_reducao_base: Optional[Decimal] = None
    icmsst_valor: Optional[Decimal] = None
    icmsst_retido_base_calculo: Optional[Decimal] = None
    icmsst_retido_valor: Optional[Decimal] = None
    icms_desoneracao_motivo: Optional[str] = None
    icms_desoneracao_valor: Optional[Decimal] = None
    icms_operacao_valor: Optional[Decimal] = None
    icms_diferimento_percentual: Optional[Decimal] = None
    icms_diferimento_valor: Optional[Decimal] = None
    icms_valor: Optional[Decimal] = None
    ipi_valor: Optional[Decimal] = None
    ipi_aliquota: Optional[Decimal] = None
    ipi_enquadramento: Optional[str] = None
    total_tributos: Optional[Decimal] = None
    natureza_item: Optional[str] = None
    natureza: Optional[str] = None
    cest: Optional[str] = None
    especifico: Optional[str] = None
    cfop: Optional[str] = None
    icms_aliquota: Optional[Decimal] = None
    icmsst_mva: Optional[Decimal] = None
    icmsst_percentual_reducao_base: Optional[Decimal] = None
    icmsst_aliquota: Optional[Decimal] = None
    pis_cst: Optional[str] = None
    pis_base_calculo: Optional[Decimal] = None
    pis_aliquota: Optional[Decimal] = None
    pis_valor: Optional[Decimal] = None
    cofins_cst: Optional[str] = None
    cofins_valor: Optional[Decimal] = None
    cofins_aliquota: Optional[Decimal] = None
    icmsdifal_base_calculo_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_fcp_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_icms_uf_destino: Optional[Decimal] = None
    icmsdifal_percentual_icms_interestadual: Optional[Decimal] = None
    icmsdifal_percentual_provisorio_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_fcp_uf_destino: Optional[Decimal] = None
    icmsdifal_valor_icms_uf_remetente: Optional[Decimal] = None
    ipi_cst: Optional[str] = None
    icmsst_base_calculo: Optional[Decimal] = None
    ipi_base_calculo: Optional[Decimal] = None
    icms_base_calculo: Optional[Decimal] = None
    icms_aliquota_credito_simples_nacional: Optional[Decimal] = None
    icms_valor_credito_simples_nacional: Optional[Decimal] = None
    unidade_tributavel: Optional[str] = None
    quantidade_tributavel: Optional[Decimal] = None
    valor_unitario_tributavel: Optional[Decimal] = None
    valor_total_frete: Optional[Decimal] = None
    valor_total_seguro: Optional[Decimal] = None
    valor_total_desconto: Optional[Decimal] = None
    valor_total_outras_despesas: Optional[Decimal] = None
    indicador_total: int
    origem: str
    icms_modalidade_base_calculo: Optional[str] = None
    icmsst_modalidade_base_calculo: Optional[str] = None
    item_total_bruto: Optional[Decimal] = None
    item_desconto: Decimal
    item_outras_despesas: Decimal
    item_total_liquido: Optional[Decimal] = None
    item_total_liquido_cancelado: Optional[Decimal] = None

@dataclass
class ViewMemoriaVendas:
    """Tabela: view_memoria_vendas (Linhas aprox: None)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    nfe_id: Optional[int] = None
    nfse_id: Optional[int] = None
    observacao: Optional[str] = None
    api_cliente_cpf: Optional[str] = None
    api_cliente_nome: Optional[str] = None
    api_faturar: Optional[str] = None
    api_status: Optional[str] = None
    api_app_name: Optional[str] = None
    api_data_hora_venda: Optional[datetime] = None
    desconto_valor: Decimal
    desconto_percentual: Decimal
    acrescimo_valor: Decimal
    acrescimo_percentual: Decimal
    percentual_comissao_venda: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    api_guid: str
    api_data_hora_lancamento: Optional[datetime] = None
    api_device_id: str
    cancelada: int
    usuario_lancamento_id: Optional[int] = None
    bloqueada: int
    parent_guid: Optional[str] = None
    usuario_cancelamento_id: Optional[int] = None
    data_hora_cancelamento: Optional[datetime] = None
    numero_documento: Optional[str] = None
    numero_caixa: Optional[str] = None
    tipo_preco_id: Optional[int] = None
    integracao_delivery: Optional[str] = None
    entregador_id: Optional[int] = None
    assistencia_id: Optional[int] = None
    caixa_funcoes_id: Optional[int] = None
    indicador_id: Optional[int] = None
    marketplace_pedido_id: Optional[int] = None
    atendente_mesa: Optional[str] = None
    comissao_entregador: Optional[Decimal] = None
    comissao_indicador: Optional[Decimal] = None
    numero_mesa: Optional[str] = None
    numero_comanda: Optional[str] = None
    origem_venda: Optional[str] = None
    quantidade_pessoas: Optional[int] = None
    quantidade_comandas: Optional[int] = None
    tipo_lancamento: str
    orcamento_id: Optional[int] = None
    orcamento_competencia: Optional[date] = None
    numero_pre_venda: Optional[str] = None
    cliente_nome: str
    cliente_tipo_cliente_id: int
    vendedor_nome: str
    venda_empresa_nome: str
    venda_empresa_nome_fantasia: str
    venda_empresa_razao_social: str
    tipo_comissao: str
    venda_item_id: int
    produto_empresa_grade_id: int
    produto_venda_quantidade: Decimal
    produto_venda_preco: Decimal
    comissao: Optional[Decimal] = None
    desconto_valor_item: Decimal
    acrescimo_valor_item: Decimal
    item_cancelado: Optional[datetime] = None
    atendente_item: Optional[int] = None
    comissao_atendente: Optional[Decimal] = None
    comissao_carta_produto: Optional[Decimal] = None
    comissao_carta_produto_tipo: Optional[str] = None
    cobrar_taxa_servico: Optional[int] = None
    data_venda: Optional[date] = None
    data_hora_venda: Optional[datetime] = None
    caixa_data: Optional[date] = None
    turno: Optional[int] = None
    operador_id: Optional[int] = None
    indicador_nome: Optional[str] = None
    produto_id: Optional[int] = None
    produto_nome: Optional[str] = None
    produto_tipo_produto: Optional[str] = None
    produto_servico: Optional[int] = None
    produto_nome_completo: Optional[str] = None
    produto_grade_descricao: Optional[str] = None
    produto_grade_estoque: Optional[Decimal] = None
    produto_empresa_id: Optional[int] = None
    produto_grade_deleted_at: Optional[datetime] = None
    grupo_id: Optional[int] = None
    grupo_nome: Optional[str] = None
    fabricante_id: Optional[int] = None
    fabricante_nome: Optional[str] = None
    mes_venda: Optional[str] = None
    ano_venda: Optional[str] = None
    mes_ano_venda: Optional[str] = None
    item_total: Optional[Decimal] = None
    item_total_real: Optional[Decimal] = None
    item_total_compra: Optional[Decimal] = None
    item_total_lucro: Optional[Decimal] = None
    item_total_desconto: Optional[Decimal] = None
    item_total_acrescimo: Optional[Decimal] = None

@dataclass
class ViewMemoriaVendasAgrupado:
    """Tabela: view_memoria_vendas_agrupado (Linhas aprox: None)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    nfe_id: Optional[int] = None
    nfse_id: Optional[int] = None
    observacao: Optional[str] = None
    api_cliente_cpf: Optional[str] = None
    api_cliente_nome: Optional[str] = None
    api_faturar: Optional[str] = None
    api_status: Optional[str] = None
    api_app_name: Optional[str] = None
    api_data_hora_venda: Optional[datetime] = None
    desconto_valor: Decimal
    desconto_percentual: Decimal
    acrescimo_valor: Decimal
    acrescimo_percentual: Decimal
    percentual_comissao_venda: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    api_guid: str
    api_data_hora_lancamento: Optional[datetime] = None
    api_device_id: str
    cancelada: int
    usuario_lancamento_id: Optional[int] = None
    bloqueada: int
    parent_guid: Optional[str] = None
    usuario_cancelamento_id: Optional[int] = None
    data_hora_cancelamento: Optional[datetime] = None
    numero_documento: Optional[str] = None
    numero_caixa: Optional[str] = None
    tipo_preco_id: Optional[int] = None
    integracao_delivery: Optional[str] = None
    entregador_id: Optional[int] = None
    assistencia_id: Optional[int] = None
    caixa_funcoes_id: Optional[int] = None
    indicador_id: Optional[int] = None
    marketplace_pedido_id: Optional[int] = None
    atendente_mesa: Optional[str] = None
    comissao_entregador: Optional[Decimal] = None
    comissao_indicador: Optional[Decimal] = None
    numero_mesa: Optional[str] = None
    numero_comanda: Optional[str] = None
    origem_venda: Optional[str] = None
    quantidade_pessoas: Optional[int] = None
    quantidade_comandas: Optional[int] = None
    tipo_lancamento: str
    orcamento_id: Optional[int] = None
    orcamento_competencia: Optional[date] = None
    numero_pre_venda: Optional[str] = None
    cliente_nome: str
    cliente_tipo_cliente_id: int
    vendedor_nome: str
    venda_empresa_nome: str
    venda_empresa_nome_fantasia: str
    venda_empresa_razao_social: str
    tipo_comissao: str
    venda_item_id: int
    produto_empresa_grade_id: int
    produto_venda_quantidade: Decimal
    produto_venda_preco: Decimal
    comissao: Optional[Decimal] = None
    desconto_valor_item: Decimal
    acrescimo_valor_item: Decimal
    item_cancelado: Optional[datetime] = None
    atendente_item: Optional[int] = None
    comissao_atendente: Optional[Decimal] = None
    cobrar_taxa_servico: Optional[int] = None
    produto_id: Optional[int] = None
    produto_nome: Optional[str] = None
    produto_tipo_produto: Optional[str] = None
    produto_servico: Optional[int] = None
    produto_nome_completo: Optional[str] = None
    produto_grade_descricao: Optional[str] = None
    produto_grade_estoque: Optional[Decimal] = None
    produto_empresa_id: Optional[int] = None
    produto_grade_deleted_at: Optional[datetime] = None
    grupo_id: Optional[int] = None
    grupo_nome: Optional[str] = None
    fabricante_id: Optional[int] = None
    fabricante_nome: Optional[str] = None
    mes_venda: Optional[str] = None
    ano_venda: Optional[str] = None
    mes_ano_venda: Optional[str] = None
    item_total: Optional[Decimal] = None
    item_total_real: Optional[Decimal] = None
    item_total_compra: Optional[Decimal] = None
    item_total_lucro: Optional[Decimal] = None
    item_total_desconto: Optional[Decimal] = None
    item_total_acrescimo: Optional[Decimal] = None
    data_venda: Optional[date] = None
    data_hora_venda: Optional[datetime] = None
    caixa_data: Optional[date] = None
    turno: Optional[int] = None
    operador_id: Optional[int] = None
    indicador_nome: Optional[str] = None

@dataclass
class ViewMemoriaVendasPagamento:
    """Tabela: view_memoria_vendas_pagamento (Linhas aprox: None)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    nfe_id: Optional[int] = None
    nfse_id: Optional[int] = None
    observacao: Optional[str] = None
    api_cliente_cpf: Optional[str] = None
    api_cliente_nome: Optional[str] = None
    api_faturar: Optional[str] = None
    api_status: Optional[str] = None
    api_app_name: Optional[str] = None
    api_data_hora_venda: Optional[datetime] = None
    desconto_valor: Decimal
    desconto_percentual: Decimal
    acrescimo_valor: Decimal
    acrescimo_percentual: Decimal
    percentual_comissao_venda: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    api_guid: str
    api_data_hora_lancamento: Optional[datetime] = None
    api_device_id: str
    cancelada: int
    usuario_lancamento_id: Optional[int] = None
    bloqueada: int
    parent_guid: Optional[str] = None
    usuario_cancelamento_id: Optional[int] = None
    data_hora_cancelamento: Optional[datetime] = None
    numero_documento: Optional[str] = None
    numero_caixa: Optional[str] = None
    tipo_preco_id: Optional[int] = None
    integracao_delivery: Optional[str] = None
    entregador_id: Optional[int] = None
    assistencia_id: Optional[int] = None
    caixa_funcoes_id: Optional[int] = None
    indicador_id: Optional[int] = None
    marketplace_pedido_id: Optional[int] = None
    atendente_mesa: Optional[str] = None
    comissao_entregador: Optional[Decimal] = None
    comissao_indicador: Optional[Decimal] = None
    numero_mesa: Optional[str] = None
    numero_comanda: Optional[str] = None
    origem_venda: Optional[str] = None
    quantidade_pessoas: Optional[int] = None
    quantidade_comandas: Optional[int] = None
    tipo_lancamento: str
    orcamento_id: Optional[int] = None
    orcamento_competencia: Optional[date] = None
    numero_pre_venda: Optional[str] = None
    data_venda: Optional[date] = None
    data_hora_venda: Optional[datetime] = None
    caixa_data: Optional[date] = None
    turno: Optional[int] = None
    operador_id: Optional[int] = None
    indicador_nome: Optional[str] = None
    cliente_nome: str
    cliente_tipo_cliente_id: int
    vendedor_nome: str
    venda_empresa_nome: str
    venda_empresa_nome_fantasia: str
    venda_empresa_razao_social: str
    tipo_comissao: str
    vencimento: date
    valor_parcela_financeiro: Decimal
    financeiro_parcela_id: int
    banco_id: Optional[int] = None
    parcela: Optional[str] = None
    parcela_cancelada: int
    forma_pagamento_id: int
    forma_pagamento_nome: str
    forma_pagamento_tipo: str
    forma_pagamento_exibir: int
    forma_pagamento_saldo_caixa: int
    forma_pagamento_codigo_nfce: str
    forma_pagamento_ordem: Optional[int] = None
    cartao_credito_id: Optional[int] = None
    cartao_nome: Optional[str] = None
    cartao_tipo: Optional[str] = None
    cartao_taxa_admin: Optional[Decimal] = None
    valor_parcela: Decimal
    valor_parcela_corrigido: Optional[Decimal] = None
    valor_pago: Decimal
    valor_pendente: Optional[Decimal] = None

@dataclass
class ViewMemoriaVendasTodas:
    """Tabela: view_memoria_vendas_todas (Linhas aprox: None)"""
    id: int
    empresa_id: int
    cliente_id: int
    funcionario_id: int
    nfe_id: Optional[int] = None
    nfse_id: Optional[int] = None
    observacao: Optional[str] = None
    api_cliente_cpf: Optional[str] = None
    api_cliente_nome: Optional[str] = None
    api_faturar: Optional[str] = None
    api_status: Optional[str] = None
    api_app_name: Optional[str] = None
    api_data_hora_venda: Optional[datetime] = None
    desconto_valor: Decimal
    desconto_percentual: Decimal
    acrescimo_valor: Decimal
    acrescimo_percentual: Decimal
    percentual_comissao_venda: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    api_guid: str
    api_data_hora_lancamento: Optional[datetime] = None
    api_device_id: str
    cancelada: int
    usuario_lancamento_id: Optional[int] = None
    bloqueada: int
    parent_guid: Optional[str] = None
    usuario_cancelamento_id: Optional[int] = None
    data_hora_cancelamento: Optional[datetime] = None
    numero_documento: Optional[str] = None
    numero_caixa: Optional[str] = None
    tipo_preco_id: Optional[int] = None
    integracao_delivery: Optional[str] = None
    entregador_id: Optional[int] = None
    assistencia_id: Optional[int] = None
    caixa_funcoes_id: Optional[int] = None
    indicador_id: Optional[int] = None
    marketplace_pedido_id: Optional[int] = None
    atendente_mesa: Optional[str] = None
    comissao_entregador: Optional[Decimal] = None
    comissao_indicador: Optional[Decimal] = None
    numero_mesa: Optional[str] = None
    numero_comanda: Optional[str] = None
    origem_venda: Optional[str] = None
    quantidade_pessoas: Optional[int] = None
    quantidade_comandas: Optional[int] = None
    tipo_lancamento: str
    orcamento_id: Optional[int] = None
    orcamento_competencia: Optional[date] = None
    numero_pre_venda: Optional[str] = None
    cliente_nome: str
    cliente_tipo_cliente_id: int
    vendedor_nome: str
    venda_empresa_nome: str
    venda_empresa_nome_fantasia: str
    venda_empresa_razao_social: str
    tipo_comissao: str
    venda_item_id: int
    produto_empresa_grade_id: int
    produto_venda_quantidade: Decimal
    produto_venda_preco: Decimal
    comissao: Optional[Decimal] = None
    desconto_valor_item: Decimal
    acrescimo_valor_item: Decimal
    item_cancelado: Optional[datetime] = None
    atendente_item: Optional[int] = None
    comissao_atendente: Optional[Decimal] = None
    comissao_carta_produto: Optional[Decimal] = None
    comissao_carta_produto_tipo: Optional[str] = None
    cobrar_taxa_servico: Optional[int] = None
    data_venda: Optional[date] = None
    data_hora_venda: Optional[datetime] = None
    caixa_data: Optional[date] = None
    turno: Optional[int] = None
    operador_id: Optional[int] = None
    indicador_nome: Optional[str] = None
    produto_id: Optional[int] = None
    produto_nome: Optional[str] = None
    produto_tipo_produto: Optional[str] = None
    produto_servico: Optional[int] = None
    produto_nome_completo: Optional[str] = None
    produto_grade_descricao: Optional[str] = None
    produto_grade_estoque: Optional[Decimal] = None
    produto_empresa_id: Optional[int] = None
    produto_grade_deleted_at: Optional[datetime] = None
    grupo_id: Optional[int] = None
    grupo_nome: Optional[str] = None
    fabricante_id: Optional[int] = None
    fabricante_nome: Optional[str] = None
    mes_venda: Optional[str] = None
    ano_venda: Optional[str] = None
    mes_ano_venda: Optional[str] = None
    item_total: Optional[Decimal] = None
    item_total_real: Optional[Decimal] = None
    item_total_compra: Optional[Decimal] = None
    item_total_lucro: Optional[Decimal] = None
    item_total_desconto: Optional[Decimal] = None
    item_total_acrescimo: Optional[Decimal] = None

@dataclass
class ViewVendaFinanceiro:
    """Tabela: view_venda_financeiro (Linhas aprox: None)"""
    venda_id: Optional[int] = None
    valor_parcela: Optional[Decimal] = None
    valor_parcela_corrigido: Optional[Decimal] = None
    valor_pago: Decimal
    valor_pendente: Optional[Decimal] = None

@dataclass
class VinculosFiscais:
    """Tabela: vinculos_fiscais (Linhas aprox: 8)"""
    id: int
    nome_vinculo: str
    tipo_item: Optional[str] = None
    tipo_vinculo: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    indicador_finalidade: Optional[str] = None
    vinculo_padrao: int
    vinculo_padrao_servico: int

@dataclass
class VinculosFiscaisConfiguracoes:
    """Tabela: vinculos_fiscais_configuracoes (Linhas aprox: 40)"""
    id: int
    vinculo_fiscal_id: int
    grupo: Optional[str] = None
    cfop_nfe_entrada: Optional[str] = None
    cfop_nfce_saida: Optional[str] = None
    cfop_nfe_saida: Optional[str] = None
    cfop_nfce_entrada: Optional[str] = None
    natureza: Optional[str] = None
    uf_origem: str
    uf_destino: Optional[str] = None
    cst_csosn: Optional[str] = None
    icms_modalidade_base: Optional[str] = None
    icms_acrescimo: Optional[Decimal] = None
    icms_st_aliquota: Optional[Decimal] = None
    icms_reducao: Optional[Decimal] = None
    icms_st_modalidade_base: Optional[str] = None
    icms_st_mva: Optional[Decimal] = None
    icms_st_reducao: Optional[Decimal] = None
    ipi_saida: Optional[str] = None
    ipi_saida_aliquota: Optional[Decimal] = None
    ipi_saida_enquadramento: Optional[str] = None
    pis_saida: Optional[str] = None
    pis_saida_aliquota: Optional[Decimal] = None
    cofins_saida: Optional[str] = None
    cofins_saida_aliquota: Optional[Decimal] = None
    icms_valor_pauta: Optional[Decimal] = None
    ipi_entrada: Optional[str] = None
    ipi_entrada_aliquota: Optional[Decimal] = None
    ipi_entrada_enquadramento: Optional[str] = None
    pis_entrada: Optional[int] = None
    pis_entrada_aliquota: Optional[Decimal] = None
    cofins_entrada: Optional[str] = None
    cofins_entrada_aliquota: Optional[Decimal] = None
    especifico: Optional[str] = None
    nfe_natureza_operacao_texto_saida: Optional[str] = None
    nfce_natureza_operacao_texto_saida: Optional[str] = None
    icms_saida_origem: Optional[int] = None
    icms_percentual_diferimento: Optional[Decimal] = None
    nfce_aliquota: Optional[Decimal] = None
    servico_iss_saida: Decimal
    servico_csll_saida: Decimal
    servico_inss_saida: Decimal
    servico_ir_saida: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    regime_tributario: Optional[str] = None
    modelo: int
    icms_normal_aliquota: Decimal
    icms_motivo_desoneracao: Optional[str] = None
    icms_valor_desoneracao: Optional[Decimal] = None
    zerar_icms: int
    ibs_cbs_cst: Optional[str] = None
    ibs_cbs_cclass_trib: Optional[str] = None
    ibs_aliquota: Optional[Decimal] = None
    cbs_aliquota: Optional[Decimal] = None
    ibs_cbs_cst_id: Optional[int] = None
    somar_ipi_icmsst_base: int

@dataclass
class VinculosFiscaisNcm:
    """Tabela: vinculos_fiscais_ncm (Linhas aprox: 7)"""
    id: int
    vinculo_fiscal_id: int
    ncm: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class VinculosNcm:
    """Tabela: vinculos_ncm (Linhas aprox: 0)"""
    id: int
    vinculo_id: int
    ncm_codigo: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

@dataclass
class WhatsappDevices:
    """Tabela: whatsapp_devices (Linhas aprox: 0)"""
    id: int
    device_id: str
    status: str
    last_updated_at: datetime
    data: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

