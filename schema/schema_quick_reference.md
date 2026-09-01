# Mapeamento Completo do Banco de Dados: softcoms_softcomshop_lanchoneteerestaurantepotira
**Gerado em:** 2026-08-31 17:22:36 | **Tabelas:** 459 | **Colunas:** 6600 | **FKs:** 518

## Indice de Tabelas
| Tabela | Tipo | Registros Aprox. | Colunas | Chave Primaria |
| :--- | :--- | :--- | :--- | :--- |
| agenda_evento | BASE TABLE | 0 | 20 | id |
| agenda_evento_arquivo | BASE TABLE | 0 | 11 | id |
| agenda_evento_atendimento | BASE TABLE | 0 | 6 | id |
| agenda_evento_participante_interno | BASE TABLE | 0 | 6 | id |
| assistencia | BASE TABLE | 0 | 14 | id |
| assistencia_otica_itens | BASE TABLE | 0 | 17 | id |
| assistencia_otica_receitas | BASE TABLE | 0 | 25 | id |
| assistencia_otica_receitas_configuracoes | BASE TABLE | 0 | 26 | id |
| assistencia_padrao_equipamento | BASE TABLE | 0 | 12 | id |
| assistencia_padrao_laudo | BASE TABLE | 0 | 8 | id |
| atendimento | BASE TABLE | 0 | 21 | id |
| atendimento_config | BASE TABLE | 0 | 7 | id |
| atendimento_lista | BASE TABLE | 0 | 12 | id |
| atendimento_lista_notificacao_controle | BASE TABLE | 0 | 5 | id |
| atestados_termos | BASE TABLE | 11 | 8 | id |
| auditoria | BASE TABLE | 0 | 9 | id |
| autopeca_checklist | BASE TABLE | 0 | 4 | id |
| autopeca_checklist_respostas | BASE TABLE | 0 | 4 | id |
| autopecas_checklist_categoria | BASE TABLE | 0 | 8 | id |
| autopecas_checklist_item | BASE TABLE | 0 | 11 | id |
| azure_keys | BASE TABLE | 0 | 21 | id |
| bairro | BASE TABLE | 14 | 7 | id |
| balanco | BASE TABLE | 0 | 9 | id |
| balanco_item | BASE TABLE | 26 | 9 | id |
| banco | VIEW | 0 | 7 | - |
| bandeira | BASE TABLE | 28 | 6 | id |
| box_prisma | BASE TABLE | 0 | 5 | id |
| cache_locks | BASE TABLE | 0 | 3 | key |
| caixa_funcoes | BASE TABLE | 0 | 13 | id |
| caixa_funcoes_digitacao | BASE TABLE | 0 | 10 | id |
| caixa_funcoes_digitacao_bandeiras | BASE TABLE | 0 | 10 | id |
| cartao_alias | BASE TABLE | 0 | 5 | id |
| cartao_credito | BASE TABLE | 11 | 15 | id |
| centro_custo | BASE TABLE | 0 | 5 | id |
| cfop | BASE TABLE | 0 | 11 | id |
| checklist_photos | BASE TABLE | 0 | 15 | id |
| cheque | BASE TABLE | 0 | 15 | id |
| cheque_motivo | BASE TABLE | 0 | 6 | id |
| cheque_movimento | BASE TABLE | 0 | 9 | id |
| cliente | BASE TABLE | 1 | 32 | id |
| cliente_condicao_pagamento | BASE TABLE | 0 | 6 | id |
| cliente_condicao_pagamento_parents | BASE TABLE | 0 | 3 | id |
| cliente_convenio | BASE TABLE | 0 | 7 | id |
| cliente_credito | BASE TABLE | 0 | 12 | id |
| cliente_imagens | BASE TABLE | 0 | 12 | id |
| cliente_ocorrencia | BASE TABLE | 0 | 14 | id |
| cliente_tag_classificacao | BASE TABLE | 0 | 6 | id |
| cliente_veiculo | BASE TABLE | 0 | 16 | id |
| cnpjs_autorizados | BASE TABLE | 0 | 6 | id |
| cobranca_parcelas | BASE TABLE | 0 | 31 | id |
| cobranca_webhooks | BASE TABLE | 0 | 5 | id |
| codigo_anp | VIEW | 0 | 6 | - |
| comissoes | BASE TABLE | 0 | 7 | id |
| compra | BASE TABLE | 62 | 79 | id |
| compra_destinatario | BASE TABLE | 62 | 24 | id |
| compra_emitente | BASE TABLE | 62 | 22 | id |
| compra_item | BASE TABLE | 347 | 86 | id |
| compra_item_grade | BASE TABLE | 267 | 7 | id |
| compra_observacao | BASE TABLE | 0 | 6 | id |
| condutor | BASE TABLE | 0 | 6 | id |
| configuracao_bancaria | BASE TABLE | 0 | 31 | id |
| configuracao_bancaria_ocorrencia | BASE TABLE | 0 | 9 | id |
| consignacao_devolucao | BASE TABLE | 0 | 10 | id |
| consignacao_devolucao_item | BASE TABLE | 0 | 10 | id |
| consignacao_requisicao | BASE TABLE | 0 | 11 | id |
| consignacao_requisicao_item | BASE TABLE | 0 | 10 | id |
| conta | BASE TABLE | 3 | 14 | id |
| conta_banco | BASE TABLE | 0 | 47 | id |
| conta_cartao | BASE TABLE | 0 | 9 | id |
| conta_softcompay | BASE TABLE | 0 | 18 | id |
| contador | BASE TABLE | 0 | 12 | id |
| contato | BASE TABLE | 0 | 16 | id |
| contrato_modelo | BASE TABLE | 0 | 6 | id |
| contrato_servico | BASE TABLE | 0 | 15 | id |
| contrato_servico_item | BASE TABLE | 0 | 14 | id |
| cotacao | BASE TABLE | 0 | 18 | id |
| cotacao_item | BASE TABLE | 0 | 9 | id |
| credenciadora | BASE TABLE | 1 | 11 | id |
| cte | BASE TABLE | 0 | 49 | id |
| cte_carga | BASE TABLE | 0 | 9 | id |
| cte_carta_correcao | BASE TABLE | 0 | 11 | id |
| cte_componente_frete | BASE TABLE | 0 | 8 | id |
| cte_documento_nfe | BASE TABLE | 0 | 9 | id |
| cte_documento_outro | BASE TABLE | 0 | 15 | id |
| cte_empresa_config | BASE TABLE | 0 | 9 | empresa_id |
| cte_evento | BASE TABLE | 0 | 14 | id |
| cte_icms | BASE TABLE | 0 | 23 | id |
| cte_modal_rodoviario | BASE TABLE | 0 | 6 | id |
| cte_occ | BASE TABLE | 0 | 13 | id |
| cte_participante | BASE TABLE | 0 | 24 | id |
| cte_quantidade | BASE TABLE | 0 | 9 | id |
| cte_tabela_frete | BASE TABLE | 0 | 13 | id |
| cte_tabela_frete_componente | BASE TABLE | 0 | 8 | id |
| documento_fiscal_csc | BASE TABLE | 0 | 8 | id |
| empresa | BASE TABLE | 1 | 40 | id |
| empresa_balanca_configuracao | BASE TABLE | 0 | 8 | id |
| empresa_email | BASE TABLE | 0 | 12 | id |
| empresa_mfe_adquirente | BASE TABLE | 0 | 9 | id |
| empresa_mfe_pos | BASE TABLE | 0 | 8 | id |
| empresa_venda_configuracao | BASE TABLE | 1 | 9 | id |
| endereco | BASE TABLE | 16 | 21 | id |
| equipamento | BASE TABLE | 0 | 5 | id |
| etiqueta_configuracao | BASE TABLE | 10 | 22 | id |
| etiqueta_item | BASE TABLE | 0 | 7 | id |
| fabricante | BASE TABLE | 0 | 5 | id |
| failed_jobs | BASE TABLE | 0 | 6 | id |
| fator_acrescimo_configuracao | BASE TABLE | 0 | 7 | id |
| financeiro | BASE TABLE | 116 | 26 | id |
| financeiro_categoria | BASE TABLE | 2 | 17 | id |
| financeiro_categoria_conta_dre | BASE TABLE | 32 | 5 | id |
| financeiro_categoria_segmento | VIEW | 0 | 17 | - |
| financeiro_centro_custo | BASE TABLE | 0 | 6 | - |
| financeiro_condicao_pagamento | BASE TABLE | 0 | 8 | id |
| financeiro_condicao_pagamento_parcela | BASE TABLE | 0 | 8 | id |
| financeiro_extrato_bancario | BASE TABLE | 0 | 22 | id |
| financeiro_parcela | BASE TABLE | 116 | 60 | id |
| financeiro_parcela_arquivo | BASE TABLE | 0 | 11 | id |
| financeiro_parcela_pagamento | BASE TABLE | 23 | 16 | id |
| financeiro_parcela_pix | BASE TABLE | 0 | 28 | id |
| financeiro_parcela_pix_billing | BASE TABLE | 0 | 18 | id |
| financeiro_troco | BASE TABLE | 0 | 11 | id |
| forma_pagamento | BASE TABLE | 28 | 19 | id |
| fornecedor | BASE TABLE | 14 | 16 | id |
| fornecedor_boleto | BASE TABLE | 0 | 7 | id |
| funcionario | BASE TABLE | 2 | 23 | id |
| gestao_estoque_configuracao | BASE TABLE | 0 | 8 | id |
| gestao_estoque_consolidado_mensal | BASE TABLE | 0 | 16 | id |
| grupo | BASE TABLE | 4 | 31 | id |
| grupo_adicional | BASE TABLE | 0 | 8 | id |
| grupo_marketplace | BASE TABLE | 0 | 11 | id |
| indicador | BASE TABLE | 0 | 14 | id |
| integracao_log | BASE TABLE | 0 | 9 | id |
| laboratorio | BASE TABLE | 0 | 11 | id |
| manifesto_documento_eletronico | BASE TABLE | 0 | 48 | id |
| manifesto_documento_eletronico_autorizado_xml | BASE TABLE | 0 | 7 | id |
| manifesto_documento_eletronico_carga_descarga | BASE TABLE | 0 | 10 | id |
| manifesto_documento_eletronico_documento | BASE TABLE | 0 | 12 | id |
| manifesto_documento_eletronico_documento_unidade_transporte | BASE TABLE | 0 | 12 | id |
| manifesto_documento_eletronico_emitente | BASE TABLE | 0 | 20 | id |
| manifesto_documento_eletronico_inclusao | BASE TABLE | 0 | 7 | id |
| manifesto_documento_eletronico_lacre | BASE TABLE | 0 | 10 | id |
| manifesto_documento_eletronico_pagamento_frete_lancamentos | BASE TABLE | 0 | 12 | id |
| manifesto_documento_eletronico_pagamentos_frete | BASE TABLE | 0 | 13 | id |
| manifesto_documento_eletronico_percurso | BASE TABLE | 0 | 7 | id |
| manifesto_documento_eletronico_produto_predominante | BASE TABLE | 0 | 15 | id |
| manifesto_documento_eletronico_responsavel_tecnico | BASE TABLE | 0 | 11 | id |
| manifesto_documento_eletronico_seguro | BASE TABLE | 0 | 12 | id |
| manifesto_documento_eletronico_veiculo | BASE TABLE | 0 | 24 | id |
| manifesto_documento_eletronico_veiculo_agencia | BASE TABLE | 0 | 10 | id |
| manifesto_documento_eletronico_veiculo_agencia_vale_pedagio | BASE TABLE | 0 | 12 | id |
| manifesto_documento_eletronico_veiculo_condutor | BASE TABLE | 0 | 8 | id |
| manifesto_documento_eletronico_veiculo_perigoso | BASE TABLE | 0 | 12 | id |
| marca_equipamento | BASE TABLE | 0 | 6 | id |
| marca_veiculo | BASE TABLE | 47 | 5 | id |
| marketplace_categoria | BASE TABLE | 0 | 11 | id |
| marketplace_config | BASE TABLE | 1 | 12 | id |
| marketplace_gestor_produto | BASE TABLE | 0 | 14 | id |
| marketplace_gestor_produto_item | BASE TABLE | 0 | 11 | id |
| marketplace_grupo_empresa | BASE TABLE | 0 | 7 | id |
| marketplace_hub_saleschannel | BASE TABLE | 0 | 9 | id |
| marketplace_pagamento_conversao | BASE TABLE | 8 | 6 | id |
| marketplace_pedido | BASE TABLE | 0 | 24 | id |
| marketplace_produto | BASE TABLE | 0 | 26 | id |
| marketplace_produto_grade | BASE TABLE | 0 | 17 | id |
| marketplace_vinculado | BASE TABLE | 0 | 12 | id |
| mdfe_serie | BASE TABLE | 0 | 11 | id |
| medico | BASE TABLE | 0 | 7 | id |
| menu_favorito | BASE TABLE | 0 | 9 | id |
| meu_lucro_visao_geral | BASE TABLE | 0 | 57 | id |
| migrations | BASE TABLE | 1299 | 2 | - |
| modulo | BASE TABLE | 41 | 14 | id |
| modulo_configuracao | BASE TABLE | 6 | 7 | id |
| movimentacao | BASE TABLE | 0 | 20 | id |
| movimentacao_item | BASE TABLE | 26 | 10 | id |
| nfce_cfop | BASE TABLE | 9 | 6 | id |
| nfce_serie | BASE TABLE | 0 | 12 | id |
| nfe_cest | VIEW | 0 | 7 | - |
| nfe_cidade | BASE TABLE | 5640 | 12 | id |
| nfe_classificacao_tributaria | VIEW | 0 | 22 | - |
| nfe_codigo_genero | BASE TABLE | 100 | 6 | id |
| nfe_cofins | BASE TABLE | 33 | 7 | id |
| nfe_cst | BASE TABLE | 25 | 9 | id |
| nfe_especifico | BASE TABLE | 4 | 6 | id |
| nfe_finalidade | BASE TABLE | 0 | 6 | id |
| nfe_grupo | BASE TABLE | 110 | 8 | id |
| nfe_grupo_tensao | BASE TABLE | 14 | 6 | id |
| nfe_ibpt | BASE TABLE | 0 | 11 | - |
| nfe_icms_aliquota | VIEW | 0 | 10 | - |
| nfe_icms_st | BASE TABLE | 4 | 6 | id |
| nfe_informacoes_adicionais | BASE TABLE | 0 | 8 | id |
| nfe_mensagem_humanizada | BASE TABLE | 4 | 10 | id |
| nfe_modbaseicms | BASE TABLE | 7 | 7 | id |
| nfe_motivo_desoneracao | BASE TABLE | 45 | 7 | id |
| nfe_natureza | VIEW | 0 | 10 | - |
| nfe_origem | BASE TABLE | 9 | 6 | id |
| nfe_pais | VIEW | 0 | 6 | - |
| nfe_pis | BASE TABLE | 34 | 7 | id |
| nfe_serie | BASE TABLE | 1 | 11 | id |
| nfe_situacao_ipi | BASE TABLE | 14 | 8 | id |
| nfe_tipo_emissao | BASE TABLE | 0 | 6 | id |
| nfe_tipo_item | BASE TABLE | 12 | 6 | id |
| nfe_tipo_servico | VIEW | 0 | 10 | - |
| nfse_aliquota_padrao | BASE TABLE | 1 | 11 | id |
| nfse_codigo_servico_item | BASE TABLE | 531 | 8 | id |
| nfse_exigibilidade_iss | BASE TABLE | 7 | 5 | id |
| nfse_natureza | BASE TABLE | 6 | 8 | id |
| nfse_regime_especial_tributacao | BASE TABLE | 7 | 6 | id |
| nfse_serie | BASE TABLE | 0 | 11 | id |
| nota_fiscal_eletronica | BASE TABLE | 76 | 89 | id |
| nota_fiscal_eletronica_autorizado | BASE TABLE | 0 | 7 | id |
| nota_fiscal_eletronica_carta_correcao | BASE TABLE | 0 | 11 | id |
| nota_fiscal_eletronica_cobranca | BASE TABLE | 0 | 8 | id |
| nota_fiscal_eletronica_destinatario | BASE TABLE | 48 | 26 | id |
| nota_fiscal_eletronica_emitente | BASE TABLE | 48 | 25 | id |
| nota_fiscal_eletronica_especifico_armamento | BASE TABLE | 0 | 9 | id |
| nota_fiscal_eletronica_especifico_combustivel | BASE TABLE | 0 | 25 | id |
| nota_fiscal_eletronica_especifico_medicamento | BASE TABLE | 0 | 7 | id |
| nota_fiscal_eletronica_especifico_medicamento_rastro | BASE TABLE | 0 | 10 | id |
| nota_fiscal_eletronica_especifico_papel | BASE TABLE | 0 | 6 | id |
| nota_fiscal_eletronica_especifico_veiculo | BASE TABLE | 0 | 29 | id |
| nota_fiscal_eletronica_exportacao | BASE TABLE | 0 | 8 | id |
| nota_fiscal_eletronica_forma_pagamento | BASE TABLE | 48 | 13 | id |
| nota_fiscal_eletronica_inutilizacao | BASE TABLE | 0 | 13 | id |
| nota_fiscal_eletronica_item | BASE TABLE | 196 | 110 | id |
| nota_fiscal_eletronica_item_combustivel_origem | BASE TABLE | 0 | 9 | id |
| nota_fiscal_eletronica_item_issqn | BASE TABLE | 0 | 21 | id |
| nota_fiscal_eletronica_local_entrega | BASE TABLE | 0 | 21 | id |
| nota_fiscal_eletronica_local_retirada | BASE TABLE | 0 | 20 | id |
| nota_fiscal_eletronica_referenciada | BASE TABLE | 0 | 7 | id |
| nota_fiscal_eletronica_responsavel_tecnico | BASE TABLE | 0 | 11 | id |
| nota_fiscal_eletronica_transportador | BASE TABLE | 48 | 16 | id |
| nota_fiscal_eletronica_volume | BASE TABLE | 0 | 11 | id |
| nota_fiscal_servico_eletronica | BASE TABLE | 0 | 46 | id |
| nota_fiscal_servico_eletronica_item | BASE TABLE | 0 | 40 | id |
| nota_fiscal_servico_eletronica_tomador | BASE TABLE | 0 | 21 | id |
| notificacao | BASE TABLE | 0 | 7 | id |
| notificacao_envio | BASE TABLE | 0 | 17 | id |
| notificacao_mensagem | BASE TABLE | 0 | 11 | id |
| notificacao_mensagem_arquivo | BASE TABLE | 0 | 11 | id |
| notificacao_pos_venda | BASE TABLE | 0 | 12 | id |
| notificacao_template | BASE TABLE | 40 | 13 | id |
| notificacao_usuario | BASE TABLE | 0 | 7 | id |
| nuvem_nfe | BASE TABLE | 0 | 28 | id |
| nuvem_nfe_emissao | BASE TABLE | 1 | 32 | id |
| nuvem_nfe_empresa | BASE TABLE | 0 | 9 | id |
| nuvem_nfe_eventos | BASE TABLE | 0 | 20 | id |
| oauth_access_tokens | BASE TABLE | 2 | 9 | access_token |
| oauth_authorization_codes | BASE TABLE | 0 | 6 | authorization_code |
| oauth_clients | BASE TABLE | 5 | 16 | client_id |
| oauth_jwt | BASE TABLE | 0 | 3 | client_id |
| oauth_refresh_tokens | BASE TABLE | 0 | 5 | refresh_token |
| oauth_scopes | BASE TABLE | 0 | 2 | - |
| oauth_users | BASE TABLE | 2 | 4 | username |
| observacao | BASE TABLE | 0 | 7 | id |
| orcamento | BASE TABLE | 0 | 46 | id |
| orcamento_autopecas | BASE TABLE | 0 | 15 | id |
| orcamento_item | BASE TABLE | 0 | 19 | id |
| orcamento_item_profissional | BASE TABLE | 0 | 7 | id |
| ordem_fornecimento | BASE TABLE | 0 | 27 | id |
| ordem_fornecimento_item | BASE TABLE | 0 | 9 | id |
| origem_venda | VIEW | 0 | 6 | - |
| password_resets | BASE TABLE | 0 | 3 | - |
| permission_role | BASE TABLE | 705 | 3 | id |
| permissions | BASE TABLE | 503 | 9 | id |
| petshop_album_foto_clinica | BASE TABLE | 0 | 6 | id |
| petshop_anamnese | BASE TABLE | 0 | 15 | id |
| petshop_anexo_exame | BASE TABLE | 0 | 11 | id |
| petshop_animal | BASE TABLE | 0 | 26 | id |
| petshop_animal_imagem | BASE TABLE | 0 | 14 | id |
| petshop_atendimento | BASE TABLE | 0 | 21 | id |
| petshop_atendimento_atestados_termos | BASE TABLE | 0 | 10 | id |
| petshop_atendimento_checklist | BASE TABLE | 0 | 6 | id |
| petshop_atendimento_servico | BASE TABLE | 0 | 6 | id |
| petshop_configuracao | BASE TABLE | 1 | 6 | id |
| petshop_contrato_pacote | BASE TABLE | 0 | 8 | id |
| petshop_contrato_pacote_item | BASE TABLE | 0 | 9 | id |
| petshop_especie | BASE TABLE | 2 | 6 | id |
| petshop_exame | BASE TABLE | 0 | 7 | id |
| petshop_exame_cabecalho | BASE TABLE | 0 | 8 | id |
| petshop_laboratorio | BASE TABLE | 0 | 5 | id |
| petshop_lancamento_vacina | BASE TABLE | 0 | 8 | id |
| petshop_modelo_prescricao | BASE TABLE | 0 | 8 | id |
| petshop_motivo_suspeita | BASE TABLE | 0 | 6 | id |
| petshop_ordem_servico | BASE TABLE | 0 | 8 | id |
| petshop_ordem_servico_item | BASE TABLE | 0 | 14 | id |
| petshop_pacote | BASE TABLE | 0 | 13 | id |
| petshop_pacote_item | BASE TABLE | 0 | 14 | id |
| petshop_pelagem | BASE TABLE | 0 | 5 | id |
| petshop_peso | BASE TABLE | 0 | 9 | id |
| petshop_porte | BASE TABLE | 0 | 5 | id |
| petshop_posologia | BASE TABLE | 0 | 15 | id |
| petshop_raca | BASE TABLE | 0 | 6 | id |
| petshop_receita | BASE TABLE | 0 | 9 | id |
| petshop_receita_prescricao | BASE TABLE | 0 | 16 | id |
| petshop_tipo_atendimento | BASE TABLE | 3 | 8 | id |
| petshop_tipo_condicao_animal | BASE TABLE | 8 | 5 | id |
| petshop_vacina | BASE TABLE | 0 | 8 | id |
| petshop_vacina_laboratorio | BASE TABLE | 0 | 6 | id |
| petshop_vacina_protocolo | BASE TABLE | 0 | 10 | id |
| petshop_vacina_protocolo_aplicacao | BASE TABLE | 0 | 12 | id |
| pivot_nfe | BASE TABLE | 0 | 6 | id |
| portal_360_categoria | BASE TABLE | 0 | 7 | id |
| portal_360_cliente | BASE TABLE | 0 | 9 | id |
| portal_360_cliente_contato | BASE TABLE | 0 | 9 | id |
| portal_360_cliente_endereco | BASE TABLE | 0 | 9 | id |
| portal_360_cliente_recebivel | BASE TABLE | 0 | 9 | id |
| portal_360_config | BASE TABLE | 0 | 15 | id |
| portal_360_forma_pagamento_conversao | BASE TABLE | 6 | 6 | id |
| portal_360_marca | BASE TABLE | 0 | 7 | id |
| portal_360_payment_term | BASE TABLE | 0 | 8 | id |
| portal_360_pedido | BASE TABLE | 0 | 21 | id |
| portal_360_produto | BASE TABLE | 0 | 7 | id |
| portal_360_promocao | BASE TABLE | 0 | 7 | id |
| portal_360_venda | BASE TABLE | 0 | 10 | id |
| portal_360_vendedor | BASE TABLE | 0 | 7 | id |
| portal_360_webhook | BASE TABLE | 0 | 10 | id |
| producao | BASE TABLE | 0 | 11 | id |
| producao_item | BASE TABLE | 0 | 10 | id |
| produto | BASE TABLE | 104 | 62 | id |
| produto_combo | BASE TABLE | 0 | 12 | id |
| produto_combo_item | BASE TABLE | 0 | 10 | id |
| produto_composicao | BASE TABLE | 0 | 8 | id |
| produto_empresa | BASE TABLE | 111 | 61 | id |
| produto_empresa_grade | BASE TABLE | 78 | 22 | id |
| produto_empresa_vinculo_fiscal | BASE TABLE | 77 | 4 | id |
| produto_especifico_armamento | BASE TABLE | 0 | 8 | id |
| produto_especifico_combustivel | BASE TABLE | 0 | 22 | id |
| produto_especifico_combustivel_origem | BASE TABLE | 0 | 8 | id |
| produto_especifico_medicamento | BASE TABLE | 0 | 6 | id |
| produto_especifico_papel | BASE TABLE | 0 | 5 | id |
| produto_especifico_veiculo | BASE TABLE | 0 | 28 | id |
| produto_estoque_ruptura | BASE TABLE | 0 | 9 | id |
| produto_fornecedor | BASE TABLE | 72 | 7 | id |
| produto_imagem | BASE TABLE | 0 | 13 | id |
| produto_marketplace | BASE TABLE | 0 | 23 | id |
| produto_marketplace_anuncio | BASE TABLE | 0 | 9 | id |
| produto_marketplace_hub_saleschannel | BASE TABLE | 0 | 10 | id |
| produto_organizar_estoque | BASE TABLE | 65 | 16 | produto_empresa_grade_id |
| produto_relacionado | BASE TABLE | 0 | 6 | id |
| produto_restaurante_setor | BASE TABLE | 0 | 5 | id |
| promocao | BASE TABLE | 0 | 18 | id |
| promocao_empresa | BASE TABLE | 0 | 6 | id |
| promocao_item | BASE TABLE | 0 | 13 | id |
| reajuste | BASE TABLE | 0 | 31 | id |
| reajuste_item | BASE TABLE | 2 | 15 | id |
| recebimento | BASE TABLE | 0 | 15 | id |
| recebimento_autorizacao | BASE TABLE | 0 | 20 | id |
| recebimento_status | BASE TABLE | 0 | 9 | id |
| recibo | BASE TABLE | 0 | 12 | id |
| registro_bloqueado | BASE TABLE | 0 | 7 | id |
| regra_fiscal | BASE TABLE | 0 | 23 | id |
| relatorio_personalizado | BASE TABLE | 0 | 6 | id |
| relatorio_personalizado_colunas | BASE TABLE | 0 | 8 | id |
| relatorio_personalizado_config | BASE TABLE | 0 | 11 | id |
| relatorio_personalizado_filtros | BASE TABLE | 0 | 8 | id |
| relatorio_personalizado_notificacao_configuracao | BASE TABLE | 0 | 10 | id |
| relatorio_ultimos_acessados | BASE TABLE | 4 | 7 | id |
| responsavel_tecnico_configuracao | BASE TABLE | 4 | 11 | id |
| restaurante_ambiente | BASE TABLE | 0 | 7 | id |
| restaurante_configuracao_impressoras | BASE TABLE | 0 | 8 | id |
| restaurante_familia | BASE TABLE | 0 | 5 | id |
| restaurante_grupo_observacao | BASE TABLE | 0 | 6 | id |
| restaurante_impressora | BASE TABLE | 9 | 7 | id |
| restaurante_mesa | BASE TABLE | 0 | 44 | id |
| restaurante_mesa_adiantamento | BASE TABLE | 0 | 27 | id |
| restaurante_mesa_configuracao | BASE TABLE | 0 | 30 | id |
| restaurante_mesa_item | BASE TABLE | 0 | 45 | id |
| restaurante_mesa_item_acompanhamento | BASE TABLE | 0 | 12 | id |
| restaurante_observacao | BASE TABLE | 0 | 5 | id |
| restaurante_setor | BASE TABLE | 0 | 9 | id |
| role_user | BASE TABLE | 3 | 5 | id |
| roles | BASE TABLE | 2 | 7 | id |
| servico_issqn | VIEW | 0 | 6 | - |
| similar | BASE TABLE | 0 | 6 | id |
| sku_atributo | BASE TABLE | 19 | 10 | id |
| softcomintro | BASE TABLE | 0 | 6 | id |
| sped_configuracoes | BASE TABLE | 0 | 42 | id |
| sped_download | BASE TABLE | 0 | 7 | id |
| sped_e111_ajuste_apuracao | BASE TABLE | 0 | 11 | id |
| sped_e113_ajuste_apuracao_documentos | BASE TABLE | 0 | 13 | id |
| sped_e115_valores_declaratorios | BASE TABLE | 0 | 9 | id |
| sped_inventario_base | BASE TABLE | 0 | 9 | id |
| sped_ipi_ajuste_apuracao | BASE TABLE | 0 | 10 | id |
| sped_plano_contas | BASE TABLE | 0 | 12 | id |
| sped_plano_contas_cfop | BASE TABLE | 0 | 7 | id |
| sped_tabela_4_5_4 | BASE TABLE | 9 | 7 | id |
| sped_tabela_5_1_1 | VIEW | 0 | 9 | - |
| sped_tabela_5_2 | BASE TABLE | 20 | 6 | id |
| sped_tabela_e115_codigo_apuracao | BASE TABLE | 1197 | 7 | id |
| ta_no_menu_categoria | BASE TABLE | 0 | 7 | id |
| ta_no_menu_config | BASE TABLE | 0 | 6 | id |
| ta_no_menu_produto | BASE TABLE | 0 | 7 | id |
| ta_no_menu_promocao | BASE TABLE | 0 | 6 | id |
| ta_no_menu_promocao_item | BASE TABLE | 0 | 7 | id |
| ta_no_menu_variation | BASE TABLE | 0 | 7 | id |
| ta_no_menu_variation_additional | BASE TABLE | 0 | 8 | id |
| ta_no_menu_variation_additional_item | BASE TABLE | 0 | 9 | id |
| ta_no_menu_variation_item | BASE TABLE | 0 | 8 | id |
| tabela_preco | BASE TABLE | 4 | 5 | id |
| tabela_preco_produto | BASE TABLE | 0 | 7 | id |
| tag_classificacao | BASE TABLE | 0 | 5 | id |
| telescope_entries | BASE TABLE | 0 | 8 | sequence |
| telescope_entries_tags | BASE TABLE | 0 | 2 | - |
| telescope_monitoring | BASE TABLE | 0 | 1 | - |
| tipo_ajuste | BASE TABLE | 3 | 6 | id |
| tipo_area | BASE TABLE | 0 | 5 | id |
| tipo_cliente | BASE TABLE | 2 | 6 | id |
| tipo_convenio | BASE TABLE | 0 | 5 | id |
| tipo_debito | BASE TABLE | 0 | 5 | id |
| tipo_documento | BASE TABLE | 3 | 6 | id |
| tipo_energia_grupotensao | BASE TABLE | 0 | 6 | id |
| tipo_energia_ligacao | BASE TABLE | 0 | 6 | id |
| tipo_fator | BASE TABLE | 0 | 6 | id |
| tipo_frete | BASE TABLE | 0 | 6 | id |
| tipo_funcao | BASE TABLE | 3 | 7 | id |
| tipo_justificativa | BASE TABLE | 6 | 6 | id |
| tipo_modelo | BASE TABLE | 0 | 7 | id |
| tipo_ncm | VIEW | 0 | 6 | - |
| tipo_setor | BASE TABLE | 0 | 5 | id |
| tipo_similar | BASE TABLE | 0 | 5 | id |
| tipo_unidade_medida | BASE TABLE | 3 | 5 | id |
| transferencia_bancaria | BASE TABLE | 0 | 11 | id |
| transportador | BASE TABLE | 0 | 16 | id |
| tributos_por_uf | BASE TABLE | 0 | 10 | id |
| troca | BASE TABLE | 0 | 14 | id |
| users | BASE TABLE | 3 | 9 | id |
| veiculo | BASE TABLE | 0 | 22 | id |
| veiculo_marca | BASE TABLE | 0 | 5 | id |
| veiculo_modelo | BASE TABLE | 0 | 5 | id |
| venda | BASE TABLE | 95 | 65 | id |
| venda_acoes | BASE TABLE | 0 | 9 | id |
| venda_bloqueio | BASE TABLE | 0 | 9 | id |
| venda_cartao | BASE TABLE | 89 | 43 | id |
| venda_endereco_entrega | BASE TABLE | 0 | 12 | id |
| venda_item | BASE TABLE | 192 | 39 | id |
| venda_item_animal | BASE TABLE | 0 | 5 | id |
| venda_item_composicao | BASE TABLE | 0 | 10 | id |
| venda_nfce | BASE TABLE | 0 | 16 | id |
| venda_nota_referenciada | BASE TABLE | 0 | 6 | id |
| venda_ordem_servico | BASE TABLE | 0 | 24 | id |
| venda_ordem_servico_contato | BASE TABLE | 0 | 8 | id |
| venda_status_historico | BASE TABLE | 0 | 8 | id |
| venda_veiculo | BASE TABLE | 0 | 14 | venda_id |
| vendas-laravel_create_financeiro_parcela_dados_cartao_table | BASE TABLE | 0 | 4 | id |
| view_memoria_financeiro_agrupada | VIEW | 0 | 92 | - |
| view_memoria_financeiro_pagamento | VIEW | 0 | 5 | - |
| view_memoria_financeiro_todas | VIEW | 0 | 118 | - |
| view_memoria_nf_entrada | VIEW | 0 | 37 | - |
| view_memoria_nf_saida | VIEW | 0 | 108 | - |
| view_memoria_vendas | VIEW | 0 | 99 | - |
| view_memoria_vendas_agrupado | VIEW | 0 | 97 | - |
| view_memoria_vendas_pagamento | VIEW | 0 | 85 | - |
| view_memoria_vendas_todas | VIEW | 0 | 99 | - |
| view_venda_financeiro | VIEW | 0 | 5 | - |
| vinculos_fiscais | BASE TABLE | 8 | 10 | id |
| vinculos_fiscais_configuracoes | BASE TABLE | 40 | 58 | id |
| vinculos_fiscais_ncm | BASE TABLE | 7 | 6 | id |
| vinculos_ncm | BASE TABLE | 0 | 6 | id |
| whatsapp_devices | BASE TABLE | 0 | 8 | id |

---
## Estrutura Detalhada das Tabelas

### Tabela: agenda_evento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 20

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | tipo_evento | enum('REUNIAO','LIGAR','INTERNO','EXTERNO','OUTROS') | SIM | - | NULL | - |
| 4 | titulo | varchar(255) | SIM | - | NULL | - |
| 5 | data_hora_inicio | datetime | SIM | - | NULL | - |
| 6 | data_hora_termino | datetime | SIM | - | NULL | - |
| 7 | repeticao | enum('NAO_REPETE','DIARIA','SEMANAL','MENSAL','ANUAL') | SIM | - | NULL | - |
| 8 | data_termino_repeticao | date | SIM | - | NULL | - |
| 9 | funcionario_id | int | SIM | - | NULL | - |
| 10 | localizacao | text | SIM | - | NULL | - |
| 11 | observacoes | text | SIM | - | NULL | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |
| 15 | data_realizacao | datetime | SIM | - | NULL | - |
| 16 | dia_inteiro | tinyint(1) | NAO | - | 0 | - |
| 17 | atendimento_id | int | SIM | - | NULL | - |
| 18 | avulso | tinyint | NAO | - | 0 | - |
| 19 | evento_repeticao_id | int | SIM | - | NULL | - |
| 20 | cliente_id | int | SIM | MUL | NULL | - |

### Tabela: agenda_evento_arquivo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | description | varchar(255) | SIM | - | NULL | - |
| 4 | filename | varchar(255) | NAO | - | NULL | - |
| 5 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 6 | mid_file | varchar(255) | SIM | - | NULL | - |
| 7 | extension | varchar(10) | NAO | - | NULL | - |
| 8 | link | text | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: agenda_evento_atendimento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | agenda_evento_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | atendimento_id | bigint unsigned | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: agenda_evento_participante_interno (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | agenda_evento_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | funcionario_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: assistencia (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | NULL | - |
| 4 | tipo_atendimento | enum('VENDA','ORCAMENTO') | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | status | enum('EM_ANDAMENTO','CONCLUIDO','CANCELADA','AGUARDANDO_RETIRADA') | SIM | - | EM_ANDAMENTO | - |
| 9 | tecnico_responsavel_id | int | SIM | MUL | NULL | - |
| 10 | nome_solicitante | varchar(255) | SIM | - | NULL | - |
| 11 | previsao_laudo | timestamp | SIM | - | NULL | - |
| 12 | data_saida | timestamp | SIM | - | NULL | - |
| 13 | tipo_assistencia | enum('OTICA','PADRAO') | NAO | - | PADRAO | - |
| 14 | valor_pago_pela_otica | decimal(15,2) | SIM | - | 0.00 | - |

### Tabela: assistencia_otica_itens (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 17

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | SIM | MUL | NULL | - |
| 3 | produto_empresa_grade_id | int | SIM | MUL | NULL | - |
| 4 | assistencia_id | int unsigned | NAO | MUL | NULL | - |
| 5 | descricao_item | varchar(255) | SIM | - | NULL | - |
| 6 | quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 7 | preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | desconto_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | acrescimo_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 10 | percentual_desconto | decimal(15,10) | SIM | - | NULL | - |
| 11 | percentual_acrescimo | decimal(15,10) | SIM | - | NULL | - |
| 12 | tipo_item | enum('LENTE_OD','LENTE_OE','AVULSO','ARMACAO') | SIM | - | NULL | - |
| 13 | receita_id | int unsigned | SIM | MUL | NULL | - |
| 14 | garantia | tinyint | SIM | - | 0 | - |
| 15 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 16 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 17 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: assistencia_otica_receitas (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 25

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | assistencia_id | int unsigned | NAO | MUL | NULL | - |
| 4 | medico_id | int unsigned | SIM | MUL | NULL | - |
| 5 | paciente_id | int | SIM | MUL | NULL | - |
| 6 | tipo_lente | enum('BIFOCAL','MULTIFOCAL','VISAO_SIMPLES_PERTO','VISAO_SIMPLES_LONGE','AVULSO') | NAO | - | NULL | - |
| 7 | lente_direita | int | SIM | - | NULL | - |
| 8 | lente_esquerda | int | SIM | - | NULL | - |
| 9 | valor_lente_direita | decimal(15,4) | NAO | - | 0.0000 | - |
| 10 | valor_lente_esquerda | decimal(15,4) | NAO | - | 0.0000 | - |
| 11 | validade_receita | date | SIM | - | NULL | - |
| 12 | armacao_propria | tinyint(1) | NAO | - | 0 | - |
| 13 | altura | decimal(15,2) | NAO | - | 0.00 | - |
| 14 | ponte_aro | decimal(15,2) | NAO | - | 0.00 | - |
| 15 | maior_diagonal | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | distancia_pupilar | decimal(15,2) | NAO | - | 0.00 | - |
| 17 | previsao_entrega | date | SIM | - | NULL | - |
| 18 | armacao_id | int | SIM | MUL | NULL | - |
| 19 | laboratorio_id | int unsigned | SIM | MUL | NULL | - |
| 20 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 21 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 22 | deleted_at | timestamp | SIM | - | NULL | - |
| 23 | paciente_nome | varchar(255) | SIM | - | NULL | - |
| 24 | convenio_id | int | SIM | MUL | NULL | - |
| 25 | observacao | text | SIM | - | NULL | - |

### Tabela: assistencia_otica_receitas_configuracoes (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 26

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | receita_id | int unsigned | NAO | MUL | NULL | - |
| 3 | esferico_od_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 4 | esferico_oe_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 5 | esferico_od_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 6 | esferico_oe_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 7 | cilindrico_od_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 8 | cilindrico_oe_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 9 | cilindrico_od_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 10 | cilindrico_oe_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 11 | eixo_od_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 12 | eixo_oe_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 13 | eixo_od_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 14 | eixo_oe_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 15 | dnp_od_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 16 | dnp_oe_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 17 | dnp_od_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 18 | dnp_oe_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 19 | co_od_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 20 | co_oe_longe | decimal(15,2) | SIM | - | 0.00 | - |
| 21 | co_od_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 22 | co_oe_perto | decimal(15,2) | SIM | - | 0.00 | - |
| 23 | adicao | decimal(15,2) | SIM | - | 0.00 | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |
| 25 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 26 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |

### Tabela: assistencia_padrao_equipamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | assistencia_id | int unsigned | NAO | MUL | NULL | - |
| 3 | equipamento_id | int unsigned | NAO | MUL | NULL | - |
| 4 | marca_id | int unsigned | SIM | MUL | NULL | - |
| 5 | modelo | varchar(255) | SIM | - | NULL | - |
| 6 | num_serie | varchar(255) | SIM | - | NULL | - |
| 7 | defeito | text | SIM | - | NULL | - |
| 8 | acessorios | text | SIM | - | NULL | - |
| 9 | observacao | text | SIM | - | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: assistencia_padrao_laudo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | assistencia_id | int unsigned | NAO | MUL | NULL | - |
| 3 | laudo_tecnico | text | SIM | - | NULL | - |
| 4 | servico_realizado | text | SIM | - | NULL | - |
| 5 | data_finalizacao | timestamp | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: atendimento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | atendimento_lista_id | bigint unsigned | NAO | MUL | NULL | - |
| 4 | ordem | int unsigned | NAO | - | 0 | - |
| 5 | data_atendimento | datetime | SIM | - | NULL | - |
| 6 | data_conclusao_lista | datetime | SIM | - | NULL | - |
| 7 | tipo_atendimento | varchar(60) | SIM | - | NULL | - |
| 8 | tipo_atendimento_kanban | varchar(50) | NAO | - | AVULSO | - |
| 9 | observacao | text | SIM | - | NULL | - |
| 10 | cliente_id | bigint unsigned | SIM | MUL | NULL | - |
| 11 | atendente_id | bigint unsigned | SIM | - | NULL | - |
| 12 | ordem_servico_id | bigint unsigned | SIM | - | NULL | - |
| 13 | venda_id | bigint unsigned | SIM | - | NULL | - |
| 14 | assistencia_id | bigint unsigned | SIM | - | NULL | - |
| 15 | receita_id | bigint unsigned | SIM | - | NULL | - |
| 16 | orcamento_id | int | SIM | MUL | NULL | - |
| 17 | status | varchar(60) | SIM | - | NULL | - |
| 18 | created_at | timestamp | SIM | - | NULL | - |
| 19 | updated_at | timestamp | SIM | - | NULL | - |
| 20 | deleted_at | timestamp | SIM | - | NULL | - |
| 21 | data_cancelamento | datetime | SIM | - | NULL | - |

### Tabela: atendimento_config (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | multiplos_cards | tinyint(1) | NAO | - | 0 | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | manutencao_equipamentos | tinyint | NAO | - | 0 | - |

### Tabela: atendimento_lista (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(150) | NAO | - | NULL | - |
| 4 | cor_hex | varchar(7) | SIM | - | NULL | - |
| 5 | ordem | int unsigned | NAO | - | 0 | - |
| 6 | manter_cards | tinyint(1) | NAO | - | 0 | - |
| 7 | ativar_mensagem | tinyint(1) | NAO | - | 0 | - |
| 8 | mensagem_id | int | SIM | MUL | NULL | - |
| 9 | ativo | tinyint(1) | NAO | - | 1 | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: atendimento_lista_notificacao_controle (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | atendimento_id | bigint unsigned | NAO | UNI | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: atestados_termos (BASE TABLE)
**Linhas aprox:** 11 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | tipo | enum('ATESTADO','TERMOS') | NAO | - | NULL | - |
| 4 | texto | text | SIM | - | NULL | - |
| 5 | padrao | tinyint | NAO | - | 0 | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: auditoria (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | usuario | varchar(255) | NAO | - | NULL | - |
| 3 | data_hora | datetime | NAO | - | NULL | - |
| 4 | api_device_id | varchar(255) | NAO | - | NULL | - |
| 5 | acao | text | NAO | - | NULL | - |
| 6 | empresa_id | int | SIM | MUL | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: autopeca_checklist (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 4

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | orcamento_autopecas_id | int | NAO | MUL | NULL | - |
| 3 | finalizado | tinyint | NAO | - | 0 | - |
| 4 | observacoes | text | SIM | - | NULL | - |

### Tabela: autopeca_checklist_respostas (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 4

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | autopeca_checklist_id | int | NAO | MUL | NULL | - |
| 3 | autopecas_checklist_item_id | bigint unsigned | NAO | MUL | NULL | - |
| 4 | resposta | text | SIM | - | NULL | - |

### Tabela: autopecas_checklist_categoria (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | ordenacao | int | NAO | - | NULL | - |
| 4 | empresa_id | int | NAO | MUL | NULL | - |
| 5 | visivel | tinyint | NAO | - | 1 | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: autopecas_checklist_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | autopecas_checklist_categoria_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | nome | text | NAO | - | NULL | - |
| 4 | tipo_resposta | text | NAO | - | NULL | - |
| 5 | ordenacao | int | NAO | - | NULL | - |
| 6 | permitir_foto | tinyint | NAO | - | 0 | - |
| 7 | obrigatorio | tinyint | NAO | - | 0 | - |
| 8 | valor_padrao | text | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: azure_keys (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | description | varchar(255) | SIM | - | NULL | - |
| 3 | type | varchar(255) | NAO | - | NULL | - |
| 4 | client_id | varchar(255) | SIM | - | NULL | - |
| 5 | client_secret | varchar(255) | SIM | - | NULL | - |
| 6 | company_id | int | NAO | MUL | NULL | - |
| 7 | portal_360_tenant_id | varchar(255) | SIM | - | NULL | - |
| 8 | portal_360_company_id | varchar(255) | SIM | - | NULL | - |
| 9 | portal_360_usuario | varchar(255) | SIM | - | NULL | - |
| 10 | portal_360_senha | varchar(255) | SIM | - | NULL | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |
| 14 | ambiente_teste | tinyint(1) | NAO | - | 0 | - |
| 15 | softconnect_company_id | varchar(255) | SIM | - | NULL | - |
| 16 | softconnect_device_id | varchar(255) | SIM | - | NULL | - |
| 17 | notification_company_id | varchar(255) | SIM | - | NULL | - |
| 18 | notification_days | varchar(255) | SIM | - | NULL | - |
| 19 | notification_sending_start_time | varchar(5) | SIM | - | NULL | - |
| 20 | notification_sending_end_time | varchar(5) | SIM | - | NULL | - |
| 21 | nfse_nacional | tinyint(1) | SIM | - | NULL | - |

### Tabela: bairro (BASE TABLE)
**Linhas aprox:** 14 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | taxa_entrega | decimal(15,2) | NAO | - | 0.00 | - |
| 4 | cobrar_taxa_entrega | tinyint | NAO | - | 1 | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: balanco (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | data_balanco | date | NAO | - | NULL | - |
| 3 | responsavel_id | int | NAO | - | NULL | - |
| 4 | observacao | text | SIM | - | NULL | - |
| 5 | empresa_id | int | NAO | MUL | NULL | - |
| 6 | status_balanco | enum('ABERTO','FINALIZADO') | NAO | - | ABERTO | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: balanco_item (BASE TABLE)
**Linhas aprox:** 26 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | - | NULL | - |
| 3 | balanco_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | quantidade | decimal(15,4) | NAO | - | NULL | - |
| 6 | estoque | decimal(15,4) | NAO | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: banco (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | codigo | varchar(255) | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | image | longtext | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: bandeira (BASE TABLE)
**Linhas aprox:** 28 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(5) | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: box_prisma (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | nome | varchar(255) | NAO | - | NULL | - |
| 2 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 3 | deleted_at | timestamp | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: cache_locks (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 3

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | key | varchar(191) | NAO | PRI | NULL | - |
| 2 | owner | varchar(255) | NAO | - | NULL | - |
| 3 | expiration | int | NAO | - | NULL | - |

### Tabela: caixa_funcoes (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | data_caixa | date | SIM | - | NULL | - |
| 3 | data_abertura | datetime | SIM | - | NULL | - |
| 4 | data_fechamento | datetime | SIM | - | NULL | - |
| 5 | api_device_id | varchar(100) | NAO | - | NULL | - |
| 6 | turno | tinyint | NAO | - | NULL | - |
| 7 | operador_id | int unsigned | SIM | MUL | NULL | - |
| 8 | usuario_abertura_id | int unsigned | SIM | MUL | NULL | - |
| 9 | usuario_fechamento_id | int unsigned | SIM | MUL | NULL | - |
| 10 | deleted_at | timestamp | SIM | MUL | NULL | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | device_client_id | varchar(40) | SIM | MUL | NULL | - |

### Tabela: caixa_funcoes_digitacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | caixa_funcoes_id | int | NAO | MUL | NULL | - |
| 3 | caixa_data | date | SIM | - | NULL | - |
| 4 | caixa_turno | varchar(255) | SIM | - | NULL | - |
| 5 | caixa_usuario_id | int | SIM | - | NULL | - |
| 6 | forma_pagamento_id | int | NAO | MUL | NULL | - |
| 7 | valor | decimal(15,4) | NAO | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: caixa_funcoes_digitacao_bandeiras (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | caixa_funcoes_id | int | SIM | - | NULL | - |
| 3 | caixa_usuario_id | int | NAO | - | NULL | - |
| 4 | caixa_data | date | NAO | - | NULL | - |
| 5 | caixa_turno | varchar(255) | NAO | - | NULL | - |
| 6 | bandeira | varchar(255) | NAO | - | NULL | - |
| 7 | valor | decimal(15,4) | NAO | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: cartao_alias (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 4 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cartao_credito (BASE TABLE)
**Linhas aprox:** 11 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | dia | int | NAO | - | 0 | - |
| 4 | taxa_admin | decimal(15,2) | NAO | - | NULL | - |
| 5 | empresa_id | int | SIM | MUL | NULL | - |
| 6 | bandeira | varchar(3) | NAO | - | NULL | - |
| 7 | credenciadora_id | int unsigned | SIM | MUL | NULL | - |
| 8 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |
| 11 | bandeira_nome | varchar(255) | NAO | - | NULL | - |
| 12 | parcelas | int | NAO | - | 1 | - |
| 13 | alias_cartao | varchar(255) | SIM | - | NULL | - |
| 14 | alias | varchar(255) | NAO | - | NULL | - |
| 15 | tipo | enum('CREDITO','DEBITO') | NAO | - | CREDITO | - |

### Tabela: centro_custo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | deleted_at | timestamp | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: cfop (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | SIM | - | NULL | - |
| 4 | aliquota_icms | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | operacao | varchar(255) | SIM | - | NULL | - |
| 6 | cfop_equivalente | int | SIM | - | NULL | - |
| 7 | nao_escriturar | int | NAO | - | 0 | - |
| 8 | devolucao | int | NAO | - | 0 | - |
| 9 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: checklist_photos (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | bigint unsigned | SIM | MUL | NULL | - |
| 3 | parent_id | bigint unsigned | SIM | MUL | NULL | - |
| 4 | orcamento_id | bigint unsigned | SIM | MUL | NULL | - |
| 5 | filename | varchar(255) | NAO | - | NULL | - |
| 6 | link | varchar(255) | NAO | - | NULL | - |
| 7 | extension | varchar(255) | SIM | - | NULL | - |
| 8 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 9 | mid_file | varchar(255) | SIM | - | NULL | - |
| 10 | description | varchar(255) | SIM | - | NULL | - |
| 11 | user_id | bigint unsigned | SIM | MUL | NULL | - |
| 12 | observacoes | text | SIM | - | NULL | - |
| 13 | created_at | timestamp | SIM | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cheque (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | parcela_id | int | SIM | MUL | NULL | - |
| 3 | parcela_repasse_id | int | SIM | MUL | NULL | - |
| 4 | banco_numero | varchar(45) | NAO | - | NULL | - |
| 5 | numero | varchar(45) | NAO | - | NULL | - |
| 6 | emitente | varchar(255) | NAO | - | NULL | - |
| 7 | data_vencimento | date | NAO | - | NULL | - |
| 8 | valor | decimal(15,2) | NAO | - | NULL | - |
| 9 | data_baixa | date | SIM | - | NULL | - |
| 10 | motivo_devolucao_id | int | SIM | - | NULL | - |
| 11 | data_devolucao | date | SIM | - | NULL | - |
| 12 | tipo | varchar(100) | NAO | - | NULL | - |
| 13 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cheque_motivo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cheque_movimento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | - |
| 2 | cheque_id | int | NAO | MUL | NULL | - |
| 3 | empresa_id | int | SIM | MUL | NULL | - |
| 4 | fornecedor_id | int | SIM | MUL | NULL | - |
| 5 | data_movimento | date | NAO | - | NULL | - |
| 6 | tipo | varchar(255) | NAO | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cliente (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 32

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | pessoa | enum('FISICA','JURIDICA','ESTRANGEIRA') | NAO | - | NULL | - |
| 3 | cpf_cnpj | varchar(18) | SIM | - | NULL | - |
| 4 | inscricao_estadual | varchar(20) | SIM | - | NULL | - |
| 5 | inscricao_municipal | varchar(50) | SIM | - | NULL | - |
| 6 | rg | varchar(20) | SIM | - | NULL | - |
| 7 | nome | varchar(255) | NAO | - | NULL | - |
| 8 | razao_social | varchar(255) | NAO | - | NULL | - |
| 9 | data_fundacao | date | SIM | - | NULL | - |
| 10 | data_nascimento | date | SIM | - | NULL | - |
| 11 | area_id | int | SIM | MUL | NULL | - |
| 12 | funcionario_id | int | SIM | MUL | NULL | - |
| 13 | tipo_cliente_id | int | NAO | MUL | NULL | - |
| 14 | tipo_preco | enum('PADRAO','A','B','C') | NAO | - | PADRAO | - |
| 15 | foto | varchar(255) | SIM | - | foto-usuario.png | - |
| 16 | bloqueado | int | SIM | MUL | 0 | - |
| 17 | desativado | int | NAO | MUL | 0 | - |
| 18 | observacao | text | SIM | - | NULL | - |
| 19 | api_guid | varchar(255) | SIM | MUL | NULL | - |
| 20 | permitir_excluir | int | NAO | - | 1 | - |
| 21 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 22 | updated_at | timestamp | SIM | - | NULL | - |
| 23 | deleted_at | timestamp | SIM | - | NULL | - |
| 24 | contribuinte_icms | int | SIM | - | 9 | - |
| 25 | indicador_finalidade | varchar(1) | SIM | - | NULL | - |
| 26 | detalhe_financeiro | longtext | SIM | - | NULL | - |
| 27 | limite_credito | decimal(15,2) | NAO | - | 0.00 | - |
| 28 | tabela_preco_id | int unsigned | SIM | MUL | NULL | - |
| 29 | id_estrangeiro | varchar(255) | SIM | - | NULL | - |
| 30 | codigo_pais | varchar(10) | SIM | - | NULL | - |
| 31 | cliente_administradora_id | int unsigned | SIM | - | NULL | - |
| 32 | nome_pais | varchar(255) | SIM | - | NULL | - |

### Tabela: cliente_condicao_pagamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cliente_id | int | SIM | MUL | NULL | - |
| 3 | condicao_pagamento_padrao_id | bigint unsigned | SIM | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cliente_condicao_pagamento_parents (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 3

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cliente_condicao_pagamento_id | int | SIM | MUL | NULL | - |
| 3 | condicao_pagamento_id | bigint unsigned | SIM | MUL | NULL | - |

### Tabela: cliente_convenio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cliente_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | valor | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cliente_credito (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cliente_id | int | NAO | MUL | NULL | - |
| 3 | venda_id | int | SIM | MUL | NULL | - |
| 4 | operacao | enum('CREDITO','DEBITO') | NAO | - | NULL | - |
| 5 | data_operacao | date | NAO | - | NULL | - |
| 6 | valor | decimal(15,4) | NAO | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | api_device_id | varchar(255) | SIM | - | NULL | - |
| 11 | utilizado | tinyint(1) | NAO | - | 0 | - |
| 12 | usuario_id | int unsigned | SIM | MUL | NULL | - |

### Tabela: cliente_imagens (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | description | varchar(255) | SIM | - | NULL | - |
| 3 | file_name | varchar(255) | NAO | - | NULL | - |
| 4 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 5 | mid_file | varchar(255) | SIM | - | NULL | - |
| 6 | extension | varchar(10) | NAO | - | NULL | - |
| 7 | link | text | SIM | - | NULL | - |
| 8 | imagem_principal | tinyint | NAO | - | 0 | - |
| 9 | cliente_id | int | NAO | MUL | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cliente_ocorrencia (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cliente_id | int | NAO | MUL | NULL | - |
| 3 | usuario_atendente_id | int | NAO | - | NULL | - |
| 4 | usuario_agendado_id | int | NAO | - | NULL | - |
| 5 | data_cadastro | date | NAO | - | NULL | - |
| 6 | motivo | text | NAO | - | NULL | - |
| 7 | data_retorno | date | SIM | - | NULL | - |
| 8 | hora_marcada | varchar(5) | SIM | - | NULL | - |
| 9 | realizado | text | SIM | - | NULL | - |
| 10 | hora_inicio | varchar(5) | SIM | - | NULL | - |
| 11 | hora_termino | varchar(5) | SIM | - | NULL | - |
| 12 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cliente_tag_classificacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cliente_id | int | SIM | MUL | NULL | - |
| 3 | tag_classificacao_id | int | SIM | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cliente_veiculo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cliente_id | int | NAO | MUL | NULL | - |
| 3 | placa | varchar(8) | NAO | - | NULL | - |
| 4 | modelo | varchar(255) | SIM | - | NULL | - |
| 5 | combustivel | varchar(50) | SIM | - | NULL | - |
| 6 | ano_fabricacao | varchar(50) | SIM | - | NULL | - |
| 7 | ano_modelo | int | SIM | - | NULL | - |
| 8 | cor | varchar(50) | SIM | - | NULL | - |
| 9 | renavam | varchar(50) | SIM | - | NULL | - |
| 10 | chassi | varchar(50) | SIM | - | NULL | - |
| 11 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |
| 14 | marca_id | int | NAO | MUL | NULL | - |
| 15 | quilometragem | int | SIM | - | NULL | - |
| 16 | observacoes | text | SIM | - | NULL | - |

### Tabela: cnpjs_autorizados (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | cnpj | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cobranca_parcelas (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 31

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | char(36) | NAO | PRI | NULL | - |
| 2 | financeiro_parcela_id | int | NAO | MUL | NULL | - |
| 3 | recipient_account_agreement_id | char(36) | NAO | - | NULL | - |
| 4 | status | varchar(20) | NAO | - | NULL | - |
| 5 | status_dispatch | varchar(20) | NAO | - | NULL | - |
| 6 | dispatch_number | varchar(20) | SIM | - | NULL | - |
| 7 | payer_type_document | varchar(1) | NAO | - | NULL | - |
| 8 | payer_document | varchar(20) | NAO | - | NULL | - |
| 9 | payer_name | varchar(50) | NAO | - | NULL | - |
| 10 | payer_postal_code | varchar(9) | NAO | - | NULL | - |
| 11 | payer_street | varchar(50) | NAO | - | NULL | - |
| 12 | payer_number | varchar(4) | NAO | - | NULL | - |
| 13 | payer_state | varchar(2) | NAO | - | NULL | - |
| 14 | payer_city | varchar(50) | NAO | - | NULL | - |
| 15 | payer_neighborhood | varchar(50) | NAO | - | NULL | - |
| 16 | our_number | varchar(50) | NAO | - | NULL | - |
| 17 | document_number | varchar(30) | SIM | - | NULL | - |
| 18 | installment | varchar(15) | SIM | - | NULL | - |
| 19 | due_date | date | NAO | - | NULL | - |
| 20 | issue_date | datetime | NAO | - | NULL | - |
| 21 | amount | decimal(15,2) | NAO | - | 0.00 | - |
| 22 | fine | decimal(15,2) | NAO | - | 0.00 | - |
| 23 | interest | decimal(15,2) | NAO | - | 0.00 | - |
| 24 | discount | decimal(15,2) | NAO | - | 0.00 | - |
| 25 | pix_qrcode | text | SIM | - | NULL | - |
| 26 | ticket_typed_line | varchar(50) | SIM | - | NULL | - |
| 27 | paid | text | SIM | - | NULL | - |
| 28 | historic | text | SIM | - | NULL | - |
| 29 | created_at | timestamp | SIM | - | NULL | - |
| 30 | updated_at | timestamp | SIM | - | NULL | - |
| 31 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cobranca_webhooks (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | payload | text | NAO | - | NULL | - |
| 3 | deleted_at | timestamp | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: codigo_anp (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | - | 0 | - |
| 2 | codigo | varchar(255) | NAO | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: comissoes (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | valor | decimal(15,2) | NAO | - | 0.00 | - |
| 4 | tipo | varchar(30) | NAO | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: compra (BASE TABLE)
**Linhas aprox:** 62 | **Colunas:** 79

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | chave_acesso | varchar(255) | SIM | - | NULL | - |
| 4 | numero_nfe | int | NAO | - | NULL | - |
| 5 | modelo | varchar(255) | SIM | - | NULL | - |
| 6 | serie | varchar(255) | NAO | - | NULL | - |
| 7 | tipo_operacao | int | SIM | - | 1 | - |
| 8 | tipo_emissao | int | SIM | - | 1 | - |
| 9 | finalidade | tinyint(1) | NAO | - | 1 | - |
| 10 | indicador_finalidade | varchar(1) | NAO | - | 1 | - |
| 11 | indicador_presencial | varchar(1) | SIM | - | 1 | - |
| 12 | data_hora_emissao | datetime | SIM | - | NULL | - |
| 13 | data_hora_entrada | datetime | SIM | - | NULL | - |
| 14 | natureza | varchar(255) | SIM | - | NULL | - |
| 15 | codigo_natureza | int | SIM | - | NULL | - |
| 16 | cfop_id | int | SIM | - | NULL | - |
| 17 | cobranca_numero_fatura | varchar(60) | SIM | - | NULL | - |
| 18 | cobranca_valor_original | decimal(13,2) | SIM | - | 0.00 | - |
| 19 | cobranca_valor_desconto | decimal(13,2) | SIM | - | 0.00 | - |
| 20 | cobranca_valor_liquido | decimal(13,2) | SIM | - | 0.00 | - |
| 21 | total_frete_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 22 | total_seguro_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 23 | total_valor_outras_despesas | decimal(15,2) | NAO | - | 0.00 | - |
| 24 | total_desconto_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 25 | total_desconto_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 26 | total_icms_base_calculo | decimal(15,2) | SIM | - | NULL | - |
| 27 | total_icms_valor | decimal(15,2) | SIM | - | NULL | - |
| 28 | total_icmsst_base_calculo | decimal(15,2) | SIM | - | NULL | - |
| 29 | total_icmsst_valor | decimal(15,2) | SIM | - | NULL | - |
| 30 | total_produto_valor | decimal(15,2) | SIM | - | NULL | - |
| 31 | total_ipi_valor | decimal(15,2) | SIM | - | NULL | - |
| 32 | total_pis_valor | decimal(15,2) | SIM | - | NULL | - |
| 33 | total_cofins_valor | decimal(15,2) | SIM | - | NULL | - |
| 34 | total_nota_valor | decimal(15,2) | SIM | - | NULL | - |
| 35 | total_tributos_valor | decimal(15,2) | SIM | - | NULL | - |
| 36 | total_icmsdesoneracao_valor | decimal(15,2) | SIM | - | NULL | - |
| 37 | total_icms_uf_destino_valor | decimal(15,2) | SIM | - | NULL | - |
| 38 | total_icms_uf_remetente_valor | decimal(15,2) | SIM | - | NULL | - |
| 39 | total_fcp_uf_destino_valor | decimal(15,2) | SIM | - | NULL | - |
| 40 | indicador_forma_pagamento | enum('0','1','2') | SIM | - | 0 | - |
| 41 | informacoes_adicionais_complementares | text | SIM | - | NULL | - |
| 42 | informacoes_adicionais_fisco | text | SIM | - | NULL | - |
| 43 | identificador_local_destino | int | SIM | - | 1 | - |
| 44 | codigo_nota_fiscal | varchar(255) | SIM | - | NULL | - |
| 45 | chave_dv | int | SIM | - | NULL | - |
| 46 | data_hora_contingencia | datetime | SIM | - | NULL | - |
| 47 | justificativa_contingencia | varchar(255) | SIM | - | NULL | - |
| 48 | ambiente | int | SIM | - | NULL | - |
| 49 | xml | text | SIM | - | NULL | - |
| 50 | xml_recibo_emissao | text | SIM | - | NULL | - |
| 51 | xml_cancelamento | text | SIM | - | NULL | - |
| 52 | justificativa_cancelamento | varchar(255) | SIM | - | NULL | - |
| 53 | recibo_situacao | enum('AGUARDANDO','NAO_ENVIADO','RECEBIDO','CANCELADA','DENEGADA') | SIM | - | NULL | - |
| 54 | lote_emissao | varchar(255) | SIM | - | NULL | - |
| 55 | numero_recibo | varchar(255) | SIM | - | NULL | - |
| 56 | numero_protocolo_autorizacao | varchar(255) | SIM | - | NULL | - |
| 57 | data_hora_protocolo_autorizacao | datetime | SIM | - | NULL | - |
| 58 | inutilizado_em | datetime | SIM | - | NULL | - |
| 59 | rateavel | tinyint(1) | NAO | - | 1 | - |
| 60 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 61 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 62 | deleted_at | timestamp | SIM | - | NULL | - |
| 63 | transportador_modalidade_frete | enum('1','0','2','9') | SIM | - | NULL | - |
| 64 | importacao | smallint | NAO | - | 0 | - |
| 65 | fundo_combate_pobreza | decimal(15,2) | NAO | - | 0.00 | - |
| 66 | nfe_id | int unsigned | SIM | MUL | NULL | - |
| 67 | atualizar_valor_compra | tinyint | NAO | - | 1 | - |
| 68 | subserie | varchar(50) | SIM | - | NULL | - |
| 69 | codigo_grupo_tensao | varchar(10) | SIM | - | NULL | - |
| 70 | tipo_ligacao | varchar(10) | SIM | - | NULL | - |
| 71 | valor_pis | decimal(15,2) | SIM | - | 0.00 | - |
| 72 | valor_cofins | decimal(15,2) | SIM | - | 0.00 | - |
| 73 | valor_fornecido | decimal(15,2) | SIM | - | 0.00 | - |
| 74 | valor_servico_nao_tributado | decimal(15,2) | SIM | - | 0.00 | - |
| 75 | valor_terceiros | decimal(15,2) | SIM | - | 0.00 | - |
| 76 | base_icms_energia | decimal(15,2) | SIM | - | 0.00 | - |
| 77 | aliq_icms_energia | decimal(15,2) | SIM | - | 0.00 | - |
| 78 | valor_icms_energia | decimal(15,2) | SIM | - | 0.00 | - |
| 79 | icms_desonerado_totalizer | tinyint | NAO | - | 0 | - |

### Tabela: compra_destinatario (BASE TABLE)
**Linhas aprox:** 62 | **Colunas:** 24

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | compra_id | int | NAO | MUL | NULL | - |
| 3 | destinatario_cpf_cnpj | varchar(14) | NAO | - | NULL | - |
| 4 | destinatario_id_estrangeiro | varchar(20) | SIM | - | NULL | - |
| 5 | destinatario_nome | varchar(60) | NAO | - | NULL | - |
| 6 | destinatario_endereco | varchar(60) | NAO | - | NULL | - |
| 7 | destinatario_numero | varchar(60) | NAO | - | NULL | - |
| 8 | destinatario_complemento | varchar(60) | SIM | - | NULL | - |
| 9 | destinatario_bairro | varchar(60) | NAO | - | NULL | - |
| 10 | destinatario_codigo_cidade | varchar(7) | NAO | - | NULL | - |
| 11 | destinatario_nome_cidade | varchar(60) | NAO | - | NULL | - |
| 12 | destinatario_uf | enum('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | SIM | - | NULL | - |
| 13 | destinatario_cep | varchar(8) | SIM | - | NULL | - |
| 14 | destinatario_codigo_pais | varchar(4) | NAO | - | NULL | - |
| 15 | destinatario_nome_pais | varchar(60) | SIM | - | NULL | - |
| 16 | destinatario_telefone | varchar(14) | SIM | - | NULL | - |
| 17 | destinatario_indicador_ie | enum('1','2','9') | NAO | - | NULL | - |
| 18 | destinatario_ie | varchar(14) | SIM | - | NULL | - |
| 19 | destinatario_inscricao_suframa | varchar(9) | SIM | - | NULL | - |
| 20 | destinatario_inscricao_municipal | varchar(15) | SIM | - | NULL | - |
| 21 | destinatario_email | varchar(60) | SIM | - | NULL | - |
| 22 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 23 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: compra_emitente (BASE TABLE)
**Linhas aprox:** 62 | **Colunas:** 22

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | compra_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | - | NULL | - |
| 4 | fornecedor_id | int | NAO | - | NULL | - |
| 5 | codigo_uf | varchar(2) | NAO | - | NULL | - |
| 6 | emitente_cnpj | varchar(14) | NAO | - | NULL | - |
| 7 | emitente_nome | varchar(60) | NAO | - | NULL | - |
| 8 | emitente_fantasia | varchar(60) | SIM | - | NULL | - |
| 9 | emitente_endereco | varchar(60) | SIM | - | NULL | - |
| 10 | emitente_numero | varchar(60) | SIM | - | NULL | - |
| 11 | emitente_complemento | varchar(60) | SIM | - | NULL | - |
| 12 | emitente_bairro | varchar(60) | SIM | - | NULL | - |
| 13 | emitente_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 14 | emitente_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 15 | emitente_uf | varchar(2) | SIM | - | NULL | - |
| 16 | emitente_cep | varchar(8) | SIM | - | NULL | - |
| 17 | emitente_telefone | varchar(14) | SIM | - | NULL | - |
| 18 | emitente_inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 19 | emitente_email | varchar(255) | SIM | - | NULL | - |
| 20 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 21 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 22 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: compra_item (BASE TABLE)
**Linhas aprox:** 347 | **Colunas:** 86

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | compra_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | tipo_especifico | enum('VEICULO','MEDICAMENTO','ARMAMENTO','COMBUSTIVEL','PAPEL') | SIM | - | NULL | - |
| 5 | codigo_produto | varchar(60) | SIM | - | NULL | - |
| 6 | codigo_ean | varchar(14) | SIM | - | NULL | - |
| 7 | produto_nome | varchar(255) | NAO | - | NULL | - |
| 8 | ncm | varchar(8) | SIM | - | NULL | - |
| 9 | cst_csosn | varchar(255) | SIM | - | NULL | - |
| 10 | unidade_comercial | varchar(6) | SIM | - | NULL | - |
| 11 | pedido_compra_numero_compra | varchar(15) | SIM | - | NULL | - |
| 12 | pedido_compra_numero_pedido | varchar(6) | SIM | - | NULL | - |
| 13 | quantidade_comercial | decimal(15,4) | SIM | - | NULL | - |
| 14 | valor_unitario_comercial | decimal(12,5) | SIM | - | NULL | - |
| 15 | valor_total_produto | decimal(13,2) | SIM | - | NULL | - |
| 16 | icms_percentual_reducao_base | decimal(15,2) | SIM | - | 0.00 | - |
| 17 | icmsst_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 18 | icmsst_retido_base_calculo | decimal(15,2) | SIM | - | 0.00 | - |
| 19 | icmsst_retido_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 20 | icms_desoneracao_motivo | decimal(15,2) | SIM | - | 0.00 | - |
| 21 | icms_desoneracao_valor | decimal(13,2) | SIM | - | NULL | - |
| 22 | icms_operacao_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 23 | icms_diferimento_percentual | decimal(15,2) | SIM | - | 0.00 | - |
| 24 | icms_diferimento_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 25 | icms_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 26 | ipi_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 27 | ipi_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 28 | ipi_enquadramento | decimal(15,2) | SIM | - | 0.00 | - |
| 29 | tributos_federais | decimal(13,2) | SIM | - | NULL | - |
| 30 | tributos_estaduais | decimal(13,2) | SIM | - | NULL | - |
| 31 | tributos_municipais | decimal(13,2) | SIM | - | NULL | - |
| 32 | total_tributos | decimal(13,2) | SIM | - | NULL | - |
| 33 | cest | varchar(255) | SIM | - | NULL | - |
| 34 | especifico | varchar(255) | SIM | - | NULL | - |
| 35 | cfop | varchar(4) | SIM | - | NULL | - |
| 36 | cfop_item_id | int | NAO | - | NULL | - |
| 37 | icms_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 38 | icmsst_mva | decimal(15,2) | SIM | - | 0.00 | - |
| 39 | icmsst_percentual_reducao_base | decimal(15,2) | SIM | - | 0.00 | - |
| 40 | icmsst_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 41 | pis_cst | varchar(255) | SIM | - | NULL | - |
| 42 | pis_base_calculo | decimal(15,2) | SIM | - | 0.00 | - |
| 43 | pis_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 44 | pis_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 45 | cofins_cst | varchar(2) | SIM | - | NULL | - |
| 46 | cofins_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 47 | cofins_valor | decimal(15,2) | SIM | - | 0.00 | - |
| 48 | icmsdifal_base_calculo_uf_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 49 | icmsdifal_percentual_fcp_uf_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 50 | icmsdifal_percentual_icms_uf_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 51 | icmsdifal_percentual_icms_interestadual | decimal(15,2) | SIM | - | 0.00 | - |
| 52 | icmsdifal_percentual_provisorio_uf_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 53 | icmsdifal_valor_fcp_uf_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 54 | icmsdifal_valor_icms_uf_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 55 | icmsdifal_valor_icms_uf_remetente | decimal(15,2) | SIM | - | 0.00 | - |
| 56 | ipi_cst | varchar(2) | SIM | - | NULL | - |
| 57 | icmsst_base_calculo | decimal(15,2) | SIM | - | 0.00 | - |
| 58 | ipi_base_calculo | decimal(15,2) | SIM | - | 0.00 | - |
| 59 | icms_base_calculo | decimal(15,2) | SIM | - | 0.00 | - |
| 60 | icms_aliquota_credito_simples_nacional | decimal(15,2) | SIM | - | 0.00 | - |
| 61 | icms_valor_credito_simples_nacional | decimal(15,2) | SIM | - | 0.00 | - |
| 62 | rateavel | tinyint(1) | NAO | - | 1 | - |
| 63 | unidade_tributavel | varchar(6) | SIM | - | NULL | - |
| 64 | quantidade_tributavel | decimal(12,2) | SIM | - | NULL | - |
| 65 | valor_unitario_tributavel | decimal(12,2) | SIM | - | NULL | - |
| 66 | valor_total_frete | decimal(15,2) | SIM | - | NULL | - |
| 67 | valor_total_seguro | decimal(15,2) | SIM | - | NULL | - |
| 68 | valor_total_desconto | decimal(15,2) | SIM | - | NULL | - |
| 69 | valor_total_outras_despesas | decimal(15,2) | SIM | - | NULL | - |
| 70 | indicador_total | int | NAO | - | 1 | - |
| 71 | origem | int | NAO | - | 0 | - |
| 72 | icms_modalidade_base_calculo | decimal(15,2) | SIM | - | 0.00 | - |
| 73 | icmsst_modalidade_base_calculo | decimal(15,2) | SIM | - | 0.00 | - |
| 74 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 75 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 76 | deleted_at | timestamp | SIM | - | NULL | - |
| 77 | unidade_medida_xml | varchar(10) | SIM | - | NULL | - |
| 78 | quantidade_xml | decimal(15,2) | SIM | - | NULL | - |
| 79 | fator_conversao | decimal(15,2) | SIM | - | NULL | - |
| 80 | fcp_st_percentual | decimal(15,4) | NAO | - | 0.0000 | - |
| 81 | fcp_st_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 82 | lote_numero | varchar(50) | SIM | - | NULL | - |
| 83 | lote_quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 84 | lote_data_fabricacao | date | SIM | - | NULL | - |
| 85 | lote_data_validade | date | SIM | - | NULL | - |
| 86 | lote_codigo_agregacao | varchar(20) | SIM | - | NULL | - |

### Tabela: compra_item_grade (BASE TABLE)
**Linhas aprox:** 267 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | compra_item_id | int | NAO | MUL | NULL | - |
| 3 | produto_empresa_grade_id | int | NAO | - | NULL | - |
| 4 | quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: compra_observacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | compra_id | int | NAO | MUL | NULL | - |
| 3 | observacao_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: condutor (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(60) | NAO | - | NULL | - |
| 3 | cpf | varchar(11) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: configuracao_bancaria (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 31

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | conta_id | int | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | banco_nome | varchar(255) | NAO | - | NULL | - |
| 5 | codigo_banco | varchar(5) | NAO | - | NULL | - |
| 6 | cnab | varchar(5) | NAO | - | NULL | - |
| 7 | logo | longtext | SIM | - | NULL | - |
| 8 | agencia | varchar(11) | NAO | - | NULL | - |
| 9 | agencia_dv | varchar(2) | NAO | - | NULL | - |
| 10 | conta | varchar(11) | NAO | - | NULL | - |
| 11 | conta_dv | varchar(2) | NAO | - | NULL | - |
| 12 | mora_multa | double(15,2) | NAO | - | NULL | - |
| 13 | juros | double(15,2) | NAO | - | NULL | - |
| 14 | carteira | varchar(11) | NAO | - | NULL | - |
| 15 | sequencial_nosso_numero | int | NAO | - | 1 | - |
| 16 | moeda | int | NAO | - | 9 | - |
| 17 | aceite | varchar(1) | NAO | - | N | - |
| 18 | especie | varchar(15) | NAO | - | REAL | - |
| 19 | convenio | varchar(255) | SIM | - | NULL | - |
| 20 | cip | varchar(255) | SIM | - | NULL | - |
| 21 | emissao | varchar(255) | SIM | - | NULL | - |
| 22 | codigo_cliente | varchar(255) | SIM | - | NULL | - |
| 23 | carteira_dv | varchar(255) | SIM | - | NULL | - |
| 24 | ios | varchar(255) | SIM | - | NULL | - |
| 25 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 26 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 27 | deleted_at | timestamp | SIM | - | NULL | - |
| 28 | protesto | int | SIM | - | NULL | - |
| 29 | devolucao | int | SIM | - | NULL | - |
| 30 | codigo_multa | int | NAO | - | 0 | - |
| 31 | codigo_juros | int | NAO | - | 1 | - |

### Tabela: configuracao_bancaria_ocorrencia (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | financeiro_parcela_id | int | NAO | MUL | NULL | - |
| 3 | boleto_bancario_id | int | NAO | - | NULL | - |
| 4 | numero_ocorrencia | varchar(255) | NAO | - | NULL | - |
| 5 | remessa | int | SIM | - | NULL | - |
| 6 | ocorrencia_retorno | int | SIM | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: consignacao_devolucao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | 1 | - |
| 4 | funcionario_id | int | NAO | MUL | 1 | - |
| 5 | observacao | text | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | venda_id | int | SIM | MUL | NULL | - |
| 10 | finalizada | smallint | NAO | - | 0 | - |

### Tabela: consignacao_devolucao_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | consignacao_devolucao_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | quantidade | decimal(15,4) | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | requisicao_item_id | int | NAO | MUL | NULL | - |
| 10 | quantidade_venda | decimal(15,4) | NAO | - | 0.0000 | - |

### Tabela: consignacao_requisicao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | 1 | - |
| 4 | funcionario_id | int | NAO | MUL | 1 | - |
| 5 | fator_id | int | SIM | MUL | NULL | - |
| 6 | observacao | text | SIM | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | cancelada | tinyint(1) | NAO | - | NULL | - |
| 11 | tipo_preco_id | int unsigned | SIM | MUL | NULL | - |

### Tabela: consignacao_requisicao_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | consignacao_requisicao_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | preco | decimal(15,4) | SIM | - | NULL | - |
| 6 | quantidade | decimal(15,4) | SIM | - | NULL | - |
| 7 | preco_compra | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: conta (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | tipo | enum('caixa','cofre','pix','cartao credito','administradora cartao','conta corrente','conta poupanca','conta emprestimo','conta garantia','carteira virtual','crediario','conta aplicacao') | NAO | - | NULL | - |
| 5 | saldo_inicial | decimal(15,2) | SIM | - | NULL | - |
| 6 | data_saldo_inicial | date | SIM | - | NULL | - |
| 7 | observacao | text | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | pattern | tinyint | NAO | - | 0 | - |
| 12 | permitir_excluir | smallint | NAO | - | 1 | - |
| 13 | visible | smallint | NAO | - | 1 | - |
| 14 | ativo | tinyint(1) | NAO | - | 0 | - |

### Tabela: conta_banco (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 47

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | conta_id | int unsigned | SIM | MUL | NULL | - |
| 3 | banco_id | int | NAO | - | NULL | - |
| 4 | agencia | varchar(4) | NAO | - | NULL | - |
| 5 | agencia_dv | varchar(1) | NAO | - | NULL | - |
| 6 | conta_corrente | varchar(10) | NAO | - | NULL | - |
| 7 | conta_corrente_dv | varchar(1) | NAO | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |
| 11 | recipient_id | char(36) | SIM | - | NULL | - |
| 12 | account_id | char(36) | SIM | - | NULL | - |
| 13 | agreement_id | char(36) | SIM | - | NULL | - |
| 14 | recipient_code | varchar(20) | SIM | - | NULL | - |
| 15 | format_recipient_code | varchar(20) | SIM | - | NULL | - |
| 16 | wallet_code | varchar(3) | SIM | - | NULL | - |
| 17 | wallet_variation | varchar(3) | SIM | - | NULL | - |
| 18 | last_dispatch | int | NAO | - | NULL | - |
| 19 | last_our_number | varchar(50) | NAO | - | NULL | - |
| 20 | format_our_number | varchar(20) | SIM | - | NULL | - |
| 21 | message_1 | text | SIM | - | NULL | - |
| 22 | message_2 | text | SIM | - | NULL | - |
| 23 | accept_code | varchar(2) | SIM | - | NULL | - |
| 24 | species_code | varchar(2) | SIM | - | NULL | - |
| 25 | fine_code | varchar(2) | SIM | - | NULL | - |
| 26 | fine_amount | decimal(15,2) | NAO | - | 0.00 | - |
| 27 | interest_code | varchar(2) | SIM | - | NULL | - |
| 28 | interest_amount | decimal(15,2) | NAO | - | 0.00 | - |
| 29 | low_code | varchar(1) | SIM | - | NULL | - |
| 30 | low_days | varchar(3) | SIM | - | NULL | - |
| 31 | occurrence_code | varchar(2) | SIM | - | NULL | - |
| 32 | protest_code | varchar(1) | SIM | - | NULL | - |
| 33 | protest_days | varchar(3) | SIM | - | NULL | - |
| 34 | discount_code | varchar(2) | SIM | - | NULL | - |
| 35 | discount_amount | decimal(15,2) | SIM | - | 0.00 | - |
| 36 | instruction_one | varchar(3) | SIM | - | NULL | - |
| 37 | instruction_two | varchar(3) | SIM | - | NULL | - |
| 38 | factor_due | int | SIM | - | 0 | - |
| 39 | company_code | varchar(50) | SIM | - | NULL | - |
| 40 | layout_print | varchar(20) | SIM | - | a4 | - |
| 41 | integration_type | varchar(20) | SIM | - | arquivo | - |
| 42 | url_webhook | varchar(255) | SIM | - | NULL | - |
| 43 | client_id | varchar(255) | SIM | - | NULL | - |
| 44 | client_secret | varchar(255) | SIM | - | NULL | - |
| 45 | posto | varchar(2) | SIM | - | NULL | - |
| 46 | type_key_pix | enum('CNPJ','CPF','EMAIL','CELULAR','EVP') | SIM | - | NULL | - |
| 47 | key_pix | varchar(100) | SIM | - | NULL | - |

### Tabela: conta_cartao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | conta_id | int unsigned | SIM | MUL | NULL | - |
| 3 | cartao_credito_id | int | NAO | MUL | NULL | - |
| 4 | conta_baixa_id | int unsigned | SIM | MUL | NULL | - |
| 5 | dia_fechamento | int | NAO | - | NULL | - |
| 6 | dia_vencimento | int | NAO | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: conta_softcompay (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 18

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | senha_supervisor | smallint | NAO | - | 0 | - |
| 3 | ambiente_teste | smallint | NAO | - | 0 | - |
| 4 | client_id | varchar(255) | NAO | - | NULL | - |
| 5 | client_secret | varchar(255) | NAO | - | NULL | - |
| 6 | bank_id | varchar(255) | NAO | - | NULL | - |
| 7 | comerciante_id | varchar(255) | NAO | - | NULL | - |
| 8 | juros_tipo | int | SIM | - | NULL | - |
| 9 | juros | decimal(15,2) | NAO | - | 0.00 | - |
| 10 | multa_tipo | int | SIM | - | NULL | - |
| 11 | multa | decimal(15,2) | NAO | - | 0.00 | - |
| 12 | abatimento_tipo | int | SIM | - | NULL | - |
| 13 | abatimento | decimal(15,2) | NAO | - | 0.00 | - |
| 14 | dias_apos_vencimento | int | SIM | - | NULL | - |
| 15 | conta_id | int unsigned | NAO | MUL | NULL | - |
| 16 | created_at | timestamp | SIM | - | NULL | - |
| 17 | updated_at | timestamp | SIM | - | NULL | - |
| 18 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: contador (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | cpf | varchar(255) | NAO | - | NULL | - |
| 5 | cnpj | varchar(255) | SIM | - | NULL | - |
| 6 | crc | varchar(255) | NAO | - | NULL | - |
| 7 | fone | varchar(255) | SIM | - | NULL | - |
| 8 | fax | varchar(255) | SIM | - | NULL | - |
| 9 | email | varchar(255) | NAO | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: contato (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | tipo | enum('PRINCIPAL','OUTROS') | NAO | - | OUTROS | - |
| 3 | cliente_id | int | SIM | MUL | NULL | - |
| 4 | fornecedor_id | int | SIM | MUL | NULL | - |
| 5 | funcionario_id | int | SIM | MUL | NULL | - |
| 6 | transportador_id | int | SIM | MUL | NULL | - |
| 7 | indicador_id | int | SIM | MUL | NULL | - |
| 8 | nome | varchar(100) | SIM | - | NULL | - |
| 9 | ddd | varchar(4) | SIM | - | NULL | - |
| 10 | telefone | varchar(10) | SIM | - | NULL | - |
| 11 | email | varchar(255) | SIM | - | NULL | - |
| 12 | nascimento | date | SIM | - | NULL | - |
| 13 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |
| 16 | ativar_notificacao | tinyint | NAO | - | 0 | - |

### Tabela: contrato_modelo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | texto | text | SIM | - | NULL | - |
| 4 | deleted_at | timestamp | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: contrato_servico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | 1 | - |
| 3 | cliente_id | int | NAO | MUL | NULL | - |
| 4 | funcionario_id | int | NAO | MUL | NULL | - |
| 5 | nfse_id | int | SIM | MUL | NULL | - |
| 6 | dia_cobranca | int | NAO | - | NULL | - |
| 7 | termino_vigencia | enum('DATA_ESPECIFICA','RECORRENTE') | NAO | - | NULL | - |
| 8 | data_termino | date | SIM | - | NULL | - |
| 9 | data_encerramento | date | SIM | - | NULL | - |
| 10 | usuario_encerramento_id | int unsigned | SIM | MUL | NULL | - |
| 11 | motivo_encerramento | text | SIM | - | NULL | - |
| 12 | status | enum('ENCERRADO','VIGENTE') | SIM | - | VIGENTE | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |
| 14 | created_at | timestamp | SIM | - | NULL | - |
| 15 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: contrato_servico_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | contrato_servico_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | descricao | varchar(255) | SIM | - | NULL | - |
| 6 | quantidade | decimal(15,2) | NAO | - | 0.00 | - |
| 7 | preco | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | desconto_valor_item | decimal(15,2) | NAO | - | 0.00 | - |
| 9 | acrescimo_valor_item | decimal(15,2) | NAO | - | 0.00 | - |
| 10 | percentual_desconto | decimal(15,10) | SIM | - | NULL | - |
| 11 | percentual_acrescimo | decimal(15,10) | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |
| 13 | created_at | timestamp | SIM | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: cotacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 18

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | data_cotacao | date | NAO | - | NULL | - |
| 3 | hora_cotacao | datetime | NAO | - | NULL | - |
| 4 | empresa_id | int | NAO | MUL | NULL | - |
| 5 | fornecedor_id | int | NAO | MUL | 1 | - |
| 6 | funcionario_id | int | NAO | MUL | 1 | - |
| 7 | transportadora_id | int | NAO | MUL | 1 | - |
| 8 | tipo_frete | enum('CIF','FOB') | NAO | - | CIF | - |
| 9 | meses_reposicao | int | NAO | - | 1 | - |
| 10 | numero_pedido | varchar(50) | SIM | - | NULL | - |
| 11 | condicao_pagamento | varchar(50) | SIM | - | NULL | - |
| 12 | garantia | varchar(50) | SIM | - | NULL | - |
| 13 | chegada | date | SIM | - | NULL | - |
| 14 | observacao | text | SIM | - | NULL | - |
| 15 | nao_mostrar_preco | int | NAO | - | 0 | - |
| 16 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 17 | updated_at | timestamp | SIM | - | NULL | - |
| 18 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cotacao_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cotacao_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | preco | decimal(15,2) | SIM | - | NULL | - |
| 6 | quantidade | decimal(15,2) | SIM | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: credenciadora (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(128) | NAO | - | NULL | - |
| 3 | cnpj | varchar(14) | SIM | - | NULL | - |
| 4 | empresa_id | int | NAO | MUL | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | inscricao_estadual | varchar(50) | SIM | - | NULL | - |
| 9 | suframa | varchar(9) | SIM | - | NULL | - |
| 10 | ponto_venda | varchar(255) | SIM | - | NULL | - |
| 11 | conta_banco_id | int | SIM | MUL | NULL | - |

### Tabela: cte (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 49

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | serie | varchar(3) | NAO | - | NULL | - |
| 4 | numero | int unsigned | NAO | - | NULL | - |
| 5 | chave_acesso | char(44) | SIM | - | NULL | - |
| 6 | data_emissao | datetime | NAO | - | NULL | - |
| 7 | tipo_servico | tinyint unsigned | NAO | - | NULL | - |
| 8 | tipo_cte | tinyint unsigned | NAO | - | NULL | - |
| 9 | tipo_impressao | tinyint unsigned | NAO | - | NULL | - |
| 10 | forma_emissao | tinyint unsigned | NAO | - | NULL | - |
| 11 | ambiente | tinyint unsigned | NAO | - | NULL | - |
| 12 | cfop | varchar(5) | NAO | - | NULL | - |
| 13 | natureza_operacao | varchar(60) | NAO | - | NULL | - |
| 14 | tomador | tinyint unsigned | NAO | - | NULL | - |
| 15 | uf_envio | char(2) | NAO | - | NULL | - |
| 16 | municipio_envio | varchar(60) | NAO | - | NULL | - |
| 17 | cod_municipio_envio | varchar(7) | NAO | - | NULL | - |
| 18 | uf_inicio | char(2) | NAO | - | NULL | - |
| 19 | municipio_inicio | varchar(60) | NAO | - | NULL | - |
| 20 | cod_municipio_inicio | varchar(7) | NAO | - | NULL | - |
| 21 | uf_fim | char(2) | NAO | - | NULL | - |
| 22 | municipio_fim | varchar(60) | NAO | - | NULL | - |
| 23 | cod_municipio_fim | varchar(7) | NAO | - | NULL | - |
| 24 | rota_envio_use_empresa | tinyint(1) | NAO | - | 0 | - |
| 25 | rota_inicio_use_remetente | tinyint(1) | NAO | - | 0 | - |
| 26 | indicador_globalizado | tinyint(1) | SIM | - | NULL | - |
| 27 | retira_no_destino | tinyint(1) | SIM | - | NULL | - |
| 28 | detalhe_retirada | varchar(160) | SIM | - | NULL | - |
| 29 | chave_cte_referenciado | char(44) | SIM | - | NULL | - |
| 30 | tabela_frete_id | bigint unsigned | SIM | MUL | NULL | - |
| 31 | valor_total_prestacao | decimal(15,2) | NAO | - | NULL | - |
| 32 | valor_a_receber | decimal(15,2) | NAO | - | NULL | - |
| 33 | valor_total_cte | decimal(15,2) | NAO | - | NULL | - |
| 34 | status | tinyint unsigned | NAO | - | NULL | - |
| 35 | response_codigo_status | smallint unsigned | SIM | - | NULL | - |
| 36 | response_motivo | text | SIM | - | NULL | - |
| 37 | response_protocolo | varchar(20) | SIM | - | NULL | - |
| 38 | response_data_recebimento | datetime | SIM | - | NULL | - |
| 39 | response_transmitido_em | datetime | SIM | - | NULL | - |
| 40 | response_xml_resposta | text | SIM | - | NULL | - |
| 41 | response_xml_link | text | SIM | - | NULL | - |
| 42 | response_pdf_link | text | SIM | - | NULL | - |
| 43 | response_cte_id | varchar(255) | SIM | - | NULL | - |
| 44 | observacoes | text | SIM | - | NULL | - |
| 45 | caracteristica_servico | varchar(30) | SIM | - | NULL | - |
| 46 | caracteristica_transporte | varchar(30) | SIM | - | NULL | - |
| 47 | created_at | timestamp | SIM | - | NULL | - |
| 48 | updated_at | timestamp | SIM | - | NULL | - |
| 49 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_carga (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | UNI | NULL | - |
| 3 | produto_predominante | varchar(60) | NAO | - | NULL | - |
| 4 | outras_caracteristicas | varchar(30) | SIM | - | NULL | - |
| 5 | valor_carga | decimal(15,2) | NAO | - | NULL | - |
| 6 | valor_averbacao | decimal(15,2) | SIM | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_carta_correcao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | sequencial | tinyint unsigned | NAO | - | NULL | - |
| 4 | correcao_json | text | NAO | - | NULL | - |
| 5 | protocolo | varchar(20) | SIM | - | NULL | - |
| 6 | codigo_status | smallint unsigned | SIM | - | NULL | - |
| 7 | motivo | varchar(255) | SIM | - | NULL | - |
| 8 | data_registro | datetime | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_componente_frete (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | nome_componente | varchar(15) | NAO | - | NULL | - |
| 4 | valor | decimal(15,2) | NAO | - | NULL | - |
| 5 | ordem | tinyint unsigned | NAO | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_documento_nfe (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | chave_nfe | char(44) | NAO | - | NULL | - |
| 4 | pin | varchar(8) | SIM | - | NULL | - |
| 5 | data_prevista | date | SIM | - | NULL | - |
| 6 | origem | varchar(10) | NAO | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_documento_outro (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | tipo_documento | varchar(5) | NAO | - | NULL | - |
| 4 | descricao | varchar(100) | SIM | - | NULL | - |
| 5 | numero | varchar(20) | SIM | - | NULL | - |
| 6 | data_emissao | date | SIM | - | NULL | - |
| 7 | valor | decimal(15,2) | SIM | - | NULL | - |
| 8 | subtipo | varchar(20) | NAO | - | NULL | - |
| 9 | forma_emissao | varchar(20) | SIM | - | NULL | - |
| 10 | chave_acesso | varchar(44) | SIM | - | NULL | - |
| 11 | cnpj_emitente_anterior | varchar(18) | SIM | - | NULL | - |
| 12 | uf_emitente_anterior | char(2) | SIM | - | NULL | - |
| 13 | created_at | timestamp | SIM | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_empresa_config (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | empresa_id | int | NAO | PRI | NULL | - |
| 2 | serie | varchar(3) | NAO | - | 1 | - |
| 3 | proximo_numero | int unsigned | NAO | - | 1 | - |
| 4 | cfop_id | int | SIM | MUL | NULL | - |
| 5 | ambiente | tinyint unsigned | NAO | - | 2 | - |
| 6 | forma_emissao | tinyint unsigned | NAO | - | 1 | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_evento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | tipo | varchar(60) | NAO | - | NULL | - |
| 4 | descricao | text | SIM | - | NULL | - |
| 5 | codigo_status | smallint unsigned | SIM | - | NULL | - |
| 6 | protocolo | varchar(30) | SIM | - | NULL | - |
| 7 | pdf_link | text | SIM | - | NULL | - |
| 8 | xml_link | text | SIM | - | NULL | - |
| 9 | payload_json | text | SIM | - | NULL | - |
| 10 | response_json | text | SIM | - | NULL | - |
| 11 | data_registro | datetime | SIM | - | NULL | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_icms (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 23

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | UNI | NULL | - |
| 3 | cst | varchar(10) | NAO | - | NULL | - |
| 4 | perc_reducao_bc | decimal(5,2) | SIM | - | NULL | - |
| 5 | base_calculo | decimal(15,2) | SIM | - | NULL | - |
| 6 | aliquota | decimal(5,2) | SIM | - | NULL | - |
| 7 | valor_icms | decimal(15,2) | SIM | - | NULL | - |
| 8 | valor_credito | decimal(15,2) | SIM | - | NULL | - |
| 9 | bc_st_retido | decimal(15,2) | SIM | - | NULL | - |
| 10 | valor_st_retido | decimal(15,2) | SIM | - | NULL | - |
| 11 | aliquota_st_retido | decimal(5,2) | SIM | - | NULL | - |
| 12 | ind_sn | tinyint(1) | SIM | - | NULL | - |
| 13 | difal_ativo | tinyint(1) | SIM | - | NULL | - |
| 14 | difal_bc_uf_fim | decimal(15,2) | SIM | - | NULL | - |
| 15 | difal_aliq_uf_fim | decimal(5,2) | SIM | - | NULL | - |
| 16 | difal_aliq_interestadual | decimal(5,2) | SIM | - | NULL | - |
| 17 | difal_valor_uf_ini | decimal(15,2) | SIM | - | NULL | - |
| 18 | difal_valor_uf_fim | decimal(15,2) | SIM | - | NULL | - |
| 19 | cst_ibs_cbs | varchar(20) | SIM | - | NULL | - |
| 20 | cod_class_trib | varchar(20) | SIM | - | NULL | - |
| 21 | created_at | timestamp | SIM | - | NULL | - |
| 22 | updated_at | timestamp | SIM | - | NULL | - |
| 23 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_modal_rodoviario (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | UNI | NULL | - |
| 3 | transportador_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_occ (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | serie | varchar(3) | SIM | - | NULL | - |
| 4 | numero | int unsigned | NAO | - | NULL | - |
| 5 | cnpj_emitente | varchar(18) | NAO | - | NULL | - |
| 6 | inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 7 | data_emissao | date | NAO | - | NULL | - |
| 8 | uf_emitente | char(2) | NAO | - | NULL | - |
| 9 | codigo_interno | varchar(10) | SIM | - | NULL | - |
| 10 | telefone | varchar(15) | SIM | - | NULL | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_participante (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 24

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | cliente_id | int | SIM | MUL | NULL | - |
| 4 | papel | varchar(20) | NAO | - | NULL | - |
| 5 | tipo_documento | char(4) | NAO | - | NULL | - |
| 6 | cpf_cnpj | varchar(18) | NAO | MUL | NULL | - |
| 7 | razao_social | varchar(60) | NAO | - | NULL | - |
| 8 | nome | varchar(60) | SIM | - | NULL | - |
| 9 | tipo_contribuinte | tinyint unsigned | NAO | - | NULL | - |
| 10 | inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 11 | telefone | varchar(12) | SIM | - | NULL | - |
| 12 | email | varchar(60) | SIM | - | NULL | - |
| 13 | end_logradouro | varchar(60) | NAO | - | NULL | - |
| 14 | end_numero | varchar(60) | NAO | - | NULL | - |
| 15 | end_complemento | varchar(60) | SIM | - | NULL | - |
| 16 | end_bairro | varchar(60) | NAO | - | NULL | - |
| 17 | end_cep | char(8) | NAO | - | NULL | - |
| 18 | end_municipio | varchar(60) | NAO | - | NULL | - |
| 19 | end_cod_municipio | varchar(7) | NAO | - | NULL | - |
| 20 | end_uf | char(2) | NAO | - | NULL | - |
| 21 | end_pais | varchar(4) | NAO | - | 1058 | - |
| 22 | created_at | timestamp | SIM | - | NULL | - |
| 23 | updated_at | timestamp | SIM | - | NULL | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_quantidade (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cte_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | unidade | varchar(10) | NAO | - | NULL | - |
| 4 | tipo_medida | varchar(20) | NAO | - | NULL | - |
| 5 | quantidade | decimal(11,4) | NAO | - | NULL | - |
| 6 | ordem | tinyint unsigned | NAO | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_tabela_frete (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(60) | NAO | - | NULL | - |
| 4 | uf_origem | char(2) | NAO | - | NULL | - |
| 5 | uf_destino | char(2) | NAO | - | NULL | - |
| 6 | peso_minimo | decimal(11,3) | SIM | - | NULL | - |
| 7 | peso_maximo | decimal(11,3) | SIM | - | NULL | - |
| 8 | data_inicio_vigencia | date | NAO | - | NULL | - |
| 9 | data_fim_vigencia | date | SIM | - | NULL | - |
| 10 | ativa | tinyint(1) | NAO | - | 1 | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: cte_tabela_frete_componente (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tabela_frete_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | nome | varchar(15) | NAO | - | NULL | - |
| 4 | valor | decimal(15,2) | NAO | - | NULL | - |
| 5 | ordem | tinyint unsigned | NAO | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: documento_fiscal_csc (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | token | varchar(36) | NAO | - | NULL | - |
| 4 | token_id | varchar(6) | NAO | - | NULL | - |
| 5 | padrao | tinyint | NAO | - | 0 | - |
| 6 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: empresa (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 40

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_email_id | int | SIM | - | NULL | - |
| 3 | cnpj | varchar(18) | NAO | MUL | NULL | - |
| 4 | inscricao_estadual | varchar(50) | SIM | - | NULL | - |
| 5 | inscricao_estadual_st | varchar(50) | SIM | - | NULL | - |
| 6 | inscricao_municipal | varchar(50) | SIM | - | NULL | - |
| 7 | nome | varchar(50) | NAO | - | NULL | - |
| 8 | fantasia | varchar(255) | NAO | MUL | NULL | - |
| 9 | razao_social | varchar(255) | NAO | MUL | NULL | - |
| 10 | ddd | varchar(4) | SIM | - | NULL | - |
| 11 | telefone | varchar(100) | SIM | - | NULL | - |
| 12 | email | varchar(255) | SIM | - | NULL | - |
| 13 | habilitar_emitir_nfe | enum('SIM','NAO') | NAO | - | NAO | - |
| 14 | sms_usuario | varchar(100) | SIM | - | NULL | - |
| 15 | sms_senha | varchar(100) | SIM | - | NULL | - |
| 16 | suporte_codigo | int | NAO | - | 0 | - |
| 17 | suporte_senha | varchar(50) | NAO | - | 1234 | - |
| 18 | preco_atacado | enum('PADRAO','A','B','C') | NAO | - | PADRAO | - |
| 19 | nome_impressao | enum('FANTASIA','RAZAO') | NAO | - | FANTASIA | - |
| 20 | mensagem_pedido | text | SIM | - | NULL | - |
| 21 | habilitar_mensagem_pedido | tinyint | NAO | - | 0 | - |
| 22 | nfe_ambiente | enum('1','2') | NAO | - | 2 | - |
| 23 | nfe_layout | enum('2.00','3.10') | NAO | - | 3.10 | - |
| 24 | nfe_serie | int | NAO | - | 1 | - |
| 25 | nfe_tipoemissao_id | int | NAO | MUL | NULL | - |
| 26 | nfe_codigo_uf | int | NAO | - | 25 | - |
| 27 | nuvem_nfe_empresa_id | int | SIM | - | NULL | - |
| 28 | certificado_nome | varchar(255) | SIM | - | NULL | - |
| 29 | logomarca | varchar(255) | SIM | - | NULL | - |
| 30 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 31 | updated_at | timestamp | SIM | - | NULL | - |
| 32 | deleted_at | timestamp | SIM | - | NULL | - |
| 33 | troca_prazo | int | SIM | - | NULL | - |
| 34 | troca_mensagem | longtext | SIM | - | NULL | - |
| 35 | mfe_chave_validador | varchar(50) | SIM | - | NULL | - |
| 36 | softcom_service_guid | char(36) | SIM | - | NULL | - |
| 37 | tipo_inventario | varchar(10) | NAO | - | CONTABIL | - |
| 38 | formacao_preco | varchar(10) | NAO | - | padrao | - |
| 39 | cartao_cadastro_proprio | tinyint | NAO | - | 0 | - |
| 40 | timezone | varchar(255) | NAO | - | America/Recife | - |

### Tabela: empresa_balanca_configuracao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | tam_codigo | enum('4','5','6') | SIM | - | NULL | - |
| 4 | info_impressao | enum('PRECO','QUANTIDADE') | SIM | - | NULL | - |
| 5 | ativar | tinyint | NAO | - | 0 | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: empresa_email (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | alias | varchar(255) | SIM | - | NULL | - |
| 4 | driver | varchar(255) | SIM | - | NULL | - |
| 5 | host | varchar(255) | SIM | - | NULL | - |
| 6 | port | varchar(255) | SIM | - | NULL | - |
| 7 | encryption | varchar(255) | SIM | - | NULL | - |
| 8 | username | varchar(255) | SIM | - | NULL | - |
| 9 | password | varchar(255) | SIM | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: empresa_mfe_adquirente (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | credenciadora_id | int unsigned | NAO | MUL | NULL | - |
| 4 | adquirente_descricao | varchar(50) | SIM | - | NULL | - |
| 5 | cnpj_adquirente | varchar(50) | SIM | - | NULL | - |
| 6 | chave_requisicao | varchar(50) | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: empresa_mfe_pos (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | credenciadora_id | int unsigned | NAO | MUL | NULL | - |
| 4 | descricao | varchar(50) | SIM | - | NULL | - |
| 5 | serial | varchar(50) | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: empresa_venda_configuracao (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | tipo_comissao | enum('PRODUTO','VENDEDOR') | NAO | - | VENDEDOR | - |
| 4 | nome_destinatario_impressao | enum('NOME_FANTASIA','RAZAO_SOCIAL') | NAO | - | NOME_FANTASIA | - |
| 5 | agrupar_pagamentos_impressao | tinyint | NAO | - | 1 | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | taxa_servico | decimal(15,2) | NAO | - | 0.00 | - |

### Tabela: endereco (BASE TABLE)
**Linhas aprox:** 16 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | tipo | enum('COBRANCA','TRABALHO','ENTREGA','PRINCIPAL','OUTRO') | NAO | - | OUTRO | - |
| 3 | empresa_id | int | SIM | MUL | NULL | - |
| 4 | funcionario_id | int | SIM | MUL | NULL | - |
| 5 | cliente_id | int | SIM | MUL | NULL | - |
| 6 | fornecedor_id | int | SIM | MUL | NULL | - |
| 7 | transportador_id | int | SIM | MUL | NULL | - |
| 8 | contador_id | int | SIM | MUL | NULL | - |
| 9 | indicador_id | int | SIM | MUL | NULL | - |
| 10 | cep | varchar(9) | SIM | - | NULL | - |
| 11 | endereco | varchar(255) | SIM | - | NULL | - |
| 12 | numero | varchar(10) | SIM | - | NULL | - |
| 13 | complemento | varchar(255) | SIM | - | NULL | - |
| 14 | ponto_referencia | varchar(255) | SIM | - | NULL | - |
| 15 | bairro | varchar(255) | SIM | - | NULL | - |
| 16 | cidade_id | int | SIM | MUL | NULL | - |
| 17 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 18 | updated_at | timestamp | SIM | - | NULL | - |
| 19 | deleted_at | timestamp | SIM | - | NULL | - |
| 20 | credenciadora_id | int unsigned | SIM | MUL | NULL | - |
| 21 | laboratorio_id | int unsigned | SIM | MUL | NULL | - |

### Tabela: equipamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: etiqueta_configuracao (BASE TABLE)
**Linhas aprox:** 10 | **Colunas:** 22

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | observacao | longtext | SIM | - | NULL | - |
| 5 | tipo_papel | enum('A4','CARTA','PERSONALIZADO') | NAO | - | NULL | - |
| 6 | papel_altura | decimal(15,2) | NAO | - | 0.00 | - |
| 7 | papel_largura | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | margem_superior | decimal(15,2) | NAO | - | 0.00 | - |
| 9 | margem_inferior | decimal(15,2) | NAO | - | 0.00 | - |
| 10 | margem_esquerda | decimal(15,2) | NAO | - | 0.00 | - |
| 11 | margem_direita | decimal(15,2) | NAO | - | 0.00 | - |
| 12 | etiqueta_altura | decimal(15,2) | NAO | - | 0.00 | - |
| 13 | etiqueta_largura | decimal(15,2) | NAO | - | 0.00 | - |
| 14 | quantidade_colunas | decimal(15,2) | NAO | - | 0.00 | - |
| 15 | espacamento_colunas | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | espacamento_linhas | decimal(15,2) | NAO | - | 0.00 | - |
| 17 | padrao | smallint | NAO | - | 0 | - |
| 18 | ativa | smallint | NAO | - | 1 | - |
| 19 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 20 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |
| 22 | tipo | enum('COM_BARRAS','SEM_BARRAS','GONDOLA_COM_BARRAS','GONDOLA_COM_BARRAS_QRCODE','GONDOLA_PRECO_PROMOCIONAL','GONDOLA_PRECO_PADRAO','NOTA_VOLUMES_SEM_BARRAS','NOTA_VOLUMES','PRODUTOS_QRCODE','JOIA_OTICA_TABELA') | NAO | - | NULL | - |

### Tabela: etiqueta_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | produto_empresa_grade_id | int | NAO | - | NULL | - |
| 4 | quantidade | decimal(15,2) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: fabricante (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | MUL | NULL | - |
| 3 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: failed_jobs (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | connection | text | NAO | - | NULL | - |
| 3 | queue | text | NAO | - | NULL | - |
| 4 | payload | longtext | NAO | - | NULL | - |
| 5 | exception | longtext | NAO | - | NULL | - |
| 6 | failed_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |

### Tabela: fator_acrescimo_configuracao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | percentual | decimal(15,4) | NAO | - | NULL | - |
| 4 | ativo | tinyint | NAO | - | 1 | - |
| 5 | empresa_id | int | SIM | MUL | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro (BASE TABLE)
**Linhas aprox:** 116 | **Colunas:** 26

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | data_lancamento | date | NAO | - | NULL | - |
| 4 | categoria_id | int | NAO | MUL | NULL | - |
| 5 | documento | varchar(20) | SIM | - | NULL | - |
| 6 | historico | varchar(255) | NAO | - | NULL | - |
| 7 | fornecedor_id | int | SIM | MUL | NULL | - |
| 8 | cliente_id | int | SIM | MUL | NULL | - |
| 9 | contrato_servico_id | int | SIM | MUL | NULL | - |
| 10 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |
| 13 | valor | decimal(15,4) | NAO | - | NULL | - |
| 14 | tipo_documento_id | int unsigned | SIM | MUL | NULL | - |
| 15 | origem | varchar(50) | SIM | - | NULL | - |
| 16 | device_id | varchar(255) | SIM | - | NULL | - |
| 17 | usuario_lancamento_id | int unsigned | SIM | MUL | NULL | - |
| 18 | api_device_id | varchar(255) | SIM | - | NULL | - |
| 19 | repeticao | enum('FIXA','PARCELADA') | NAO | - | NULL | - |
| 20 | repeticao_tipo | enum('Mensal','Bimestral','Trimestral','Semestral','Anual','Intervalo') | NAO | - | NULL | - |
| 21 | repeticao_quantidade | int | NAO | - | NULL | - |
| 22 | repeticao_intervalo | int | NAO | - | NULL | - |
| 23 | termino_vigencia | enum('DATA_ESPECIFICA','RECORRENTE') | NAO | - | NULL | - |
| 24 | data_termino_vigencia | date | SIM | - | NULL | - |
| 25 | lancamento_troco | tinyint | NAO | - | 0 | - |
| 26 | transferencia_grupo_id | char(36) | SIM | - | NULL | - |

### Tabela: financeiro_categoria (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 17

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | code | varchar(20) | NAO | - | NULL | - |
| 3 | name | varchar(255) | NAO | - | NULL | - |
| 4 | tag | varchar(255) | NAO | - | NULL | - |
| 5 | parent_id | int | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | fixed | int | NAO | - | NULL | - |
| 10 | root | int | NAO | - | NULL | - |
| 11 | color | char(7) | NAO | - | NULL | - |
| 12 | permitir_excluir | smallint | NAO | - | 1 | - |
| 13 | nao_exibir_dre | smallint | NAO | - | 0 | - |
| 14 | descricao_original | varchar(255) | SIM | - | NULL | - |
| 15 | segmento | varchar(30) | SIM | - | NULL | - |
| 16 | conta_dre_id | int unsigned | SIM | MUL | NULL | - |
| 17 | ativo | smallint | NAO | - | 1 | - |

### Tabela: financeiro_categoria_conta_dre (BASE TABLE)
**Linhas aprox:** 32 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(100) | NAO | UNI | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_categoria_segmento (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 17

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | NULL | - |
| 2 | code | varchar(20) | NAO | - | NULL | - |
| 3 | name | varchar(255) | NAO | - | NULL | - |
| 4 | tag | varchar(255) | NAO | - | NULL | - |
| 5 | parent_id | int | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | fixed | int | NAO | - | NULL | - |
| 10 | root | int | NAO | - | NULL | - |
| 11 | color | char(7) | NAO | - | NULL | - |
| 12 | permitir_excluir | smallint | NAO | - | 1 | - |
| 13 | nao_exibir_dre | smallint | NAO | - | 0 | - |
| 14 | descricao_original | varchar(255) | SIM | - | NULL | - |
| 15 | segmento | varchar(30) | SIM | - | NULL | - |
| 16 | conta_dre_id | int unsigned | SIM | - | NULL | - |
| 17 | ativo | smallint | NAO | - | 1 | - |

### Tabela: financeiro_centro_custo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | financeiro_parcela_id | int | NAO | MUL | NULL | - |
| 2 | centro_custo_id | int | NAO | MUL | NULL | - |
| 3 | percentual | decimal(15,2) | NAO | - | NULL | - |
| 4 | deleted_at | timestamp | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_condicao_pagamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | description | varchar(255) | NAO | - | NULL | - |
| 3 | forma_pagamento_id | bigint unsigned | NAO | MUL | NULL | - |
| 4 | discount | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | active | tinyint(1) | NAO | - | 1 | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_condicao_pagamento_parcela (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | financeiro_condicao_pagamento_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | order | int unsigned | NAO | - | 1 | - |
| 4 | days | int unsigned | NAO | - | 0 | - |
| 5 | acrescimo | decimal(15,2) | NAO | - | 0.00 | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_extrato_bancario (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 22

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tipo | varchar(255) | NAO | - | NULL | - |
| 3 | data | date | NAO | - | NULL | - |
| 4 | valor | decimal(15,2) | NAO | - | NULL | - |
| 5 | operacao | varchar(20) | NAO | - | NULL | - |
| 6 | banco | varchar(255) | SIM | - | NULL | - |
| 7 | banco_codigo | varchar(255) | SIM | - | NULL | - |
| 8 | banco_agencia | varchar(255) | SIM | - | NULL | - |
| 9 | banco_agencia_dv | varchar(255) | SIM | - | NULL | - |
| 10 | banco_conta | varchar(255) | SIM | - | NULL | - |
| 11 | banco_conta_dv | varchar(255) | SIM | - | NULL | - |
| 12 | credenciadora | varchar(255) | SIM | - | NULL | - |
| 13 | bandeira | varchar(255) | SIM | - | NULL | - |
| 14 | bandeira_tipo | varchar(255) | SIM | - | NULL | - |
| 15 | identificador_transacao | varchar(255) | NAO | - | NULL | - |
| 16 | numero_checagem | varchar(255) | NAO | - | NULL | - |
| 17 | descricao | longtext | SIM | - | NULL | - |
| 18 | conciliado | smallint | NAO | - | 0 | - |
| 19 | empresa_id | int | NAO | MUL | NULL | - |
| 20 | created_at | timestamp | SIM | - | NULL | - |
| 21 | updated_at | timestamp | SIM | - | NULL | - |
| 22 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_parcela (BASE TABLE)
**Linhas aprox:** 116 | **Colunas:** 60

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | compra_id | int | SIM | MUL | NULL | - |
| 3 | venda_id | int | SIM | MUL | NULL | - |
| 4 | financeiro_id | int | SIM | MUL | NULL | - |
| 5 | transferencia_id | int | SIM | - | NULL | - |
| 6 | fornecedor_id | int | SIM | MUL | NULL | - |
| 7 | cliente_id | int | SIM | MUL | NULL | - |
| 8 | contrato_servico_id | int | SIM | MUL | NULL | - |
| 9 | documento | varchar(50) | SIM | - | NULL | - |
| 10 | forma_pagamento_id | int | NAO | MUL | NULL | - |
| 11 | conta_id | int | SIM | - | NULL | - |
| 12 | cartao_credito_id | int | SIM | MUL | NULL | - |
| 13 | venda_cartao_id | int unsigned | SIM | MUL | NULL | - |
| 14 | api_codigo_pagamento | varchar(255) | SIM | - | NULL | - |
| 15 | api_nome_pagamento | varchar(255) | SIM | - | NULL | - |
| 16 | parcela | varchar(255) | SIM | - | NULL | - |
| 17 | cheque_agenciabancaria_id | int | SIM | MUL | NULL | - |
| 18 | cheque_agencia | varchar(10) | SIM | - | NULL | - |
| 19 | cheque_conta | varchar(15) | SIM | - | NULL | - |
| 20 | cheque_numero | varchar(10) | SIM | - | NULL | - |
| 21 | cheque_emitente | varchar(255) | SIM | - | NULL | - |
| 22 | cheque_devolucao_data | date | SIM | - | NULL | - |
| 23 | cheque_devolucao_motivo | int | SIM | - | NULL | - |
| 24 | vencimento | date | NAO | - | NULL | - |
| 25 | valor_parcela | decimal(15,4) | NAO | - | NULL | - |
| 26 | tarifa | decimal(15,2) | SIM | - | NULL | - |
| 27 | duplicata_pendente | int | NAO | - | 0 | - |
| 28 | banco_id | int | SIM | MUL | NULL | - |
| 29 | forma_pagamento_baixa_id | int | SIM | - | NULL | - |
| 30 | financeira_id | int | SIM | MUL | NULL | - |
| 31 | data_pagamento | date | SIM | - | NULL | - |
| 32 | valor_pago | decimal(15,4) | SIM | - | NULL | - |
| 33 | data_caixa | date | SIM | - | NULL | - |
| 34 | observacao | varchar(255) | SIM | - | NULL | - |
| 35 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 36 | updated_at | timestamp | SIM | - | NULL | - |
| 37 | deleted_at | timestamp | SIM | - | NULL | - |
| 38 | acrescimo | decimal(15,4) | SIM | - | 0.0000 | - |
| 39 | desconto | decimal(15,4) | SIM | - | 0.0000 | - |
| 40 | cancelada | tinyint(1) | NAO | - | 0 | - |
| 41 | parcela_vinculada | int | SIM | - | NULL | - |
| 42 | operacao | enum('DEBITO','CREDITO') | SIM | - | NULL | - |
| 43 | empresa_id | int | SIM | - | NULL | - |
| 44 | user_id | int unsigned | SIM | MUL | NULL | - |
| 45 | motivo_cancelamento | longtext | SIM | - | NULL | - |
| 46 | cheque_banco | varchar(255) | SIM | - | NULL | - |
| 47 | data_cancelamento | timestamp | SIM | - | NULL | - |
| 48 | guid | char(36) | SIM | - | NULL | - |
| 49 | pos_habilitar | smallint | SIM | - | 0 | - |
| 50 | tp_integra | bigint | SIM | - | NULL | - |
| 51 | api_cobranca_id | char(36) | SIM | - | NULL | - |
| 52 | api_cobranca_agreemente_id | char(36) | SIM | - | NULL | - |
| 53 | codigo_autorizacao | varchar(50) | SIM | - | NULL | - |
| 54 | cnpj_instituicao_financeira | varchar(50) | SIM | - | NULL | - |
| 55 | cartao_credito_taxa_admin | decimal(15,2) | SIM | - | NULL | - |
| 56 | tipo_debito_id | int | SIM | MUL | NULL | - |
| 57 | conciliacao_extrato_bancario | smallint | NAO | - | 0 | - |
| 58 | caixa_funcoes_id | int | SIM | MUL | NULL | - |
| 59 | financeiro_condicao_pagamento_id | bigint unsigned | SIM | MUL | NULL | - |
| 60 | condicao_pagamento_id | bigint unsigned | SIM | MUL | NULL | - |

### Tabela: financeiro_parcela_arquivo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int | NAO | MUL | NULL | - |
| 3 | description | varchar(255) | SIM | - | NULL | - |
| 4 | filename | varchar(255) | NAO | - | NULL | - |
| 5 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 6 | mid_file | varchar(255) | SIM | - | NULL | - |
| 7 | extension | varchar(10) | NAO | - | NULL | - |
| 8 | link | text | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_parcela_pagamento (BASE TABLE)
**Linhas aprox:** 23 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | valor_pago | decimal(15,4) | NAO | - | NULL | - |
| 3 | acrescimo | decimal(15,4) | NAO | - | 0.0000 | - |
| 4 | desconto | decimal(15,4) | NAO | - | 0.0000 | - |
| 5 | conta_id | int unsigned | SIM | MUL | NULL | - |
| 6 | forma_pagamento_baixa_id | int | NAO | MUL | NULL | - |
| 7 | financeiro_parcela_id | int | NAO | MUL | NULL | - |
| 8 | data_pagamento | date | NAO | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |
| 12 | user_baixa_id | int unsigned | SIM | MUL | NULL | - |
| 13 | api_device_id | varchar(255) | SIM | - | NULL | - |
| 14 | valor_recebido | decimal(15,4) | NAO | - | 0.0000 | - |
| 15 | caixa_funcoes_id | int | SIM | MUL | NULL | - |
| 16 | caixa_turno | varchar(255) | SIM | MUL | NULL | - |

### Tabela: financeiro_parcela_pix (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 28

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | financeiro_parcela_id | int | NAO | MUL | NULL | - |
| 3 | conta_id | int unsigned | NAO | MUL | NULL | - |
| 4 | key_alias_id | varchar(255) | NAO | - | NULL | - |
| 5 | amount | decimal(15,2) | NAO | - | NULL | - |
| 6 | qrcode_type | enum('IMMEDIATE','BILLING') | NAO | - | IMMEDIATE | - |
| 7 | expiration | int | NAO | - | NULL | - |
| 8 | duedate | date | NAO | - | NULL | - |
| 9 | vencimento | date | NAO | - | NULL | - |
| 10 | days_after_duedate | int | NAO | - | NULL | - |
| 11 | description | text | SIM | - | NULL | - |
| 12 | transaction_id | varchar(255) | SIM | - | NULL | - |
| 13 | transaction_type | varchar(255) | SIM | - | NULL | - |
| 14 | transaction_status | varchar(255) | SIM | - | NULL | - |
| 15 | transaction_qrcode | text | SIM | - | NULL | - |
| 16 | transaction_link | text | SIM | - | NULL | - |
| 17 | transaction_all | text | SIM | - | NULL | - |
| 18 | transaction_data_pagamento | date | SIM | - | NULL | - |
| 19 | transaction_valor_pago | decimal(15,2) | SIM | - | NULL | - |
| 20 | transaction_comprovante | text | SIM | - | NULL | - |
| 21 | response_id | varchar(50) | SIM | - | NULL | - |
| 22 | bank_tax_id | varchar(50) | SIM | - | NULL | - |
| 23 | end_to_end | varchar(50) | SIM | - | NULL | - |
| 24 | estorno_all | text | SIM | - | NULL | - |
| 25 | estorno_comprovante | text | SIM | - | NULL | - |
| 26 | created_at | timestamp | SIM | - | NULL | - |
| 27 | updated_at | timestamp | SIM | - | NULL | - |
| 28 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_parcela_pix_billing (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 18

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | financeiro_parcela_pix_id | int | NAO | MUL | NULL | - |
| 3 | payer_name | varchar(255) | NAO | - | NULL | - |
| 4 | payer_taxid | varchar(50) | NAO | - | NULL | - |
| 5 | payer_email | varchar(255) | NAO | - | NULL | - |
| 6 | payer_address_street | varchar(255) | NAO | - | NULL | - |
| 7 | payer_address_city | varchar(50) | NAO | - | NULL | - |
| 8 | payer_address_state | varchar(2) | NAO | - | NULL | - |
| 9 | payer_address_postalcode | varchar(255) | NAO | - | NULL | - |
| 10 | interest_modality | int | SIM | - | NULL | - |
| 11 | interest_value | decimal(15,2) | SIM | - | NULL | - |
| 12 | fine_modality | int | SIM | - | NULL | - |
| 13 | fine_value | decimal(15,2) | SIM | - | NULL | - |
| 14 | discount_modality | int | SIM | - | NULL | - |
| 15 | discount_value | decimal(15,2) | SIM | - | NULL | - |
| 16 | created_at | timestamp | SIM | - | NULL | - |
| 17 | updated_at | timestamp | SIM | - | NULL | - |
| 18 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: financeiro_troco (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | valor | double(15,4) | NAO | - | 0.0000 | - |
| 3 | caixa_usuario_id | bigint unsigned | SIM | - | NULL | - |
| 4 | caixa_data | date | SIM | - | NULL | - |
| 5 | caixa_turno | tinyint unsigned | SIM | - | NULL | - |
| 6 | caixa_funcoes_id | int | SIM | MUL | NULL | - |
| 7 | tipo | enum('INICIAL','FINAL') | NAO | - | NULL | - |
| 8 | device_id | varchar(255) | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: forma_pagamento (BASE TABLE)
**Linhas aprox:** 28 | **Colunas:** 19

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | tipo | varchar(255) | NAO | - | DUPLICATA | - |
| 4 | permitir_excluir | tinyint | NAO | - | 1 | - |
| 5 | codigo_nfce | varchar(255) | NAO | - | 99 | - |
| 6 | credenciadora_id | int unsigned | SIM | MUL | NULL | - |
| 7 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | ordem | int | SIM | - | 0 | - |
| 11 | codigo_transacao_sitef | varchar(255) | SIM | - | NULL | - |
| 12 | carteira_digital | int | NAO | - | 0 | - |
| 13 | pdv_pos | tinyint | NAO | - | 0 | - |
| 14 | integrar_api | tinyint | NAO | - | 1 | - |
| 15 | permitir_alterar | tinyint(1) | NAO | - | 1 | - |
| 16 | exibir_pagamento | tinyint(1) | NAO | - | 1 | - |
| 17 | pre_venda | tinyint(1) | NAO | - | 0 | - |
| 18 | saldo_caixa | tinyint(1) | NAO | - | 0 | - |
| 19 | atalho_numero | int | SIM | - | NULL | - |

### Tabela: fornecedor (BASE TABLE)
**Linhas aprox:** 14 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | pessoa | enum('FISICA','JURIDICA') | NAO | - | JURIDICA | - |
| 3 | cpf_cnpj | varchar(18) | SIM | - | NULL | - |
| 4 | inscricao_estadual | varchar(20) | SIM | - | NULL | - |
| 5 | inscricao_municipal | varchar(50) | SIM | - | NULL | - |
| 6 | nome | varchar(255) | NAO | - | NULL | - |
| 7 | razao_social | varchar(255) | NAO | - | NULL | - |
| 8 | representante | varchar(255) | SIM | - | NULL | - |
| 9 | ddd | varchar(4) | SIM | - | NULL | - |
| 10 | telefone | varchar(20) | SIM | - | NULL | - |
| 11 | site | varchar(255) | SIM | - | NULL | - |
| 12 | observacao | text | SIM | - | NULL | - |
| 13 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |
| 16 | funcionario_id | int | SIM | MUL | NULL | - |

### Tabela: fornecedor_boleto (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | fornecedor_id | int | NAO | MUL | NULL | - |
| 3 | banco | varchar(50) | NAO | - | NULL | - |
| 4 | codigo_boleto | varchar(50) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: funcionario (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 23

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cpf | varchar(14) | SIM | - | NULL | - |
| 4 | rg | varchar(45) | SIM | - | NULL | - |
| 5 | nome | varchar(255) | NAO | - | NULL | - |
| 6 | usuario_id | int | SIM | MUL | NULL | - |
| 7 | funcao_id | int | NAO | MUL | NULL | - |
| 8 | setor_id | int | SIM | MUL | NULL | - |
| 9 | data_admissao | date | SIM | - | NULL | - |
| 10 | data_demissao | date | SIM | - | NULL | - |
| 11 | desconto_percentual | decimal(15,2) | SIM | - | 0.00 | - |
| 12 | comissao | decimal(15,2) | SIM | - | 0.00 | - |
| 13 | desativado | int | NAO | - | 0 | - |
| 14 | observacao | text | SIM | - | NULL | - |
| 15 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 16 | updated_at | timestamp | SIM | - | NULL | - |
| 17 | deleted_at | timestamp | SIM | - | NULL | - |
| 18 | supervisor | smallint | NAO | - | 0 | - |
| 19 | numero_cartao_supervisor | varchar(255) | SIM | - | NULL | - |
| 20 | veterinario | tinyint | SIM | - | NULL | - |
| 21 | crmv | varchar(10) | SIM | - | NULL | - |
| 22 | numero_mapa | varchar(50) | SIM | - | NULL | - |
| 23 | numero_sipeagro | varchar(50) | SIM | - | NULL | - |

### Tabela: gestao_estoque_configuracao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tipo | varchar(255) | NAO | - | NULL | - |
| 3 | empresa_id | int | SIM | MUL | NULL | - |
| 4 | dados | text | SIM | - | NULL | - |
| 5 | filtro_ultimos_meses | varchar(255) | NAO | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: gestao_estoque_consolidado_mensal (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | data_competencia | date | SIM | - | NULL | - |
| 4 | estoque_volume_medio | decimal(15,2) | SIM | - | 0.00 | - |
| 5 | quantidade_produtos_disponiveis | decimal(15,2) | SIM | - | 0.00 | - |
| 6 | quantidade_produtos_vendidos | decimal(15,2) | SIM | - | 0.00 | - |
| 7 | quantidade_volumes_vendidos | decimal(15,2) | SIM | - | 0.00 | - |
| 8 | media_diaria_venda | decimal(15,2) | SIM | - | 0.00 | - |
| 9 | quantidade_ruptura | decimal(15,2) | SIM | - | 0.00 | - |
| 10 | valor_compra | decimal(15,2) | SIM | - | 0.00 | - |
| 11 | valor_venda | decimal(15,2) | SIM | - | 0.00 | - |
| 12 | quantidade_baixa_demanda | decimal(15,2) | SIM | - | 0.00 | - |
| 13 | porcentagem_positivacao_produtos | decimal(15,2) | SIM | - | 0.00 | - |
| 14 | created_at | timestamp | SIM | - | NULL | - |
| 15 | updated_at | timestamp | SIM | - | NULL | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: grupo (BASE TABLE)
**Linhas aprox:** 4 | **Colunas:** 31

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int | SIM | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | editavel | enum('SIM','NAO') | SIM | - | SIM | - |
| 5 | vender | int | NAO | - | 1 | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | imagem | varchar(255) | SIM | - | NULL | - |
| 10 | armacao | smallint | NAO | - | 0 | - |
| 11 | lente | smallint | NAO | - | 0 | - |
| 12 | restaurante_familia_id | int | SIM | MUL | NULL | - |
| 13 | habilitar_acompanhamento | tinyint(1) | SIM | - | NULL | - |
| 14 | acompanhamento_grupo_id | int | SIM | MUL | NULL | - |
| 15 | qtd_max | int | SIM | - | NULL | - |
| 16 | self_service | tinyint(1) | SIM | - | NULL | - |
| 17 | perguntar_adicionais | tinyint(1) | SIM | - | NULL | - |
| 18 | nao_enviar_comanda | tinyint(1) | SIM | - | NULL | - |
| 19 | cobrar_taxa_servico | tinyint(1) | SIM | - | NULL | - |
| 20 | adicional | tinyint(1) | SIM | - | 0 | - |
| 21 | marketplace_created_at | timestamp | SIM | - | NULL | - |
| 22 | marketplace_updated_at | timestamp | SIM | - | NULL | - |
| 23 | marketplace_code | varchar(255) | SIM | - | NULL | - |
| 24 | restaurante_setor_id | int | SIM | MUL | NULL | - |
| 25 | hub_code | varchar(50) | SIM | - | NULL | - |
| 26 | hub_name | varchar(50) | SIM | - | NULL | - |
| 27 | hub_name_full | varchar(255) | SIM | - | NULL | - |
| 28 | ativo | smallint | NAO | - | 1 | - |
| 29 | comissao | decimal(15,2) | NAO | - | 0.00 | - |
| 30 | hortifruit | tinyint | NAO | - | 0 | - |
| 31 | restricao_idade | tinyint | NAO | - | 0 | - |

### Tabela: grupo_adicional (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | grupo_id | int | NAO | MUL | NULL | - |
| 3 | grupo_adicional_id | int | NAO | MUL | NULL | - |
| 4 | quantidade_limite | int | NAO | - | 0 | - |
| 5 | ordem | int | NAO | - | 0 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: grupo_marketplace (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | habilitar | smallint | NAO | - | 0 | - |
| 5 | grupo_id | int | NAO | MUL | NULL | - |
| 6 | marketplace_vinculado_id | int | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | hub_code | varchar(50) | SIM | - | NULL | - |
| 11 | hub_name | varchar(50) | SIM | - | NULL | - |

### Tabela: indicador (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cpf_cnpj | varchar(18) | SIM | - | NULL | - |
| 4 | inscricao_estadual | varchar(20) | SIM | - | NULL | - |
| 5 | inscricao_municipal | varchar(50) | SIM | - | NULL | - |
| 6 | pessoa | enum('FISICA','JURIDICA') | NAO | - | FISICA | - |
| 7 | nome | varchar(255) | NAO | - | NULL | - |
| 8 | razao_social | varchar(255) | NAO | - | NULL | - |
| 9 | observacao | text | SIM | - | NULL | - |
| 10 | comissao | decimal(15,2) | NAO | - | 0.00 | - |
| 11 | desativado | int | NAO | MUL | 0 | - |
| 12 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: integracao_log (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | data | timestamp | SIM | - | NULL | - |
| 3 | tipo_integracao | varchar(50) | NAO | - | NULL | - |
| 4 | origem | varchar(100) | NAO | - | NULL | - |
| 5 | origem_id | varchar(50) | SIM | - | NULL | - |
| 6 | mensagem | text | NAO | - | NULL | - |
| 7 | requisicao_id | varchar(255) | SIM | - | NULL | - |
| 8 | endpoint | varchar(255) | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: laboratorio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cnpj | varchar(14) | SIM | - | NULL | - |
| 4 | nome | varchar(255) | NAO | - | NULL | - |
| 5 | responsavel | varchar(255) | SIM | - | NULL | - |
| 6 | telefone | varchar(255) | SIM | - | NULL | - |
| 7 | observacao | longtext | SIM | - | NULL | - |
| 8 | desativado | smallint | NAO | - | 0 | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 48

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | versao | varchar(3) | NAO | - | NULL | - |
| 4 | chave_acesso | varchar(48) | NAO | - | NULL | - |
| 5 | tipo_ambiente | int | NAO | - | NULL | - |
| 6 | tipo_emitente | int | NAO | - | NULL | - |
| 7 | tipo_transporte | int | SIM | - | NULL | - |
| 8 | modelo | varchar(2) | NAO | - | NULL | - |
| 9 | serie | varchar(3) | NAO | - | NULL | - |
| 10 | numero_mdfe | int | NAO | - | NULL | - |
| 11 | codigo_chave_acesso | varchar(8) | NAO | - | NULL | - |
| 12 | digito_verificador | int | NAO | - | NULL | - |
| 13 | modal | int | NAO | - | 1 | - |
| 14 | modalidade_transporte | int | NAO | - | NULL | - |
| 15 | data_hora_emissao | datetime | SIM | - | NULL | - |
| 16 | tipo_emissao | int | NAO | - | NULL | - |
| 17 | processo_emissao | int | NAO | - | NULL | - |
| 18 | versao_processo | varchar(20) | NAO | - | NULL | - |
| 19 | carregamento_uf | varchar(2) | NAO | - | NULL | - |
| 20 | descarregamento_uf | varchar(2) | NAO | - | NULL | - |
| 21 | numero_lacre | varchar(20) | SIM | - | NULL | - |
| 22 | total_quantidade_cte | decimal(15,2) | NAO | - | 0.00 | - |
| 23 | total_quantidade_nfe | decimal(15,2) | NAO | - | 0.00 | - |
| 24 | total_quantidade_mdfe | decimal(15,2) | NAO | - | 0.00 | - |
| 25 | total_carga_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 26 | total_carga_quantidade | decimal(15,2) | NAO | - | 0.00 | - |
| 27 | total_codigo_unidade | varchar(2) | NAO | - | NULL | - |
| 28 | unidade_medida | varchar(2) | NAO | - | NULL | - |
| 29 | data_hora_encerramento | timestamp | SIM | - | NULL | - |
| 30 | validado | int | SIM | - | NULL | - |
| 31 | informacao_fisco | text | SIM | - | NULL | - |
| 32 | informacao_complementar_contribuinte | text | SIM | - | NULL | - |
| 33 | xml | text | SIM | - | NULL | - |
| 34 | cancelamento_xml | text | SIM | - | NULL | - |
| 35 | recibo_situacao | enum('AGUARDANDO','NAO_ENVIADO','RECEBIDO','CANCELADO','INUTILIZADO','SINCRONIZADO') | NAO | - | AGUARDANDO | - |
| 36 | recibo_numero | varchar(255) | SIM | - | NULL | - |
| 37 | lote_numero | varchar(255) | SIM | - | NULL | - |
| 38 | data_inutilizacao | datetime | SIM | - | NULL | - |
| 39 | recibo_xml | text | SIM | - | NULL | - |
| 40 | recibo_protocolo | text | SIM | - | NULL | - |
| 41 | encerramento_xml | text | SIM | - | NULL | - |
| 42 | encerramento_protocolo | varchar(255) | SIM | - | NULL | - |
| 43 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 44 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 45 | deleted_at | timestamp | SIM | - | NULL | - |
| 46 | rntrc_emitente | varchar(20) | SIM | - | NULL | - |
| 47 | canal_verde | tinyint | SIM | - | NULL | - |
| 48 | carregamento_posterior | tinyint | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_autorizado_xml (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | autorizado_cpf | varchar(11) | SIM | - | NULL | - |
| 4 | autorizado_cnpj | varchar(14) | SIM | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_carga_descarga (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | carregamento_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 4 | carregamento_nome | varchar(60) | SIM | - | NULL | - |
| 5 | descarregamento_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 6 | descarregamento_nome | varchar(60) | SIM | - | NULL | - |
| 7 | ordem | int | NAO | - | 0 | - |
| 8 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_documento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | carga_descarga_id | int | NAO | MUL | NULL | - |
| 4 | documento_tipo | enum('CTE','NFE','MDFE_TRANSPORTE') | SIM | - | NULL | - |
| 5 | documento_chave_acesso | varchar(44) | NAO | - | NULL | - |
| 6 | documento_segundo_codigo_barra | varchar(36) | SIM | - | NULL | - |
| 7 | documento_indicador_reentrega | int | NAO | - | NULL | - |
| 8 | documento_quantidade_rateada | decimal(5,2) | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |
| 12 | manifesto_documento_eletronico_inclusao_id | int | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_documento_unidade_transporte (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | manifesto_documento_eletronico_documento_id | int | NAO | MUL | NULL | - |
| 4 | unidade_transporte_id | int | SIM | - | NULL | - |
| 5 | unidade_transporte_tipo_unidade | int | SIM | - | NULL | - |
| 6 | unidade_transporte_identificacao | varchar(20) | SIM | - | NULL | - |
| 7 | unidade_transporte_quantidade_rateada | decimal(3,2) | SIM | - | NULL | - |
| 8 | unidade_carga_tipo_unidade | int | SIM | - | NULL | - |
| 9 | unidade_carga_identificacao | varchar(20) | SIM | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_emitente (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 20

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | codigo_uf | varchar(2) | NAO | - | NULL | - |
| 4 | emitente_cnpj | varchar(14) | NAO | - | NULL | - |
| 5 | emitente_nome | varchar(60) | NAO | - | NULL | - |
| 6 | emitente_fantasia | varchar(60) | SIM | - | NULL | - |
| 7 | emitente_endereco | varchar(60) | SIM | - | NULL | - |
| 8 | emitente_numero | varchar(60) | SIM | - | NULL | - |
| 9 | emitente_complemento | varchar(60) | SIM | - | NULL | - |
| 10 | emitente_bairro | varchar(60) | SIM | - | NULL | - |
| 11 | emitente_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 12 | emitente_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 13 | emitente_uf | varchar(2) | SIM | - | NULL | - |
| 14 | emitente_cep | varchar(8) | SIM | - | NULL | - |
| 15 | emitente_telefone | varchar(14) | SIM | - | NULL | - |
| 16 | emitente_inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 17 | emitente_email | varchar(255) | SIM | - | NULL | - |
| 18 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 19 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 20 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_inclusao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | mdfe_id | int | NAO | - | NULL | - |
| 3 | sequencia | int | NAO | - | 1 | - |
| 4 | xml_evento | longtext | SIM | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_lacre (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | unidade_transporte_id | int | SIM | MUL | NULL | - |
| 4 | lacre_numero | varchar(60) | SIM | - | NULL | - |
| 5 | veiculo_lacre_numero | varchar(20) | SIM | - | NULL | - |
| 6 | documento_transporte_lacre_numero | varchar(20) | SIM | - | NULL | - |
| 7 | documento_carga_lacre_numero | varchar(20) | SIM | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_pagamento_frete_lancamentos (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tipo | enum('PARCELA','COMPONENTE') | NAO | - | NULL | - |
| 3 | tipo_pagamento | varchar(20) | NAO | - | NULL | - |
| 4 | numero_parcela | varchar(50) | SIM | - | NULL | - |
| 5 | vencimento | date | SIM | - | NULL | - |
| 6 | valor | decimal(15,2) | NAO | - | NULL | - |
| 7 | tipo_componente | varchar(10) | SIM | - | NULL | - |
| 8 | descricao_componente | varchar(255) | NAO | - | NULL | - |
| 9 | manifesto_documento_eletronico_pagamento_frete_id | bigint unsigned | NAO | MUL | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_pagamentos_frete (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | responsavel | varchar(255) | NAO | - | NULL | - |
| 3 | cpf_cnpj | varchar(255) | NAO | - | NULL | - |
| 4 | valor_contrato | decimal(15,2) | NAO | - | NULL | - |
| 5 | banco_id | int | NAO | - | NULL | - |
| 6 | banco_agencia | varchar(255) | NAO | - | NULL | - |
| 7 | banco_cnpj | varchar(255) | NAO | - | NULL | - |
| 8 | tipo_pagamento | varchar(10) | NAO | - | NULL | - |
| 9 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 10 | empresa_id | int | NAO | MUL | NULL | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_percurso (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | percurso_sigla_uf | varchar(2) | NAO | - | NULL | - |
| 4 | percurso_data_hora_inicio | timestamp | SIM | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_produto_predominante (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | tipo_carga | varchar(2) | NAO | - | NULL | - |
| 4 | produto | varchar(120) | NAO | - | NULL | - |
| 5 | ncm | varchar(8) | SIM | - | NULL | - |
| 6 | codigo_barras | varchar(20) | SIM | - | NULL | - |
| 7 | carregamento_cep | varchar(10) | SIM | - | NULL | - |
| 8 | carregamento_latitude | double(10,6) | SIM | - | NULL | - |
| 9 | carregamento_longitude | double(10,6) | SIM | - | NULL | - |
| 10 | descarregamento_cep | varchar(10) | SIM | - | NULL | - |
| 11 | descarregamento_latitude | double(10,6) | SIM | - | NULL | - |
| 12 | descarregamento_longitude | double(10,6) | SIM | - | NULL | - |
| 13 | created_at | timestamp | SIM | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_responsavel_tecnico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | cnpj | varchar(14) | NAO | - | NULL | - |
| 4 | contato | varchar(60) | NAO | - | NULL | - |
| 5 | email | varchar(60) | NAO | - | NULL | - |
| 6 | fone | varchar(14) | NAO | - | NULL | - |
| 7 | id_csrt | varchar(2) | SIM | - | NULL | - |
| 8 | hash_csrt | varchar(28) | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_seguro (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | seguro_responsavel | varchar(60) | NAO | - | NULL | - |
| 4 | seguro_cnpj | varchar(14) | SIM | - | NULL | - |
| 5 | seguro_cpf | varchar(11) | SIM | - | NULL | - |
| 6 | seguro_nome_seguradora | varchar(30) | SIM | - | NULL | - |
| 7 | seguro_cnpj_seguradora | varchar(14) | SIM | - | NULL | - |
| 8 | seguro_numero_apolice | varchar(20) | SIM | - | NULL | - |
| 9 | seguro_numero_averbacao | varchar(40) | SIM | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_veiculo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 24

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | veiculo_tipo | enum('TRACAO','REBOQUE') | SIM | - | NULL | - |
| 4 | veiculo_codigo_veiculo | varchar(10) | SIM | - | NULL | - |
| 5 | veiculo_placa | varchar(7) | SIM | - | NULL | - |
| 6 | veiculo_renavam | varchar(11) | SIM | - | NULL | - |
| 7 | veiculo_tara | varchar(6) | SIM | - | NULL | - |
| 8 | veiculo_capacidade_kg | varchar(6) | SIM | - | NULL | - |
| 9 | veiculo_capacidade_m3 | varchar(3) | SIM | - | NULL | - |
| 10 | veiculo_proprietario_cpf | varchar(11) | SIM | - | NULL | - |
| 11 | veiculo_proprietario_cnpj | varchar(14) | SIM | - | NULL | - |
| 12 | veiculo_proprietario_rntrc | varchar(8) | SIM | - | NULL | - |
| 13 | veiculo_proprietario_nome | varchar(60) | SIM | - | NULL | - |
| 14 | veiculo_proprietario_inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 15 | veiculo_proprietario_uf | varchar(2) | SIM | - | NULL | - |
| 16 | veiculo_proprietario_tipo | tinyint | SIM | - | NULL | - |
| 17 | veiculo_tipo_rodado | varchar(2) | SIM | - | NULL | - |
| 18 | veiculo_tipo_carroceria | varchar(2) | SIM | - | NULL | - |
| 19 | veiculo_uf_licenciado | varchar(2) | SIM | - | NULL | - |
| 20 | veiculo_codigo_agendamento_portuario | varchar(16) | SIM | - | NULL | - |
| 21 | agencia_reguladora_rntrc | varchar(16) | SIM | - | NULL | - |
| 22 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 23 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_veiculo_agencia (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | veiculo_id | int | SIM | MUL | NULL | - |
| 4 | agencia_tipo | enum('CIOT','CONTRATANTE') | SIM | - | NULL | - |
| 5 | agencia_codigo | varchar(12) | SIM | - | NULL | - |
| 6 | agencia_cpf | varchar(11) | SIM | - | NULL | - |
| 7 | agencia_cnpj | varchar(14) | SIM | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_veiculo_agencia_vale_pedagio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | veiculo_id | int | NAO | MUL | NULL | - |
| 4 | agencia_id | int | NAO | MUL | NULL | - |
| 5 | vale_pedagio_cnpj_fornecedora | varchar(14) | SIM | - | NULL | - |
| 6 | vale_pedagio_cnpj_pg | varchar(14) | SIM | - | NULL | - |
| 7 | vale_pedagio_cpf_pg | varchar(11) | SIM | - | NULL | - |
| 8 | vale_pedagio_numero_comprovante | varchar(20) | NAO | - | NULL | - |
| 9 | vale_pedagio_valor | decimal(15,2) | NAO | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_veiculo_condutor (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | veiculo_id | int | NAO | MUL | NULL | - |
| 4 | veiculo_condutor_nome | varchar(60) | NAO | - | NULL | - |
| 5 | veiculo_condutor_cpf | varchar(11) | NAO | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: manifesto_documento_eletronico_veiculo_perigoso (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | manifesto_documento_eletronico_id | int | NAO | MUL | NULL | - |
| 3 | documento_id | int | NAO | MUL | NULL | - |
| 4 | perigoso_numero_onu | varchar(4) | NAO | - | NULL | - |
| 5 | perigoso_nome_embarque | varchar(150) | SIM | - | NULL | - |
| 6 | perigoso_classe_risco | varchar(40) | SIM | - | NULL | - |
| 7 | perigoso_grupo_embalagem | varchar(6) | SIM | - | NULL | - |
| 8 | perigoso_quantidade_total_produto | varchar(20) | NAO | - | NULL | - |
| 9 | perigoso_quantidade_volume_tipo | varchar(60) | NAO | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marca_equipamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | equipamento_id | int unsigned | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marca_veiculo (BASE TABLE)
**Linhas aprox:** 47 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | marca | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_categoria (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | merchant_marketplace_id | varchar(50) | SIM | - | NULL | - |
| 3 | category_id | varchar(50) | NAO | - | NULL | - |
| 4 | category_name | varchar(50) | NAO | - | NULL | - |
| 5 | category_code | varchar(255) | SIM | - | NULL | - |
| 6 | category_availability | varchar(20) | NAO | - | NULL | - |
| 7 | grupo_id | int | SIM | MUL | NULL | - |
| 8 | empresa_id | int | NAO | MUL | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_config (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | funcionario_id | int | SIM | MUL | NULL | - |
| 3 | empresa_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | ultima_sincronizacao_cadastro | timestamp | SIM | - | NULL | - |
| 8 | tempo_sinc_cadastro | int | NAO | - | 60 | - |
| 9 | ultima_sincronizacao_venda | timestamp | SIM | - | NULL | - |
| 10 | tempo_sinc_venda | int | NAO | - | 60 | - |
| 11 | ultima_sincronizacao_estoque | timestamp | SIM | - | NULL | - |
| 12 | tempo_sinc_estoque | int | NAO | - | 60 | - |

### Tabela: marketplace_gestor_produto (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | produto_empresa_grade_id | int | SIM | - | NULL | - |
| 4 | grupo_id | int | SIM | - | NULL | - |
| 5 | categoria_id | int | SIM | - | NULL | - |
| 6 | marketplace_id | varchar(255) | SIM | - | NULL | - |
| 7 | integrar | varchar(255) | SIM | - | NULL | - |
| 8 | status | varchar(255) | SIM | - | NULL | - |
| 9 | atualizar_categoria_id | int | SIM | - | NULL | - |
| 10 | atualizar_disponibilidade | varchar(255) | SIM | - | NULL | - |
| 11 | atualizar_integrar | tinyint(1) | SIM | - | NULL | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_gestor_produto_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | marketplace_gestor_produto_id | int unsigned | NAO | - | NULL | - |
| 3 | produto_id | int | SIM | - | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | - | NULL | - |
| 5 | categoria_item_id | int | SIM | - | NULL | - |
| 6 | disponibilidade | varchar(255) | NAO | - | NULL | - |
| 7 | integrar | tinyint(1) | NAO | - | NULL | - |
| 8 | status | varchar(255) | NAO | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_grupo_empresa (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | grupo_id | int | NAO | - | NULL | - |
| 4 | marketplace_code | varchar(255) | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_hub_saleschannel (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | - | NULL | - |
| 3 | codigo | varchar(50) | NAO | - | NULL | - |
| 4 | nome | varchar(255) | NAO | - | NULL | - |
| 5 | possui_anuncio | tinyint(1) | NAO | - | 0 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | seller_id | varchar(100) | SIM | - | NULL | - |

### Tabela: marketplace_pagamento_conversao (BASE TABLE)
**Linhas aprox:** 8 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | forma_pagamento_marketplace | varchar(255) | NAO | - | NULL | - |
| 3 | forma_pagamento_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_pedido (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 24

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | marketplace_id | varchar(255) | NAO | - | NULL | - |
| 4 | merchant_marketplace_id | varchar(255) | NAO | - | NULL | - |
| 5 | order_id | varchar(255) | NAO | - | NULL | - |
| 6 | order_number | varchar(255) | NAO | - | NULL | - |
| 7 | order_date | datetime | NAO | - | NULL | - |
| 8 | notes | varchar(255) | SIM | - | NULL | - |
| 9 | status | varchar(255) | NAO | - | NULL | - |
| 10 | invoice_number | varchar(255) | SIM | - | NULL | - |
| 11 | discount | decimal(15,2) | NAO | - | NULL | - |
| 12 | shipping_cost | decimal(15,2) | NAO | - | NULL | - |
| 13 | total | decimal(15,2) | NAO | - | NULL | - |
| 14 | customer_name | text | NAO | - | NULL | - |
| 15 | customer_document | text | NAO | - | NULL | - |
| 16 | customer | text | NAO | - | NULL | - |
| 17 | shipping | text | NAO | - | NULL | - |
| 18 | invoice_issue_date | datetime | SIM | - | NULL | - |
| 19 | done_date | datetime | SIM | - | NULL | - |
| 20 | items | text | NAO | - | NULL | - |
| 21 | payments | text | NAO | - | NULL | - |
| 22 | created_at | timestamp | SIM | - | NULL | - |
| 23 | updated_at | timestamp | SIM | - | NULL | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_produto (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 26

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | merchant_marketplace_id | varchar(50) | SIM | - | NULL | - |
| 3 | product_code | varchar(255) | SIM | - | NULL | - |
| 4 | product_id | varchar(50) | NAO | - | NULL | - |
| 5 | product_name | varchar(100) | NAO | - | NULL | - |
| 6 | product_sku | varchar(20) | SIM | - | NULL | - |
| 7 | product_gtin | varchar(20) | SIM | - | NULL | - |
| 8 | product_availability | varchar(20) | SIM | - | NULL | - |
| 9 | product_measure | varchar(10) | SIM | - | NULL | - |
| 10 | product_grid | smallint | NAO | - | 0 | - |
| 11 | product_stock_active | smallint | NAO | - | 1 | - |
| 12 | product_stock_min | decimal(15,4) | NAO | - | 0.0000 | - |
| 13 | product_stock | decimal(15,4) | NAO | - | 0.0000 | - |
| 14 | product_price | decimal(15,2) | NAO | - | 0.00 | - |
| 15 | product_description | mediumtext | SIM | - | NULL | - |
| 16 | product_promotion_price | decimal(15,4) | NAO | - | 0.0000 | - |
| 17 | product_promotion_start | date | SIM | - | NULL | - |
| 18 | product_promotion_validity | date | SIM | - | NULL | - |
| 19 | category_id | varchar(50) | SIM | - | NULL | - |
| 20 | category_code | varchar(255) | SIM | - | NULL | - |
| 21 | category_name | varchar(50) | SIM | - | NULL | - |
| 22 | produto_empresa_id | int | SIM | MUL | NULL | - |
| 23 | empresa_id | int | NAO | MUL | NULL | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |
| 25 | created_at | timestamp | SIM | - | NULL | - |
| 26 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_produto_grade (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 17

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | merchant_marketplace_id | varchar(50) | SIM | - | NULL | - |
| 3 | product_grid_id | varchar(50) | NAO | - | NULL | - |
| 4 | product_grid_code | varchar(255) | SIM | - | NULL | - |
| 5 | product_grid_name | varchar(100) | SIM | - | NULL | - |
| 6 | product_grid_sku | varchar(20) | SIM | - | NULL | - |
| 7 | product_grid_gtin | varchar(20) | SIM | - | NULL | - |
| 8 | product_grid_availability | varchar(20) | SIM | - | NULL | - |
| 9 | product_grid_price | decimal(15,2) | NAO | - | 0.00 | - |
| 10 | product_grid_specifications | mediumtext | SIM | - | NULL | - |
| 11 | product_id | varchar(50) | SIM | - | NULL | - |
| 12 | product_name | varchar(100) | SIM | - | NULL | - |
| 13 | produto_empresa_grade_id | int | SIM | MUL | NULL | - |
| 14 | empresa_id | int | NAO | MUL | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |
| 16 | created_at | timestamp | SIM | - | NULL | - |
| 17 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: marketplace_vinculado (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | merchant_marketplace_id | varchar(255) | NAO | - | NULL | - |
| 4 | name | varchar(255) | NAO | - | NULL | - |
| 5 | active | smallint | NAO | - | 0 | - |
| 6 | marketplace_id | varchar(255) | NAO | - | NULL | - |
| 7 | marketplace_name | varchar(255) | NAO | - | NULL | - |
| 8 | marketplace_crypto_data | varchar(255) | NAO | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |
| 12 | is_hub | tinyint(1) | NAO | - | 0 | - |

### Tabela: mdfe_serie (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | serie | int | NAO | - | NULL | - |
| 4 | numeracao_inicial | int | NAO | - | 1 | - |
| 5 | padrao | tinyint | NAO | - | 0 | - |
| 6 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | ambiente | tinyint | SIM | - | 2 | - |
| 10 | tipo_serie | enum('SISTEMA','DISPOSITIVO') | SIM | - | SISTEMA | - |
| 11 | oauth_client_id | varchar(255) | SIM | - | NULL | - |

### Tabela: medico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | crm | varchar(255) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: menu_favorito (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | user_id | int unsigned | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | ordem | int | NAO | - | NULL | - |
| 5 | url | varchar(255) | NAO | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | data | text | SIM | - | NULL | - |

### Tabela: meu_lucro_visao_geral (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 57

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | data_competencia | date | SIM | - | NULL | - |
| 4 | config_lucro_pretendido | decimal(15,4) | SIM | - | 0.0000 | - |
| 5 | config_saldo_caixa | decimal(15,4) | SIM | - | 0.0000 | - |
| 6 | config_quantidade_funcionario | int | SIM | - | 0 | - |
| 7 | config_tamanho_estrutura | decimal(15,4) | SIM | - | 0.0000 | - |
| 8 | config_despesa_fixa_folha_pagamento | decimal(15,4) | SIM | - | 0.0000 | - |
| 9 | config_despesa_fixa_pro_labore | decimal(15,4) | SIM | - | 0.0000 | - |
| 10 | config_despesa_fixa_aluguel | decimal(15,4) | SIM | - | 0.0000 | - |
| 11 | config_despesa_fixa_outras | decimal(15,4) | SIM | - | 0.0000 | - |
| 12 | config_despesa_variavel_imposto | decimal(15,4) | SIM | - | 0.0000 | - |
| 13 | config_despesa_variavel_taxa_antecipacao | decimal(15,4) | SIM | - | 0.0000 | - |
| 14 | config_despesa_variavel_comissao | decimal(15,4) | SIM | - | 0.0000 | - |
| 15 | config_despesa_variavel_custo_mercadoria_vendida | decimal(15,4) | SIM | - | 0.0000 | - |
| 16 | config_despesa_variavel_custo_mercadoria_vendida_sistema | tinyint(1) | NAO | - | 0 | - |
| 17 | config_despesa_variavel_margem_lucro_bruto | decimal(15,4) | NAO | - | 0.0000 | - |
| 18 | config_despesa_variavel_outras_despesas | decimal(15,4) | SIM | - | 0.0000 | - |
| 19 | config_categoria_receita_id | int | SIM | - | NULL | - |
| 20 | config_categoria_despesa_id | int | SIM | - | NULL | - |
| 21 | config_emprestimo_financiamento_manual | tinyint(1) | NAO | - | 0 | - |
| 22 | config_valor_emprestimo_entrada | decimal(15,2) | NAO | - | 0.00 | - |
| 23 | config_valor_emprestimo_saida | decimal(15,2) | NAO | - | 0.00 | - |
| 24 | ind_faturamento_por_funcionario | decimal(15,4) | SIM | - | 0.0000 | - |
| 25 | ind_faturamento_por_m2 | decimal(15,4) | SIM | - | 0.0000 | - |
| 26 | ind_prazo_medio_pagamento | decimal(15,4) | SIM | - | 0.0000 | - |
| 27 | ind_prazo_medio_recebimento | decimal(15,4) | SIM | - | 0.0000 | - |
| 28 | ind_ticket_medio | decimal(15,4) | SIM | - | 0.0000 | - |
| 29 | ind_custo_por_mercadoria | decimal(15,4) | SIM | - | 0.0000 | - |
| 30 | ind_lucro_por_funcionario | decimal(15,4) | SIM | - | 0.0000 | - |
| 31 | ind_lucro_por_m2 | decimal(15,4) | SIM | - | 0.0000 | - |
| 32 | created_at | timestamp | SIM | - | NULL | - |
| 33 | updated_at | timestamp | SIM | - | NULL | - |
| 34 | deleted_at | timestamp | SIM | - | NULL | - |
| 35 | ind_faturamento | decimal(15,2) | NAO | - | 0.00 | - |
| 36 | ind_faturamento_mes_anterior | decimal(15,2) | NAO | - | 0.00 | - |
| 37 | ind_recebimentos_vendas | decimal(15,2) | NAO | - | 0.00 | - |
| 38 | ind_pagamento_fornecedores | decimal(15,2) | NAO | - | 0.00 | - |
| 39 | ind_outras_despesas | decimal(15,2) | NAO | - | 0.00 | - |
| 40 | ind_entradas_financiamentos | decimal(15,2) | NAO | - | 0.00 | - |
| 41 | ind_pagamentos_financiamentos | decimal(15,2) | NAO | - | 0.00 | - |
| 42 | ind_lucro_prejuizo_acumulado | decimal(15,2) | NAO | - | 0.00 | - |
| 43 | ind_quantidade_pedidos | int | NAO | - | 0 | - |
| 44 | ind_valor_taxas_cartao | decimal(15,2) | NAO | - | 0.00 | - |
| 45 | ind_percentual_taxas_cartao | decimal(15,4) | NAO | - | 0.0000 | - |
| 46 | ind_impostos | decimal(15,2) | NAO | - | 0.00 | - |
| 47 | ind_receita_liquida | decimal(15,2) | NAO | - | 0.00 | - |
| 48 | ind_custo_mercadoria | decimal(15,2) | NAO | - | 0.00 | - |
| 49 | ind_taxa_cartao | decimal(15,2) | NAO | - | 0.00 | - |
| 50 | ind_comissao | decimal(15,2) | NAO | - | 0.00 | - |
| 51 | ind_custos_fixos | decimal(15,2) | NAO | - | 0.00 | - |
| 52 | ind_margem_lucro | decimal(15,4) | NAO | - | 0.0000 | - |
| 53 | ind_margem_contribuicao | decimal(15,2) | NAO | - | 0.00 | - |
| 54 | ind_lucro_liquido | decimal(15,2) | NAO | - | 0.00 | - |
| 55 | ind_saldo_fco | decimal(15,2) | NAO | - | 0.00 | - |
| 56 | ind_saldo_fcf | decimal(15,4) | NAO | - | 0.0000 | - |
| 57 | ind_saldo_final | decimal(15,2) | NAO | - | 0.00 | - |

### Tabela: migrations (BASE TABLE)
**Linhas aprox:** 1299 | **Colunas:** 2

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | migration | varchar(255) | NAO | - | NULL | - |
| 2 | batch | int | NAO | - | NULL | - |

### Tabela: modulo (BASE TABLE)
**Linhas aprox:** 41 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | versao_atual | varchar(255) | NAO | - | NULL | - |
| 3 | modulo | varchar(255) | NAO | - | NULL | - |
| 4 | descricao | varchar(255) | NAO | - | NULL | - |
| 5 | visivel | smallint | NAO | - | NULL | - |
| 6 | separado | smallint | NAO | - | NULL | - |
| 7 | versao | varchar(255) | NAO | - | NULL | - |
| 8 | nivel | int | NAO | - | NULL | - |
| 9 | ativo | smallint | NAO | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |
| 13 | parametrizacao_fiscal | varchar(255) | NAO | - | FISCAL | - |
| 14 | segmento_assistencia | varchar(255) | SIM | - | NULL | - |

### Tabela: modulo_configuracao (BASE TABLE)
**Linhas aprox:** 6 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | modulo_id | int unsigned | NAO | MUL | NULL | - |
| 3 | configuracao | text | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | alias | varchar(255) | SIM | - | NULL | - |

### Tabela: movimentacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 20

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | data_operacao | date | NAO | - | NULL | - |
| 4 | operacao | enum('ENTRADA','SAIDA','TRANSFERENCIA') | NAO | - | NULL | - |
| 5 | tipo_ajuste_id | int | SIM | MUL | NULL | - |
| 6 | empresa_destino_id | int | SIM | MUL | NULL | - |
| 7 | observacao | text | SIM | - | NULL | - |
| 8 | tipo_destinatario | enum('FORNECEDOR','CLIENTE','TRANSFERENCIA') | NAO | - | FORNECEDOR | - |
| 9 | fornecedor_id | int | SIM | MUL | NULL | - |
| 10 | cliente_id | int | SIM | MUL | NULL | - |
| 11 | finalidade_codigo | int | NAO | MUL | 1 | - |
| 12 | cfop_codigo | int | SIM | MUL | NULL | - |
| 13 | chave_nfe | varchar(44) | SIM | - | NULL | - |
| 14 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 15 | updated_at | timestamp | SIM | - | NULL | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |
| 17 | balanco_id | int | SIM | - | NULL | - |
| 18 | producao_id | int | SIM | - | NULL | - |
| 19 | caixa_funcoes_id | int | SIM | MUL | NULL | - |
| 20 | nfe_id | int unsigned | SIM | MUL | NULL | - |

### Tabela: movimentacao_item (BASE TABLE)
**Linhas aprox:** 26 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | movimentacao_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | produto_empresa_grade_destino_id | int | SIM | MUL | NULL | - |
| 6 | quantidade | decimal(15,4) | NAO | - | NULL | - |
| 7 | preco | decimal(15,4) | NAO | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfce_cfop (BASE TABLE)
**Linhas aprox:** 9 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | - | NULL | - |
| 3 | natureza | text | SIM | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfce_serie (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | serie | int | NAO | - | NULL | - |
| 4 | numeracao_inicial | int | NAO | - | 1 | - |
| 5 | padrao | tinyint | NAO | - | 0 | - |
| 6 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | ambiente | tinyint | SIM | - | 2 | - |
| 10 | tipo_serie | enum('SISTEMA','DISPOSITIVO') | SIM | - | SISTEMA | - |
| 11 | oauth_client_id | varchar(255) | SIM | - | NULL | - |
| 12 | numero | varchar(255) | SIM | - | NULL | - |

### Tabela: nfe_cest (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | - | 0 | - |
| 2 | codigo | varchar(10) | NAO | - | NULL | - |
| 3 | ncm | varchar(255) | SIM | - | NULL | - |
| 4 | descricao | text | SIM | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_cidade (BASE TABLE)
**Linhas aprox:** 5640 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cidade_uf | varchar(50) | NAO | - | NULL | - |
| 3 | c_cidade | int | NAO | - | NULL | - |
| 4 | cidade | varchar(255) | NAO | - | NULL | - |
| 5 | c_uf | int | NAO | MUL | NULL | - |
| 6 | short_uf | varchar(2) | NAO | - | NULL | - |
| 7 | full_uf | varchar(20) | NAO | - | NULL | - |
| 8 | c_pais | varchar(11) | NAO | - | NULL | - |
| 9 | pais | varchar(50) | NAO | - | NULL | - |
| 10 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_classificacao_tributaria (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 22

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | - | 0 | - |
| 2 | cst | varchar(10) | NAO | - | NULL | - |
| 3 | cst_descricao | varchar(255) | NAO | - | NULL | - |
| 4 | cclass_trib | varchar(20) | NAO | - | NULL | - |
| 5 | cclass_trib_nome | varchar(255) | NAO | - | NULL | - |
| 6 | cclass_trib_descricao | longtext | NAO | - | NULL | - |
| 7 | ibs_percentual_red | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | cbs_percentual_red | decimal(15,2) | NAO | - | 0.00 | - |
| 9 | ind_nfe | smallint | NAO | - | 0 | - |
| 10 | ind_nfce | smallint | NAO | - | 0 | - |
| 11 | ind_nfse | smallint | NAO | - | 0 | - |
| 12 | ind_cte | smallint | NAO | - | 0 | - |
| 13 | vigencia_data_inicio | date | SIM | - | NULL | - |
| 14 | vigencia_data_fim | date | SIM | - | NULL | - |
| 15 | data_atualizacao | date | SIM | - | NULL | - |
| 16 | created_at | timestamp | SIM | - | NULL | - |
| 17 | updated_at | timestamp | SIM | - | NULL | - |
| 18 | deleted_at | timestamp | SIM | - | NULL | - |
| 19 | ind_g_ibs_cbs | smallint | NAO | - | 0 | - |
| 20 | ind_g_ibs_cbs_mono | smallint | NAO | - | 0 | - |
| 21 | ind_g_red | smallint | NAO | - | 0 | - |
| 22 | ind_g_dif | smallint | NAO | - | 0 | - |

### Tabela: nfe_codigo_genero (BASE TABLE)
**Linhas aprox:** 100 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_cofins (BASE TABLE)
**Linhas aprox:** 33 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(3) | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | tipo | enum('ENTRADA','SAIDA') | NAO | - | SAIDA | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_cst (BASE TABLE)
**Linhas aprox:** 25 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cst | varchar(255) | NAO | - | NULL | - |
| 3 | natureza | varchar(255) | NAO | - | NULL | - |
| 4 | nome | varchar(255) | SIM | - | NULL | - |
| 5 | crt | int | NAO | - | 1 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | nfce | int | SIM | - | 0 | - |
| 8 | crt_mei | tinyint | NAO | - | 0 | - |
| 9 | cst_substituicao | varchar(255) | NAO | - | 0 | - |

### Tabela: nfe_especifico (BASE TABLE)
**Linhas aprox:** 4 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(255) | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_finalidade (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | - |
| 2 | codigo | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(50) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_grupo (BASE TABLE)
**Linhas aprox:** 110 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | cst_relacionado | varchar(255) | SIM | - | NULL | - |
| 4 | cst_relacionado2 | varchar(255) | SIM | - | NULL | - |
| 5 | sub_grupo | varchar(255) | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_grupo_tensao (BASE TABLE)
**Linhas aprox:** 14 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(10) | NAO | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_ibpt (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | NULL | - |
| 2 | ncm | int | NAO | - | NULL | - |
| 3 | aliquota_federal | decimal(15,2) | NAO | - | 0.00 | - |
| 4 | aliquota_estadual | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | aliquota_municipal | decimal(15,2) | NAO | - | 0.00 | - |
| 6 | aliquota_federal_texto | varchar(50) | SIM | - | NULL | - |
| 7 | aliquota_estadual_texto | varchar(50) | SIM | - | NULL | - |
| 8 | aliquota_municipal_texto | varchar(50) | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_icms_aliquota (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | uf_origem_id | int | NAO | - | NULL | - |
| 3 | uf_origem_sigla | varchar(2) | NAO | - | NULL | - |
| 4 | uf_destino_id | int | NAO | - | NULL | - |
| 5 | uf_destino_sigla | varchar(2) | NAO | - | NULL | - |
| 6 | aliquota | decimal(6,2) | NAO | - | NULL | - |
| 7 | ano_base | int | NAO | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_icms_st (BASE TABLE)
**Linhas aprox:** 4 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_informacoes_adicionais (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | texto | varchar(255) | SIM | - | NULL | - |
| 4 | tipo | enum('COMPLEMENTAR','FISCO') | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | padrao | tinyint | NAO | - | 0 | - |

### Tabela: nfe_mensagem_humanizada (BASE TABLE)
**Linhas aprox:** 4 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | ws_id | varchar(255) | SIM | - | NULL | - |
| 3 | codigo_app | varchar(255) | SIM | - | NULL | - |
| 4 | codigo_erro | varchar(255) | SIM | - | NULL | - |
| 5 | codigo_faq | varchar(255) | SIM | - | NULL | - |
| 6 | mensagem | text | SIM | - | NULL | - |
| 7 | link | varchar(255) | SIM | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_modbaseicms (BASE TABLE)
**Linhas aprox:** 7 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | tinyint(1) | NAO | MUL | 0 | - |
| 3 | descricao | varchar(50) | NAO | - | NULL | - |
| 4 | descricao_st | varchar(50) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_motivo_desoneracao (BASE TABLE)
**Linhas aprox:** 45 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | cst_codigo | varchar(3) | NAO | MUL | NULL | - |
| 3 | codigo | int | NAO | MUL | NULL | - |
| 4 | motivo | varchar(255) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_natureza (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | natureza | varchar(255) | NAO | - | NULL | - |
| 3 | cfop | varchar(255) | NAO | - | NULL | - |
| 4 | operacao | enum('ENTRADA','SAIDA') | NAO | - | NULL | - |
| 5 | descricao | varchar(255) | NAO | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | nfce | int | NAO | - | 0 | - |
| 10 | cfop_substituicao | tinyint | SIM | - | 0 | - |

### Tabela: nfe_origem (BASE TABLE)
**Linhas aprox:** 9 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_pais (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | NULL | - |
| 2 | cpais | int | NAO | - | NULL | - |
| 3 | xpais | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_pis (BASE TABLE)
**Linhas aprox:** 34 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(2) | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | tipo | enum('ENTRADA','SAIDA') | NAO | - | SAIDA | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_serie (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | serie | varchar(10) | NAO | - | NULL | - |
| 4 | numeracao_inicial | int | NAO | - | 1 | - |
| 5 | padrao | int | NAO | - | 0 | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | ambiente | tinyint | SIM | - | 2 | - |
| 10 | tipo_serie | enum('SISTEMA','DISPOSITIVO') | SIM | - | SISTEMA | - |
| 11 | oauth_client_id | varchar(255) | SIM | - | NULL | - |

### Tabela: nfe_situacao_ipi (BASE TABLE)
**Linhas aprox:** 14 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(3) | NAO | MUL | NULL | - |
| 3 | nome | varchar(50) | NAO | - | NULL | - |
| 4 | destacar_ipi | int | NAO | - | 0 | - |
| 5 | tipo | enum('ENTRADA','SAIDA') | NAO | - | SAIDA | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_tipo_emissao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | - |
| 2 | codigo | int | NAO | - | NULL | - |
| 3 | nome | varchar(50) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_tipo_item (BASE TABLE)
**Linhas aprox:** 12 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | tipo | varchar(255) | SIM | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfe_tipo_servico (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | - | 0 | - |
| 2 | codigo | int | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | aliquota | decimal(15,2) | SIM | - | NULL | - |
| 5 | item_lista_servico | decimal(15,2) | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | c_cidade | varchar(255) | NAO | - | NULL | - |
| 10 | descricao | text | NAO | - | NULL | - |

### Tabela: nfse_aliquota_padrao (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | iss | decimal(15,2) | NAO | - | 0.00 | - |
| 3 | pis | decimal(15,2) | NAO | - | 0.00 | - |
| 4 | cssl | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | cofins | decimal(15,2) | NAO | - | 0.00 | - |
| 6 | inss | decimal(15,2) | NAO | - | 0.00 | - |
| 7 | ir | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | empresa_id | int | NAO | MUL | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfse_codigo_servico_item (BASE TABLE)
**Linhas aprox:** 531 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(20) | NAO | - | NULL | - |
| 3 | codigo_numerico | varchar(20) | NAO | - | NULL | - |
| 4 | descricao | varchar(255) | NAO | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | ambiente_nacional | tinyint(1) | NAO | - | 0 | - |

### Tabela: nfse_exigibilidade_iss (BASE TABLE)
**Linhas aprox:** 7 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfse_natureza (BASE TABLE)
**Linhas aprox:** 6 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | cfop | varchar(255) | NAO | - | NULL | - |
| 4 | operacao | varchar(255) | NAO | - | NULL | - |
| 5 | percentual_icms | decimal(8,2) | NAO | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfse_regime_especial_tributacao (BASE TABLE)
**Linhas aprox:** 7 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | tipo | varchar(5) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nfse_serie (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | serie | int | NAO | - | NULL | - |
| 4 | numeracao_inicial | int | NAO | - | 1 | - |
| 5 | padrao | tinyint | NAO | - | 0 | - |
| 6 | ambiente | tinyint | NAO | - | 2 | - |
| 7 | tipo_serie | enum('SISTEMA','DISPOSITIVO') | NAO | - | SISTEMA | - |
| 8 | oauth_client_id | varchar(255) | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica (BASE TABLE)
**Linhas aprox:** 76 | **Colunas:** 89

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | versao | varchar(255) | SIM | - | NULL | - |
| 4 | chave_acesso | varchar(255) | SIM | MUL | NULL | - |
| 5 | codigo_nota_fiscal | varchar(255) | SIM | - | NULL | - |
| 6 | natureza | varchar(255) | NAO | - | NULL | - |
| 7 | indicador_forma_pagamento | int | SIM | - | 0 | - |
| 8 | modelo | varchar(255) | SIM | MUL | NULL | - |
| 9 | serie | varchar(255) | SIM | - | NULL | - |
| 10 | numero_nfe | int | NAO | - | NULL | - |
| 11 | data_hora_emissao | timestamp | SIM | MUL | NULL | - |
| 12 | data_hora_saida | timestamp | SIM | - | NULL | - |
| 13 | tipo_operacao | int | SIM | - | 1 | - |
| 14 | identificador_local_destino | int | SIM | - | 1 | - |
| 15 | tipo_emissao | int | SIM | - | 1 | - |
| 16 | chave_dv | int | SIM | - | NULL | - |
| 17 | ambiente | int | SIM | - | NULL | - |
| 18 | xml | longtext | SIM | - | NULL | - |
| 19 | xml_recibo_emissao | text | SIM | - | NULL | - |
| 20 | xml_cancelamento | text | SIM | - | NULL | - |
| 21 | justificativa_cancelamento | varchar(255) | SIM | - | NULL | - |
| 22 | recibo_situacao | enum('AGUARDANDO','NAO_ENVIADO','RECEBIDO','CANCELADA','DENEGADA','CONTINGENCIA') | SIM | - | NULL | - |
| 23 | lote_emissao | varchar(255) | SIM | - | NULL | - |
| 24 | numero_recibo | varchar(255) | SIM | - | NULL | - |
| 25 | numero_protocolo_autorizacao | varchar(255) | SIM | - | NULL | - |
| 26 | data_hora_protocolo_autorizacao | timestamp | SIM | - | NULL | - |
| 27 | inutilizado_em | datetime | SIM | - | NULL | - |
| 28 | rateavel | tinyint | NAO | - | 1 | - |
| 29 | finalidade | tinyint(1) | NAO | - | 1 | - |
| 30 | indicador_finalidade | varchar(1) | NAO | - | 1 | - |
| 31 | indicador_presencial | varchar(1) | SIM | - | 1 | - |
| 32 | indicador_intermediador | smallint | NAO | - | 0 | - |
| 33 | codigo_natureza | int | SIM | - | NULL | - |
| 34 | data_hora_contingencia | timestamp | SIM | - | NULL | - |
| 35 | justificativa_contingencia | varchar(255) | SIM | - | NULL | - |
| 36 | cobranca_numero_fatura | varchar(60) | SIM | - | NULL | - |
| 37 | cobranca_valor_original | decimal(13,2) | SIM | - | 0.00 | - |
| 38 | cobranca_valor_desconto | decimal(13,2) | SIM | - | 0.00 | - |
| 39 | cobranca_valor_liquido | decimal(13,2) | SIM | - | 0.00 | - |
| 40 | total_frete_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 41 | total_seguro_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 42 | total_valor_outras_despesas | decimal(15,2) | NAO | - | 0.00 | - |
| 43 | total_desconto_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 44 | total_desconto_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 45 | total_icms_base_calculo | decimal(15,2) | SIM | - | NULL | - |
| 46 | total_icms_valor | decimal(15,2) | SIM | - | NULL | - |
| 47 | total_icmsst_base_calculo | decimal(15,2) | SIM | - | NULL | - |
| 48 | total_icmsst_valor | decimal(15,2) | SIM | - | NULL | - |
| 49 | total_produto_valor | decimal(15,2) | SIM | - | NULL | - |
| 50 | total_ipi_valor | decimal(15,2) | SIM | - | NULL | - |
| 51 | total_pis_valor | decimal(15,2) | SIM | - | NULL | - |
| 52 | total_cofins_valor | decimal(15,2) | SIM | - | NULL | - |
| 53 | total_nota_valor | decimal(15,2) | SIM | - | NULL | - |
| 54 | total_tributos_valor | decimal(15,2) | SIM | - | NULL | - |
| 55 | total_icmsdesoneracao_valor | decimal(15,2) | SIM | - | NULL | - |
| 56 | total_icms_uf_destino_valor | decimal(15,2) | SIM | - | NULL | - |
| 57 | total_icms_uf_remetente_valor | decimal(15,2) | SIM | - | NULL | - |
| 58 | total_fcp_uf_destino_valor | decimal(15,2) | SIM | - | NULL | - |
| 59 | total_icms_fundo_combate_pobreza_valor | decimal(15,2) | SIM | - | NULL | - |
| 60 | total_icmsst_fundo_combate_pobreza_valor | decimal(15,2) | SIM | - | NULL | - |
| 61 | total_issqn_valor_servico | decimal(15,2) | SIM | - | NULL | - |
| 62 | total_issqn_valor_base_calculo | decimal(15,2) | SIM | - | NULL | - |
| 63 | total_issqn_valor_iss | decimal(15,2) | SIM | - | NULL | - |
| 64 | total_issqn_valor_pis | decimal(15,2) | SIM | - | NULL | - |
| 65 | total_issqn_valor_cofins | decimal(15,2) | SIM | - | NULL | - |
| 66 | total_issqn_valor_deducao | decimal(15,2) | SIM | - | NULL | - |
| 67 | total_issqn_valor_outro | decimal(15,2) | SIM | - | NULL | - |
| 68 | total_issqn_valor_desconto_incondicionado | decimal(15,2) | SIM | - | NULL | - |
| 69 | total_issqn_data_competencia | date | SIM | - | NULL | - |
| 70 | total_issqn_regime_tributario | varchar(2) | SIM | - | NULL | - |
| 71 | total_issqn_valor_desconto_condicionado | decimal(15,2) | SIM | - | NULL | - |
| 72 | total_issqn_valor_iss_retencao | decimal(15,2) | SIM | - | NULL | - |
| 73 | informacoes_adicionais_complementares | text | SIM | - | NULL | - |
| 74 | informacoes_adicionais_fisco | text | SIM | - | NULL | - |
| 75 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 76 | updated_at | timestamp | SIM | - | NULL | - |
| 77 | deleted_at | timestamp | SIM | - | NULL | - |
| 78 | digest_value | varchar(255) | SIM | - | NULL | - |
| 79 | codigo_status | varchar(255) | SIM | - | NULL | - |
| 80 | mensagem_erro | varchar(255) | SIM | - | NULL | - |
| 81 | sat_equipamento_serie | varchar(50) | SIM | - | NULL | - |
| 82 | sat_assinatura_qr_code | varchar(255) | SIM | - | NULL | - |
| 83 | compra_id | int | SIM | MUL | NULL | - |
| 84 | duplicidade | smallint | NAO | - | 0 | - |
| 85 | confirmacao_duplicidade | smallint | NAO | - | 0 | - |
| 86 | chave_acesso_anterior_duplicidade | varchar(255) | SIM | - | NULL | - |
| 87 | memoria_fiscal | smallint | NAO | - | 1 | - |
| 88 | operacao_tipo | varchar(50) | SIM | - | NULL | - |
| 89 | movimentar_estoque | smallint | NAO | - | 0 | - |

### Tabela: nota_fiscal_eletronica_autorizado (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | cpf_cnpj | varchar(50) | NAO | - | NULL | - |
| 4 | nome | varchar(255) | SIM | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_carta_correcao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | - | NULL | - |
| 3 | chave_acesso | varchar(44) | SIM | - | NULL | - |
| 4 | tipo_ambiente | tinyint(1) | NAO | - | 2 | - |
| 5 | sequencial | int | SIM | - | 1 | - |
| 6 | correcao | text | SIM | - | NULL | - |
| 7 | retorno_sefaz | text | SIM | - | NULL | - |
| 8 | data_hora_registro | timestamp | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_cobranca (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | numero_duplicata | varchar(60) | SIM | - | NULL | - |
| 4 | vencimento | date | SIM | - | NULL | - |
| 5 | valor_duplicata | decimal(13,2) | NAO | - | 0.00 | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_destinatario (BASE TABLE)
**Linhas aprox:** 48 | **Colunas:** 26

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | destinatario_cpf_cnpj | varchar(14) | NAO | - | NULL | - |
| 4 | destinatario_id_estrangeiro | varchar(20) | SIM | - | NULL | - |
| 5 | destinatario_nome | varchar(60) | NAO | - | NULL | - |
| 6 | destinatario_endereco | varchar(60) | SIM | - | NULL | - |
| 7 | destinatario_numero | varchar(60) | SIM | - | NULL | - |
| 8 | destinatario_complemento | varchar(60) | SIM | - | NULL | - |
| 9 | destinatario_bairro | varchar(60) | SIM | - | NULL | - |
| 10 | destinatario_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 11 | destinatario_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 12 | destinatario_uf | enum('AC','AL','AP','AM','BA','CE','DF','ES','EX','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | SIM | - | NULL | - |
| 13 | destinatario_cep | varchar(8) | SIM | - | NULL | - |
| 14 | destinatario_codigo_pais | varchar(4) | SIM | - | NULL | - |
| 15 | destinatario_nome_pais | varchar(60) | SIM | - | NULL | - |
| 16 | destinatario_telefone | varchar(14) | SIM | - | NULL | - |
| 17 | destinatario_indicador_ie | enum('1','2','9') | SIM | - | NULL | - |
| 18 | destinatario_ie | varchar(14) | SIM | - | NULL | - |
| 19 | destinatario_inscricao_suframa | varchar(9) | SIM | - | NULL | - |
| 20 | destinatario_inscricao_municipal | varchar(15) | SIM | - | NULL | - |
| 21 | destinatario_email | varchar(60) | SIM | - | NULL | - |
| 22 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 23 | updated_at | timestamp | SIM | - | NULL | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |
| 25 | destinatario_id | int | SIM | - | NULL | - |
| 26 | destinatario_tipo | varchar(50) | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_emitente (BASE TABLE)
**Linhas aprox:** 48 | **Colunas:** 25

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | emitente_cnpj | varchar(14) | NAO | - | NULL | - |
| 4 | emitente_nome | varchar(60) | NAO | - | NULL | - |
| 5 | emitente_fantasia | varchar(60) | SIM | - | NULL | - |
| 6 | emitente_endereco | varchar(60) | SIM | - | NULL | - |
| 7 | emitente_numero | varchar(60) | SIM | - | NULL | - |
| 8 | emitente_complemento | varchar(60) | SIM | - | NULL | - |
| 9 | emitente_bairro | varchar(60) | SIM | - | NULL | - |
| 10 | emitente_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 11 | emitente_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 12 | emitente_uf | enum('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO') | SIM | - | NULL | - |
| 13 | emitente_codigo_uf | int | SIM | - | NULL | - |
| 14 | emitente_cep | varchar(8) | SIM | - | NULL | - |
| 15 | emitente_codigo_pais | varchar(4) | SIM | - | NULL | - |
| 16 | emitente_nome_pais | varchar(60) | SIM | - | NULL | - |
| 17 | emitente_telefone | varchar(14) | SIM | - | NULL | - |
| 18 | emitente_inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 19 | emitente_inscricao_estadual_st | varchar(14) | SIM | - | NULL | - |
| 20 | emitente_inscricao_municipal | varchar(15) | SIM | - | NULL | - |
| 21 | emitente_cnae | varchar(7) | SIM | - | NULL | - |
| 22 | emitente_codigo_regime_tributario | varchar(255) | SIM | - | NULL | - |
| 23 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 24 | updated_at | timestamp | SIM | - | NULL | - |
| 25 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_especifico_armamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 3 | especifico_tipo_arma | varchar(1) | NAO | - | NULL | - |
| 4 | especifico_numero_serie_arma | varchar(15) | NAO | - | NULL | - |
| 5 | especifico_numero_serie_cano | varchar(15) | NAO | - | NULL | - |
| 6 | especifico_descricao | varchar(255) | NAO | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_especifico_combustivel (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 25

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 3 | especifico_codigo_produto | varchar(9) | NAO | - | NULL | - |
| 4 | especifico_descricao_produto | varchar(255) | NAO | - |  | - |
| 5 | especifico_percentual_glp | decimal(7,4) | SIM | - | 0.0000 | - |
| 6 | especifico_percentual_gas_natural_importado | decimal(7,4) | SIM | - | 0.0000 | - |
| 7 | especifico_valor_partida | decimal(15,2) | SIM | - | 0.00 | - |
| 8 | especifico_percentual_gas_natural | decimal(7,4) | SIM | - | NULL | - |
| 9 | especifico_codif | varchar(21) | SIM | - | NULL | - |
| 10 | especifico_quantidade_combustivel | decimal(16,4) | SIM | - | NULL | - |
| 11 | especifico_uf_consumo | varchar(2) | NAO | - | NULL | - |
| 12 | especifico_quantidade_bc_cide | decimal(16,4) | SIM | - | NULL | - |
| 13 | especifico_aliquota_cide | decimal(15,4) | SIM | - | NULL | - |
| 14 | especifico_valor_cide | decimal(15,2) | SIM | - | NULL | - |
| 15 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 16 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 17 | deleted_at | timestamp | SIM | - | NULL | - |
| 18 | percentual_bio | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | aliquota_ad_rem | decimal(15,2) | NAO | - | 0.00 | - |
| 20 | aliquota_ad_rem_icms_reten | decimal(15,2) | NAO | - | 0.00 | - |
| 21 | aliquota_ad_rem_icms_ret | decimal(15,2) | NAO | - | 0.00 | - |
| 22 | percentual_reducao_ad_rem | decimal(15,2) | NAO | - | 0.00 | - |
| 23 | motivo_reducao_ad_rem | int | SIM | - | NULL | - |
| 24 | quantidade_base_calculo_tributada | decimal(15,4) | NAO | - | 0.0000 | - |
| 25 | quantidade_retida_base_calculo_tributada | decimal(15,4) | NAO | - | 0.0000 | - |

### Tabela: nota_fiscal_eletronica_especifico_medicamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | especifico_codigo_anvisa | varchar(255) | NAO | - | NULL | - |
| 3 | especifico_motivo_isencao | varchar(255) | SIM | - | NULL | - |
| 4 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_especifico_medicamento_rastro (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 3 | especifico_numero_lote | varchar(20) | NAO | - | NULL | - |
| 4 | especifico_quantidade_lote | decimal(11,3) | NAO | - | NULL | - |
| 5 | especifico_data_fabricacao | date | NAO | - | NULL | - |
| 6 | especifico_data_validade | date | NAO | - | NULL | - |
| 7 | especifico_preco_maximo | decimal(15,2) | NAO | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_especifico_papel (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 3 | especifico_numero_recopi | varchar(20) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_especifico_veiculo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 29

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 3 | especifico_tipo_operacao | varchar(1) | NAO | - | NULL | - |
| 4 | especifico_chassi | varchar(17) | NAO | - | NULL | - |
| 5 | especifico_cor_codigo | varchar(4) | NAO | - | NULL | - |
| 6 | especifico_cor_descricao | varchar(40) | NAO | - | NULL | - |
| 7 | especifico_potencia_motor | varchar(4) | NAO | - | NULL | - |
| 8 | especifico_cilindrada | varchar(4) | NAO | - | NULL | - |
| 9 | especifico_peso_liquido | varchar(9) | NAO | - | NULL | - |
| 10 | especifico_peso_bruto | varchar(9) | NAO | - | NULL | - |
| 11 | especifico_numero_serie | varchar(9) | NAO | - | NULL | - |
| 12 | especifico_tipo_combustivel | varchar(2) | NAO | - | NULL | - |
| 13 | especifico_numero_motor | varchar(21) | NAO | - | NULL | - |
| 14 | especifico_capacidade_maxima_tracao | varchar(9) | NAO | - | NULL | - |
| 15 | especifico_distancia_eixo | varchar(4) | NAO | - | NULL | - |
| 16 | especifico_ano_modelo | tinyint | NAO | - | NULL | - |
| 17 | especifico_ano_fabricacao | tinyint | NAO | - | NULL | - |
| 18 | especifico_tipo_pintura | varchar(1) | NAO | - | NULL | - |
| 19 | especifico_tipo_veiculo | varchar(2) | NAO | - | NULL | - |
| 20 | especifico_especie_veiculo | varchar(1) | NAO | - | NULL | - |
| 21 | especifico_condicao_vin | varchar(1) | NAO | - | NULL | - |
| 22 | especifico_condicao_veiculo | varchar(1) | NAO | - | NULL | - |
| 23 | especifico_codigo_marca_modelo | varchar(6) | NAO | - | NULL | - |
| 24 | especifico_codigo_cor_denatran | varchar(2) | NAO | - | NULL | - |
| 25 | especifico_lotacao_capacidade | varchar(3) | NAO | - | NULL | - |
| 26 | especifico_tipo_restricao | varchar(1) | NAO | - | NULL | - |
| 27 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 28 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 29 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_exportacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | uf_saida_pais | varchar(2) | NAO | - | NULL | - |
| 4 | localizacao | varchar(60) | NAO | - | NULL | - |
| 5 | localizacao_despacho | varchar(60) | NAO | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_forma_pagamento (BASE TABLE)
**Linhas aprox:** 48 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | pagamento_tipo | varchar(2) | NAO | - | 01 | - |
| 4 | pagamento_valor | decimal(15,4) | SIM | - | 0.0000 | - |
| 5 | pagamento_tipo_integracao | varchar(2) | SIM | - | 2 | - |
| 6 | pagamento_cnpj_credenciadora | varchar(14) | SIM | - | NULL | - |
| 7 | pagamento_bandeira_operadora | varchar(2) | SIM | - | 99 | - |
| 8 | pagamento_numero_autorizacao | varchar(20) | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |
| 12 | pagamento_valor_troco | decimal(15,4) | SIM | - | NULL | - |
| 13 | pagamento_descricao | varchar(255) | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_inutilizacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | modelo | varchar(255) | NAO | - | 55 | - |
| 4 | numero_inicial | int | SIM | - | NULL | - |
| 5 | numero_final | int | SIM | - | NULL | - |
| 6 | serie | int | SIM | - | NULL | - |
| 7 | justificativa | varchar(255) | SIM | - | NULL | - |
| 8 | tipo_ambiente | int | NAO | - | 2 | - |
| 9 | retorno_sefaz | text | SIM | - | NULL | - |
| 10 | data_hora_registro | timestamp | SIM | - | NULL | - |
| 11 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_item (BASE TABLE)
**Linhas aprox:** 196 | **Colunas:** 110

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 4 | produto_id | int | NAO | - | NULL | - |
| 5 | servico | tinyint | NAO | - | 0 | - |
| 6 | tipo_especifico | enum('VEICULO','MEDICAMENTO','ARMAMENTO','COMBUSTIVEL','PAPEL') | SIM | - | NULL | - |
| 7 | codigo_produto | varchar(60) | SIM | - | NULL | - |
| 8 | codigo_ean | varchar(14) | SIM | - | NULL | - |
| 9 | produto_nome | varchar(255) | NAO | - | NULL | - |
| 10 | ncm | varchar(8) | SIM | - | NULL | - |
| 11 | cest | varchar(10) | SIM | - | NULL | - |
| 12 | cfop | varchar(4) | SIM | - | NULL | - |
| 13 | unidade_comercial | varchar(6) | SIM | - | NULL | - |
| 14 | pedido_compra_numero_compra | varchar(15) | SIM | - | NULL | - |
| 15 | pedido_compra_numero_pedido | varchar(6) | SIM | - | NULL | - |
| 16 | quantidade_comercial | decimal(15,4) | SIM | - | NULL | - |
| 17 | valor_unitario_comercial | decimal(15,4) | SIM | - | NULL | - |
| 18 | valor_total_produto | decimal(15,4) | SIM | - | NULL | - |
| 19 | unidade_tributavel | varchar(6) | SIM | - | NULL | - |
| 20 | quantidade_tributavel | decimal(15,4) | SIM | - | NULL | - |
| 21 | valor_unitario_tributavel | decimal(15,4) | SIM | - | NULL | - |
| 22 | valor_total_frete | decimal(13,2) | SIM | - | NULL | - |
| 23 | valor_total_seguro | decimal(13,2) | SIM | - | NULL | - |
| 24 | valor_total_desconto | decimal(13,2) | SIM | - | NULL | - |
| 25 | valor_total_outras_despesas | decimal(13,2) | SIM | - | NULL | - |
| 26 | indicador_total | int | NAO | - | 1 | - |
| 27 | origem | varchar(1) | NAO | - | 0 | - |
| 28 | cst_csosn | varchar(255) | SIM | - | NULL | - |
| 29 | icms_modalidade_base_calculo | varchar(2) | SIM | - | NULL | - |
| 30 | icms_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 31 | icms_aliquota_credito_simples_nacional | decimal(15,2) | SIM | - | NULL | - |
| 32 | icms_valor_credito_simples_nacional | decimal(15,2) | SIM | - | NULL | - |
| 33 | rateavel | tinyint | NAO | - | 1 | - |
| 34 | icms_percentual_reducao_base | decimal(13,2) | SIM | - | NULL | - |
| 35 | icms_aliquota | decimal(13,2) | SIM | - | NULL | - |
| 36 | icms_aliquota_automatica | int | NAO | - | 1 | - |
| 37 | icms_valor | decimal(13,2) | SIM | - | NULL | - |
| 38 | icmsst_modalidade_base_calculo | varchar(2) | SIM | - | NULL | - |
| 39 | icmsst_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 40 | icmsst_percentual_reducao_base | decimal(13,2) | SIM | - | NULL | - |
| 41 | icmsst_mva | decimal(13,2) | SIM | - | NULL | - |
| 42 | icmsst_aliquota | decimal(13,2) | SIM | - | NULL | - |
| 43 | icmsst_valor | decimal(13,2) | SIM | - | NULL | - |
| 44 | icmsst_retido_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 45 | icmsst_retido_valor | decimal(13,2) | SIM | - | NULL | - |
| 46 | icms_aliquota_suportada_consumidor | decimal(5,2) | NAO | - | 0.00 | - |
| 47 | icms_desoneracao_motivo | varchar(60) | SIM | - | NULL | - |
| 48 | icms_desoneracao_valor | decimal(13,2) | SIM | - | NULL | - |
| 49 | icms_operacao_valor | decimal(13,2) | SIM | - | NULL | - |
| 50 | icms_diferimento_percentual | decimal(13,2) | SIM | - | NULL | - |
| 51 | icms_diferimento_valor | decimal(13,2) | SIM | - | NULL | - |
| 52 | ipi_cst | varchar(2) | SIM | - | NULL | - |
| 53 | ipi_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 54 | ipi_aliquota | decimal(13,2) | SIM | - | NULL | - |
| 55 | ipi_devolucao | decimal(15,2) | SIM | - | NULL | - |
| 56 | ipi_valor | decimal(13,2) | SIM | - | NULL | - |
| 57 | ipi_enquadramento | varchar(5) | SIM | - | NULL | - |
| 58 | tributos_federais | decimal(13,2) | SIM | - | NULL | - |
| 59 | tributos_estaduais | decimal(13,2) | SIM | - | NULL | - |
| 60 | tributos_municipais | decimal(13,2) | SIM | - | NULL | - |
| 61 | total_tributos | decimal(13,2) | SIM | - | NULL | - |
| 62 | especifico | varchar(255) | SIM | - | NULL | - |
| 63 | pis_cst | varchar(255) | SIM | - | NULL | - |
| 64 | pis_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 65 | pis_aliquota | decimal(14,3) | SIM | - | NULL | - |
| 66 | pis_valor | decimal(13,2) | SIM | - | NULL | - |
| 67 | cofins_cst | varchar(2) | SIM | - | NULL | - |
| 68 | cofins_aliquota | decimal(14,3) | SIM | - | NULL | - |
| 69 | cofins_valor | decimal(13,2) | SIM | - | NULL | - |
| 70 | icmsdifal_base_calculo_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 71 | icmsdifal_base_calculo_fcp_destino | decimal(15,2) | SIM | - | NULL | - |
| 72 | icmsdifal_percentual_fcp_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 73 | icmsdifal_percentual_icms_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 74 | icmsdifal_percentual_icms_interestadual | decimal(13,2) | SIM | - | NULL | - |
| 75 | icmsdifal_percentual_provisorio_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 76 | icmsdifal_valor_fcp_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 77 | icmsdifal_valor_icms_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 78 | icmsdifal_valor_icms_uf_remetente | decimal(13,2) | SIM | - | NULL | - |
| 79 | natureza | varchar(255) | SIM | - | NULL | - |
| 80 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 81 | updated_at | timestamp | SIM | - | NULL | - |
| 82 | deleted_at | timestamp | SIM | - | NULL | - |
| 83 | informacoes_adicionais_produto | longtext | SIM | - | NULL | - |
| 84 | codigo_beneficio_fiscal | varchar(255) | SIM | - | NULL | - |
| 85 | icmsst_base_calculo_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 86 | icmsst_valor_destino | decimal(15,2) | SIM | - | 0.00 | - |
| 87 | peso | decimal(15,4) | SIM | - | NULL | - |
| 88 | icms_st_modalidade_base | varchar(255) | SIM | - | NULL | - |
| 89 | icms_st_mva | decimal(15,2) | SIM | - | NULL | - |
| 90 | icms_st_aliquota | decimal(15,2) | SIM | - | NULL | - |
| 91 | icms_st_reducao | decimal(15,2) | SIM | - | NULL | - |
| 92 | icms_valor_pauta | decimal(15,2) | SIM | - | NULL | - |
| 93 | icmsst_valor_base_calculo_fundo_combate_pobreza | decimal(15,2) | SIM | - | NULL | - |
| 94 | icmsst_percentual_fundo_combate_pobreza | decimal(15,2) | SIM | - | NULL | - |
| 95 | icmsst_valor_fundo_combate_pobreza | decimal(15,2) | SIM | - | NULL | - |
| 96 | imposto_manual | smallint | NAO | - | 0 | - |
| 97 | zerar_icms | smallint | NAO | - | 0 | - |
| 98 | ibs_cbs_cst | varchar(10) | NAO | - | 000 | - |
| 99 | ibs_cbs_cclass_trib | varchar(20) | NAO | - | 000001 | - |
| 100 | ibs_aliquota | decimal(15,2) | NAO | - | 0.10 | - |
| 101 | cbs_aliquota | decimal(15,2) | NAO | - | 0.90 | - |
| 102 | ibs_percentual_red | decimal(15,2) | NAO | - | 0.00 | - |
| 103 | cbs_percentual_red | decimal(15,2) | NAO | - | 0.00 | - |
| 104 | ibs_cbs_cst_id | bigint unsigned | SIM | - | NULL | - |
| 105 | agro_numero_receituario | varchar(255) | SIM | - | NULL | - |
| 106 | agro_cpf_responsavel | varchar(14) | SIM | - | NULL | - |
| 107 | icms_desoneracao_codigo | varchar(10) | SIM | - | NULL | - |
| 108 | icms_original_normal_aliquota | decimal(19,2) | NAO | - | 0.00 | - |
| 109 | icms_original_aliquota | decimal(19,2) | NAO | - | 0.00 | - |
| 110 | somar_ipi_icmsst_base | smallint | NAO | - | 0 | - |

### Tabela: nota_fiscal_eletronica_item_combustivel_origem (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | indicador_importacao | int | NAO | - | NULL | - |
| 3 | codigo_uf_origem | varchar(255) | NAO | - | NULL | - |
| 4 | percentual_originario_uf | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 6 | nota_fiscal_eletronica_especifico_combustivel_id | int unsigned | NAO | MUL | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_item_issqn (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_item_id | int unsigned | NAO | MUL | NULL | - |
| 3 | issqn_valor_base_calculo | decimal(15,2) | NAO | - | NULL | - |
| 4 | issqn_valor_aliquota | decimal(7,4) | NAO | - | NULL | - |
| 5 | issqn_valor_issqn | decimal(15,2) | NAO | - | NULL | - |
| 6 | issqn_codigo_municipio_fato_gerador | varchar(7) | NAO | - | NULL | - |
| 7 | issqn_item_lista_servico | varchar(5) | NAO | - | NULL | - |
| 8 | issqn_valor_deducao | decimal(15,2) | SIM | - | NULL | - |
| 9 | issqn_valor_outro | decimal(15,2) | SIM | - | NULL | - |
| 10 | issqn_valor_desconto_incondicionado | decimal(15,2) | SIM | - | NULL | - |
| 11 | issqn_valor_desconto_condicionado | decimal(15,2) | SIM | - | NULL | - |
| 12 | issqn_valor_retencao_iss | decimal(15,2) | SIM | - | NULL | - |
| 13 | issqn_indicador_exigibilidade_iss | varchar(2) | NAO | - | NULL | - |
| 14 | issqn_codigo_servico | varchar(20) | SIM | - | NULL | - |
| 15 | issqn_codigo_municipio | varchar(7) | SIM | - | NULL | - |
| 16 | issqn_codigo_pais | varchar(4) | SIM | - | NULL | - |
| 17 | issqn_numero_processo | varchar(30) | SIM | - | NULL | - |
| 18 | issqn_indicador_incentivo_fiscal | varchar(1) | NAO | - | NULL | - |
| 19 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 20 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_local_entrega (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | local_entrega_cpf_cnpj | varchar(14) | SIM | - | NULL | - |
| 4 | local_entrega_endereco | varchar(60) | SIM | - | NULL | - |
| 5 | local_entrega_numero | varchar(60) | SIM | - | NULL | - |
| 6 | local_entrega_complemento | varchar(60) | SIM | - | NULL | - |
| 7 | local_entrega_bairro | varchar(60) | SIM | - | NULL | - |
| 8 | local_entrega_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 9 | local_entrega_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 10 | local_entrega_uf | varchar(2) | SIM | - | NULL | - |
| 11 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |
| 14 | local_entrega_nome | varchar(60) | SIM | - | NULL | - |
| 15 | local_entrega_cep | varchar(8) | SIM | - | NULL | - |
| 16 | local_entrega_pais | varchar(60) | SIM | - | NULL | - |
| 17 | local_entrega_codigo_pais | varchar(4) | SIM | - | NULL | - |
| 18 | local_entrega_telefone | varchar(14) | SIM | - | NULL | - |
| 19 | local_entrega_email | varchar(60) | SIM | - | NULL | - |
| 20 | local_entrega_inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 21 | local_entrega_motivo_isencao | varchar(255) | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_local_retirada (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 20

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | local_retirada_cpf_cnpj | varchar(14) | SIM | - | NULL | - |
| 4 | local_retirada_endereco | varchar(60) | SIM | - | NULL | - |
| 5 | local_retirada_numero | varchar(60) | SIM | - | NULL | - |
| 6 | local_retirada_complemento | varchar(60) | SIM | - | NULL | - |
| 7 | local_retirada_bairro | varchar(60) | SIM | - | NULL | - |
| 8 | local_retirada_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 9 | local_retirada_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 10 | local_retirada_cidade_uf | varchar(2) | SIM | - | NULL | - |
| 11 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |
| 14 | local_retirada_nome | varchar(60) | SIM | - | NULL | - |
| 15 | local_retirada_cep | varchar(8) | SIM | - | NULL | - |
| 16 | local_retirada_pais | varchar(60) | SIM | - | NULL | - |
| 17 | local_retirada_codigo_pais | varchar(4) | SIM | - | NULL | - |
| 18 | local_retirada_telefone | varchar(14) | SIM | - | NULL | - |
| 19 | local_retirada_email | varchar(60) | SIM | - | NULL | - |
| 20 | local_retirada_inscricao_estadual | varchar(14) | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_referenciada (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | numero | varchar(11) | NAO | - | NULL | - |
| 4 | chave_acesso | varchar(44) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_responsavel_tecnico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | cnpj | varchar(14) | NAO | - | NULL | - |
| 4 | contato | varchar(60) | NAO | - | NULL | - |
| 5 | email | varchar(60) | NAO | - | NULL | - |
| 6 | fone | varchar(14) | NAO | - | NULL | - |
| 7 | id_csrt | varchar(2) | SIM | - | NULL | - |
| 8 | hash_csrt | varchar(28) | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_eletronica_transportador (BASE TABLE)
**Linhas aprox:** 48 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | transportador_nome | varchar(255) | SIM | - | NULL | - |
| 4 | transportador_cpf_cnpj | varchar(14) | SIM | - | NULL | - |
| 5 | transportador_ie | varchar(14) | SIM | - | NULL | - |
| 6 | transportador_uf | enum('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | SIM | - | NULL | - |
| 7 | transportador_endereco | varchar(60) | SIM | - | NULL | - |
| 8 | transportador_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 9 | transportador_modalidade_frete | int | NAO | - | 1 | - |
| 10 | transportador_placa | varchar(255) | SIM | - | NULL | - |
| 11 | transportador_placa_uf | enum('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | SIM | - | NULL | - |
| 12 | transportador_rntc | varchar(20) | SIM | - | NULL | - |
| 13 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |
| 16 | volume_manual | tinyint | NAO | - | 0 | - |

### Tabela: nota_fiscal_eletronica_volume (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 3 | volumes_quantidade | int | SIM | - | NULL | - |
| 4 | volumes_especie | varchar(60) | SIM | - | NULL | - |
| 5 | volumes_marca | varchar(60) | SIM | - | NULL | - |
| 6 | volumes_numero | varchar(60) | SIM | - | NULL | - |
| 7 | volumes_peso_bruto | decimal(15,4) | SIM | - | NULL | - |
| 8 | volumes_peso_liquido | decimal(15,4) | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nota_fiscal_servico_eletronica (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 46

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | serie | varchar(25) | NAO | - | NULL | - |
| 4 | ambiente | tinyint | NAO | - | 2 | - |
| 5 | numero_rps | varchar(15) | SIM | - | NULL | - |
| 6 | status_rps | int | NAO | - | 0 | - |
| 7 | data_emissao | datetime | SIM | - | NULL | - |
| 8 | data_competencia | date | SIM | - | NULL | - |
| 9 | total_valor_servico | decimal(15,4) | SIM | - | 0.0000 | - |
| 10 | total_valor_deducoes | decimal(15,4) | SIM | - | 0.0000 | - |
| 11 | total_valor_outras_retencoes | decimal(15,4) | SIM | - | 0.0000 | - |
| 12 | total_valor_desconto_incondicionado | decimal(15,4) | SIM | - | 0.0000 | - |
| 13 | total_valor_desconto_condicionado | decimal(15,4) | SIM | - | 0.0000 | - |
| 14 | iss_retido | tinyint | NAO | - | 0 | - |
| 15 | simples_nacional | tinyint | NAO | - | 0 | - |
| 16 | aliquota_iss | decimal(15,4) | SIM | - | 0.0000 | - |
| 17 | aliquota_pis | decimal(15,4) | SIM | - | 0.0000 | - |
| 18 | aliquota_cofins | decimal(15,4) | SIM | - | 0.0000 | - |
| 19 | aliquota_ir | decimal(15,4) | SIM | - | 0.0000 | - |
| 20 | aliquota_inss | decimal(15,4) | SIM | - | 0.0000 | - |
| 21 | aliquota_csll | decimal(15,4) | SIM | - | 0.0000 | - |
| 22 | nfse_exigibilidade_iss_id | int | SIM | MUL | NULL | - |
| 23 | nfse_regime_especial_tributacao_id | int | SIM | MUL | NULL | - |
| 24 | total_base_calculo | decimal(15,4) | SIM | - | 0.0000 | - |
| 25 | valor_liquido_nfse | decimal(15,4) | SIM | - | 0.0000 | - |
| 26 | total_iss | decimal(15,4) | SIM | - | 0.0000 | - |
| 27 | total_iss_retido | decimal(15,4) | SIM | - | 0.0000 | - |
| 28 | total_pis | decimal(15,4) | SIM | - | 0.0000 | - |
| 29 | total_cofins | decimal(15,4) | SIM | - | 0.0000 | - |
| 30 | total_ir | decimal(15,4) | SIM | - | 0.0000 | - |
| 31 | total_inss | decimal(15,4) | SIM | - | 0.0000 | - |
| 32 | total_csll | decimal(15,4) | SIM | - | 0.0000 | - |
| 33 | response_status | varchar(255) | SIM | - | ELABORACAO | - |
| 34 | response_status_descricao | text | SIM | - | NULL | - |
| 35 | response_validacao | text | SIM | - | NULL | - |
| 36 | response_xml | longtext | SIM | - | NULL | - |
| 37 | response_xml_link | text | SIM | - | NULL | - |
| 38 | response_pdf_link | text | SIM | - | NULL | - |
| 39 | response_nfse_id | varchar(255) | SIM | - | NULL | - |
| 40 | api_requisicao_data_hora | datetime | SIM | - | NULL | - |
| 41 | api_requisicao_contador | int | NAO | - | 0 | - |
| 42 | nfse_json | text | SIM | - | NULL | - |
| 43 | created_at | timestamp | SIM | - | NULL | - |
| 44 | updated_at | timestamp | SIM | - | NULL | - |
| 45 | deleted_at | timestamp | SIM | - | NULL | - |
| 46 | com_tomador | tinyint | NAO | - | 1 | - |

### Tabela: nota_fiscal_servico_eletronica_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 40

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nfse_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | SIM | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | SIM | MUL | NULL | - |
| 5 | servico_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 6 | servico_nome_cidade | varchar(255) | SIM | - | NULL | - |
| 7 | servico_uf | varchar(5) | SIM | - | NULL | - |
| 8 | servico_codigo_pais | varchar(4) | SIM | - | NULL | - |
| 9 | servico_nome_pais | varchar(60) | SIM | - | NULL | - |
| 10 | nfse_codigo_servico_item_id | int | SIM | MUL | NULL | - |
| 11 | codigo_numerico_servico_item | varchar(20) | SIM | - | NULL | - |
| 12 | codigo_tributacao_municipal | varchar(20) | SIM | - | NULL | - |
| 13 | descricao_servico | text | SIM | - | NULL | - |
| 14 | base_calculo | decimal(15,4) | SIM | - | 0.0000 | - |
| 15 | valor_servico | decimal(15,4) | SIM | - | 0.0000 | - |
| 16 | valor_deducoes | decimal(15,4) | SIM | - | 0.0000 | - |
| 17 | valor_outras_retencoes | decimal(15,4) | SIM | - | 0.0000 | - |
| 18 | valor_desconto_incondicionado | decimal(15,4) | SIM | - | 0.0000 | - |
| 19 | valor_desconto_condicionado | decimal(15,4) | SIM | - | 0.0000 | - |
| 20 | aliquota_iss | decimal(15,4) | SIM | - | 0.0000 | - |
| 21 | aliquota_pis | decimal(15,4) | SIM | - | 0.0000 | - |
| 22 | aliquota_cofins | decimal(15,4) | SIM | - | 0.0000 | - |
| 23 | aliquota_ir | decimal(15,4) | SIM | - | 0.0000 | - |
| 24 | aliquota_inss | decimal(15,4) | SIM | - | 0.0000 | - |
| 25 | aliquota_csll | decimal(15,4) | SIM | - | 0.0000 | - |
| 26 | valor_iss | decimal(15,4) | SIM | - | 0.0000 | - |
| 27 | valor_iss_retido | decimal(15,4) | SIM | - | 0.0000 | - |
| 28 | valor_pis | decimal(15,4) | SIM | - | 0.0000 | - |
| 29 | valor_cofins | decimal(15,4) | SIM | - | 0.0000 | - |
| 30 | valor_ir | decimal(15,4) | SIM | - | 0.0000 | - |
| 31 | valor_inss | decimal(15,4) | SIM | - | 0.0000 | - |
| 32 | valor_csll | decimal(15,4) | SIM | - | 0.0000 | - |
| 33 | created_at | timestamp | SIM | - | NULL | - |
| 34 | updated_at | timestamp | SIM | - | NULL | - |
| 35 | deleted_at | timestamp | SIM | - | NULL | - |
| 36 | tributos_federais | decimal(13,2) | SIM | - | 0.00 | - |
| 37 | tributos_estaduais | decimal(13,2) | SIM | - | 0.00 | - |
| 38 | tributos_municipais | decimal(13,2) | SIM | - | 0.00 | - |
| 39 | descricao_tributos | varchar(255) | SIM | - | NULL | - |
| 40 | nbs_cnae | varchar(255) | SIM | - | NULL | - |

### Tabela: nota_fiscal_servico_eletronica_tomador (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nfse_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | SIM | MUL | NULL | - |
| 4 | nome | varchar(100) | SIM | - | NULL | - |
| 5 | cpf_cnpj | varchar(14) | SIM | - | NULL | - |
| 6 | inscricao_municipal | varchar(15) | SIM | - | NULL | - |
| 7 | cep | varchar(8) | SIM | - | NULL | - |
| 8 | codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 9 | nome_cidade | varchar(255) | SIM | - | NULL | - |
| 10 | uf | varchar(5) | SIM | - | NULL | - |
| 11 | codigo_pais | varchar(4) | SIM | - | NULL | - |
| 12 | nome_pais | varchar(60) | SIM | - | NULL | - |
| 13 | endereco | varchar(100) | SIM | - | NULL | - |
| 14 | numero | varchar(40) | SIM | - | NULL | - |
| 15 | complemento | varchar(100) | SIM | - | NULL | - |
| 16 | bairro | varchar(100) | SIM | - | NULL | - |
| 17 | telefone | varchar(15) | SIM | - | NULL | - |
| 18 | email | varchar(100) | SIM | - | NULL | - |
| 19 | created_at | timestamp | SIM | - | NULL | - |
| 20 | updated_at | timestamp | SIM | - | NULL | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: notificacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tipo | varchar(255) | NAO | - | NULL | - |
| 3 | mensagem | text | NAO | - | NULL | - |
| 4 | empresa_id | int | NAO | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: notificacao_envio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 17

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | notificacao_template_id | int | SIM | MUL | NULL | - |
| 3 | data_hora_geracao | datetime | SIM | - | NULL | - |
| 4 | data_hora_envio | datetime | SIM | - | NULL | - |
| 5 | origem_pessoa_id | int | SIM | - | NULL | - |
| 6 | origem_registro_id | int | SIM | - | NULL | - |
| 7 | destino_fone | varchar(20) | SIM | - | NULL | - |
| 8 | destino_email | varchar(100) | SIM | - | NULL | - |
| 9 | retorno | varchar(255) | SIM | - | NULL | - |
| 10 | mensagem | text | SIM | - | NULL | - |
| 11 | status | varchar(255) | SIM | - | NULL | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |
| 15 | mensagem_id | varchar(255) | SIM | - | NULL | - |
| 16 | error | varchar(255) | SIM | - | NULL | - |
| 17 | data_erro | timestamp | SIM | - | NULL | - |

### Tabela: notificacao_mensagem (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | assunto | varchar(255) | NAO | - | NULL | - |
| 3 | canal | varchar(255) | NAO | - | NULL | - |
| 4 | titulo | varchar(255) | NAO | - | NULL | - |
| 5 | tipo | varchar(255) | SIM | - | NULL | - |
| 6 | mensagem | text | NAO | - | NULL | - |
| 7 | enviar_link_pesquisa | tinyint | NAO | - | 0 | - |
| 8 | permitir_excluir | tinyint | NAO | - | 1 | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: notificacao_mensagem_arquivo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int | NAO | MUL | NULL | - |
| 3 | description | varchar(255) | SIM | - | NULL | - |
| 4 | filename | varchar(255) | NAO | - | NULL | - |
| 5 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 6 | mid_file | varchar(255) | SIM | - | NULL | - |
| 7 | extension | varchar(10) | NAO | - | NULL | - |
| 8 | link | text | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: notificacao_pos_venda (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 3 | grupo_id | int | SIM | MUL | NULL | - |
| 4 | mensagem_id | int | SIM | MUL | NULL | - |
| 5 | dias | int | NAO | - | NULL | - |
| 6 | empresa_id | int | NAO | MUL | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | whatsapp | smallint | NAO | - | NULL | - |
| 11 | email | smallint | NAO | - | NULL | - |
| 12 | todos_produtos | tinyint | NAO | - | 0 | - |

### Tabela: notificacao_template (BASE TABLE)
**Linhas aprox:** 40 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | tipo_notificacao | varchar(255) | SIM | - | NULL | - |
| 3 | tipo_pessoa | varchar(255) | SIM | - | NULL | - |
| 4 | tipo_envio | enum('WHATSAPP','EMAIL') | SIM | - | NULL | - |
| 5 | origem_registro_tabela | varchar(255) | SIM | - | NULL | - |
| 6 | mensagem_titulo | text | SIM | - | NULL | - |
| 7 | mensagem_template | text | SIM | - | NULL | - |
| 8 | envio_automatico | tinyint | SIM | - | NULL | - |
| 9 | possui_anexo | tinyint | SIM | - | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |
| 13 | titulo | varchar(255) | SIM | - | NULL | - |

### Tabela: notificacao_usuario (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | notificacao_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | usuario_id | int unsigned | NAO | MUL | NULL | - |
| 4 | lido_at | timestamp | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nuvem_nfe (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 28

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | chave_nfe | varchar(50) | NAO | - | NULL | - |
| 4 | nfe_id | int | SIM | - | NULL | - |
| 5 | numero_protocolo | varchar(50) | SIM | - | NULL | - |
| 6 | numero_nfe | varchar(50) | SIM | - | NULL | - |
| 7 | serie | varchar(50) | SIM | - | NULL | - |
| 8 | cnpj_emitente | varchar(50) | SIM | - | NULL | - |
| 9 | x_nome_emitente | varchar(255) | SIM | - | NULL | - |
| 10 | inscricao_estadual | varchar(50) | SIM | - | NULL | - |
| 11 | data_hora_emissao | datetime | SIM | - | NULL | - |
| 12 | valor_nota_fiscal | decimal(15,4) | SIM | - | NULL | - |
| 13 | tipo_amb_consulta | int | SIM | - | NULL | - |
| 14 | cnpj_consulta | varchar(50) | SIM | - | NULL | - |
| 15 | data_consulta | datetime | SIM | - | NULL | - |
| 16 | tipo_destino | varchar(50) | SIM | - | NULL | - |
| 17 | resumido_nsu | varchar(50) | SIM | - | NULL | - |
| 18 | resumido_schema | varchar(50) | SIM | - | NULL | - |
| 19 | resumido_xml | text | SIM | - | NULL | - |
| 20 | processamento_nsu | varchar(50) | SIM | - | NULL | - |
| 21 | processamento_schema | varchar(50) | SIM | - | NULL | - |
| 22 | processamento_xml | longtext | SIM | - | NULL | - |
| 23 | status_nfe | varchar(50) | SIM | - | NULL | - |
| 24 | codigo_manifestacao | varchar(10) | SIM | - | 000000 | - |
| 25 | codigo_situacao_nfe | int | SIM | - | NULL | - |
| 26 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 27 | updated_at | timestamp | SIM | - | NULL | - |
| 28 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: nuvem_nfe_emissao (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 32

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | ambiente_nuvem | int | NAO | - | 2 | - |
| 4 | ambiente_nfe | int | NAO | - | 2 | - |
| 5 | codigo_status_emissao_nfe | int | NAO | - | 1 | - |
| 6 | ambiente_mdfe | int | NAO | - | 2 | - |
| 7 | codigo_status_emissao_mdfe | tinyint | NAO | - | 1 | - |
| 8 | ambiente_nfce | tinyint | NAO | - | 2 | - |
| 9 | codigo_status_emissao_nfce | tinyint | NAO | - | 1 | - |
| 10 | regime_tributario | int | NAO | - | 1 | - |
| 11 | aliquota_credito | decimal(15,2) | NAO | - | 0.00 | - |
| 12 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |
| 15 | nfce_solicitar_cpf_cnpj_valor | decimal(15,2) | SIM | - | NULL | - |
| 16 | nome_nota_fiscal | enum('RAZAO_SOCIAL','NOME_FANTASIA') | NAO | - | NOME_FANTASIA | - |
| 17 | nome_destinatario | enum('NOME_FANTASIA','RAZAO_SOCIAL') | NAO | - | NOME_FANTASIA | - |
| 18 | icms_desoneracao | smallint | NAO | - | 0 | - |
| 19 | contingencia_nfce | smallint | NAO | - | 0 | - |
| 20 | ultima_sincronizacao_contingencia | timestamp | SIM | - | NULL | - |
| 21 | contingencia_nfe | smallint | NAO | - | 0 | - |
| 22 | ambiente_nfse | tinyint | NAO | - | 2 | - |
| 23 | regime_especial_nfse | varchar(255) | SIM | - | NULL | - |
| 24 | ultimo_rps_nfse | varchar(50) | SIM | - | NULL | - |
| 25 | exigibilidade_iss | tinyint | NAO | - | 1 | - |
| 26 | competencia_nota_automatica_nfse | varchar(255) | NAO | - | data_vencimento_parcela | - |
| 27 | exibir_pagamento | tinyint | NAO | - | 1 | - |
| 28 | memoria_fiscal | smallint | NAO | - | 2 | - |
| 29 | exigibilidade_casas_decimais | tinyint | NAO | - | 2 | - |
| 30 | cfop_id | int | SIM | - | NULL | - |
| 31 | nfe_pdv_emissao | smallint | NAO | - | 1 | - |
| 32 | deduzir_icms_base_pis_cofins | tinyint | NAO | - | 0 | - |

### Tabela: nuvem_nfe_empresa (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | maximo_nsu | int | SIM | - | NULL | - |
| 3 | ultimo_nsu | int | SIM | - | NULL | - |
| 4 | ultimo_tipo_amb | int | SIM | - | NULL | - |
| 5 | ultima_data_consulta | datetime | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | empresa_id | int | NAO | MUL | 1 | - |

### Tabela: nuvem_nfe_eventos (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 20

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | evento_id | int | SIM | - | NULL | - |
| 3 | chave_nfe | varchar(50) | SIM | - | NULL | - |
| 4 | numero_protocolo | varchar(50) | SIM | - | NULL | - |
| 5 | tipo_evento | varchar(50) | SIM | - | NULL | - |
| 6 | x_evento | varchar(255) | SIM | - | NULL | - |
| 7 | numero_sequencial_evento | int | SIM | - | NULL | - |
| 8 | data_hora_registro_evento | datetime | SIM | - | NULL | - |
| 9 | tipo_amb_consulta | int | SIM | - | NULL | - |
| 10 | cnpj_consulta | varchar(50) | SIM | - | NULL | - |
| 11 | data_consulta | datetime | SIM | - | NULL | - |
| 12 | resumido_nsu | varchar(50) | SIM | - | NULL | - |
| 13 | resumido_schema | varchar(50) | SIM | - | NULL | - |
| 14 | resumido_xml | text | SIM | - | NULL | - |
| 15 | processamento_nsu | varchar(50) | SIM | - | NULL | - |
| 16 | processamento_schema | varchar(50) | SIM | - | NULL | - |
| 17 | processamento_xml | text | SIM | - | NULL | - |
| 18 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 19 | updated_at | timestamp | SIM | - | NULL | - |
| 20 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: oauth_access_tokens (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | access_token | varchar(255) | NAO | PRI | NULL | - |
| 2 | refresh_token | varchar(255) | SIM | - | NULL | - |
| 3 | client_id | varchar(255) | NAO | - | NULL | - |
| 4 | user_id | varchar(255) | SIM | - | NULL | - |
| 5 | scope | text | SIM | - | NULL | - |
| 6 | expires | datetime | NAO | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: oauth_authorization_codes (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | authorization_code | varchar(40) | NAO | PRI | NULL | - |
| 2 | client_id | varchar(80) | NAO | - | NULL | - |
| 3 | user_id | varchar(255) | SIM | - | NULL | - |
| 4 | redirect_uri | varchar(2000) | SIM | - | NULL | - |
| 5 | expires | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| 6 | scope | varchar(2000) | SIM | - | NULL | - |

### Tabela: oauth_clients (BASE TABLE)
**Linhas aprox:** 5 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | client_id | varchar(255) | NAO | PRI | NULL | - |
| 2 | client_secret | varchar(255) | NAO | - | NULL | - |
| 3 | name | varchar(255) | NAO | - | NULL | - |
| 4 | device_id | varchar(255) | NAO | - | NULL | - |
| 5 | redirect_uri | varchar(255) | SIM | - | NULL | - |
| 6 | grant_types | varchar(255) | SIM | - | NULL | - |
| 7 | scope | varchar(255) | SIM | - | NULL | - |
| 8 | user_id | varchar(255) | SIM | - | NULL | - |
| 9 | empresa_id | int | NAO | MUL | NULL | - |
| 10 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |
| 13 | visivel | smallint | SIM | - | 1 | - |
| 14 | previous_device_id | varchar(255) | SIM | - | NULL | - |
| 15 | tipo_dispositivo | varchar(60) | SIM | - | NULL | - |
| 16 | configuracao_dispositivo | text | SIM | - | NULL | - |

### Tabela: oauth_jwt (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 3

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | client_id | varchar(80) | NAO | PRI | NULL | - |
| 2 | subject | varchar(80) | SIM | - | NULL | - |
| 3 | public_key | varchar(2000) | SIM | - | NULL | - |

### Tabela: oauth_refresh_tokens (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | refresh_token | varchar(40) | NAO | PRI | NULL | - |
| 2 | client_id | varchar(80) | NAO | - | NULL | - |
| 3 | user_id | varchar(255) | SIM | - | NULL | - |
| 4 | expires | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| 5 | scope | varchar(2000) | SIM | - | NULL | - |

### Tabela: oauth_scopes (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 2

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | scope | text | SIM | - | NULL | - |
| 2 | is_default | tinyint(1) | SIM | - | NULL | - |

### Tabela: oauth_users (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 4

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | username | varchar(255) | NAO | PRI | NULL | - |
| 2 | password | varchar(2000) | SIM | - | NULL | - |
| 3 | first_name | varchar(255) | SIM | - | NULL | - |
| 4 | last_name | varchar(255) | SIM | - | NULL | - |

### Tabela: observacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | MUL | NULL | - |
| 3 | nome | text | NAO | - | NULL | - |
| 4 | tipo | varchar(50) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: orcamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 46

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | venda_id | int | SIM | - | NULL | - |
| 4 | cliente_id | int | NAO | MUL | 1 | - |
| 5 | cliente_nome | varchar(255) | NAO | - | NULL | - |
| 6 | cpf_cnpj | varchar(18) | SIM | - | NULL | - |
| 7 | email | varchar(255) | SIM | - | NULL | - |
| 8 | telefone | varchar(50) | SIM | - | NULL | - |
| 9 | condicao_pagamento | varchar(255) | SIM | - | NULL | - |
| 10 | garantia | varchar(50) | SIM | - | NULL | - |
| 11 | validade | varchar(55) | SIM | - | NULL | - |
| 12 | status | varchar(100) | SIM | - | ANDAMENTO | - |
| 13 | funcionario_id | int | NAO | MUL | 1 | - |
| 14 | observacao | text | SIM | - | NULL | - |
| 15 | desconto_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | desconto_percentual | decimal(15,2) | SIM | - | 0.00 | - |
| 17 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 18 | updated_at | timestamp | SIM | - | NULL | - |
| 19 | deleted_at | timestamp | SIM | - | NULL | - |
| 20 | cep | varchar(255) | SIM | - | NULL | - |
| 21 | endereco | varchar(255) | SIM | - | NULL | - |
| 22 | numero | varchar(255) | SIM | - | NULL | - |
| 23 | cidade_id | int | SIM | MUL | NULL | - |
| 24 | bairro | varchar(255) | SIM | - | NULL | - |
| 25 | previsao_entrega | varchar(255) | SIM | - | NULL | - |
| 26 | cancelada | tinyint(1) | NAO | - | 0 | - |
| 27 | servico_descricao | text | SIM | - | NULL | - |
| 28 | complemento | varchar(50) | SIM | - | NULL | - |
| 29 | responsavel | varchar(50) | SIM | - | NULL | - |
| 30 | tipo_lancamento | varchar(50) | SIM | - | NULL | - |
| 31 | prazo_entrega | varchar(50) | SIM | - | NULL | - |
| 32 | proposta_objetivo | varchar(255) | SIM | - | NULL | - |
| 33 | contrato_vigencia | varchar(50) | SIM | - | NULL | - |
| 34 | contrato_data_inicio | date | SIM | - | NULL | - |
| 35 | contrato_data_termino | date | SIM | - | NULL | - |
| 36 | contrato_forma_pagamento_id | int | SIM | - | NULL | - |
| 37 | contrato_conta_id | int | SIM | - | NULL | - |
| 38 | contrato_dia_vencimento | int | SIM | - | NULL | - |
| 39 | contrato_cobranca_automatica | tinyint | SIM | - | NULL | - |
| 40 | contrato_emissao_nota_automatica | tinyint | SIM | - | NULL | - |
| 41 | data_validade | date | SIM | - | NULL | - |
| 42 | contrato_data_primeiro_vencimento | varchar(255) | SIM | - | NULL | - |
| 43 | tipo_preco_id | int unsigned | SIM | MUL | NULL | - |
| 44 | contrato_cartao_id | int unsigned | SIM | - | NULL | - |
| 45 | tipo_debito_id | int | SIM | MUL | NULL | - |
| 46 | frete | enum('DESTINATARIO','REMETENTE') | SIM | - | DESTINATARIO | - |

### Tabela: orcamento_autopecas (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | orcamento_id | int | NAO | UNI | NULL | - |
| 3 | cliente_veiculo_id | int | SIM | MUL | NULL | - |
| 4 | quilometragem | int | SIM | - | NULL | - |
| 5 | funcionario_id | int | SIM | MUL | NULL | - |
| 6 | solicitacao_cliente | text | SIM | - | NULL | - |
| 7 | observacoes_tecnicas | text | SIM | - | NULL | - |
| 8 | status | enum('AGUARDANDO_APROVACAO','APROVADO','AGUARDANDO_PECAS','EM_ATENDIMENTO','CONCLUIDO','AGUARDANDO_FATURAMENTO','FATURADO','ENTREGUE','CANCELADO') | SIM | - | NULL | - |
| 9 | ordem | int | SIM | - | NULL | - |
| 10 | ordem_servico | tinyint | SIM | - | NULL | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |
| 14 | combustivel | enum('0','1/4','1/2','3/4','1') | SIM | - | NULL | - |
| 15 | box_prisma_id | bigint unsigned | SIM | MUL | NULL | - |

### Tabela: orcamento_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 19

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | orcamento_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | descricao_item | varchar(255) | SIM | - | NULL | - |
| 6 | quantidade | decimal(15,4) | NAO | - | NULL | - |
| 7 | preco | decimal(15,4) | NAO | - | NULL | - |
| 8 | preco_compra | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | preco_caixa | decimal(15,4) | NAO | - | 0.0000 | - |
| 10 | quantidade_caixa | decimal(15,2) | NAO | - | 0.00 | - |
| 11 | desconto_valor_item | decimal(15,2) | NAO | - | 0.00 | - |
| 12 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |
| 15 | acrescimo_valor_item | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | percentual_desconto | decimal(15,10) | SIM | - | NULL | - |
| 17 | percentual_acrescimo | decimal(15,10) | SIM | - | NULL | - |
| 18 | desabilita_rateio | tinyint(1) | NAO | - | 0 | - |
| 19 | essencial | tinyint | NAO | - | 0 | - |

### Tabela: orcamento_item_profissional (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | orcamento_item_id | int | NAO | MUL | NULL | - |
| 3 | funcionario_id | int | SIM | MUL | NULL | - |
| 4 | rateio | decimal(10,2) | NAO | - | 0.00 | - |
| 5 | comissao | decimal(15,2) | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: ordem_fornecimento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 27

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | fornecedor_id | int | SIM | MUL | NULL | - |
| 4 | fornecedor_nome | varchar(255) | SIM | - | NULL | - |
| 5 | telefone | varchar(15) | SIM | - | NULL | - |
| 6 | tipo_frete | enum('CIF','FOB') | SIM | - | NULL | - |
| 7 | data_previsao_chegada | datetime | SIM | - | NULL | - |
| 8 | data_envio_email | datetime | SIM | - | NULL | - |
| 9 | pedido_fornecedor | varchar(15) | SIM | - | NULL | - |
| 10 | pagamento | varchar(255) | SIM | - | NULL | - |
| 11 | observacao | text | SIM | - | NULL | - |
| 12 | periodo_vendas | enum('ULTIMOS_3_MESES','PERSONALIZADO') | SIM | - | NULL | - |
| 13 | data_periodo_de | datetime | SIM | - | NULL | - |
| 14 | data_periodo_ate | datetime | SIM | - | NULL | - |
| 15 | prazo_medio | int | NAO | - | NULL | - |
| 16 | compra_para | int | NAO | - | NULL | - |
| 17 | estoque_seguranca | int | NAO | - | NULL | - |
| 18 | grupos_lista | varchar(255) | NAO | - | NULL | - |
| 19 | fabricantes_lista | varchar(255) | NAO | - | NULL | - |
| 20 | fornecedores_lista | varchar(255) | NAO | - | NULL | - |
| 21 | produtos_sem_movimentacao | tinyint | NAO | - | NULL | - |
| 22 | created_at | timestamp | SIM | - | NULL | - |
| 23 | updated_at | timestamp | SIM | - | NULL | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |
| 25 | recebida | tinyint | NAO | - | 0 | - |
| 26 | data_hora_recebimento | datetime | SIM | - | NULL | - |
| 27 | funcionario_recebimento_id | int | SIM | MUL | NULL | - |

### Tabela: ordem_fornecimento_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | ordem_fornecimento_id | int unsigned | SIM | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | quantidade | decimal(15,4) | NAO | - | NULL | - |
| 6 | preco_compra | decimal(15,4) | NAO | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: origem_venda (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: password_resets (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 3

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | email | varchar(255) | NAO | MUL | NULL | - |
| 2 | token | varchar(255) | NAO | MUL | NULL | - |
| 3 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |

### Tabela: permission_role (BASE TABLE)
**Linhas aprox:** 705 | **Colunas:** 3

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | permission_id | int | NAO | - | NULL | - |
| 3 | role_id | int | NAO | - | NULL | - |

### Tabela: permissions (BASE TABLE)
**Linhas aprox:** 503 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | permission_title | varchar(255) | NAO | - | NULL | - |
| 3 | permission_slug | varchar(255) | NAO | - | NULL | - |
| 4 | permission_description | varchar(255) | SIM | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | permission_module | varchar(255) | NAO | - | NULL | - |
| 9 | integrar_api | smallint | NAO | - | 1 | - |

### Tabela: petshop_album_foto_clinica (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | animal_id | int | SIM | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_anamnese (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | animal_id | int | SIM | MUL | NULL | - |
| 3 | tipo | enum('PADRAO','DETALHADA') | SIM | - | NULL | - |
| 4 | retorno | tinyint | SIM | - | NULL | - |
| 5 | data_atendimento | datetime | SIM | - | NULL | - |
| 6 | motivo | text | SIM | - | NULL | - |
| 7 | exame_fisico | text | SIM | - | NULL | - |
| 8 | diagnostico | text | SIM | - | NULL | - |
| 9 | tratamento | text | SIM | - | NULL | - |
| 10 | proximos_passos | text | SIM | - | NULL | - |
| 11 | observacoes_internas | text | SIM | - | NULL | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | nome_usuario_funcionario | varchar(255) | NAO | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_anexo_exame (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int unsigned | NAO | MUL | NULL | - |
| 3 | description | varchar(255) | SIM | - | NULL | - |
| 4 | filename | varchar(255) | NAO | - | NULL | - |
| 5 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 6 | mid_file | varchar(255) | SIM | - | NULL | - |
| 7 | extension | varchar(10) | NAO | - | NULL | - |
| 8 | link | text | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_animal (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 26

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | cliente_id | int | NAO | MUL | NULL | - |
| 3 | especie_id | int | NAO | MUL | NULL | - |
| 4 | raca_id | int | SIM | MUL | NULL | - |
| 5 | pelagem_id | int | SIM | MUL | NULL | - |
| 6 | porte_id | int | SIM | MUL | NULL | - |
| 7 | nome | varchar(255) | NAO | - | NULL | - |
| 8 | sexo | enum('MACHO','FEMEA') | NAO | - | NULL | - |
| 9 | data_nascimento | date | SIM | - | NULL | - |
| 10 | anos | int | SIM | - | 0 | - |
| 11 | meses | int | SIM | - | 0 | - |
| 12 | peso | decimal(15,2) | NAO | - | NULL | - |
| 13 | alergia | text | SIM | - | NULL | - |
| 14 | temperamento | text | SIM | - | NULL | - |
| 15 | numero_pedigree | varchar(255) | SIM | - | NULL | - |
| 16 | chip | varchar(255) | SIM | - | NULL | - |
| 17 | observacao | text | SIM | - | NULL | - |
| 18 | esterelizacao | enum('FERTIL','VAZECTOMIZADO','CASTRADO') | NAO | - | NULL | - |
| 19 | status | enum('VIVO','OBITO') | NAO | - | NULL | - |
| 20 | imagem | varchar(255) | SIM | - | NULL | - |
| 21 | filename | varchar(255) | SIM | - | NULL | - |
| 22 | created_at | timestamp | SIM | - | NULL | - |
| 23 | desativar | tinyint | NAO | - | NULL | - |
| 24 | updated_at | timestamp | SIM | - | NULL | - |
| 25 | deleted_at | timestamp | SIM | - | NULL | - |
| 26 | consumo_racao | decimal(8,2) | SIM | - | NULL | - |

### Tabela: petshop_animal_imagem (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int | NAO | MUL | NULL | - |
| 3 | observacoes | varchar(255) | SIM | - | NULL | - |
| 4 | description | varchar(255) | SIM | - | NULL | - |
| 5 | filename | varchar(255) | NAO | - | NULL | - |
| 6 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 7 | mid_file | varchar(255) | SIM | - | NULL | - |
| 8 | extension | varchar(10) | NAO | - | NULL | - |
| 9 | link | text | SIM | - | NULL | - |
| 10 | clinica | tinyint | NAO | - | NULL | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |
| 14 | album_foto_clinica_id | bigint unsigned | SIM | MUL | NULL | - |

### Tabela: petshop_atendimento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | animal_id | int | NAO | MUL | NULL | - |
| 4 | tipo_atendimento_id | int unsigned | SIM | MUL | NULL | - |
| 5 | duracao | int | NAO | - | NULL | - |
| 6 | horario | varchar(5) | SIM | - | NULL | - |
| 7 | turno | enum('MANHA','TARDE') | NAO | - | MANHA | - |
| 8 | funcionario_id | int | SIM | MUL | NULL | - |
| 9 | data_atendimento | date | NAO | - | NULL | - |
| 10 | observacao | text | SIM | - | NULL | - |
| 11 | status | enum('AGENDADO','EM_ESPERA','EM_ATENDIMENTO','CONCLUIDO','CANCELADO') | NAO | - | NULL | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | nome_usuario_funcionario | varchar(255) | NAO | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |
| 16 | avulso | tinyint | NAO | - | 0 | - |
| 17 | inicio_atendimento | timestamp | SIM | - | NULL | - |
| 18 | inicio_espera | timestamp | SIM | - | NULL | - |
| 19 | doenca_pre_existente | varchar(255) | SIM | - | NULL | - |
| 20 | problema_auditivo | varchar(255) | SIM | - | NULL | - |
| 21 | doenca_pele | varchar(255) | SIM | - | NULL | - |

### Tabela: petshop_atendimento_atestados_termos (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | animal_id | int | SIM | MUL | NULL | - |
| 3 | texto | text | SIM | - | NULL | - |
| 4 | nome | varchar(255) | NAO | - | NULL | - |
| 5 | tipo | enum('ATESTADO','TERMOS') | NAO | - | NULL | - |
| 6 | data_atendimento | date | NAO | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | nome_usuario_funcionario | varchar(255) | NAO | - | NULL | - |

### Tabela: petshop_atendimento_checklist (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | atendimento_id | int unsigned | NAO | MUL | NULL | - |
| 3 | tipo_condicao_animal_id | bigint unsigned | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_atendimento_servico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tipo_atendimento_id | int unsigned | SIM | MUL | NULL | - |
| 3 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_configuracao (BASE TABLE)
**Linhas aprox:** 1 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | gerar_atendimento_servico | tinyint | NAO | - | NULL | - |
| 3 | tipo_registro_tempo | enum('HORARIO','TURNO') | NAO | - | HORARIO | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_contrato_pacote (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int | SIM | - | NULL | - |
| 3 | venda_id | int | SIM | MUL | NULL | - |
| 4 | animal_id | int | NAO | MUL | NULL | - |
| 5 | data_validade | datetime | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_contrato_pacote_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | contrato_pacote_id | int | NAO | MUL | NULL | - |
| 3 | pacote_item_id | int | NAO | MUL | NULL | - |
| 4 | quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 5 | quantidade_retirada | decimal(15,4) | NAO | - | 0.0000 | - |
| 6 | valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_especie (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | desativar | tinyint | NAO | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_exame (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | SIM | - | NULL | - |
| 3 | observacoes | text | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | petshop_exame_cabecalho_id | int unsigned | NAO | MUL | NULL | - |

### Tabela: petshop_exame_cabecalho (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | animal_id | int | SIM | MUL | NULL | - |
| 3 | observacoes | varchar(255) | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | nome_usuario_funcionario | varchar(255) | NAO | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | data_solicitacao | date | SIM | - | NULL | - |

### Tabela: petshop_laboratorio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | SIM | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_lancamento_vacina (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | animal_id | int | SIM | MUL | NULL | - |
| 3 | vacina_protocolo_id | int | SIM | MUL | NULL | - |
| 4 | data_inicio | date | SIM | - | NULL | - |
| 5 | data_interrupcao | date | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_modelo_prescricao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | SIM | - | NULL | - |
| 3 | tipo | enum('PROCEDIMENTO','MEDICAMENTO') | SIM | - | NULL | - |
| 4 | tipo_farmacia | enum('VETERINARIA','HUMANA') | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | desativar | tinyint | NAO | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_motivo_suspeita (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | petshop_exame_cabecalho_id | int unsigned | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_ordem_servico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | venda_id | int | SIM | MUL | NULL | - |
| 4 | animal_id | int | NAO | MUL | NULL | - |
| 5 | atendimento_id | int unsigned | SIM | MUL | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_ordem_servico_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | MUL | NULL | - |
| 3 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 4 | ordem_servico_id | int | NAO | MUL | NULL | - |
| 5 | funcionario_id | int | SIM | MUL | NULL | - |
| 6 | atendimento_id | int unsigned | SIM | MUL | NULL | - |
| 7 | horario | varchar(5) | SIM | - | NULL | - |
| 8 | turno | enum('MANHA','TARDE') | NAO | - | MANHA | - |
| 9 | contrato_pacote_item_id | int | SIM | MUL | NULL | - |
| 10 | quantidade | decimal(15,2) | NAO | - | NULL | - |
| 11 | preco | decimal(15,2) | NAO | - | NULL | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_pacote (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | controlar_validade | tinyint | NAO | - | 0 | - |
| 5 | validade_dias | int | SIM | - | NULL | - |
| 6 | ativa | tinyint | NAO | - | NULL | - |
| 7 | desconto_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | desconto_percentual | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | acrescimo_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 10 | acrescimo_percentual | decimal(15,4) | NAO | - | 0.0000 | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_pacote_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | pacote_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | preco | decimal(15,2) | NAO | - | 0.00 | - |
| 6 | quantidade | decimal(15,2) | NAO | - | 0.00 | - |
| 7 | preco_compra | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | desconto_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | acrescimo_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 10 | percentual_desconto | decimal(15,4) | NAO | - | 0.0000 | - |
| 11 | percentual_acrescimo | decimal(15,4) | NAO | - | 0.0000 | - |
| 12 | created_at | timestamp | SIM | - | NULL | - |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_pelagem (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_peso (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | animal_id | int | SIM | MUL | NULL | - |
| 3 | peso | decimal(8,2) | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | data_registro | date | NAO | - | NULL | - |
| 6 | nome_usuario_funcionario | varchar(255) | NAO | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | observacao | text | SIM | - | NULL | - |

### Tabela: petshop_porte (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_posologia (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | modelo_prescricao_id | int | SIM | MUL | NULL | - |
| 3 | referencia | varchar(50) | SIM | - | NULL | - |
| 4 | dosagem | enum('1/4','1/2','1','2','3','4','5') | SIM | - | NULL | - |
| 5 | medida | enum('CAPSULAS','COMPRIMIDOS','DRAGEAS','DOSES','GRAMAS','GOTAS','MILIGRAMAS','MILILITROS') | SIM | - | NULL | - |
| 6 | duracao | enum('CONTINUO','HORAS','DIAS','SEMANAS','MESES') | SIM | - | NULL | - |
| 7 | frequencia | enum('HORAS','DIAS','SEMANAS','MESES') | SIM | - | NULL | - |
| 8 | via | enum('ORAL','TOPICO','OFTALMICO','OTOLOGICO','AMBIENTE') | SIM | - | NULL | - |
| 9 | quantidade | enum('1','2','3','4','5','6','7','8','9','10') | SIM | - | NULL | - |
| 10 | descricao_final | text | SIM | - | NULL | - |
| 11 | quantidade_duracao | int | SIM | - | NULL | - |
| 12 | frequencia_duracao | int | SIM | - | NULL | - |
| 13 | created_at | timestamp | SIM | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_raca (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | especie_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_receita (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | animal_id | int | SIM | MUL | NULL | - |
| 3 | tipo_prescricao | enum('SIMPLES','CONTROLE_ESPECIAL') | SIM | - | NULL | - |
| 4 | observacoes | text | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | nome_usuario_funcionario | varchar(255) | NAO | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | data | date | NAO | - | NULL | - |

### Tabela: petshop_receita_prescricao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | receita_id | int unsigned | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | dosagem | enum('1/4','1/2','1','2','3','4','5') | SIM | - | NULL | - |
| 5 | medida | enum('CAPSULAS','COMPRIMIDOS','DRAGEAS','DOSES','GRAMAS','GOTAS','MILIGRAMAS','MILILITROS') | SIM | - | NULL | - |
| 6 | frequencia | enum('HORAS','DIAS','SEMANAS','MESES') | SIM | - | NULL | - |
| 7 | frequencia_duracao | int | SIM | - | NULL | - |
| 8 | duracao | enum('CONTINUO','HORAS','DIAS','SEMANAS','MESES') | SIM | - | NULL | - |
| 9 | tipo_farmacia | enum('VETERINARIA','HUMANA') | SIM | - | NULL | - |
| 10 | via | enum('ORAL','TOPICO','OFTALMICO','OTOLOGICO','AMBIENTE') | SIM | - | NULL | - |
| 11 | quantidade | enum('1','2','3','4','5','6','7','8','9','10') | SIM | - | NULL | - |
| 12 | descricao_final | text | NAO | - | NULL | - |
| 13 | created_at | timestamp | SIM | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |
| 16 | duracao_periodo | int | SIM | - | NULL | - |

### Tabela: petshop_tipo_atendimento (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome_atendimento | varchar(255) | SIM | - | NULL | - |
| 3 | duracao | varchar(50) | SIM | - | NULL | - |
| 4 | cor | varchar(7) | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | desativar | tinyint | NAO | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_tipo_condicao_animal (BASE TABLE)
**Linhas aprox:** 8 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_vacina (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | SIM | - | NULL | - |
| 3 | grupo | enum('VACINA','VERMIFUGO','ANTIPARASITARIO') | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | desativar | tinyint | NAO | - | 0 | - |
| 8 | respeitar_intervalo | int | NAO | - | 1 | - |

### Tabela: petshop_vacina_laboratorio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | vacina_id | int | SIM | MUL | NULL | - |
| 3 | laboratorio_id | int | SIM | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_vacina_protocolo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | vacina_id | int | SIM | MUL | NULL | - |
| 3 | especie_id | int | SIM | MUL | NULL | - |
| 4 | nome | varchar(255) | SIM | - | NULL | - |
| 5 | aplicacao | enum('TEMPO_INDETERMINADO','1','2','3','4','5','6','7','8','9','10') | SIM | - | NULL | - |
| 6 | intervalo | int | SIM | - | NULL | - |
| 7 | vem_apos | int | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: petshop_vacina_protocolo_aplicacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | lancamento_vacina_id | int | SIM | MUL | NULL | - |
| 3 | data_programacao | date | SIM | - | NULL | - |
| 4 | data_aplicacao | datetime | SIM | - | NULL | - |
| 5 | laboratorio_id | int | SIM | MUL | NULL | - |
| 6 | laboratorio_nome | varchar(255) | SIM | - | NULL | - |
| 7 | lote | varchar(255) | SIM | - | NULL | - |
| 8 | data_cancelamento | datetime | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | nome_usuario_funcionario | varchar(255) | NAO | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: pivot_nfe (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | SIM | MUL | NULL | - |
| 3 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_categoria (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | grupo_id | int | NAO | MUL | NULL | - |
| 4 | portal_360_category_id | varchar(255) | SIM | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_cliente (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | NULL | - |
| 4 | portal_360_customer_id | varchar(255) | SIM | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | portal_360_contact_id | varchar(255) | SIM | MUL | NULL | - |
| 9 | portal_360_address_id | varchar(255) | SIM | MUL | NULL | - |

### Tabela: portal_360_cliente_contato (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | NULL | - |
| 4 | contato_id | int | SIM | MUL | NULL | - |
| 5 | portal_360_customer_id | varchar(255) | SIM | MUL | NULL | - |
| 6 | portal_360_contact_id | varchar(255) | SIM | MUL | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_cliente_endereco (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | NULL | - |
| 4 | endereco_id | int | SIM | MUL | NULL | - |
| 5 | portal_360_customer_id | varchar(255) | SIM | MUL | NULL | - |
| 6 | portal_360_address_id | varchar(255) | SIM | MUL | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_cliente_recebivel (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | NULL | - |
| 4 | parcela_id | int | NAO | MUL | NULL | - |
| 5 | portal_360_customer_id | varchar(255) | SIM | MUL | NULL | - |
| 6 | portal_360_receivable_id | varchar(255) | SIM | MUL | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_config (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | ultima_sincronizacao_cadastro | datetime | SIM | - | NULL | - |
| 4 | ultima_sincronizacao_vendas | datetime | SIM | - | NULL | - |
| 5 | ultima_sincronizacao_clientes | datetime | SIM | - | NULL | - |
| 6 | ultima_sincronizacao_estoque | datetime | SIM | - | NULL | - |
| 7 | ultima_sincronizacao_recebiveis | datetime | SIM | - | NULL | - |
| 8 | tempo_sinc_cadastro | int | SIM | - | NULL | - |
| 9 | tempo_sinc_venda | int | SIM | - | NULL | - |
| 10 | tempo_sinc_estoque | int | SIM | - | NULL | - |
| 11 | tasks_ativo | tinyint | NAO | - | 1 | - |
| 12 | log_webhook_ativo | tinyint | NAO | - | 0 | - |
| 13 | created_at | timestamp | SIM | - | NULL | - |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_forma_pagamento_conversao (BASE TABLE)
**Linhas aprox:** 6 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | forma_pagamento_portal360 | varchar(255) | SIM | MUL | NULL | - |
| 3 | forma_pagamento_id | int | SIM | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_marca (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | fabricante_id | int | SIM | MUL | NULL | - |
| 4 | portal_360_brand_id | varchar(255) | SIM | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_payment_term (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | financeiro_condicao_pagamento_id | bigint unsigned | NAO | MUL | NULL | - |
| 4 | portal_360_payment_term_id | varchar(36) | SIM | MUL | NULL | - |
| 5 | sync_hash | varchar(64) | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_pedido (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 21

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | portal_360_order_id | varchar(255) | SIM | MUL | NULL | - |
| 4 | order_number | varchar(255) | SIM | - | NULL | - |
| 5 | order_date | datetime | SIM | - | NULL | - |
| 6 | customer | longtext | SIM | - | NULL | - |
| 7 | customer_name | varchar(255) | SIM | - | NULL | - |
| 8 | customer_document | varchar(255) | SIM | - | NULL | - |
| 9 | portal_360_seller_id | varchar(255) | SIM | MUL | NULL | - |
| 10 | items | longtext | SIM | - | NULL | - |
| 11 | payments | longtext | SIM | - | NULL | - |
| 12 | order_payload | longtext | SIM | - | NULL | - |
| 13 | observations | text | SIM | - | NULL | - |
| 14 | status | varchar(255) | SIM | - | NULL | - |
| 15 | total | decimal(15,2) | SIM | - | NULL | - |
| 16 | discount | decimal(15,2) | SIM | - | NULL | - |
| 17 | shipping_cost | decimal(15,2) | SIM | - | NULL | - |
| 18 | venda_id | int | SIM | MUL | NULL | - |
| 19 | created_at | timestamp | SIM | - | NULL | - |
| 20 | updated_at | timestamp | SIM | - | NULL | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_produto (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | produto_empresa_id | int | NAO | MUL | NULL | - |
| 4 | portal_360_product_id | varchar(255) | SIM | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_promocao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | promocao_id | int | SIM | MUL | NULL | - |
| 4 | portal_360_promotion_id | varchar(255) | SIM | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_venda (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | venda_id | int | SIM | MUL | NULL | - |
| 4 | portal_360_order_id | varchar(255) | SIM | MUL | NULL | - |
| 5 | numero | varchar(255) | SIM | - | NULL | - |
| 6 | data | datetime | SIM | - | NULL | - |
| 7 | status | varchar(255) | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_vendedor (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | funcionario_id | int | SIM | MUL | NULL | - |
| 4 | portal_360_seller_id | varchar(255) | SIM | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: portal_360_webhook (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | portal_360_webhook_id | varchar(255) | SIM | MUL | NULL | - |
| 4 | group | varchar(255) | SIM | - | NULL | - |
| 5 | group_event | varchar(255) | SIM | - | NULL | - |
| 6 | signature_version | int | NAO | - | 1 | - |
| 7 | url_callback | varchar(255) | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: producao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | tipo_producao | varchar(10) | NAO | - | DIRETA | - |
| 3 | status | varchar(10) | NAO | - | ABERTO | - |
| 4 | observacao | text | SIM | - | NULL | - |
| 5 | producao_produto_id | int | NAO | - | NULL | - |
| 6 | producao_produto_empresa_grade_id | int | NAO | - | NULL | - |
| 7 | producao_quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | empresa_id | int | NAO | MUL | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: producao_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | producao_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | - | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | - | NULL | - |
| 5 | quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 6 | preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 7 | peso | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto (BASE TABLE)
**Linhas aprox:** 104 | **Colunas:** 62

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | referencia | varchar(20) | SIM | - | NULL | - |
| 3 | codigo_barras | varchar(20) | SIM | - | NULL | - |
| 4 | nome | varchar(255) | NAO | - | NULL | - |
| 5 | api_guid | varchar(255) | SIM | MUL | NULL | - |
| 6 | grupo_id | int | NAO | MUL | NULL | - |
| 7 | fabricante_id | int | SIM | MUL | NULL | - |
| 8 | especifico_id | int unsigned | NAO | - | NULL | - |
| 9 | tipo_especifico | enum('VEICULO','MEDICAMENTO','ARMAMENTO','COMBUSTIVEL','PAPEL') | SIM | - | NULL | - |
| 10 | similar_id | int | SIM | MUL | NULL | - |
| 11 | observacao | text | SIM | - | NULL | - |
| 12 | informacao_adicional | text | SIM | - | NULL | - |
| 13 | unidade_medida | varchar(10) | SIM | - | UND | - |
| 14 | peso | decimal(15,4) | SIM | - | 0.0000 | - |
| 15 | altura | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | largura | decimal(15,2) | NAO | - | 0.00 | - |
| 17 | comprimento | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | garantia | varchar(50) | SIM | - | NULL | - |
| 19 | especificacao | text | SIM | - | NULL | - |
| 20 | preco_compra | decimal(15,4) | NAO | - | 0.0000 | - |
| 21 | preco_venda | decimal(15,4) | NAO | - | 0.0000 | - |
| 22 | margem_lucro | decimal(15,2) | NAO | - | 0.00 | - |
| 23 | tipo_margem_lucro | enum('PERCENTUAL','VALOR') | SIM | - | PERCENTUAL | - |
| 24 | vender | int | SIM | MUL | 1 | - |
| 25 | controlar_estoque | int | SIM | MUL | 1 | - |
| 26 | desativado | int | SIM | MUL | 0 | - |
| 27 | genero | varchar(255) | SIM | - | NULL | - |
| 28 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 29 | updated_at | timestamp | SIM | - | NULL | - |
| 30 | deleted_at | timestamp | SIM | - | NULL | - |
| 31 | habilitar_grade | int | SIM | - | 0 | - |
| 32 | order_attributes | varchar(255) | SIM | - | NULL | - |
| 33 | ncm | varchar(8) | SIM | - | NULL | - |
| 34 | origem | varchar(255) | SIM | - | 0 | - |
| 35 | cest | varchar(10) | SIM | - | NULL | - |
| 36 | percentual_comissao_produto | decimal(15,2) | NAO | - | 0.00 | - |
| 37 | servico | int | SIM | - | NULL | - |
| 38 | tipo_produto | varchar(50) | NAO | - | PRODUTO | - |
| 39 | agrupar_pedido | tinyint | NAO | - | 1 | - |
| 40 | detalhe | text | SIM | - | NULL | - |
| 41 | quantidade_caixa | decimal(15,2) | SIM | - | NULL | - |
| 42 | codigo_barras_caixa | varchar(255) | SIM | - | NULL | - |
| 43 | taxa_entrega | tinyint | NAO | - | 0 | - |
| 44 | habilitar_acompanhamento | tinyint(1) | NAO | - | 0 | - |
| 45 | self_service | tinyint(1) | SIM | - | NULL | - |
| 46 | perguntar_adicionais | tinyint(1) | SIM | - | NULL | - |
| 47 | cobrar_taxa_entrega | tinyint(1) | SIM | - | NULL | - |
| 48 | nao_enviar_comanda | tinyint(1) | SIM | - | NULL | - |
| 49 | cobrar_taxa_servico | tinyint(1) | NAO | - | 1 | - |
| 50 | controlar_estoque_composicao | tinyint | NAO | - | 0 | - |
| 51 | taxa_adicional_delivery | tinyint | NAO | - | 0 | - |
| 52 | tipo_combo | smallint | NAO | - | 0 | - |
| 53 | tipo_faturamento | smallint | NAO | - | 0 | - |
| 54 | preco_a_partir_de | decimal(15,4) | NAO | - | 0.0000 | - |
| 55 | agrupar_impressao_item_combo | tinyint | NAO | - | 0 | - |
| 56 | modo_preparo | text | SIM | - | NULL | - |
| 57 | kds_tempo_preparo | int | SIM | - | NULL | - |
| 58 | item_complementar | tinyint | NAO | - | 0 | - |
| 59 | localizacao | text | SIM | - | NULL | - |
| 60 | comissao_id | int | SIM | MUL | NULL | - |
| 61 | embalagem_id | int | SIM | - | NULL | - |
| 62 | ifood_id | varchar(255) | SIM | - | NULL | - |

### Tabela: produto_combo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | SIM | MUL | NULL | - |
| 3 | descricao | varchar(100) | NAO | - | NULL | - |
| 4 | quantidade_minima | int | NAO | - | 0 | - |
| 5 | quantidade_maxima | int | NAO | - | 0 | - |
| 6 | ordem | int | NAO | - | 0 | - |
| 7 | habilitar_pizza | tinyint(1) | NAO | - | 0 | - |
| 8 | tipo_calculo_preco | int | NAO | - | 1 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | ifood_grupo_id | varchar(255) | SIM | - | NULL | - |

### Tabela: produto_combo_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_combo_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | SIM | MUL | NULL | - |
| 4 | codigo_pdv | varchar(255) | SIM | - | NULL | - |
| 5 | preco_venda | decimal(15,4) | NAO | - | 0.0000 | - |
| 6 | quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | ifood_item_id | varchar(255) | SIM | - | NULL | - |

### Tabela: produto_composicao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | MUL | NULL | - |
| 3 | materia_prima_id | int | NAO | MUL | NULL | - |
| 4 | quantidade | decimal(15,4) | NAO | - | 0.0000 | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | produto_empresa_grade_id | int | SIM | MUL | NULL | - |

### Tabela: produto_empresa (BASE TABLE)
**Linhas aprox:** 111 | **Colunas:** 61

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | MUL | NULL | - |
| 3 | empresa_id | int | NAO | MUL | NULL | - |
| 4 | regra_fiscal_id | int | SIM | MUL | NULL | - |
| 5 | tributos_federais | decimal(15,2) | NAO | - | 0.00 | - |
| 6 | tributos_estaduais | decimal(15,2) | NAO | - | 0.00 | - |
| 7 | tributos_municipais | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | data_validade_ibpt | date | SIM | - | NULL | - |
| 9 | fundo_combate_pobreza | decimal(15,2) | NAO | - | 0.00 | - |
| 10 | preco_compra | decimal(15,4) | NAO | - | 0.0000 | - |
| 11 | icms_compra | decimal(15,2) | NAO | - | 0.00 | - |
| 12 | icms_fronteira | decimal(15,2) | NAO | - | 0.00 | - |
| 13 | ipi | decimal(15,2) | NAO | - | 0.00 | - |
| 14 | frete | decimal(15,2) | NAO | - | 0.00 | - |
| 15 | encargo_financeiro | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | custo_fixo | decimal(15,2) | NAO | - | 0.00 | - |
| 17 | imposto_federal | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | icms_venda | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | comissao | decimal(15,2) | NAO | - | 0.00 | - |
| 20 | marketing | decimal(15,2) | NAO | - | 0.00 | - |
| 21 | outro_custo | decimal(15,2) | NAO | - | 0.00 | - |
| 22 | preco_custo | decimal(15,4) | NAO | - | 0.0000 | - |
| 23 | margem_sugerida | decimal(15,2) | NAO | - | 0.00 | - |
| 24 | preco_sugerido | decimal(15,4) | NAO | - | 0.0000 | - |
| 25 | preco_venda | decimal(15,4) | NAO | - | 0.0000 | - |
| 26 | preco_a | decimal(15,2) | NAO | - | 0.00 | - |
| 27 | preco_b | decimal(15,2) | NAO | - | 0.00 | - |
| 28 | preco_c | decimal(15,2) | NAO | - | 0.00 | - |
| 29 | estoque_minimo | decimal(15,2) | NAO | - | 0.00 | - |
| 30 | localizacao | varchar(50) | SIM | - | NULL | - |
| 31 | alteracao_preco | date | SIM | - | NULL | - |
| 32 | promocao_preco | decimal(15,2) | NAO | - | 0.00 | - |
| 33 | promocao_validade | date | SIM | - | NULL | - |
| 34 | promocao_quantidade_tipo | enum('A PARTIR DE','MULTIPLOS DE','LEVE MAIS PAGUE MENOS') | SIM | - | NULL | - |
| 35 | promocao_multiplos | int | SIM | - | NULL | - |
| 36 | promocao_quantidade_bonificada | int | SIM | - | NULL | - |
| 37 | balanca | int | NAO | - | 0 | - |
| 38 | balanca_validade_dias | int | SIM | - | 0 | - |
| 39 | balanca_tara | int | NAO | - | 0 | - |
| 40 | sku_atributo | varchar(255) | SIM | - | NULL | - |
| 41 | aliquota_issqn | decimal(15,2) | SIM | - | NULL | - |
| 42 | item_lista_servico | varchar(5) | SIM | - | NULL | - |
| 43 | indicador_exigibilidade | varchar(2) | SIM | - | NULL | - |
| 44 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 45 | updated_at | timestamp | SIM | - | NULL | - |
| 46 | deleted_at | timestamp | SIM | - | NULL | - |
| 47 | preco_d | decimal(15,2) | NAO | - | 0.00 | - |
| 48 | preco_e | decimal(15,2) | NAO | - | 0.00 | - |
| 49 | codigo_beneficio_fiscal | varchar(255) | SIM | - | NULL | - |
| 50 | embalagem | decimal(15,2) | NAO | - | NULL | - |
| 51 | codigo_tributacao_municipal | varchar(255) | SIM | - | NULL | - |
| 52 | nfse_codigo_servico_item_id | int | SIM | MUL | NULL | - |
| 53 | codigo_numerico_servico_item | varchar(20) | SIM | - | NULL | - |
| 54 | data_atualizacao_preco | datetime | SIM | - | NULL | - |
| 55 | marketplace_created_at | timestamp | SIM | - | NULL | - |
| 56 | marketplace_updated_at | timestamp | SIM | - | NULL | - |
| 57 | marketplace_code | varchar(255) | SIM | - | NULL | - |
| 58 | especifico_id | int unsigned | SIM | MUL | NULL | - |
| 59 | nbs_cnae | varchar(255) | SIM | - | NULL | - |
| 60 | status_fiscal | tinyint | NAO | - | 0 | - |
| 61 | codigo_imendes | varchar(255) | SIM | - | NULL | - |

### Tabela: produto_empresa_grade (BASE TABLE)
**Linhas aprox:** 78 | **Colunas:** 22

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_empresa_id | int | NAO | MUL | NULL | - |
| 3 | sku | varchar(50) | NAO | MUL | 0 | - |
| 4 | sku_atributo | varchar(255) | NAO | - | NULL | - |
| 5 | codigo_barra | varchar(45) | NAO | - | NULL | - |
| 6 | descricao | varchar(255) | NAO | - | NULL | - |
| 7 | preco_venda | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | estoque | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | estoque_minimo | decimal(15,4) | SIM | - | 0.0000 | - |
| 10 | validade | date | SIM | - | NULL | - |
| 11 | fabricacao | date | SIM | - | NULL | - |
| 12 | ativo | tinyint(1) | NAO | - | 1 | - |
| 13 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 14 | updated_at | timestamp | SIM | - | NULL | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |
| 16 | softshop_grade | varchar(255) | SIM | - | NULL | - |
| 17 | marketplace_created_at | timestamp | SIM | - | NULL | - |
| 18 | marketplace_updated_at | timestamp | SIM | - | NULL | - |
| 19 | marketplace_code | varchar(255) | SIM | - | NULL | - |
| 20 | lote_codigo_agregacao | varchar(20) | SIM | - | NULL | - |
| 21 | curva_abc | varchar(5) | SIM | - | NULL | - |
| 22 | data_atualizacao_curva_abc | datetime | SIM | - | NULL | - |

### Tabela: produto_empresa_vinculo_fiscal (BASE TABLE)
**Linhas aprox:** 77 | **Colunas:** 4

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | produto_empresa_id | int | NAO | MUL | NULL | - |
| 3 | vinculo_fiscal_id | int unsigned | NAO | MUL | NULL | - |
| 4 | empresa_id | int | SIM | MUL | NULL | - |

### Tabela: produto_especifico_armamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | especifico_tipo_arma | varchar(1) | NAO | - | NULL | - |
| 3 | especifico_numero_serie_arma | varchar(15) | NAO | - | NULL | - |
| 4 | especifico_numero_serie_cano | varchar(15) | NAO | - | NULL | - |
| 5 | especifico_ | varchar(255) | NAO | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_especifico_combustivel (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 22

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | especifico_codigo_produto | varchar(9) | NAO | - | NULL | - |
| 3 | especifico_descricao_produto | varchar(255) | NAO | - |  | - |
| 4 | especifico_percentual_glp | decimal(7,4) | SIM | - | 0.0000 | - |
| 5 | especifico_percentual_gas_natural_importado | decimal(7,4) | SIM | - | 0.0000 | - |
| 6 | especifico_valor_partida | decimal(15,2) | SIM | - | 0.00 | - |
| 7 | especifico_percentual_gas_natural | decimal(7,4) | SIM | - | NULL | - |
| 8 | especifico_codif | varchar(21) | SIM | - | NULL | - |
| 9 | especifico_quantidade_combustivel | decimal(16,4) | SIM | - | NULL | - |
| 10 | especifico_uf_consumo | varchar(2) | SIM | - | NULL | - |
| 11 | especifico_quantidade_bc_cide | decimal(16,4) | SIM | - | NULL | - |
| 12 | especifico_aliquota_cide | decimal(15,4) | SIM | - | NULL | - |
| 13 | especifico_valor_cide | decimal(15,2) | SIM | - | NULL | - |
| 14 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 15 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |
| 17 | percentual_bio | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | aliquota_ad_rem | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | aliquota_ad_rem_icms_reten | decimal(15,2) | NAO | - | 0.00 | - |
| 20 | aliquota_ad_rem_icms_ret | decimal(15,2) | NAO | - | 0.00 | - |
| 21 | percentual_reducao_ad_rem | decimal(15,2) | NAO | - | 0.00 | - |
| 22 | motivo_reducao_ad_rem | int | SIM | - | NULL | - |

### Tabela: produto_especifico_combustivel_origem (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | indicador_importacao | int | NAO | - | NULL | - |
| 3 | codigo_uf_origem | varchar(255) | NAO | - | NULL | - |
| 4 | percentual_originario_uf | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | produto_especifico_combustivel_id | int unsigned | NAO | MUL | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_especifico_medicamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 3 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 4 | deleted_at | timestamp | SIM | - | NULL | - |
| 5 | especifico_codigo_anvisa | varchar(20) | NAO | - | NULL | - |
| 6 | especifico_motivo_isencao | varchar(255) | SIM | - | NULL | - |

### Tabela: produto_especifico_papel (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | especifico_numero_recopi | varchar(20) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 4 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_especifico_veiculo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 28

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | especifico_tipo_operacao | varchar(1) | NAO | - | NULL | - |
| 3 | especifico_chassi | varchar(17) | NAO | - | NULL | - |
| 4 | especifico_cor_codigo | varchar(4) | NAO | - | NULL | - |
| 5 | especifico_cor_descricao | varchar(40) | NAO | - | NULL | - |
| 6 | especifico_potencia_motor | varchar(4) | NAO | - | NULL | - |
| 7 | especifico_cilindrada | varchar(4) | NAO | - | NULL | - |
| 8 | especifico_peso_liquido | varchar(9) | NAO | - | NULL | - |
| 9 | especifico_peso_bruto | varchar(9) | NAO | - | NULL | - |
| 10 | especifico_numero_serie | varchar(9) | NAO | - | NULL | - |
| 11 | especifico_tipo_combustivel | varchar(2) | NAO | - | NULL | - |
| 12 | especifico_numero_motor | varchar(21) | NAO | - | NULL | - |
| 13 | especifico_capacidade_maxima_tracao | varchar(9) | NAO | - | NULL | - |
| 14 | especifico_distancia_eixo | varchar(4) | NAO | - | NULL | - |
| 15 | especifico_ano_modelo | tinyint | NAO | - | NULL | - |
| 16 | especifico_ano_fabricacao | tinyint | NAO | - | NULL | - |
| 17 | especifico_tipo_pintura | varchar(1) | NAO | - | NULL | - |
| 18 | especifico_tipo_veiculo | varchar(2) | NAO | - | NULL | - |
| 19 | especifico_especie_veiculo | varchar(1) | NAO | - | NULL | - |
| 20 | especifico_condicao_vin | varchar(1) | NAO | - | NULL | - |
| 21 | especifico_condicao_veiculo | varchar(1) | NAO | - | NULL | - |
| 22 | especifico_codigo_marca_modelo | varchar(6) | NAO | - | NULL | - |
| 23 | especifico_codigo_cor_denatran | varchar(2) | NAO | - | NULL | - |
| 24 | especifico_lotacao_capacidade | varchar(3) | NAO | - | NULL | - |
| 25 | especifico_tipo_restricao | varchar(1) | NAO | - | NULL | - |
| 26 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 27 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 28 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_estoque_ruptura (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | estoque | decimal(15,4) | NAO | - | NULL | - |
| 3 | data_ruptura | date | NAO | - | NULL | - |
| 4 | produto_id | int | NAO | MUL | NULL | - |
| 5 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 6 | venda_id | int | NAO | MUL | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_fornecedor (BASE TABLE)
**Linhas aprox:** 72 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_empresa_id | int | NAO | MUL | NULL | - |
| 3 | codigo_fornecedor | varchar(50) | NAO | - | NULL | - |
| 4 | cnpj_fornecedor | varchar(18) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_imagem (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int | NAO | - | NULL | - |
| 3 | description | varchar(255) | SIM | - | NULL | - |
| 4 | filename | varchar(255) | NAO | - | NULL | - |
| 5 | thumbnail | varchar(255) | SIM | - | NULL | - |
| 6 | mid_file | varchar(255) | SIM | - | NULL | - |
| 7 | extension | varchar(10) | NAO | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |
| 11 | link | text | SIM | - | NULL | - |
| 12 | use_default | tinyint(1) | SIM | - | 0 | - |
| 13 | produto_empresa_id | int | SIM | - | NULL | - |

### Tabela: produto_marketplace (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 23

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | produto_empresa_id | int | NAO | MUL | NULL | - |
| 3 | disponibilidade | enum('DISPONIVEL','INDISPONIVEL','ESTOQUE') | NAO | - | NULL | - |
| 4 | descricao | longtext | NAO | - | NULL | - |
| 5 | preco | decimal(15,2) | NAO | - | NULL | - |
| 6 | preco_personalizado | smallint | NAO | - | NULL | - |
| 7 | habilitar | smallint | NAO | - | NULL | - |
| 8 | link_carrinho | varchar(255) | SIM | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |
| 12 | habilitar_estoque | smallint | NAO | - | NULL | - |
| 13 | quantidade_por_pedido | decimal(15,4) | NAO | - | 0.0000 | - |
| 14 | promocao_preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 15 | promocao_data_inicial | date | SIM | - | NULL | - |
| 16 | promocao_data_final | date | SIM | - | NULL | - |
| 17 | estoque_ruptura | decimal(15,4) | NAO | - | 0.0000 | - |
| 18 | produto_personalizado | smallint | NAO | - | 0 | - |
| 19 | produto_descricao | varchar(255) | SIM | - | NULL | - |
| 20 | grupo_id | int | SIM | - | NULL | - |
| 21 | marketplace_vinculado_id | int | SIM | - | NULL | - |
| 22 | status_api | varchar(255) | SIM | - | NULL | - |
| 23 | personalizar_canais_venda | tinyint(1) | NAO | - | 0 | - |

### Tabela: produto_marketplace_anuncio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_empresa_id | int | NAO | - | NULL | - |
| 3 | tipo | varchar(50) | NAO | - | NULL | - |
| 4 | titulo | varchar(255) | NAO | - | NULL | - |
| 5 | descricao | text | NAO | - | NULL | - |
| 6 | habilitar | tinyint(1) | NAO | - | 1 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_marketplace_hub_saleschannel (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_empresa_id | int | NAO | - | NULL | - |
| 3 | saleschannel_codigo | varchar(50) | NAO | - | NULL | - |
| 4 | preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 5 | promocao_preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 6 | promocao_data_inicial | date | SIM | - | NULL | - |
| 7 | promocao_data_final | date | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_organizar_estoque (BASE TABLE)
**Linhas aprox:** 65 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | produto_id | int | NAO | - | NULL | - |
| 2 | produto_empresa_grade_id | int | NAO | PRI | NULL | - |
| 3 | venda | decimal(15,4) | NAO | - | 0.0000 | - |
| 4 | compra | decimal(15,4) | NAO | - | 0.0000 | - |
| 5 | ajuste_entrada | decimal(15,4) | NAO | - | 0.0000 | - |
| 6 | ajuste_saida | decimal(15,4) | NAO | - | 0.0000 | - |
| 7 | transferencia_entrada | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | transferencia_saida | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | requisicao | decimal(15,4) | NAO | - | 0.0000 | - |
| 10 | devolucao | decimal(15,4) | NAO | - | 0.0000 | - |
| 11 | composicao | decimal(15,4) | NAO | - | 0.0000 | - |
| 12 | nfe_entrada | decimal(15,4) | NAO | - | 0.0000 | - |
| 13 | nfe_saida | decimal(15,4) | NAO | - | 0.0000 | - |
| 14 | created_at | timestamp | SIM | - | NULL | - |
| 15 | updated_at | timestamp | SIM | - | NULL | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_relacionado (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | MUL | NULL | - |
| 3 | produto_relacionado_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: produto_restaurante_setor (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | MUL | NULL | - |
| 3 | restaurante_setor_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: promocao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 18

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | data_hora_inicio | datetime | NAO | - | NULL | - |
| 4 | data_hora_fim | datetime | NAO | - | NULL | - |
| 5 | ativa | tinyint(1) | SIM | - | 0 | - |
| 6 | segunda | tinyint(1) | SIM | - | NULL | - |
| 7 | terca | tinyint(1) | SIM | - | NULL | - |
| 8 | quarta | tinyint(1) | SIM | - | NULL | - |
| 9 | quinta | tinyint(1) | SIM | - | NULL | - |
| 10 | sexta | tinyint(1) | SIM | - | NULL | - |
| 11 | sabado | tinyint(1) | SIM | - | NULL | - |
| 12 | domingo | tinyint(1) | SIM | - | NULL | - |
| 13 | hora_inicio | time | SIM | - | NULL | - |
| 14 | hora_fim | time | SIM | - | NULL | - |
| 15 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 16 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 17 | deleted_at | timestamp | SIM | - | NULL | - |
| 18 | modulo | varchar(255) | SIM | - | NULL | - |

### Tabela: promocao_empresa (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | promocao_id | int unsigned | NAO | MUL | NULL | - |
| 3 | empresa_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: promocao_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | MUL | NULL | - |
| 3 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 4 | promocao_id | int unsigned | NAO | MUL | NULL | - |
| 5 | percentual_promocao | decimal(15,4) | SIM | - | 0.0000 | - |
| 6 | tipo_promocao | enum('PERCENTUAL','APARTIRDE','MAISPORMENOS','MULTIPLOSDE') | SIM | - | PERCENTUAL | - |
| 7 | quantidade | decimal(15,4) | SIM | - | 0.0000 | - |
| 8 | quantidade_bonificada | decimal(15,4) | SIM | - | 0.0000 | - |
| 9 | valor_promocional_unidade | decimal(15,4) | SIM | - | 0.0000 | - |
| 10 | descricao_promocional_quantidade | text | SIM | - | NULL | - |
| 11 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: reajuste (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 31

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tipo | enum('TODOS','NOTA_ENTRADA') | NAO | - | NULL | - |
| 3 | data_inicial | timestamp | SIM | - | NULL | - |
| 4 | data_final | timestamp | SIM | - | NULL | - |
| 5 | numero_nota | varchar(255) | SIM | - | NULL | - |
| 6 | imposto_compra | decimal(15,2) | NAO | - | NULL | - |
| 7 | imposto_venda | decimal(15,2) | NAO | - | NULL | - |
| 8 | icms_compra | decimal(15,2) | NAO | - | NULL | - |
| 9 | icms_fronteira_compra | decimal(15,2) | NAO | - | NULL | - |
| 10 | ipi_compra | decimal(15,2) | NAO | - | NULL | - |
| 11 | frete_compra | decimal(15,2) | NAO | - | NULL | - |
| 12 | embalagem_compra | decimal(15,2) | NAO | - | NULL | - |
| 13 | encargos_compra | decimal(15,2) | NAO | - | NULL | - |
| 14 | custo_fixo_venda | decimal(15,4) | NAO | - | NULL | - |
| 15 | impostos_federais_venda | decimal(15,2) | NAO | - | NULL | - |
| 16 | icms_venda | decimal(15,2) | NAO | - | NULL | - |
| 17 | comissao_venda | decimal(15,2) | NAO | - | NULL | - |
| 18 | marketing_venda | decimal(15,2) | NAO | - | NULL | - |
| 19 | outros_venda | decimal(15,2) | NAO | - | NULL | - |
| 20 | margem_lucro | decimal(15,2) | NAO | - | NULL | - |
| 21 | produto_id | int | SIM | MUL | NULL | - |
| 22 | fabricante_id | int | SIM | MUL | NULL | - |
| 23 | fornecedor_id | int | SIM | - | NULL | - |
| 24 | grupo_id | int | SIM | MUL | NULL | - |
| 25 | tabela_preco_id | int unsigned | SIM | MUL | NULL | - |
| 26 | operacao | enum('AJUSTAR_PRECO','FORMAR_PRECO') | NAO | - | NULL | - |
| 27 | reajuste | decimal(15,4) | NAO | - | NULL | - |
| 28 | status | enum('ABERTO','FINALIZADO') | NAO | - | ABERTO | - |
| 29 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 30 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 31 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: reajuste_item (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | reajuste_id | int unsigned | NAO | MUL | NULL | - |
| 3 | produto_empresa_id | int | NAO | MUL | NULL | - |
| 4 | imposto_compra | decimal(15,2) | NAO | - | 0.00 | - |
| 5 | imposto_venda | decimal(15,2) | NAO | - | 0.00 | - |
| 6 | custo_produto | decimal(15,4) | NAO | - | 0.0000 | - |
| 7 | ponto_equilibrio | decimal(15,4) | NAO | - | 0.0000 | - |
| 8 | margem_lucro | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | preco_compra | decimal(15,4) | NAO | - | NULL | - |
| 10 | preco_venda | decimal(15,4) | NAO | - | NULL | - |
| 11 | reajuste | decimal(15,4) | NAO | - | NULL | - |
| 12 | preco_reajuste | decimal(15,4) | NAO | - | NULL | - |
| 13 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 14 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: recebimento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 15

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | char(36) | NAO | PRI | NULL | - |
| 2 | dispositivo_id | varchar(255) | NAO | - | NULL | - |
| 3 | transacao_descricao | varchar(255) | NAO | - | NULL | - |
| 4 | transacao_tipo | varchar(255) | NAO | - | 0 | - |
| 5 | operacao_tipo | varchar(255) | NAO | - | 0 | - |
| 6 | transacao_id | varchar(255) | NAO | - | NULL | - |
| 7 | transacao_data_utc | varchar(255) | NAO | - | NULL | - |
| 8 | valor | decimal(15,2) | NAO | - | 0.00 | - |
| 9 | parcelas | int | SIM | - | 0 | - |
| 10 | restricoes | text | SIM | - | NULL | - |
| 11 | doc | varchar(255) | SIM | - | NULL | - |
| 12 | outras_informacoes | text | SIM | - | NULL | - |
| 13 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 14 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 15 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: recebimento_autorizacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 20

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | char(36) | NAO | PRI | NULL | - |
| 2 | recebimento_id | char(36) | NAO | - | NULL | - |
| 3 | numero_terminal | varchar(255) | SIM | - | NULL | - |
| 4 | forma_pagamento | varchar(255) | SIM | - | NULL | - |
| 5 | comprovante_tipo | varchar(255) | SIM | - | NULL | - |
| 6 | comprovante_cliente | varchar(255) | SIM | - | NULL | - |
| 7 | comprovante_estabelecimento | varchar(255) | SIM | - | NULL | - |
| 8 | nsu | varchar(255) | NAO | - | NULL | - |
| 9 | host | varchar(255) | NAO | - | NULL | - |
| 10 | auto | varchar(255) | SIM | - | NULL | - |
| 11 | bin | varchar(255) | SIM | - | NULL | - |
| 12 | bandeira | varchar(255) | SIM | - | NULL | - |
| 13 | bandeira_tipo | varchar(255) | SIM | - | NULL | - |
| 14 | cnpj_credenciadora | varchar(255) | SIM | - | NULL | - |
| 15 | codigo_autorizacao | varchar(255) | SIM | - | NULL | - |
| 16 | cartao_validade | varchar(255) | SIM | - | NULL | - |
| 17 | cartao_titular | varchar(255) | SIM | - | NULL | - |
| 18 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 19 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 20 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: recebimento_status (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | char(36) | NAO | PRI | NULL | - |
| 2 | recebimento_id | char(36) | NAO | - | NULL | - |
| 3 | mensagem | text | NAO | - | NULL | - |
| 4 | data_hora | date | NAO | - | NULL | - |
| 5 | operador | varchar(255) | NAO | - | NULL | - |
| 6 | status | enum('AGUARDANDO','INICIADO','AUTORIZADO','CANCELADO','REJEITADO') | NAO | - | AGUARDANDO | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: recibo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(150) | NAO | - | NULL | - |
| 4 | cnpj | varchar(50) | SIM | - | NULL | - |
| 5 | valor | decimal(15,10) | NAO | - | NULL | - |
| 6 | servico_realizado | text | NAO | - | NULL | - |
| 7 | data_recibo | date | NAO | - | NULL | - |
| 8 | user_lancamento_id | int | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |
| 12 | parcela_pagamento_id | int unsigned | SIM | MUL | NULL | - |

### Tabela: registro_bloqueado (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | table_name | varchar(255) | NAO | - | NULL | - |
| 3 | field_where | varchar(255) | NAO | - | id | - |
| 4 | value_where | varchar(255) | NAO | - | NULL | - |
| 5 | bloqueado | tinyint | NAO | - | 1 | - |
| 6 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |

### Tabela: regra_fiscal (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 23

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | ncm_codigo | varchar(8) | NAO | MUL | NULL | - |
| 3 | origem_codigo | int | NAO | MUL | 0 | - |
| 4 | cst_codigo | varchar(3) | NAO | MUL | 01 | - |
| 5 | modalidade_base_codigo | int | NAO | MUL | NULL | - |
| 6 | percentual_icms | decimal(15,2) | NAO | - | 0.00 | - |
| 7 | percentual_reducao | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | percentual_diferimento | decimal(15,2) | NAO | - | 0.00 | - |
| 9 | desoneracao_icms_codigo | int | SIM | MUL | NULL | - |
| 10 | modalidade_base_st_codigo | int | NAO | MUL | NULL | - |
| 11 | percentual_icms_st | decimal(15,2) | NAO | - | 0.00 | - |
| 12 | aliquota_icms_st | decimal(15,2) | NAO | - | 0.00 | - |
| 13 | percentual_reducao_st | decimal(15,2) | NAO | - | 0.00 | - |
| 14 | ipi_cst_codigo | varchar(3) | NAO | MUL | NULL | - |
| 15 | ipi_aliquota | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | ipi_enquadramento | varchar(3) | SIM | - | 999 | - |
| 17 | pis_cst_codigo | int | NAO | MUL | NULL | - |
| 18 | pis_aliquota | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | cofins_cst_codigo | int | NAO | MUL | NULL | - |
| 20 | cofins_aliquota | decimal(15,2) | NAO | - | 0.00 | - |
| 21 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 22 | updated_at | timestamp | SIM | - | NULL | - |
| 23 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: relatorio_personalizado (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | parent | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: relatorio_personalizado_colunas (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | relatorio_personalizado_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | cabecalho_id | varchar(255) | NAO | - | NULL | - |
| 5 | ativar | tinyint | NAO | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: relatorio_personalizado_config (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | user_id | int unsigned | SIM | MUL | NULL | - |
| 3 | nome_relatorio | varchar(100) | NAO | - | NULL | - |
| 4 | filtros | text | SIM | - | NULL | - |
| 5 | colunas | text | SIM | - | NULL | - |
| 6 | ativar_notificacao | tinyint(1) | NAO | - | NULL | - |
| 7 | email | varchar(255) | SIM | - | NULL | - |
| 8 | telefone | varchar(11) | SIM | - | NULL | - |
| 9 | created_at | timestamp | SIM | - | NULL | - |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: relatorio_personalizado_filtros (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | relatorio_personalizado_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | label | varchar(255) | NAO | - | NULL | - |
| 4 | filtro_id | varchar(255) | NAO | - | NULL | - |
| 5 | valor | varchar(255) | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: relatorio_personalizado_notificacao_configuracao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | relatorio_personalizado_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | ativar_notificacao | tinyint | NAO | - | NULL | - |
| 4 | frequencia | enum('DIARIAMEMTE','3dias','5dias','MENSALMENTE') | NAO | - | NULL | - |
| 5 | horario | varchar(255) | NAO | - | NULL | - |
| 6 | destino_email | varchar(255) | NAO | - | NULL | - |
| 7 | destino_fone | varchar(255) | NAO | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: relatorio_ultimos_acessados (BASE TABLE)
**Linhas aprox:** 4 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | parent | varchar(255) | NAO | - | NULL | - |
| 3 | payload | text | NAO | - | NULL | - |
| 4 | usuario_id | int unsigned | SIM | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: responsavel_tecnico_configuracao (BASE TABLE)
**Linhas aprox:** 4 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | ambiente | varchar(255) | NAO | - | NULL | - |
| 3 | uf | varchar(255) | NAO | - | NULL | - |
| 4 | modelo | varchar(255) | NAO | - | NULL | - |
| 5 | cnpj | varchar(255) | NAO | - | NULL | - |
| 6 | contato | varchar(255) | NAO | - | NULL | - |
| 7 | email | varchar(255) | NAO | - | NULL | - |
| 8 | fone | varchar(255) | NAO | - | NULL | - |
| 9 | id_csrt | varchar(255) | SIM | - | NULL | - |
| 10 | csrt | varchar(255) | SIM | - | NULL | - |
| 11 | sync | timestamp | NAO | - | 0000-00-00 00:00:00 | - |

### Tabela: restaurante_ambiente (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | padrao | tinyint | NAO | - | 0 | - |
| 4 | empresa_id | int | NAO | MUL | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_configuracao_impressoras (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | ambiente_id | int | NAO | MUL | NULL | - |
| 4 | setor_id | int | NAO | MUL | NULL | - |
| 5 | impressora_id | int | NAO | MUL | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_familia (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | deleted_at | timestamp | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_grupo_observacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | grupo_id | int | NAO | MUL | NULL | - |
| 3 | restaurante_observacao_id | int | NAO | MUL | NULL | - |
| 4 | deleted_at | timestamp | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_impressora (BASE TABLE)
**Linhas aprox:** 9 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | caminho | varchar(255) | SIM | - | NULL | - |
| 4 | empresa_id | int | NAO | MUL | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_mesa (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 44

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | id_auxiliar | int | SIM | - | NULL | - |
| 4 | codigo_mesa | varchar(10) | NAO | - | NULL | - |
| 5 | mesa_fechada | tinyint | NAO | - | 0 | - |
| 6 | data_hora_abertura | datetime | SIM | - | NULL | - |
| 7 | cliente_id | int | NAO | MUL | NULL | - |
| 8 | cliente_nome | varchar(255) | SIM | - | NULL | - |
| 9 | numero_agrupamento | int | SIM | - | NULL | - |
| 10 | tele_entrega | tinyint | NAO | - | NULL | - |
| 11 | desconto | decimal(10,2) | NAO | - | 0.00 | - |
| 12 | atendente_id | int | NAO | MUL | NULL | - |
| 13 | atendente_nome | varchar(255) | SIM | - | NULL | - |
| 14 | dados_entrega | text | SIM | - | NULL | - |
| 15 | numero_comanda | text | SIM | - | NULL | - |
| 16 | data_hora_ultimo_item | datetime | SIM | - | NULL | - |
| 17 | lacrar | tinyint(1) | NAO | - | 0 | - |
| 18 | nao_cobrar_10_porcento | tinyint(1) | NAO | - | 0 | - |
| 19 | cpf_cliente | varchar(14) | SIM | - | NULL | - |
| 20 | indicador_id | int | SIM | MUL | NULL | - |
| 21 | indicador_nome | varchar(255) | SIM | - | NULL | - |
| 22 | ponto_referencia | text | SIM | - | NULL | - |
| 23 | delivery | int | SIM | - | NULL | - |
| 24 | entregador_id | int | SIM | MUL | NULL | - |
| 25 | pedido_pronto | int | SIM | - | NULL | - |
| 26 | cliente_vem_retirar | int | SIM | - | NULL | - |
| 27 | data_preparacao_pedido | date | SIM | - | NULL | - |
| 28 | impresso_conferencia | int | SIM | - | NULL | - |
| 29 | fechamento_tipo_pagamento | int | SIM | - | NULL | - |
| 30 | fechamento_valor_pago | decimal(10,2) | NAO | - | 0.00 | - |
| 31 | quantidade_comandas | int | SIM | - | NULL | - |
| 32 | quantidade_pessoas | int | SIM | - | NULL | - |
| 33 | solicitado_conferencia | tinyint(1) | NAO | - | 0 | - |
| 34 | solicitado_conferencia_atendente_id | int | SIM | MUL | NULL | - |
| 35 | excluido | tinyint(1) | NAO | - | 0 | - |
| 36 | desconto_valor_promocao | decimal(10,2) | NAO | - | 0.00 | - |
| 37 | numero_nfce | int | SIM | - | NULL | - |
| 38 | tipo_preco_venda | varchar(50) | SIM | - | NULL | - |
| 39 | catraca_bloqueada | tinyint(1) | NAO | - | 0 | - |
| 40 | pedido_origem | varchar(50) | SIM | - | NULL | - |
| 41 | pedido_confirmado | tinyint(1) | NAO | - | 0 | - |
| 42 | created_at | timestamp | SIM | - | NULL | - |
| 43 | updated_at | timestamp | SIM | - | NULL | - |
| 44 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_mesa_adiantamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 27

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | restaurante_mesa_id | bigint unsigned | NAO | MUL | NULL | - |
| 3 | descricao | varchar(50) | SIM | - | NULL | - |
| 4 | valor_pago | double | SIM | - | NULL | - |
| 5 | valor_digitado | double | SIM | - | NULL | - |
| 6 | numero_documento | varchar(50) | SIM | - | NULL | - |
| 7 | prazo | double | SIM | - | NULL | - |
| 8 | vencimento | date | SIM | - | NULL | - |
| 9 | nome_cartao | varchar(50) | SIM | - | NULL | - |
| 10 | numero_parcelas | varchar(50) | SIM | - | NULL | - |
| 11 | cache_enviado | tinyint(1) | NAO | - | 0 | - |
| 12 | chave_smobile | varchar(50) | SIM | - | NULL | - |
| 13 | tp_integra | double | SIM | - | NULL | - |
| 14 | rede | varchar(50) | SIM | - | NULL | - |
| 15 | cliente_nome | varchar(255) | SIM | - | NULL | - |
| 16 | cancelado | tinyint(1) | NAO | - | 0 | - |
| 17 | pdv_tef | tinyint(1) | NAO | - | 0 | - |
| 18 | pdv_pos | tinyint(1) | NAO | - | 0 | - |
| 19 | cache_id | varchar(100) | SIM | MUL | NULL | - |
| 20 | cartao_via_cliente | text | SIM | - | NULL | - |
| 21 | cartao_via_estabelecimento | text | SIM | - | NULL | - |
| 22 | impresso | tinyint(1) | NAO | - | 0 | - |
| 23 | tp_cred | varchar(255) | SIM | - | NULL | - |
| 24 | bandeira | varchar(255) | SIM | - | NULL | - |
| 25 | created_at | timestamp | SIM | - | NULL | - |
| 26 | updated_at | timestamp | SIM | - | NULL | - |
| 27 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_mesa_configuracao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 30

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | intervalo_comanda_inicial | int | NAO | - | 0 | - |
| 4 | intervalo_comanda_final | int | NAO | - | 0 | - |
| 5 | intervalo_mesa_inicial | int | NAO | - | 0 | - |
| 6 | intervalo_mesa_final | int | NAO | - | 0 | - |
| 7 | impressao_async | int | NAO | - | 0 | - |
| 8 | registro_delivery | int | NAO | - | 0 | - |
| 9 | utilizar_comanda | tinyint | NAO | - | 0 | - |
| 10 | utilizar_mesa | tinyint | NAO | - | 0 | - |
| 11 | utilizar_teclado_numerico | tinyint | NAO | - | 0 | - |
| 12 | impressao_por_usuario | tinyint | NAO | - | 0 | - |
| 13 | habilitar_cobranca_10_porcento | tinyint | NAO | - | 0 | - |
| 14 | bloquear_mesa_apos_conferencia | tinyint | NAO | - | 0 | - |
| 15 | versao_banco | int | NAO | - | 0 | - |
| 16 | bloquear_conta_parcial | tinyint | NAO | - | 0 | - |
| 17 | mesa_ociosa | varchar(255) | SIM | - | NULL | - |
| 18 | filtrar_mesa_garcom | tinyint | NAO | - | 0 | - |
| 19 | classificacao_listagem | varchar(255) | SIM | - | NULL | - |
| 20 | impressao_setores | varchar(255) | SIM | - | NULL | - |
| 21 | impressao_config | varchar(255) | SIM | - | NULL | - |
| 22 | exibir_servico_opcional | tinyint | NAO | - | 0 | - |
| 23 | solicitar_senha_transferencia_itens | tinyint | NAO | - | 0 | - |
| 24 | solicitar_senha_cancelar_delivery | tinyint | NAO | - | 0 | - |
| 25 | solicitar_senha_remover_taxa_servico | tinyint | NAO | - | 0 | - |
| 26 | solicitar_senha_juntar_mesa | tinyint | NAO | - | 0 | - |
| 27 | solicitar_senha_cancelar_item | tinyint | NAO | - | 0 | - |
| 28 | created_at | timestamp | SIM | - | NULL | - |
| 29 | updated_at | timestamp | SIM | - | NULL | - |
| 30 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_mesa_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 45

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | api_guid | varchar(100) | SIM | - | NULL | - |
| 3 | adicional_mesa_item_id | int | SIM | - | NULL | - |
| 4 | restaurante_mesa_id | bigint unsigned | NAO | MUL | NULL | - |
| 5 | produto_id | int | NAO | MUL | NULL | - |
| 6 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 7 | quantidade | decimal(10,2) | NAO | - | 0.00 | - |
| 8 | preco | decimal(10,2) | NAO | - | 0.00 | - |
| 9 | cancelado | tinyint(1) | NAO | - | 0 | - |
| 10 | numero_mesa_origem | int | SIM | - | NULL | - |
| 11 | descricao | varchar(255) | SIM | - | NULL | - |
| 12 | selecionado | tinyint(1) | NAO | - | 0 | - |
| 13 | remover | tinyint(1) | NAO | - | 0 | - |
| 14 | pronto | tinyint(1) | NAO | - | 0 | - |
| 15 | data_hora_registro | datetime | SIM | - | NULL | - |
| 16 | cozinha | tinyint(1) | NAO | - | 0 | - |
| 17 | observacao | text | SIM | - | NULL | - |
| 18 | atendente_item_id | int | SIM | MUL | NULL | - |
| 19 | atendente_item_nome | varchar(255) | SIM | - | NULL | - |
| 20 | acomp | text | SIM | - | NULL | - |
| 21 | nao_agrupar | tinyint(1) | NAO | - | 0 | - |
| 22 | quantidade_cancelada | decimal(10,2) | NAO | - | 0.00 | - |
| 23 | codigo_pesquisa | varchar(100) | SIM | - | NULL | - |
| 24 | bar | int | SIM | - | NULL | - |
| 25 | data_hora_pronto | datetime | SIM | - | NULL | - |
| 26 | data_hora_painel_chamada | datetime | SIM | - | NULL | - |
| 27 | impresso | tinyint(1) | NAO | - | 0 | - |
| 28 | comanda_item | int | SIM | - | NULL | - |
| 29 | couvert | tinyint(1) | NAO | - | 0 | - |
| 30 | cobrar_servico | tinyint(1) | NAO | - | 0 | - |
| 31 | delivery | tinyint(1) | NAO | - | 0 | - |
| 32 | cancelamento_usuario | varchar(255) | SIM | - | NULL | - |
| 33 | cancelamento_data_hora | datetime | SIM | - | NULL | - |
| 34 | cancelamento_motivo | text | SIM | - | NULL | - |
| 35 | mesa_origem_id | int | SIM | - | NULL | - |
| 36 | setor | varchar(255) | SIM | - | NULL | - |
| 37 | sem_desconto_convenio | tinyint(1) | NAO | - | 0 | - |
| 38 | restaurante_setor_id | int | SIM | MUL | NULL | - |
| 39 | cliente_item_nome | varchar(255) | SIM | - | NULL | - |
| 40 | lancamento_guid | varchar(100) | SIM | - | NULL | - |
| 41 | lancamento_origem | varchar(100) | SIM | - | NULL | - |
| 42 | lancamento_confirmado | tinyint(1) | NAO | - | 0 | - |
| 43 | created_at | timestamp | SIM | - | NULL | - |
| 44 | updated_at | timestamp | SIM | - | NULL | - |
| 45 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_mesa_item_acompanhamento (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | api_guid | varchar(100) | SIM | - | NULL | - |
| 3 | restaurante_mesa_item_id | bigint unsigned | NAO | MUL | NULL | - |
| 4 | numero_mesa | int | NAO | - | NULL | - |
| 5 | produto_id | int | NAO | MUL | NULL | - |
| 6 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 7 | quantidade | decimal(10,2) | NAO | - | 0.00 | - |
| 8 | descricao | varchar(255) | SIM | - | NULL | - |
| 9 | produto_combo_item_id | int | NAO | MUL | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_observacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | descricao | text | NAO | - | NULL | - |
| 3 | deleted_at | timestamp | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: restaurante_setor (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | SIM | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | impressora | varchar(255) | SIM | - | NULL | - |
| 5 | painel_cozinha | smallint | NAO | - | 0 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | kds_painel | varchar(255) | SIM | - | NULL | - |

### Tabela: role_user (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | role_id | int unsigned | NAO | MUL | NULL | - |
| 3 | user_id | int unsigned | NAO | MUL | NULL | - |
| 4 | empresa_id | int | NAO | MUL | NULL | - |
| 5 | favorita | tinyint(1) | NAO | - | 0 | - |

### Tabela: roles (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | role_title | varchar(255) | NAO | - | NULL | - |
| 3 | role_slug | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | profile | enum('CLIENTE','CONTADOR') | NAO | - | CLIENTE | - |

### Tabela: servico_issqn (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | - | 0 | - |
| 2 | codigo | varchar(5) | NAO | - | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: similar (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 4 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |
| 6 | aplicacao | text | NAO | - | NULL | - |

### Tabela: sku_atributo (BASE TABLE)
**Linhas aprox:** 19 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | parent_id | int | SIM | - | NULL | - |
| 3 | nome | varchar(50) | NAO | - | NULL | - |
| 4 | restrito | int | SIM | - | 0 | - |
| 5 | cor | varchar(7) | NAO | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | hub_code | varchar(50) | SIM | - | NULL | - |
| 10 | hub_name | varchar(50) | SIM | - | NULL | - |

### Tabela: softcomintro (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | intro | varchar(255) | NAO | - | NULL | - |
| 3 | user_id | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_configuracoes (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 42

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | geral_exibir_escolha_perfil | int | NAO | - | NULL | - |
| 4 | geral_gerar_c170_mod55 | int | NAO | - | NULL | - |
| 5 | geral_gerar_c170_mod65 | int | NAO | - | NULL | - |
| 6 | geral_perfil_de_escrituracao | enum('A','B','C') | NAO | - | NULL | - |
| 7 | geral_atividade_empresa | enum('0','1') | NAO | - | NULL | - |
| 8 | icms_permitir_apurar_credito | int | NAO | - | NULL | - |
| 9 | icms_permitir_apurar_debito | int | NAO | - | NULL | - |
| 10 | icms_nfe_propria_data_imposto | enum('DATA_EMISSAO','DATA_SAIDA') | NAO | - | NULL | - |
| 11 | icms_entradas_adicionar_st | enum('CAMPO_PROPRIO','OUTRAS_DESPESAS') | NAO | - | NULL | - |
| 12 | icms_codigo_receita_e116 | varchar(255) | NAO | - | NULL | - |
| 13 | ipi_entradas_adicionar_ipi | enum('CAMPO_PROPRIO','OUTRAS_DESPESAS') | NAO | - | NULL | - |
| 14 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 15 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |
| 17 | fiscal_1601_regime | int | NAO | - | 0 | - |
| 18 | geral_natureza_juridica | int | NAO | - | 2 | - |
| 19 | geral_situacao_especial | int | SIM | - | NULL | - |
| 20 | geral_atividade | int | NAO | - | 2 | - |
| 21 | geral_incidencia_tributaria | int | NAO | - | 2 | - |
| 22 | geral_apropriacao_creditos | int | NAO | - | 1 | - |
| 23 | geral_tipo_contribuicao_apurada | int | NAO | - | 1 | - |
| 24 | geral_criterio_escrituracao | int | NAO | - | 9 | - |
| 25 | geral_indicador_escrituracao | int | NAO | - | 2 | - |
| 26 | valores_gerar_bc_aliqzero | tinyint(1) | NAO | - | 0 | - |
| 27 | valores_personalizar_bc_compras | tinyint(1) | NAO | - | 0 | - |
| 28 | valores_bc_en_desconto | tinyint(1) | NAO | - | 0 | - |
| 29 | valores_bc_en_icmscte | tinyint(1) | NAO | - | 0 | - |
| 30 | valores_bc_en_seguro | tinyint(1) | NAO | - | 0 | - |
| 31 | valores_bc_en_frete | tinyint(1) | NAO | - | 0 | - |
| 32 | valores_bc_en_icmsst | tinyint(1) | NAO | - | 0 | - |
| 33 | valores_bc_en_ipi | tinyint(1) | NAO | - | 0 | - |
| 34 | valores_bc_en_outrasdespesas | tinyint(1) | NAO | - | 0 | - |
| 35 | valores_personalizar_base_vendas | tinyint(1) | NAO | - | 0 | - |
| 36 | valores_bc_sd_desconto | tinyint(1) | NAO | - | 0 | - |
| 37 | valores_bc_sd_icms | tinyint(1) | NAO | - | 0 | - |
| 38 | valores_bc_sd_seguro | tinyint(1) | NAO | - | 0 | - |
| 39 | valores_bc_sd_frete | tinyint(1) | NAO | - | 0 | - |
| 40 | valores_bc_sd_icmsst | tinyint(1) | NAO | - | 0 | - |
| 41 | valores_bc_sd_ipi | tinyint(1) | NAO | - | 0 | - |
| 42 | valores_bc_sd_outrasdespesas | tinyint(1) | NAO | - | 0 | - |

### Tabela: sped_download (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | access_key | varchar(255) | NAO | - | NULL | - |
| 4 | data_inicio | date | NAO | - | NULL | - |
| 5 | data_fim | date | NAO | - | NULL | - |
| 6 | data_sync | timestamp | NAO | - | 2019-02-14 21:07:40 | - |
| 7 | download | smallint | NAO | - | NULL | - |

### Tabela: sped_e111_ajuste_apuracao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | data_referencia | date | NAO | - | NULL | - |
| 4 | tipo_ajuste | enum('D','C','SC') | NAO | - | NULL | - |
| 5 | codigo_ajuste | varchar(255) | SIM | - | NULL | - |
| 6 | descricao_ajuste | varchar(255) | SIM | - | NULL | - |
| 7 | valor_ajuste | decimal(15,2) | NAO | - | NULL | - |
| 8 | mes_referencia | enum('1','2','3','4','5','6','7','8','9','10','11','12') | NAO | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_e113_ajuste_apuracao_documentos (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 13

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | e111_ajuste_id | int | NAO | MUL | NULL | - |
| 3 | fornecedor_id | int | NAO | MUL | NULL | - |
| 4 | modelo_documento | varchar(255) | NAO | - | NULL | - |
| 5 | serie_documento | varchar(255) | NAO | - | NULL | - |
| 6 | numero_documento | int | NAO | - | NULL | - |
| 7 | data_documento | date | NAO | - | NULL | - |
| 8 | codigo_item | int | NAO | - | NULL | - |
| 9 | valor_ajuste | decimal(15,2) | NAO | - | NULL | - |
| 10 | chave_acesso | varchar(255) | NAO | - | NULL | - |
| 11 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 12 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 13 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_e115_valores_declaratorios (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | data_referencia | date | NAO | - | NULL | - |
| 4 | codigo_ajuste | varchar(255) | NAO | - | NULL | - |
| 5 | descricao_ajuste | varchar(255) | SIM | - | NULL | - |
| 6 | valor_ajuste | decimal(15,2) | NAO | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_inventario_base (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | NAO | MUL | NULL | - |
| 3 | produto_empresa_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | nome | varchar(255) | NAO | - | NULL | - |
| 6 | data | date | NAO | - | NULL | - |
| 7 | quantidade | decimal(15,2) | NAO | - | 0.00 | - |
| 8 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |

### Tabela: sped_ipi_ajuste_apuracao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | data_referencia | date | NAO | - | NULL | - |
| 4 | tipo_ajuste | enum('D','C','SC') | NAO | - | NULL | - |
| 5 | codigo_ajuste | varchar(255) | NAO | - | NULL | - |
| 6 | descricao_ajuste | varchar(255) | SIM | - | NULL | - |
| 7 | valor_ajuste | decimal(15,2) | NAO | - | NULL | - |
| 8 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_plano_contas (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | data_inclusao | datetime | NAO | - | NULL | - |
| 3 | codigo | varchar(50) | SIM | - | NULL | - |
| 4 | descricao | varchar(50) | SIM | - | NULL | - |
| 5 | tipo | char(1) | SIM | - | NULL | - |
| 6 | natureza | varchar(2) | SIM | - | NULL | - |
| 7 | nivel | int | NAO | - | 0 | - |
| 8 | codigo_referencial | varchar(50) | SIM | - | NULL | - |
| 9 | empresa_id | int | NAO | MUL | NULL | - |
| 10 | created_at | timestamp | SIM | - | NULL | - |
| 11 | updated_at | timestamp | SIM | - | NULL | - |
| 12 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_plano_contas_cfop (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | sped_plano_conta_id | int unsigned | NAO | MUL | NULL | - |
| 4 | cfop | varchar(255) | NAO | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_tabela_4_5_4 (BASE TABLE)
**Linhas aprox:** 9 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(255) | NAO | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | cd | varchar(255) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_tabela_5_1_1 (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | - | 0 | - |
| 2 | codigo | varchar(255) | NAO | - | NULL | - |
| 3 | descricao | longtext | NAO | - | NULL | - |
| 4 | cd | varchar(255) | NAO | - | NULL | - |
| 5 | tipo_icms | varchar(255) | NAO | - | NULL | - |
| 6 | uf | varchar(255) | NAO | - | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_tabela_5_2 (BASE TABLE)
**Linhas aprox:** 20 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(255) | NAO | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: sped_tabela_e115_codigo_apuracao (BASE TABLE)
**Linhas aprox:** 1197 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(255) | NAO | - | NULL | - |
| 3 | descricao | varchar(255) | NAO | - | NULL | - |
| 4 | uf | varchar(255) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_categoria (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | grupo_id | varchar(50) | SIM | - | NULL | - |
| 4 | category_code | varchar(255) | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_config (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | ultima_sincronizacao_cadastro | timestamp | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_produto (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | produto_id | int | SIM | - | NULL | - |
| 3 | product_code | varchar(255) | SIM | - | NULL | - |
| 4 | deleted_at | timestamp | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | empresa_id | int | NAO | - | NULL | - |

### Tabela: ta_no_menu_promocao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | promocao_id | int | NAO | - | NULL | - |
| 3 | promotion_code | varchar(255) | SIM | - | NULL | - |
| 4 | deleted_at | timestamp | SIM | - | NULL | - |
| 5 | created_at | timestamp | SIM | - | NULL | - |
| 6 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_promocao_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | promocao_id | int | NAO | - | NULL | - |
| 3 | produto_empresa_grade_id | int | SIM | - | NULL | - |
| 4 | promotion_item_code | varchar(255) | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_variation (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | produto_combo_id | int | NAO | - | NULL | - |
| 4 | variation_code | varchar(255) | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_variation_additional (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | grupo_id | int | NAO | - | NULL | - |
| 4 | produto_id | int | SIM | - | NULL | - |
| 5 | variation_code | varchar(255) | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_variation_additional_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | grupo_adicional_id | int | NAO | - | NULL | - |
| 4 | produto_id | int | SIM | - | NULL | - |
| 5 | produto_adicional_id | int | SIM | - | NULL | - |
| 6 | variation_item_code | varchar(255) | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: ta_no_menu_variation_item (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | produto_combo_id | int | NAO | - | NULL | - |
| 4 | produto_id | int | SIM | - | NULL | - |
| 5 | variation_item_code | varchar(255) | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: tabela_preco (BASE TABLE)
**Linhas aprox:** 4 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 4 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tabela_preco_produto (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | tabela_preco_id | int unsigned | NAO | MUL | NULL | - |
| 3 | produto_empresa_id | int | SIM | MUL | NULL | - |
| 4 | preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 5 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tag_classificacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: telescope_entries (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | sequence | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | uuid | char(36) | NAO | UNI | NULL | - |
| 3 | batch_id | char(36) | NAO | MUL | NULL | - |
| 4 | family_hash | varchar(255) | SIM | MUL | NULL | - |
| 5 | should_display_on_index | tinyint(1) | NAO | - | 1 | - |
| 6 | type | varchar(20) | NAO | MUL | NULL | - |
| 7 | content | longtext | NAO | - | NULL | - |
| 8 | created_at | datetime | SIM | MUL | NULL | - |

### Tabela: telescope_entries_tags (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 2

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | entry_uuid | char(36) | NAO | MUL | NULL | - |
| 2 | tag | varchar(255) | NAO | MUL | NULL | - |

### Tabela: telescope_monitoring (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 1

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | tag | varchar(255) | NAO | - | NULL | - |

### Tabela: tipo_ajuste (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | permitir_excluir | tinyint | NAO | - | 1 | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_area (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_cliente (BASE TABLE)
**Linhas aprox:** 2 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | UNI | NULL | - |
| 3 | permitir_excluir | tinyint | NAO | - | 1 | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_convenio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_debito (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | SIM | - | NULL | - |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_documento (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | deleted_at | timestamp | SIM | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | permitir_excluir | smallint | NAO | - | 1 | - |

### Tabela: tipo_energia_grupotensao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(2) | NAO | MUL | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_energia_ligacao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(50) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_fator (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_frete (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | int | NAO | MUL | NULL | - |
| 3 | nome | varchar(50) | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_funcao (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | permitir_excluir | tinyint | NAO | - | 1 | - |
| 4 | atendente | tinyint | NAO | - | 0 | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_justificativa (BASE TABLE)
**Linhas aprox:** 6 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | descricao | varchar(255) | NAO | - | NULL | - |
| 3 | rotina | text | SIM | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_modelo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 7

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | codigo | varchar(3) | NAO | UNI | NULL | - |
| 3 | nome | varchar(255) | NAO | - | NULL | - |
| 4 | operacao | varchar(50) | NAO | - | NULL | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_ncm (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | codigo | varchar(8) | NAO | - | NULL | - |
| 3 | nome | varchar(255) | SIM | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_setor (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_similar (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | - |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tipo_unidade_medida (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(255) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 4 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: transferencia_bancaria (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 11

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | data_operacao | date | NAO | - | NULL | - |
| 4 | banco_origem_id | int | NAO | - | NULL | - |
| 5 | banco_destino_id | int | NAO | - | NULL | - |
| 6 | forma_pagamento_id | int | NAO | - | NULL | - |
| 7 | historico | varchar(250) | NAO | - | NULL | - |
| 8 | valor | decimal(15,2) | NAO | - | NULL | - |
| 9 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 10 | updated_at | timestamp | SIM | - | NULL | - |
| 11 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: transportador (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | pessoa | enum('FISICA','JURIDICA') | NAO | - | JURIDICA | - |
| 4 | cpf_cnpj | varchar(18) | SIM | - | NULL | - |
| 5 | inscricao_estadual | varchar(20) | SIM | - | NULL | - |
| 6 | rg | varchar(20) | SIM | - | NULL | - |
| 7 | nome | varchar(255) | NAO | - | NULL | - |
| 8 | razao_social | varchar(255) | NAO | - | NULL | - |
| 9 | observacao | text | SIM | - | NULL | - |
| 10 | veiculo_placa | varchar(8) | SIM | - | NULL | - |
| 11 | veiculo_uf | enum('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | SIM | - | NULL | - |
| 12 | rntrc | varchar(8) | SIM | - | NULL | - |
| 13 | tipo_transportador | enum('ETC','TAC Próprio','TAC Agregado') | SIM | - | NULL | - |
| 14 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 15 | updated_at | timestamp | SIM | - | NULL | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: tributos_por_uf (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | uf_destino | varchar(10) | NAO | - | NULL | - |
| 3 | ncm | varchar(20) | SIM | - | NULL | - |
| 4 | ncm_descricao | varchar(255) | SIM | - | NULL | - |
| 5 | fcp_aliquota | decimal(15,2) | NAO | - | 0.00 | - |
| 6 | fcp_st_aliquota | decimal(15,2) | NAO | - | 0.00 | - |
| 7 | empresa_id | int | NAO | MUL | NULL | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: troca (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | devolucao_id | int | SIM | MUL | NULL | - |
| 3 | nfe_devolucao_id | int unsigned | SIM | MUL | NULL | - |
| 4 | venda_id | int | SIM | MUL | NULL | - |
| 5 | movimentacao_id | int | NAO | - | NULL | - |
| 6 | user_id | int unsigned | NAO | MUL | NULL | - |
| 7 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |
| 10 | api_guid_nova_venda | char(36) | SIM | - | NULL | - |
| 11 | venda_origem_funcionario_id | int | SIM | MUL | NULL | - |
| 12 | cliente_id | int | SIM | MUL | NULL | - |
| 13 | caixa_turno | tinyint unsigned | SIM | MUL | NULL | - |
| 14 | caixa_operador_id | int unsigned | SIM | MUL | NULL | - |

### Tabela: users (BASE TABLE)
**Linhas aprox:** 3 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | name | varchar(255) | NAO | - | NULL | - |
| 3 | email | varchar(255) | NAO | - | NULL | - |
| 4 | password | varchar(60) | NAO | - | NULL | - |
| 5 | remember_token | varchar(100) | SIM | - | NULL | - |
| 6 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 7 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |
| 9 | default | tinyint(1) | NAO | - | 0 | - |

### Tabela: veiculo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 22

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | placa | varchar(8) | NAO | - | NULL | - |
| 3 | renavam | varchar(11) | SIM | - | NULL | - |
| 4 | tara | varchar(6) | NAO | - | NULL | - |
| 5 | capacidade_kg | varchar(6) | SIM | - | NULL | - |
| 6 | capacidade_m | varchar(3) | SIM | - | NULL | - |
| 7 | prorietario_tipo_pessoa | enum('F','J') | SIM | - | NULL | - |
| 8 | proprietario_cpf_cnpj | varchar(14) | SIM | - | NULL | - |
| 9 | proprietario_rntrc | varchar(8) | SIM | - | NULL | - |
| 10 | proprietario_nome | varchar(60) | SIM | - | NULL | - |
| 11 | proprietario_inscricao_estadual | varchar(14) | SIM | - | NULL | - |
| 12 | proprietario_uf | varchar(2) | SIM | - | NULL | - |
| 13 | proprietario_tipo | varchar(2) | SIM | - | NULL | - |
| 14 | tipo_rodado | varchar(2) | NAO | - | NULL | - |
| 15 | tipo_carroceria | varchar(2) | NAO | - | NULL | - |
| 16 | uf_licenciado | varchar(2) | NAO | - | NULL | - |
| 17 | reboque | int | NAO | - | 0 | - |
| 18 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 19 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 20 | deleted_at | timestamp | SIM | - | NULL | - |
| 21 | codigo_veiculo | varchar(10) | SIM | - | NULL | - |
| 22 | codigo_agendamento_portuario | varchar(16) | SIM | - | NULL | - |

### Tabela: veiculo_marca (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: veiculo_modelo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | nome | varchar(50) | NAO | - | NULL | - |
| 3 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 4 | updated_at | timestamp | SIM | - | NULL | - |
| 5 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda (BASE TABLE)
**Linhas aprox:** 95 | **Colunas:** 65

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | empresa_id | int | NAO | MUL | NULL | - |
| 3 | cliente_id | int | NAO | MUL | 1 | - |
| 4 | funcionario_id | int | NAO | MUL | 1 | - |
| 5 | nfe_id | int unsigned | SIM | MUL | NULL | - |
| 6 | nfse_id | int | SIM | MUL | NULL | - |
| 7 | observacao | text | SIM | - | NULL | - |
| 8 | api_cliente_cpf | varchar(255) | SIM | - | NULL | - |
| 9 | api_cliente_nome | varchar(50) | SIM | - | NULL | - |
| 10 | api_faturar | varchar(255) | SIM | - | NULL | - |
| 11 | api_status | varchar(255) | SIM | - | NULL | - |
| 12 | api_app_name | varchar(50) | SIM | - | NULL | - |
| 13 | api_data_hora_venda | timestamp | SIM | - | NULL | - |
| 14 | desconto_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 15 | desconto_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | acrescimo_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 17 | acrescimo_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | percentual_comissao_venda | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 20 | updated_at | timestamp | SIM | - | NULL | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |
| 22 | api_guid | varchar(50) | NAO | MUL | NULL | - |
| 23 | api_device_id | varchar(100) | NAO | - | NULL | - |
| 24 | cancelada | tinyint(1) | NAO | - | 0 | - |
| 25 | usuario_lancamento_id | int unsigned | SIM | MUL | NULL | - |
| 26 | bloqueada | smallint | NAO | - | 0 | - |
| 27 | parent_guid | varchar(50) | SIM | - | NULL | - |
| 28 | usuario_cancelamento_id | int unsigned | SIM | MUL | NULL | - |
| 29 | data_hora_cancelamento | datetime | SIM | - | NULL | - |
| 30 | numero_documento | varchar(255) | SIM | - | NULL | - |
| 31 | numero_caixa | varchar(20) | SIM | - | NULL | - |
| 32 | tipo_preco_id | int unsigned | SIM | MUL | NULL | - |
| 33 | integracao_delivery | varchar(50) | SIM | - | NULL | - |
| 34 | entregador_id | int | SIM | MUL | NULL | - |
| 35 | tipo_entrega | varchar(20) | NAO | - | RETIRADA | - |
| 36 | observacao_retirada | text | SIM | - | NULL | - |
| 37 | previsao_entrega | date | SIM | - | NULL | - |
| 38 | cliente_endereco_id | int | SIM | MUL | NULL | - |
| 39 | pedido_entregador_id | int | SIM | MUL | NULL | - |
| 40 | assistencia_id | int unsigned | SIM | MUL | NULL | - |
| 41 | caixa_funcoes_id | int | SIM | MUL | NULL | - |
| 42 | caixa_turno | tinyint unsigned | SIM | MUL | NULL | - |
| 43 | caixa_data | date | SIM | MUL | NULL | - |
| 44 | indicador_id | int | SIM | MUL | NULL | - |
| 45 | marketplace_pedido_id | int | SIM | MUL | NULL | - |
| 46 | atendente_mesa | varchar(255) | SIM | - | NULL | - |
| 47 | comissao_entregador | decimal(15,2) | SIM | - | NULL | - |
| 48 | comissao_indicador | decimal(15,2) | SIM | - | NULL | - |
| 49 | numero_mesa | varchar(255) | SIM | - | NULL | - |
| 50 | numero_comanda | varchar(255) | SIM | - | NULL | - |
| 51 | origem_venda | varchar(255) | SIM | - | NULL | - |
| 52 | quantidade_pessoas | int | SIM | - | NULL | - |
| 53 | quantidade_comandas | int | SIM | - | NULL | - |
| 54 | tipo_lancamento | varchar(50) | NAO | - | VENDA | - |
| 55 | orcamento_id | int | SIM | MUL | NULL | - |
| 56 | orcamento_competencia | date | SIM | - | NULL | - |
| 57 | numero_pre_venda | varchar(50) | SIM | - | NULL | - |
| 58 | api_data_hora_lancamento | timestamp | SIM | - | NULL | - |
| 59 | valor_total | decimal(15,2) | NAO | - | 0.00 | - |
| 60 | total_pagamento | decimal(15,2) | NAO | - | 0.00 | - |
| 61 | total_desconto | decimal(15,2) | NAO | - | 0.00 | - |
| 62 | total_acrescimo | decimal(15,2) | NAO | - | 0.00 | - |
| 63 | status | varchar(20) | NAO | - | ABERTA | - |
| 64 | data_hora_venda | datetime | SIM | - | NULL | - |
| 65 | fator_acrescimo_id | bigint unsigned | SIM | MUL | NULL | - |

### Tabela: venda_acoes (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | impresso | tinyint | NAO | - | 0 | - |
| 4 | nota_fiscal | tinyint | NAO | - | 0 | - |
| 5 | boleto | tinyint | NAO | - | 0 | - |
| 6 | pix | tinyint | NAO | - | 0 | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_bloqueio (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 9

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | funcionario_id | int | SIM | MUL | NULL | - |
| 4 | observacao | text | SIM | - | NULL | - |
| 5 | motivo_bloqueio | enum('CREDITO_INSUFICIENTE','CLIENTE_INADIMPLENTE','CONDICAO_PAGAMENTO_NAO_AUTORIZADA','DIVERGENCIA_ESTOQUE','REVISAO_FISCAL','SOLICITACAO_GERENCIA','OUTRO') | NAO | - | OUTRO | - |
| 6 | bloqueio | enum('SEM_BLOQUEIO','BLOQUEADO','LIBERADO') | NAO | - | SEM_BLOQUEIO | - |
| 7 | created_at | timestamp | SIM | - | NULL | - |
| 8 | updated_at | timestamp | SIM | - | NULL | - |
| 9 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_cartao (BASE TABLE)
**Linhas aprox:** 89 | **Colunas:** 43

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | valor_recebido | decimal(15,2) | NAO | - | 0.00 | - |
| 3 | tipo_integracao_cartao | varchar(255) | SIM | - | NULL | - |
| 4 | nome_credenciadora_cartao | varchar(255) | SIM | - | NULL | - |
| 5 | cnpj_credenciadora_cartao | varchar(255) | SIM | - | NULL | - |
| 6 | tipo_bandeira_cartao | varchar(255) | SIM | - | NULL | - |
| 7 | codigo_autorizacao_cartao | varchar(255) | SIM | - | NULL | - |
| 8 | recibo_aid | varchar(255) | SIM | - | NULL | - |
| 9 | recibo_arqc | varchar(255) | SIM | - | NULL | - |
| 10 | recibo_autorizacao | varchar(255) | SIM | - | NULL | - |
| 11 | recibo_cnpj | varchar(255) | SIM | - | NULL | - |
| 12 | recibo_nome_loja | varchar(255) | SIM | - | NULL | - |
| 13 | recibo_cv | varchar(255) | SIM | - | NULL | - |
| 14 | recibo_nsu | varchar(255) | SIM | - | NULL | - |
| 15 | recibo_nome_cliente | varchar(255) | SIM | - | NULL | - |
| 16 | recibo_numero_terminal | varchar(255) | SIM | - | NULL | - |
| 17 | recibo_nome_emissor | varchar(255) | SIM | - | NULL | - |
| 18 | recibo_tipo_operacao | varchar(255) | SIM | - | NULL | - |
| 19 | recibo_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 20 | recibo_valor_parcela | decimal(15,2) | NAO | - | 0.00 | - |
| 21 | recibo_parcelas | int | NAO | - | 1 | - |
| 22 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 23 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |
| 25 | mfe_codigo_nsu_adquirente | varchar(255) | SIM | - | NULL | - |
| 26 | mfe_codigo_autorizacao_adquirente | varchar(255) | SIM | - | NULL | - |
| 27 | mfe_instituicao_financeira | varchar(255) | SIM | - | NULL | - |
| 28 | mfe_bandeira_cartao | varchar(255) | SIM | - | NULL | - |
| 29 | mfe_codigo_nsu_sefaz | varchar(255) | SIM | - | NULL | - |
| 30 | mfe_autorizacao_online | tinyint | SIM | - | NULL | - |
| 31 | mfe_pos_id | int | SIM | MUL | NULL | - |
| 32 | mfe_id_fechamento | varchar(255) | SIM | - | NULL | - |
| 33 | caixa_funcoes_id | int | SIM | MUL | NULL | - |
| 34 | conciliacao_maquina_id | varchar(255) | SIM | - | NULL | - |
| 35 | conciliacao_id | varchar(255) | SIM | - | NULL | - |
| 36 | conciliacao_status | varchar(255) | SIM | - | NULL | - |
| 37 | conciliacao_confirmacao | smallint | NAO | - | 0 | - |
| 38 | conciliacao_nsu | varchar(255) | SIM | - | NULL | - |
| 39 | conciliacao_data | timestamp | SIM | - | NULL | - |
| 40 | geracao_automatica | smallint | NAO | - | 0 | - |
| 41 | conciliacao_bandeira | varchar(255) | SIM | - | NULL | - |
| 42 | conciliacao_bandeira_codigo | varchar(255) | SIM | - | NULL | - |
| 43 | conciliacao_modalidade | varchar(255) | SIM | - | NULL | - |

### Tabela: venda_endereco_entrega (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 12

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | cep | varchar(9) | SIM | - | NULL | - |
| 4 | endereco | varchar(255) | SIM | - | NULL | - |
| 5 | numero | varchar(10) | SIM | - | NULL | - |
| 6 | complemento | varchar(255) | SIM | - | NULL | - |
| 7 | bairro | varchar(255) | SIM | - | NULL | - |
| 8 | cidade | varchar(255) | SIM | - | NULL | - |
| 9 | uf | varchar(2) | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |
| 11 | created_at | timestamp | SIM | - | NULL | - |
| 12 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_item (BASE TABLE)
**Linhas aprox:** 192 | **Colunas:** 39

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | produto_id | int | NAO | MUL | NULL | - |
| 4 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 5 | descricao_item | varchar(255) | SIM | - | NULL | - |
| 6 | preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 7 | quantidade | decimal(15,4) | NAO | - | 1.0000 | - |
| 8 | preco_compra | decimal(15,4) | NAO | - | 0.0000 | - |
| 9 | desconto_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 10 | acrescimo_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 11 | comissao | decimal(15,2) | SIM | - | 0.00 | - |
| 12 | vinculo_nfe | enum('AGUARDANDO','POSSUI','NAO_POSSUI') | NAO | - | AGUARDANDO | - |
| 13 | desabilita_rateio | tinyint(1) | NAO | - | 0 | - |
| 14 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 15 | updated_at | timestamp | SIM | - | NULL | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |
| 17 | codigo_beneficio_fiscal | varchar(255) | SIM | - | NULL | - |
| 18 | percentual_desconto | decimal(15,10) | SIM | - | NULL | - |
| 19 | percentual_acrescimo | decimal(15,10) | SIM | - | NULL | - |
| 20 | tipo_promocao | varchar(255) | SIM | - | NULL | - |
| 21 | descricao_promocao | varchar(255) | SIM | - | NULL | - |
| 22 | quantidade_promocao | decimal(15,4) | NAO | - | 0.0000 | - |
| 23 | quantidade_bonificada_promocao | decimal(15,4) | NAO | - | 0.0000 | - |
| 24 | valor_unidade_promocao | decimal(15,4) | NAO | - | 0.0000 | - |
| 25 | promocao_aplicada | smallint | NAO | - | 0 | - |
| 26 | preco_original | decimal(15,4) | NAO | - | 0.0000 | - |
| 27 | existe_tabela_preco | smallint | NAO | - | 0 | - |
| 28 | tabela_preco_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 29 | peso | decimal(15,4) | SIM | - | NULL | - |
| 30 | atendente_item | int | SIM | - | NULL | - |
| 31 | comissao_atendente | decimal(15,2) | SIM | - | NULL | - |
| 32 | cobrar_taxa_servico | tinyint | SIM | - | NULL | - |
| 33 | guid | varchar(50) | SIM | - | NULL | - |
| 34 | parent_guid | varchar(50) | SIM | - | NULL | - |
| 35 | tipo_faturamento | smallint | NAO | - | 0 | - |
| 36 | valor_desconto_promocao | decimal(15,2) | NAO | - | 0.00 | - |
| 37 | comissao_atendente_lancamento | decimal(15,2) | SIM | - | NULL | - |
| 38 | comissao_carta_produto | decimal(15,4) | SIM | - | NULL | - |
| 39 | comissao_carta_produto_tipo | enum('VALOR','PERCENTUAL') | SIM | - | PERCENTUAL | - |

### Tabela: venda_item_animal (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | venda_item_id | int | NAO | MUL | NULL | - |
| 3 | animal_id | int | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_item_composicao (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | venda_item_id | int | SIM | MUL | NULL | - |
| 4 | venda_item_produto_id | int | NAO | MUL | NULL | - |
| 5 | produto_id | int | NAO | MUL | NULL | - |
| 6 | produto_empresa_grade_id | int | NAO | MUL | NULL | - |
| 7 | quantidade | decimal(15,4) | SIM | - | 0.0000 | - |
| 8 | created_at | timestamp | SIM | - | NULL | - |
| 9 | updated_at | timestamp | SIM | - | NULL | - |
| 10 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_nfce (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 16

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | nfce_nro | int | NAO | - | 0 | - |
| 4 | nfce_protocolo | varchar(50) | SIM | - | NULL | - |
| 5 | nfce_serie | varchar(3) | SIM | - | NULL | - |
| 6 | nfce_chave | varchar(44) | SIM | - | NULL | - |
| 7 | nfce_data | varchar(50) | SIM | - | NULL | - |
| 8 | nfce_digestvalue | varchar(255) | SIM | - | NULL | - |
| 9 | nfce_cstat | varchar(10) | SIM | - | NULL | - |
| 10 | nfce_tipoemissao | varchar(50) | SIM | - | NULL | - |
| 11 | nfce_msgerro | varchar(255) | SIM | - | NULL | - |
| 12 | nfce_datahora_contingencia | datetime | SIM | - | NULL | - |
| 13 | nfce_motivo_contingencia | varchar(255) | SIM | - | NULL | - |
| 14 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 15 | updated_at | timestamp | SIM | - | NULL | - |
| 16 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_nota_referenciada (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | nota_fiscal_eletronica_id | int unsigned | NAO | MUL | NULL | - |
| 4 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 5 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_ordem_servico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 24

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | status | enum('EM_ANDAMENTO','CONCLUIDO','AGUARDANDO_RETIRADA','CANCELADO') | SIM | - | NULL | - |
| 4 | nome_solicitante | varchar(255) | SIM | - | NULL | - |
| 5 | tecnico_responsavel | varchar(255) | SIM | - | NULL | - |
| 6 | data_previsao_entrega | datetime | SIM | - | NULL | - |
| 7 | atendimento_externo | tinyint | SIM | - | NULL | - |
| 8 | data_atendimento | date | SIM | - | NULL | - |
| 9 | hora_marcada | varchar(10) | SIM | - | NULL | - |
| 10 | hora_inicio | varchar(10) | SIM | - | NULL | - |
| 11 | hora_fim | varchar(10) | SIM | - | NULL | - |
| 12 | equipamento_id | int unsigned | SIM | MUL | NULL | - |
| 13 | marca_equipamento_id | int unsigned | SIM | MUL | NULL | - |
| 14 | equipamento_modelo | varchar(50) | SIM | - | NULL | - |
| 15 | equipamento_numero_serie | varchar(50) | SIM | - | NULL | - |
| 16 | equipamento_defeito | text | SIM | - | NULL | - |
| 17 | equipamento_acessorios | text | SIM | - | NULL | - |
| 18 | laudo_tecnico | text | SIM | - | NULL | - |
| 19 | servico_realizado | text | SIM | - | NULL | - |
| 20 | observacoes_internas | text | SIM | - | NULL | - |
| 21 | data_hora_finalizacao | datetime | SIM | - | NULL | - |
| 22 | created_at | timestamp | SIM | - | NULL | - |
| 23 | updated_at | timestamp | SIM | - | NULL | - |
| 24 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_ordem_servico_contato (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | ordem_servico_id | int unsigned | SIM | MUL | NULL | - |
| 3 | nome | varchar(255) | SIM | - | NULL | - |
| 4 | email | varchar(255) | SIM | - | NULL | - |
| 5 | telefone | varchar(20) | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_status_historico (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | venda_id | int | NAO | MUL | NULL | - |
| 3 | status | varchar(255) | NAO | - | NULL | - |
| 4 | observacao | text | SIM | - | NULL | - |
| 5 | funcionario_id | int | SIM | MUL | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: venda_veiculo (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 14

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | venda_id | int | NAO | PRI | NULL | - |
| 2 | veiculo_id | int | SIM | MUL | NULL | - |
| 3 | placa | varchar(8) | SIM | - | NULL | - |
| 4 | marca | varchar(50) | SIM | - | NULL | - |
| 5 | modelo | varchar(50) | SIM | - | NULL | - |
| 6 | cor | varchar(50) | SIM | - | NULL | - |
| 7 | combustivel | varchar(50) | SIM | - | NULL | - |
| 8 | ano_fabricacao | varchar(4) | SIM | - | NULL | - |
| 9 | renavam | varchar(50) | SIM | - | NULL | - |
| 10 | chassi | varchar(50) | SIM | - | NULL | - |
| 11 | km | int | SIM | - | NULL | - |
| 12 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 13 | updated_at | timestamp | SIM | - | NULL | - |
| 14 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: vendas-laravel_create_financeiro_parcela_dados_cartao_table (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 4

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 3 | updated_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 4 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: view_memoria_financeiro_agrupada (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 92

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | financeiro_id | int | NAO | - | 0 | - |
| 2 | financeiro_empresa_id | int | NAO | - | NULL | - |
| 3 | financeiro_data_lancamento | date | NAO | - | NULL | - |
| 4 | financeiro_documento | varchar(20) | SIM | - | NULL | - |
| 5 | financeiro_historico | varchar(255) | NAO | - | NULL | - |
| 6 | financeiro_fornecedor_id | int | SIM | - | NULL | - |
| 7 | financeiro_cliente_id | int | SIM | - | NULL | - |
| 8 | financeiro_contrato_servico_id | int | SIM | - | NULL | - |
| 9 | financeiro_created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 10 | financeiro_updated_at | timestamp | SIM | - | NULL | - |
| 11 | financeiro_deleted_at | timestamp | SIM | - | NULL | - |
| 12 | financeiro_valor | decimal(15,4) | NAO | - | NULL | - |
| 13 | financeiro_tipo_documento_id | int unsigned | SIM | - | NULL | - |
| 14 | financeiro_origem | varchar(50) | SIM | - | NULL | - |
| 15 | financeiro_device_id | varchar(255) | SIM | - | NULL | - |
| 16 | financeiro_usuario_lancamento_id | int unsigned | SIM | - | NULL | - |
| 17 | financeiro_api_device_id | varchar(255) | SIM | - | NULL | - |
| 18 | financeiro_repeticao | enum('FIXA','PARCELADA') | NAO | - | NULL | - |
| 19 | financeiro_repeticao_tipo | enum('Mensal','Bimestral','Trimestral','Semestral','Anual','Intervalo') | NAO | - | NULL | - |
| 20 | financeiro_repeticao_quantidade | int | NAO | - | NULL | - |
| 21 | financeiro_repeticao_intervalo | int | NAO | - | NULL | - |
| 22 | financeiro_termino_vigencia | enum('DATA_ESPECIFICA','RECORRENTE') | NAO | - | NULL | - |
| 23 | financeiro_data_termino_vigencia | date | SIM | - | NULL | - |
| 24 | financeiro_caixa_operador_id | int unsigned | SIM | - | NULL | - |
| 25 | financeiro_empresa_nome | varchar(50) | NAO | - | NULL | - |
| 26 | financeiro_empresa_nome_fantasia | varchar(255) | NAO | - | NULL | - |
| 27 | financeiro_empresa_razao_social | varchar(255) | NAO | - | NULL | - |
| 28 | financeiro_categoria_id | int | NAO | - | NULL | - |
| 29 | categoria_nome | varchar(255) | SIM | - | NULL | - |
| 30 | categoria_codigo | varchar(20) | SIM | - | NULL | - |
| 31 | categoria_conta_dre_id | int unsigned | SIM | - | NULL | - |
| 32 | categoria_tag | varchar(255) | SIM | - | NULL | - |
| 33 | categoria_tipo | varchar(7) | SIM | - | NULL | - |
| 34 | parcela_id | int | NAO | - | 0 | - |
| 35 | parcela_compra_id | int | SIM | - | NULL | - |
| 36 | parcela_venda_id | int | SIM | - | NULL | - |
| 37 | parcela_financeiro_id | int | SIM | - | NULL | - |
| 38 | parcela_transferencia_id | int | SIM | - | NULL | - |
| 39 | parcela_fornecedor_id | int | SIM | - | NULL | - |
| 40 | parcela_cliente_id | int | SIM | - | NULL | - |
| 41 | parcela_contrato_servico_id | int | SIM | - | NULL | - |
| 42 | parcela_documento | varchar(50) | SIM | - | NULL | - |
| 43 | parcela_conta_id | int | SIM | - | NULL | - |
| 44 | parcela_cartao_credito_id | int | SIM | - | NULL | - |
| 45 | parcela_venda_cartao_id | int unsigned | SIM | - | NULL | - |
| 46 | parcela_api_codigo_pagamento | varchar(255) | SIM | - | NULL | - |
| 47 | parcela_api_nome_pagamento | varchar(255) | SIM | - | NULL | - |
| 48 | parcela_numero | varchar(255) | SIM | - | NULL | - |
| 49 | parcela_vencimento | date | NAO | - | NULL | - |
| 50 | parcela_tarifa | decimal(15,2) | SIM | - | NULL | - |
| 51 | parcela_duplicata_pendente | int | NAO | - | 0 | - |
| 52 | parcela_banco_id | int | SIM | - | NULL | - |
| 53 | parcela_financeira_id | int | SIM | - | NULL | - |
| 54 | parcela_data_caixa | date | SIM | - | NULL | - |
| 55 | parcela_observacao | varchar(255) | SIM | - | NULL | - |
| 56 | parcela_created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 57 | parcela_updated_at | timestamp | SIM | - | NULL | - |
| 58 | parcela_deleted_at | timestamp | SIM | - | NULL | - |
| 59 | parcela_cancelada | tinyint(1) | NAO | - | 0 | - |
| 60 | parcela_parcela_vinculada | int | SIM | - | NULL | - |
| 61 | parcela_operacao | enum('DEBITO','CREDITO') | SIM | - | NULL | - |
| 62 | parcela_empresa_id | int | SIM | - | NULL | - |
| 63 | parcela_user_id | int unsigned | SIM | - | NULL | - |
| 64 | parcela_motivo_cancelamento | longtext | SIM | - | NULL | - |
| 65 | parcela_cheque_banco | varchar(255) | SIM | - | NULL | - |
| 66 | parcela_data_cancelamento | timestamp | SIM | - | NULL | - |
| 67 | parcela_guid | char(36) | SIM | - | NULL | - |
| 68 | parcela_pos_habilitar | smallint | SIM | - | 0 | - |
| 69 | parcela_tp_integra | bigint | SIM | - | NULL | - |
| 70 | parcela_api_cobranca_id | char(36) | SIM | - | NULL | - |
| 71 | parcela_api_cobranca_agreemente_id | char(36) | SIM | - | NULL | - |
| 72 | parcela_codigo_autorizacao | varchar(50) | SIM | - | NULL | - |
| 73 | parcela_cnpj_instituicao_financeira | varchar(50) | SIM | - | NULL | - |
| 74 | parcela_cartao_credito_taxa_admin | decimal(15,2) | SIM | - | NULL | - |
| 75 | parcela_tipo_debito_id | int | SIM | - | NULL | - |
| 76 | parcela_conciliacao_extrato_bancario | smallint | NAO | - | 0 | - |
| 77 | cartao_nome | varchar(50) | SIM | - | NULL | - |
| 78 | cartao_taxa_admin | decimal(15,2) | SIM | - | NULL | - |
| 79 | parcela_forma_pagamento_id | int | NAO | - | NULL | - |
| 80 | parcela_forma_pagamento_nome | varchar(50) | SIM | - | NULL | - |
| 81 | parcela_forma_pagamento_tipo | varchar(255) | SIM | - | DUPLICATA | - |
| 82 | parcela_forma_pagamento_exibir | tinyint(1) | SIM | - | 1 | - |
| 83 | parcela_forma_pagamento_saldo_caixa | tinyint(1) | SIM | - | 0 | - |
| 84 | parcela_forma_pagamento_codigo_nfce | varchar(255) | SIM | - | 99 | - |
| 85 | parcela_forma_pagamento_ordem | int | SIM | - | 0 | - |
| 86 | valor_pago_parcela | decimal(37,4) | NAO | - | 0.0000 | - |
| 87 | valor_pago_liquido_parcela | decimal(39,4) | NAO | - | 0.0000 | - |
| 88 | acrescimo_parcela | decimal(37,4) | NAO | - | 0.0000 | - |
| 89 | desconto_parcela | decimal(37,4) | NAO | - | 0.0000 | - |
| 90 | valor_parcela | decimal(15,4) | NAO | - | NULL | - |
| 91 | valor_parcela_corrigido | decimal(27,2) | SIM | - | NULL | - |
| 92 | valor_pendente | decimal(36,2) | SIM | - | NULL | - |

### Tabela: view_memoria_financeiro_pagamento (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | financeiro_parcela_id | int | NAO | - | NULL | - |
| 2 | valor_pago | decimal(37,4) | SIM | - | NULL | - |
| 3 | acrescimo | decimal(37,4) | SIM | - | NULL | - |
| 4 | desconto | decimal(37,4) | SIM | - | NULL | - |
| 5 | valor_total | decimal(39,4) | SIM | - | NULL | - |

### Tabela: view_memoria_financeiro_todas (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 118

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | financeiro_id | int | NAO | - | 0 | - |
| 2 | financeiro_empresa_id | int | NAO | - | NULL | - |
| 3 | financeiro_data_lancamento | date | NAO | - | NULL | - |
| 4 | financeiro_documento | varchar(20) | SIM | - | NULL | - |
| 5 | financeiro_historico | varchar(255) | NAO | - | NULL | - |
| 6 | financeiro_fornecedor_id | int | SIM | - | NULL | - |
| 7 | financeiro_cliente_id | int | SIM | - | NULL | - |
| 8 | financeiro_contrato_servico_id | int | SIM | - | NULL | - |
| 9 | financeiro_created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 10 | financeiro_updated_at | timestamp | SIM | - | NULL | - |
| 11 | financeiro_deleted_at | timestamp | SIM | - | NULL | - |
| 12 | financeiro_valor | decimal(15,4) | NAO | - | NULL | - |
| 13 | financeiro_tipo_documento_id | int unsigned | SIM | - | NULL | - |
| 14 | financeiro_origem | varchar(50) | SIM | - | NULL | - |
| 15 | financeiro_device_id | varchar(255) | SIM | - | NULL | - |
| 16 | financeiro_usuario_lancamento_id | int unsigned | SIM | - | NULL | - |
| 17 | financeiro_api_device_id | varchar(255) | SIM | - | NULL | - |
| 18 | financeiro_repeticao | enum('FIXA','PARCELADA') | NAO | - | NULL | - |
| 19 | financeiro_repeticao_tipo | enum('Mensal','Bimestral','Trimestral','Semestral','Anual','Intervalo') | NAO | - | NULL | - |
| 20 | financeiro_repeticao_quantidade | int | NAO | - | NULL | - |
| 21 | financeiro_repeticao_intervalo | int | NAO | - | NULL | - |
| 22 | financeiro_termino_vigencia | enum('DATA_ESPECIFICA','RECORRENTE') | NAO | - | NULL | - |
| 23 | financeiro_data_termino_vigencia | date | SIM | - | NULL | - |
| 24 | financeiro_caixa_operador_id | int unsigned | SIM | - | NULL | - |
| 25 | financeiro_empresa_nome | varchar(50) | NAO | - | NULL | - |
| 26 | financeiro_empresa_nome_fantasia | varchar(255) | NAO | - | NULL | - |
| 27 | financeiro_empresa_razao_social | varchar(255) | NAO | - | NULL | - |
| 28 | financeiro_categoria_id | int | NAO | - | NULL | - |
| 29 | categoria_nome | varchar(255) | SIM | - | NULL | - |
| 30 | categoria_codigo | varchar(20) | SIM | - | NULL | - |
| 31 | categoria_conta_dre_id | int unsigned | SIM | - | NULL | - |
| 32 | categoria_tag | varchar(255) | SIM | - | NULL | - |
| 33 | categoria_tipo | varchar(7) | SIM | - | NULL | - |
| 34 | parcela_id | int | NAO | - | 0 | - |
| 35 | parcela_compra_id | int | SIM | - | NULL | - |
| 36 | parcela_venda_id | int | SIM | - | NULL | - |
| 37 | parcela_financeiro_id | int | SIM | - | NULL | - |
| 38 | parcela_transferencia_id | int | SIM | - | NULL | - |
| 39 | parcela_fornecedor_id | int | SIM | - | NULL | - |
| 40 | parcela_cliente_id | int | SIM | - | NULL | - |
| 41 | parcela_contrato_servico_id | int | SIM | - | NULL | - |
| 42 | parcela_documento | varchar(50) | SIM | - | NULL | - |
| 43 | parcela_conta_id | int | SIM | - | NULL | - |
| 44 | parcela_cartao_credito_id | int | SIM | - | NULL | - |
| 45 | parcela_venda_cartao_id | int unsigned | SIM | - | NULL | - |
| 46 | parcela_api_codigo_pagamento | varchar(255) | SIM | - | NULL | - |
| 47 | parcela_api_nome_pagamento | varchar(255) | SIM | - | NULL | - |
| 48 | parcela_numero | varchar(255) | SIM | - | NULL | - |
| 49 | parcela_vencimento | date | NAO | - | NULL | - |
| 50 | parcela_tarifa | decimal(15,2) | SIM | - | NULL | - |
| 51 | parcela_duplicata_pendente | int | NAO | - | 0 | - |
| 52 | parcela_banco_id | int | SIM | - | NULL | - |
| 53 | parcela_financeira_id | int | SIM | - | NULL | - |
| 54 | parcela_data_caixa | date | SIM | - | NULL | - |
| 55 | parcela_observacao | varchar(255) | SIM | - | NULL | - |
| 56 | parcela_created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 57 | parcela_updated_at | timestamp | SIM | - | NULL | - |
| 58 | parcela_deleted_at | timestamp | SIM | - | NULL | - |
| 59 | parcela_cancelada | tinyint(1) | NAO | - | 0 | - |
| 60 | parcela_parcela_vinculada | int | SIM | - | NULL | - |
| 61 | parcela_operacao | enum('DEBITO','CREDITO') | SIM | - | NULL | - |
| 62 | parcela_empresa_id | int | SIM | - | NULL | - |
| 63 | parcela_user_id | int unsigned | SIM | - | NULL | - |
| 64 | parcela_motivo_cancelamento | longtext | SIM | - | NULL | - |
| 65 | parcela_cheque_banco | varchar(255) | SIM | - | NULL | - |
| 66 | parcela_data_cancelamento | timestamp | SIM | - | NULL | - |
| 67 | parcela_guid | char(36) | SIM | - | NULL | - |
| 68 | parcela_pos_habilitar | smallint | SIM | - | 0 | - |
| 69 | parcela_tp_integra | bigint | SIM | - | NULL | - |
| 70 | parcela_api_cobranca_id | char(36) | SIM | - | NULL | - |
| 71 | parcela_api_cobranca_agreemente_id | char(36) | SIM | - | NULL | - |
| 72 | parcela_codigo_autorizacao | varchar(50) | SIM | - | NULL | - |
| 73 | parcela_cnpj_instituicao_financeira | varchar(50) | SIM | - | NULL | - |
| 74 | parcela_cartao_credito_taxa_admin | decimal(15,2) | SIM | - | NULL | - |
| 75 | parcela_tipo_debito_id | int | SIM | - | NULL | - |
| 76 | parcela_conciliacao_extrato_bancario | smallint | NAO | - | 0 | - |
| 77 | cartao_nome | varchar(50) | SIM | - | NULL | - |
| 78 | cartao_taxa_admin | decimal(15,2) | SIM | - | NULL | - |
| 79 | parcela_forma_pagamento_id | int | NAO | - | NULL | - |
| 80 | parcela_forma_pagamento_nome | varchar(50) | SIM | - | NULL | - |
| 81 | parcela_forma_pagamento_tipo | varchar(255) | SIM | - | DUPLICATA | - |
| 82 | parcela_forma_pagamento_exibir | tinyint(1) | SIM | - | 1 | - |
| 83 | parcela_forma_pagamento_saldo_caixa | tinyint(1) | SIM | - | 0 | - |
| 84 | parcela_forma_pagamento_codigo_nfce | varchar(255) | SIM | - | 99 | - |
| 85 | parcela_forma_pagamento_ordem | int | SIM | - | 0 | - |
| 86 | valor_pago_parcela | decimal(37,4) | NAO | - | 0.0000 | - |
| 87 | valor_pago_liquido_parcela | decimal(39,4) | NAO | - | 0.0000 | - |
| 88 | acrescimo_parcela | decimal(37,4) | NAO | - | 0.0000 | - |
| 89 | desconto_parcela | decimal(37,4) | NAO | - | 0.0000 | - |
| 90 | valor_parcela | decimal(15,4) | NAO | - | NULL | - |
| 91 | valor_parcela_corrigido | decimal(27,2) | SIM | - | NULL | - |
| 92 | valor_pendente | decimal(36,2) | SIM | - | NULL | - |
| 93 | pagamento_id | int unsigned | SIM | - | 0 | - |
| 94 | pagamento_valor_pago | decimal(15,4) | SIM | - | NULL | - |
| 95 | pagamento_acrescimo | decimal(15,4) | SIM | - | 0.0000 | - |
| 96 | pagamento_desconto | decimal(15,4) | SIM | - | 0.0000 | - |
| 97 | pagamento_valor_pago_liquido | decimal(17,4) | SIM | - | NULL | - |
| 98 | pagamento_conta_id | int unsigned | SIM | - | NULL | - |
| 99 | pagamento_conta_nome | varchar(255) | SIM | - | NULL | - |
| 100 | pagamento_conta_tipo | enum('caixa','cofre','pix','cartao credito','administradora cartao','conta corrente','conta poupanca','conta emprestimo','conta garantia','carteira virtual','crediario','conta aplicacao') | SIM | - | NULL | - |
| 101 | pagamento_financeiro_parcela_id | int | SIM | - | NULL | - |
| 102 | pagamento_data_pagamento | date | SIM | - | NULL | - |
| 103 | data_hora_pagamento | varchar(24) | SIM | - | NULL | - |
| 104 | pagamento_created_at | timestamp | SIM | - | 0000-00-00 00:00:00 | - |
| 105 | pagamento_updated_at | timestamp | SIM | - | 0000-00-00 00:00:00 | - |
| 106 | pagamento_deleted_at | timestamp | SIM | - | NULL | - |
| 107 | pagamento_user_baixa_id | int unsigned | SIM | - | NULL | - |
| 108 | pagamento_api_device_id | varchar(255) | SIM | - | NULL | - |
| 109 | pagamento_valor_recebido | decimal(15,4) | SIM | - | 0.0000 | - |
| 110 | pagamento_caixa_funcoes_id | int | SIM | - | NULL | - |
| 111 | pagamento_caixa_turno | varchar(255) | SIM | - | NULL | - |
| 112 | pagamento_forma_pagamento_baixa_id | int | SIM | - | NULL | - |
| 113 | pagamento_forma_pagamento_nome | varchar(50) | SIM | - | NULL | - |
| 114 | pagamento_forma_pagamento_tipo | varchar(255) | SIM | - | DUPLICATA | - |
| 115 | pagamento_forma_pagamento_exibir | tinyint(1) | SIM | - | 1 | - |
| 116 | pagamento_forma_pagamento_saldo_caixa | tinyint(1) | SIM | - | 0 | - |
| 117 | pagamento_forma_pagamento_codigo_nfce | varchar(255) | SIM | - | 99 | - |
| 118 | pagamento_forma_pagamento_ordem | int | SIM | - | 0 | - |

### Tabela: view_memoria_nf_entrada (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 37

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint | NAO | - | 0 | - |
| 2 | origem | varchar(6) | NAO | - |  | - |
| 3 | empresa_id | int | NAO | - | 0 | - |
| 4 | data_hora_emissao | datetime | SIM | - | NULL | - |
| 5 | data_hora_entrada | datetime | SIM | - | NULL | - |
| 6 | numero_nfe | int | NAO | - | 0 | - |
| 7 | modelo | varchar(255) | SIM | - | NULL | - |
| 8 | serie | varchar(255) | SIM | - | NULL | - |
| 9 | ambiente | int | SIM | - | NULL | - |
| 10 | destinatario_nome | varchar(60) | NAO | - |  | - |
| 11 | destinatario_cpf_cnpj | varchar(14) | NAO | - |  | - |
| 12 | xml_recibo_emissao | mediumtext | SIM | - | NULL | - |
| 13 | numero_protocolo_autorizacao | varchar(255) | SIM | - | NULL | - |
| 14 | xml_cancelamento | mediumtext | SIM | - | NULL | - |
| 15 | recibo_situacao | varchar(12) | SIM | - | NULL | - |
| 16 | cancelada | bigint | NAO | - | 0 | - |
| 17 | denegada | bigint | NAO | - | 0 | - |
| 18 | chave_acesso | varchar(255) | SIM | - | NULL | - |
| 19 | tipo_emissao | int | SIM | - | NULL | - |
| 20 | deleted_at | timestamp | SIM | - | NULL | - |
| 21 | cfop | varchar(255) | SIM | - | NULL | - |
| 22 | cfop_natureza | varchar(255) | NAO | - |  | - |
| 23 | pis_cst | varchar(255) | SIM | - | NULL | - |
| 24 | cofins_cst | varchar(2) | SIM | - | NULL | - |
| 25 | produto_id | int | NAO | - | 0 | - |
| 26 | quantidade_tributavel | decimal(15,4) | SIM | - | NULL | - |
| 27 | valor_unitario_tributavel | decimal(16,5) | SIM | - | NULL | - |
| 28 | valor_total_desconto | decimal(15,2) | NAO | - | 0.00 | - |
| 29 | valor_total_frete | decimal(15,2) | NAO | - | 0.00 | - |
| 30 | valor_total_outras_despesas | decimal(15,2) | NAO | - | 0.00 | - |
| 31 | icms_base_calculo | decimal(15,2) | NAO | - | 0.00 | - |
| 32 | icms_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 33 | icmsst_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 34 | fcp_st_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 35 | ipi_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 36 | pis_valor | decimal(15,2) | NAO | - | 0.00 | - |
| 37 | cofins_valor | decimal(15,2) | NAO | - | 0.00 | - |

### Tabela: view_memoria_nf_saida (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 108

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | - | 0 | - |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | numero_nfe | int | NAO | - | NULL | - |
| 4 | modelo | varchar(255) | SIM | - | NULL | - |
| 5 | serie | varchar(255) | SIM | - | NULL | - |
| 6 | ambiente | int | SIM | - | NULL | - |
| 7 | data_hora_emissao | timestamp | SIM | - | NULL | - |
| 8 | data_hora_saida | timestamp | SIM | - | NULL | - |
| 9 | recibo_situacao | enum('AGUARDANDO','NAO_ENVIADO','RECEBIDO','CANCELADA','DENEGADA','CONTINGENCIA') | SIM | - | NULL | - |
| 10 | cancelada | int | NAO | - | 0 | - |
| 11 | denegada | int | NAO | - | 0 | - |
| 12 | numero_recibo | varchar(255) | SIM | - | NULL | - |
| 13 | status | varchar(12) | NAO | - |  | - |
| 14 | numero_protocolo_autorizacao | varchar(255) | SIM | - | NULL | - |
| 15 | xml_recibo_emissao | text | SIM | - | NULL | - |
| 16 | xml_cancelamento | text | SIM | - | NULL | - |
| 17 | chave_acesso | varchar(255) | SIM | - | NULL | - |
| 18 | tipo_emissao | int | SIM | - | 1 | - |
| 19 | xml | longtext | SIM | - | NULL | - |
| 20 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 21 | updated_at | timestamp | SIM | - | NULL | - |
| 22 | deleted_at | timestamp | SIM | - | NULL | - |
| 23 | destinatario_cpf_cnpj | varchar(14) | NAO | - | NULL | - |
| 24 | destinatario_nome | varchar(60) | NAO | - | NULL | - |
| 25 | destinatario_endereco | varchar(60) | SIM | - | NULL | - |
| 26 | destinatario_numero | varchar(60) | SIM | - | NULL | - |
| 27 | destinatario_complemento | varchar(60) | SIM | - | NULL | - |
| 28 | destinatario_bairro | varchar(60) | SIM | - | NULL | - |
| 29 | destinatario_codigo_cidade | varchar(7) | SIM | - | NULL | - |
| 30 | destinatario_nome_cidade | varchar(60) | SIM | - | NULL | - |
| 31 | destinatario_uf | enum('AC','AL','AP','AM','BA','CE','DF','ES','EX','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | SIM | - | NULL | - |
| 32 | destinatario_cep | varchar(8) | SIM | - | NULL | - |
| 33 | destinatario_codigo_pais | varchar(4) | SIM | - | NULL | - |
| 34 | destinatario_nome_pais | varchar(60) | SIM | - | NULL | - |
| 35 | destinatario_telefone | varchar(14) | SIM | - | NULL | - |
| 36 | destinatario_indicador_ie | enum('1','2','9') | SIM | - | NULL | - |
| 37 | destinatario_ie | varchar(14) | SIM | - | NULL | - |
| 38 | destinatario_inscricao_suframa | varchar(9) | SIM | - | NULL | - |
| 39 | destinatario_inscricao_municipal | varchar(15) | SIM | - | NULL | - |
| 40 | destinatario_email | varchar(60) | SIM | - | NULL | - |
| 41 | produto_id | int | NAO | - | NULL | - |
| 42 | codigo_ean | varchar(14) | SIM | - | NULL | - |
| 43 | produto_nome | varchar(255) | NAO | - | NULL | - |
| 44 | ncm | varchar(8) | SIM | - | NULL | - |
| 45 | cst_csosn | varchar(255) | SIM | - | NULL | - |
| 46 | unidade_comercial | varchar(6) | SIM | - | NULL | - |
| 47 | quantidade_comercial | decimal(15,4) | SIM | - | NULL | - |
| 48 | valor_unitario_comercial | decimal(15,4) | SIM | - | NULL | - |
| 49 | valor_total_produto | decimal(15,4) | SIM | - | NULL | - |
| 50 | icms_percentual_reducao_base | decimal(13,2) | SIM | - | NULL | - |
| 51 | icmsst_valor | decimal(13,2) | SIM | - | NULL | - |
| 52 | icmsst_retido_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 53 | icmsst_retido_valor | decimal(13,2) | SIM | - | NULL | - |
| 54 | icms_desoneracao_motivo | varchar(60) | SIM | - | NULL | - |
| 55 | icms_desoneracao_valor | decimal(13,2) | SIM | - | NULL | - |
| 56 | icms_operacao_valor | decimal(13,2) | SIM | - | NULL | - |
| 57 | icms_diferimento_percentual | decimal(13,2) | SIM | - | NULL | - |
| 58 | icms_diferimento_valor | decimal(13,2) | SIM | - | NULL | - |
| 59 | icms_valor | decimal(13,2) | SIM | - | NULL | - |
| 60 | ipi_valor | decimal(13,2) | SIM | - | NULL | - |
| 61 | ipi_aliquota | decimal(13,2) | SIM | - | NULL | - |
| 62 | ipi_enquadramento | varchar(5) | SIM | - | NULL | - |
| 63 | total_tributos | decimal(13,2) | SIM | - | NULL | - |
| 64 | natureza_item | varchar(255) | SIM | - | NULL | - |
| 65 | natureza | varchar(255) | SIM | - | NULL | - |
| 66 | cest | varchar(10) | SIM | - | NULL | - |
| 67 | especifico | varchar(255) | SIM | - | NULL | - |
| 68 | cfop | varchar(4) | SIM | - | NULL | - |
| 69 | icms_aliquota | decimal(13,2) | SIM | - | NULL | - |
| 70 | icmsst_mva | decimal(13,2) | SIM | - | NULL | - |
| 71 | icmsst_percentual_reducao_base | decimal(13,2) | SIM | - | NULL | - |
| 72 | icmsst_aliquota | decimal(13,2) | SIM | - | NULL | - |
| 73 | pis_cst | varchar(255) | SIM | - | NULL | - |
| 74 | pis_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 75 | pis_aliquota | decimal(14,3) | SIM | - | NULL | - |
| 76 | pis_valor | decimal(13,2) | SIM | - | NULL | - |
| 77 | cofins_cst | varchar(2) | SIM | - | NULL | - |
| 78 | cofins_valor | decimal(13,2) | SIM | - | NULL | - |
| 79 | cofins_aliquota | decimal(14,3) | SIM | - | NULL | - |
| 80 | icmsdifal_base_calculo_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 81 | icmsdifal_percentual_fcp_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 82 | icmsdifal_percentual_icms_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 83 | icmsdifal_percentual_icms_interestadual | decimal(13,2) | SIM | - | NULL | - |
| 84 | icmsdifal_percentual_provisorio_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 85 | icmsdifal_valor_fcp_uf_destino | decimal(13,2) | SIM | - | NULL | - |
| 86 | icmsdifal_valor_icms_uf_remetente | decimal(13,2) | SIM | - | NULL | - |
| 87 | ipi_cst | varchar(2) | SIM | - | NULL | - |
| 88 | icmsst_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 89 | ipi_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 90 | icms_base_calculo | decimal(13,2) | SIM | - | NULL | - |
| 91 | icms_aliquota_credito_simples_nacional | decimal(15,2) | SIM | - | NULL | - |
| 92 | icms_valor_credito_simples_nacional | decimal(15,2) | SIM | - | NULL | - |
| 93 | unidade_tributavel | varchar(6) | SIM | - | NULL | - |
| 94 | quantidade_tributavel | decimal(15,4) | SIM | - | NULL | - |
| 95 | valor_unitario_tributavel | decimal(15,4) | SIM | - | NULL | - |
| 96 | valor_total_frete | decimal(13,2) | SIM | - | NULL | - |
| 97 | valor_total_seguro | decimal(13,2) | SIM | - | NULL | - |
| 98 | valor_total_desconto | decimal(13,2) | SIM | - | NULL | - |
| 99 | valor_total_outras_despesas | decimal(13,2) | SIM | - | NULL | - |
| 100 | indicador_total | int | NAO | - | 1 | - |
| 101 | origem | varchar(1) | NAO | - | 0 | - |
| 102 | icms_modalidade_base_calculo | varchar(2) | SIM | - | NULL | - |
| 103 | icmsst_modalidade_base_calculo | varchar(2) | SIM | - | NULL | - |
| 104 | item_total_bruto | decimal(30,8) | SIM | - | NULL | - |
| 105 | item_desconto | decimal(13,2) | NAO | - | 0.00 | - |
| 106 | item_outras_despesas | decimal(13,2) | NAO | - | 0.00 | - |
| 107 | item_total_liquido | decimal(32,8) | SIM | - | NULL | - |
| 108 | item_total_liquido_cancelado | decimal(32,8) | SIM | - | NULL | - |

### Tabela: view_memoria_vendas (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 99

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | cliente_id | int | NAO | - | 1 | - |
| 4 | funcionario_id | int | NAO | - | 1 | - |
| 5 | nfe_id | int unsigned | SIM | - | NULL | - |
| 6 | nfse_id | int | SIM | - | NULL | - |
| 7 | observacao | text | SIM | - | NULL | - |
| 8 | api_cliente_cpf | varchar(255) | SIM | - | NULL | - |
| 9 | api_cliente_nome | varchar(50) | SIM | - | NULL | - |
| 10 | api_faturar | varchar(255) | SIM | - | NULL | - |
| 11 | api_status | varchar(255) | SIM | - | NULL | - |
| 12 | api_app_name | varchar(50) | SIM | - | NULL | - |
| 13 | api_data_hora_venda | timestamp | SIM | - | NULL | - |
| 14 | desconto_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 15 | desconto_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | acrescimo_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 17 | acrescimo_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | percentual_comissao_venda | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 20 | updated_at | timestamp | SIM | - | NULL | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |
| 22 | api_guid | varchar(50) | NAO | - | NULL | - |
| 23 | api_data_hora_lancamento | timestamp | SIM | - | NULL | - |
| 24 | api_device_id | varchar(100) | NAO | - | NULL | - |
| 25 | cancelada | tinyint(1) | NAO | - | 0 | - |
| 26 | usuario_lancamento_id | int unsigned | SIM | - | NULL | - |
| 27 | bloqueada | smallint | NAO | - | 0 | - |
| 28 | parent_guid | varchar(50) | SIM | - | NULL | - |
| 29 | usuario_cancelamento_id | int unsigned | SIM | - | NULL | - |
| 30 | data_hora_cancelamento | datetime | SIM | - | NULL | - |
| 31 | numero_documento | varchar(255) | SIM | - | NULL | - |
| 32 | numero_caixa | varchar(20) | SIM | - | NULL | - |
| 33 | tipo_preco_id | int unsigned | SIM | - | NULL | - |
| 34 | integracao_delivery | varchar(50) | SIM | - | NULL | - |
| 35 | entregador_id | int | SIM | - | NULL | - |
| 36 | assistencia_id | int unsigned | SIM | - | NULL | - |
| 37 | caixa_funcoes_id | int | SIM | - | NULL | - |
| 38 | indicador_id | int | SIM | - | NULL | - |
| 39 | marketplace_pedido_id | int | SIM | - | NULL | - |
| 40 | atendente_mesa | varchar(255) | SIM | - | NULL | - |
| 41 | comissao_entregador | decimal(15,2) | SIM | - | NULL | - |
| 42 | comissao_indicador | decimal(15,2) | SIM | - | NULL | - |
| 43 | numero_mesa | varchar(255) | SIM | - | NULL | - |
| 44 | numero_comanda | varchar(255) | SIM | - | NULL | - |
| 45 | origem_venda | varchar(255) | SIM | - | NULL | - |
| 46 | quantidade_pessoas | int | SIM | - | NULL | - |
| 47 | quantidade_comandas | int | SIM | - | NULL | - |
| 48 | tipo_lancamento | varchar(50) | NAO | - | VENDA | - |
| 49 | orcamento_id | int | SIM | - | NULL | - |
| 50 | orcamento_competencia | date | SIM | - | NULL | - |
| 51 | numero_pre_venda | varchar(50) | SIM | - | NULL | - |
| 52 | cliente_nome | varchar(255) | NAO | - | NULL | - |
| 53 | cliente_tipo_cliente_id | int | NAO | - | NULL | - |
| 54 | vendedor_nome | varchar(255) | NAO | - | NULL | - |
| 55 | venda_empresa_nome | varchar(50) | NAO | - | NULL | - |
| 56 | venda_empresa_nome_fantasia | varchar(255) | NAO | - | NULL | - |
| 57 | venda_empresa_razao_social | varchar(255) | NAO | - | NULL | - |
| 58 | tipo_comissao | enum('PRODUTO','VENDEDOR') | NAO | - | VENDEDOR | - |
| 59 | venda_item_id | int | NAO | - | 0 | - |
| 60 | produto_empresa_grade_id | int | NAO | - | NULL | - |
| 61 | produto_venda_quantidade | decimal(15,4) | NAO | - | 1.0000 | - |
| 62 | produto_venda_preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 63 | comissao | decimal(15,2) | SIM | - | 0.00 | - |
| 64 | desconto_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 65 | acrescimo_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 66 | item_cancelado | timestamp | SIM | - | NULL | - |
| 67 | atendente_item | int | SIM | - | NULL | - |
| 68 | comissao_atendente | decimal(15,2) | SIM | - | NULL | - |
| 69 | comissao_carta_produto | decimal(15,4) | SIM | - | NULL | - |
| 70 | comissao_carta_produto_tipo | enum('VALOR','PERCENTUAL') | SIM | - | PERCENTUAL | - |
| 71 | cobrar_taxa_servico | tinyint | SIM | - | NULL | - |
| 72 | data_venda | date | SIM | - | NULL | - |
| 73 | data_hora_venda | datetime | SIM | - | NULL | - |
| 74 | caixa_data | date | SIM | - | NULL | - |
| 75 | turno | tinyint unsigned | SIM | - | NULL | - |
| 76 | operador_id | int unsigned | SIM | - | NULL | - |
| 77 | indicador_nome | varchar(255) | SIM | - | NULL | - |
| 78 | produto_id | int | SIM | - | 0 | - |
| 79 | produto_nome | varchar(255) | SIM | - | NULL | - |
| 80 | produto_tipo_produto | varchar(50) | SIM | - | PRODUTO | - |
| 81 | produto_servico | int | SIM | - | NULL | - |
| 82 | produto_nome_completo | varchar(511) | SIM | - | NULL | - |
| 83 | produto_grade_descricao | varchar(255) | SIM | - | NULL | - |
| 84 | produto_grade_estoque | decimal(15,4) | SIM | - | 0.0000 | - |
| 85 | produto_empresa_id | int | SIM | - | NULL | - |
| 86 | produto_grade_deleted_at | timestamp | SIM | - | NULL | - |
| 87 | grupo_id | int | SIM | - | 0 | - |
| 88 | grupo_nome | varchar(255) | SIM | - | NULL | - |
| 89 | fabricante_id | int | SIM | - | 0 | - |
| 90 | fabricante_nome | varchar(50) | SIM | - | NULL | - |
| 91 | mes_venda | varchar(2) | SIM | - | NULL | - |
| 92 | ano_venda | varchar(4) | SIM | - | NULL | - |
| 93 | mes_ano_venda | varchar(7) | SIM | - | NULL | - |
| 94 | item_total | decimal(31,4) | SIM | - | NULL | - |
| 95 | item_total_real | decimal(33,4) | SIM | - | NULL | - |
| 96 | item_total_compra | decimal(31,4) | SIM | - | NULL | - |
| 97 | item_total_lucro | decimal(34,4) | SIM | - | NULL | - |
| 98 | item_total_desconto | decimal(25,4) | SIM | - | NULL | - |
| 99 | item_total_acrescimo | decimal(25,4) | SIM | - | NULL | - |

### Tabela: view_memoria_vendas_agrupado (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 97

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | cliente_id | int | NAO | - | 1 | - |
| 4 | funcionario_id | int | NAO | - | 1 | - |
| 5 | nfe_id | int unsigned | SIM | - | NULL | - |
| 6 | nfse_id | int | SIM | - | NULL | - |
| 7 | observacao | text | SIM | - | NULL | - |
| 8 | api_cliente_cpf | varchar(255) | SIM | - | NULL | - |
| 9 | api_cliente_nome | varchar(50) | SIM | - | NULL | - |
| 10 | api_faturar | varchar(255) | SIM | - | NULL | - |
| 11 | api_status | varchar(255) | SIM | - | NULL | - |
| 12 | api_app_name | varchar(50) | SIM | - | NULL | - |
| 13 | api_data_hora_venda | timestamp | SIM | - | NULL | - |
| 14 | desconto_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 15 | desconto_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | acrescimo_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 17 | acrescimo_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | percentual_comissao_venda | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | created_at | timestamp | NAO | - | 0000-00-00 00:00:00 | - |
| 20 | updated_at | timestamp | SIM | - | NULL | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |
| 22 | api_guid | varchar(50) | NAO | - | NULL | - |
| 23 | api_data_hora_lancamento | timestamp | SIM | - | NULL | - |
| 24 | api_device_id | varchar(100) | NAO | - | NULL | - |
| 25 | cancelada | tinyint(1) | NAO | - | 0 | - |
| 26 | usuario_lancamento_id | int unsigned | SIM | - | NULL | - |
| 27 | bloqueada | smallint | NAO | - | 0 | - |
| 28 | parent_guid | varchar(50) | SIM | - | NULL | - |
| 29 | usuario_cancelamento_id | int unsigned | SIM | - | NULL | - |
| 30 | data_hora_cancelamento | datetime | SIM | - | NULL | - |
| 31 | numero_documento | varchar(255) | SIM | - | NULL | - |
| 32 | numero_caixa | varchar(20) | SIM | - | NULL | - |
| 33 | tipo_preco_id | int unsigned | SIM | - | NULL | - |
| 34 | integracao_delivery | varchar(50) | SIM | - | NULL | - |
| 35 | entregador_id | int | SIM | - | NULL | - |
| 36 | assistencia_id | int unsigned | SIM | - | NULL | - |
| 37 | caixa_funcoes_id | int | SIM | - | NULL | - |
| 38 | indicador_id | int | SIM | - | NULL | - |
| 39 | marketplace_pedido_id | int | SIM | - | NULL | - |
| 40 | atendente_mesa | varchar(255) | SIM | - | NULL | - |
| 41 | comissao_entregador | decimal(15,2) | SIM | - | NULL | - |
| 42 | comissao_indicador | decimal(15,2) | SIM | - | NULL | - |
| 43 | numero_mesa | varchar(255) | SIM | - | NULL | - |
| 44 | numero_comanda | varchar(255) | SIM | - | NULL | - |
| 45 | origem_venda | varchar(255) | SIM | - | NULL | - |
| 46 | quantidade_pessoas | int | SIM | - | NULL | - |
| 47 | quantidade_comandas | int | SIM | - | NULL | - |
| 48 | tipo_lancamento | varchar(50) | NAO | - | VENDA | - |
| 49 | orcamento_id | int | SIM | - | NULL | - |
| 50 | orcamento_competencia | date | SIM | - | NULL | - |
| 51 | numero_pre_venda | varchar(50) | SIM | - | NULL | - |
| 52 | cliente_nome | varchar(255) | NAO | - | NULL | - |
| 53 | cliente_tipo_cliente_id | int | NAO | - | NULL | - |
| 54 | vendedor_nome | varchar(255) | NAO | - | NULL | - |
| 55 | venda_empresa_nome | varchar(50) | NAO | - | NULL | - |
| 56 | venda_empresa_nome_fantasia | varchar(255) | NAO | - | NULL | - |
| 57 | venda_empresa_razao_social | varchar(255) | NAO | - | NULL | - |
| 58 | tipo_comissao | enum('PRODUTO','VENDEDOR') | NAO | - | VENDEDOR | - |
| 59 | venda_item_id | int | NAO | - | 0 | - |
| 60 | produto_empresa_grade_id | int | NAO | - | NULL | - |
| 61 | produto_venda_quantidade | decimal(15,4) | NAO | - | 1.0000 | - |
| 62 | produto_venda_preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 63 | comissao | decimal(15,2) | SIM | - | 0.00 | - |
| 64 | desconto_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 65 | acrescimo_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 66 | item_cancelado | timestamp | SIM | - | NULL | - |
| 67 | atendente_item | int | SIM | - | NULL | - |
| 68 | comissao_atendente | decimal(15,2) | SIM | - | NULL | - |
| 69 | cobrar_taxa_servico | tinyint | SIM | - | NULL | - |
| 70 | produto_id | int | SIM | - | 0 | - |
| 71 | produto_nome | varchar(255) | SIM | - | NULL | - |
| 72 | produto_tipo_produto | varchar(50) | SIM | - | PRODUTO | - |
| 73 | produto_servico | int | SIM | - | NULL | - |
| 74 | produto_nome_completo | varchar(511) | SIM | - | NULL | - |
| 75 | produto_grade_descricao | varchar(255) | SIM | - | NULL | - |
| 76 | produto_grade_estoque | decimal(15,4) | SIM | - | 0.0000 | - |
| 77 | produto_empresa_id | int | SIM | - | NULL | - |
| 78 | produto_grade_deleted_at | timestamp | SIM | - | NULL | - |
| 79 | grupo_id | int | SIM | - | 0 | - |
| 80 | grupo_nome | varchar(255) | SIM | - | NULL | - |
| 81 | fabricante_id | int | SIM | - | 0 | - |
| 82 | fabricante_nome | varchar(50) | SIM | - | NULL | - |
| 83 | mes_venda | varchar(2) | SIM | - | NULL | - |
| 84 | ano_venda | varchar(4) | SIM | - | NULL | - |
| 85 | mes_ano_venda | varchar(7) | SIM | - | NULL | - |
| 86 | item_total | decimal(53,4) | SIM | - | NULL | - |
| 87 | item_total_real | decimal(55,4) | SIM | - | NULL | - |
| 88 | item_total_compra | decimal(53,4) | SIM | - | NULL | - |
| 89 | item_total_lucro | decimal(56,4) | SIM | - | NULL | - |
| 90 | item_total_desconto | decimal(47,4) | SIM | - | NULL | - |
| 91 | item_total_acrescimo | decimal(47,4) | SIM | - | NULL | - |
| 92 | data_venda | date | SIM | - | NULL | - |
| 93 | data_hora_venda | datetime | SIM | - | NULL | - |
| 94 | caixa_data | date | SIM | - | NULL | - |
| 95 | turno | tinyint unsigned | SIM | - | NULL | - |
| 96 | operador_id | int unsigned | SIM | - | NULL | - |
| 97 | indicador_nome | varchar(255) | SIM | - | NULL | - |

### Tabela: view_memoria_vendas_pagamento (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 85

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | cliente_id | int | NAO | - | 1 | - |
| 4 | funcionario_id | int | NAO | - | 1 | - |
| 5 | nfe_id | int unsigned | SIM | - | NULL | - |
| 6 | nfse_id | int | SIM | - | NULL | - |
| 7 | observacao | text | SIM | - | NULL | - |
| 8 | api_cliente_cpf | varchar(255) | SIM | - | NULL | - |
| 9 | api_cliente_nome | varchar(50) | SIM | - | NULL | - |
| 10 | api_faturar | varchar(255) | SIM | - | NULL | - |
| 11 | api_status | varchar(255) | SIM | - | NULL | - |
| 12 | api_app_name | varchar(50) | SIM | - | NULL | - |
| 13 | api_data_hora_venda | timestamp | SIM | - | NULL | - |
| 14 | desconto_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 15 | desconto_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | acrescimo_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 17 | acrescimo_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | percentual_comissao_venda | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 20 | updated_at | timestamp | SIM | - | NULL | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |
| 22 | api_guid | varchar(50) | NAO | - | NULL | - |
| 23 | api_data_hora_lancamento | timestamp | SIM | - | NULL | - |
| 24 | api_device_id | varchar(100) | NAO | - | NULL | - |
| 25 | cancelada | tinyint(1) | NAO | - | 0 | - |
| 26 | usuario_lancamento_id | int unsigned | SIM | - | NULL | - |
| 27 | bloqueada | smallint | NAO | - | 0 | - |
| 28 | parent_guid | varchar(50) | SIM | - | NULL | - |
| 29 | usuario_cancelamento_id | int unsigned | SIM | - | NULL | - |
| 30 | data_hora_cancelamento | datetime | SIM | - | NULL | - |
| 31 | numero_documento | varchar(255) | SIM | - | NULL | - |
| 32 | numero_caixa | varchar(20) | SIM | - | NULL | - |
| 33 | tipo_preco_id | int unsigned | SIM | - | NULL | - |
| 34 | integracao_delivery | varchar(50) | SIM | - | NULL | - |
| 35 | entregador_id | int | SIM | - | NULL | - |
| 36 | assistencia_id | int unsigned | SIM | - | NULL | - |
| 37 | caixa_funcoes_id | int | SIM | - | NULL | - |
| 38 | indicador_id | int | SIM | - | NULL | - |
| 39 | marketplace_pedido_id | int | SIM | - | NULL | - |
| 40 | atendente_mesa | varchar(255) | SIM | - | NULL | - |
| 41 | comissao_entregador | decimal(15,2) | SIM | - | NULL | - |
| 42 | comissao_indicador | decimal(15,2) | SIM | - | NULL | - |
| 43 | numero_mesa | varchar(255) | SIM | - | NULL | - |
| 44 | numero_comanda | varchar(255) | SIM | - | NULL | - |
| 45 | origem_venda | varchar(255) | SIM | - | NULL | - |
| 46 | quantidade_pessoas | int | SIM | - | NULL | - |
| 47 | quantidade_comandas | int | SIM | - | NULL | - |
| 48 | tipo_lancamento | varchar(50) | NAO | - | VENDA | - |
| 49 | orcamento_id | int | SIM | - | NULL | - |
| 50 | orcamento_competencia | date | SIM | - | NULL | - |
| 51 | numero_pre_venda | varchar(50) | SIM | - | NULL | - |
| 52 | data_venda | date | SIM | - | NULL | - |
| 53 | data_hora_venda | datetime | SIM | - | NULL | - |
| 54 | caixa_data | date | SIM | - | NULL | - |
| 55 | turno | tinyint unsigned | SIM | - | NULL | - |
| 56 | operador_id | int unsigned | SIM | - | NULL | - |
| 57 | indicador_nome | varchar(255) | SIM | - | NULL | - |
| 58 | cliente_nome | varchar(255) | NAO | - | NULL | - |
| 59 | cliente_tipo_cliente_id | int | NAO | - | NULL | - |
| 60 | vendedor_nome | varchar(255) | NAO | - | NULL | - |
| 61 | venda_empresa_nome | varchar(50) | NAO | - | NULL | - |
| 62 | venda_empresa_nome_fantasia | varchar(255) | NAO | - | NULL | - |
| 63 | venda_empresa_razao_social | varchar(255) | NAO | - | NULL | - |
| 64 | tipo_comissao | enum('PRODUTO','VENDEDOR') | NAO | - | VENDEDOR | - |
| 65 | vencimento | date | NAO | - | NULL | - |
| 66 | valor_parcela_financeiro | decimal(15,4) | NAO | - | NULL | - |
| 67 | financeiro_parcela_id | int | NAO | - | 0 | - |
| 68 | banco_id | int | SIM | - | NULL | - |
| 69 | parcela | varchar(255) | SIM | - | NULL | - |
| 70 | parcela_cancelada | tinyint(1) | NAO | - | 0 | - |
| 71 | forma_pagamento_id | int | NAO | - | NULL | - |
| 72 | forma_pagamento_nome | varchar(50) | NAO | - | NULL | - |
| 73 | forma_pagamento_tipo | varchar(255) | NAO | - | DUPLICATA | - |
| 74 | forma_pagamento_exibir | tinyint(1) | NAO | - | 1 | - |
| 75 | forma_pagamento_saldo_caixa | tinyint(1) | NAO | - | 0 | - |
| 76 | forma_pagamento_codigo_nfce | varchar(255) | NAO | - | 99 | - |
| 77 | forma_pagamento_ordem | int | SIM | - | 0 | - |
| 78 | cartao_credito_id | int | SIM | - | NULL | - |
| 79 | cartao_nome | varchar(50) | SIM | - | NULL | - |
| 80 | cartao_tipo | enum('CREDITO','DEBITO') | SIM | - | CREDITO | - |
| 81 | cartao_taxa_admin | decimal(15,2) | SIM | - | NULL | - |
| 82 | valor_parcela | decimal(15,4) | NAO | - | NULL | - |
| 83 | valor_parcela_corrigido | decimal(27,2) | SIM | - | NULL | - |
| 84 | valor_pago | decimal(37,4) | NAO | - | 0.0000 | - |
| 85 | valor_pendente | decimal(36,2) | SIM | - | NULL | - |

### Tabela: view_memoria_vendas_todas (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 99

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int | NAO | - | 0 | - |
| 2 | empresa_id | int | NAO | - | NULL | - |
| 3 | cliente_id | int | NAO | - | 1 | - |
| 4 | funcionario_id | int | NAO | - | 1 | - |
| 5 | nfe_id | int unsigned | SIM | - | NULL | - |
| 6 | nfse_id | int | SIM | - | NULL | - |
| 7 | observacao | text | SIM | - | NULL | - |
| 8 | api_cliente_cpf | varchar(255) | SIM | - | NULL | - |
| 9 | api_cliente_nome | varchar(50) | SIM | - | NULL | - |
| 10 | api_faturar | varchar(255) | SIM | - | NULL | - |
| 11 | api_status | varchar(255) | SIM | - | NULL | - |
| 12 | api_app_name | varchar(50) | SIM | - | NULL | - |
| 13 | api_data_hora_venda | timestamp | SIM | - | NULL | - |
| 14 | desconto_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 15 | desconto_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 16 | acrescimo_valor | decimal(15,4) | NAO | - | 0.0000 | - |
| 17 | acrescimo_percentual | decimal(15,2) | NAO | - | 0.00 | - |
| 18 | percentual_comissao_venda | decimal(15,2) | NAO | - | 0.00 | - |
| 19 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 20 | updated_at | timestamp | SIM | - | NULL | - |
| 21 | deleted_at | timestamp | SIM | - | NULL | - |
| 22 | api_guid | varchar(50) | NAO | - | NULL | - |
| 23 | api_data_hora_lancamento | timestamp | SIM | - | NULL | - |
| 24 | api_device_id | varchar(100) | NAO | - | NULL | - |
| 25 | cancelada | tinyint(1) | NAO | - | 0 | - |
| 26 | usuario_lancamento_id | int unsigned | SIM | - | NULL | - |
| 27 | bloqueada | smallint | NAO | - | 0 | - |
| 28 | parent_guid | varchar(50) | SIM | - | NULL | - |
| 29 | usuario_cancelamento_id | int unsigned | SIM | - | NULL | - |
| 30 | data_hora_cancelamento | datetime | SIM | - | NULL | - |
| 31 | numero_documento | varchar(255) | SIM | - | NULL | - |
| 32 | numero_caixa | varchar(20) | SIM | - | NULL | - |
| 33 | tipo_preco_id | int unsigned | SIM | - | NULL | - |
| 34 | integracao_delivery | varchar(50) | SIM | - | NULL | - |
| 35 | entregador_id | int | SIM | - | NULL | - |
| 36 | assistencia_id | int unsigned | SIM | - | NULL | - |
| 37 | caixa_funcoes_id | int | SIM | - | NULL | - |
| 38 | indicador_id | int | SIM | - | NULL | - |
| 39 | marketplace_pedido_id | int | SIM | - | NULL | - |
| 40 | atendente_mesa | varchar(255) | SIM | - | NULL | - |
| 41 | comissao_entregador | decimal(15,2) | SIM | - | NULL | - |
| 42 | comissao_indicador | decimal(15,2) | SIM | - | NULL | - |
| 43 | numero_mesa | varchar(255) | SIM | - | NULL | - |
| 44 | numero_comanda | varchar(255) | SIM | - | NULL | - |
| 45 | origem_venda | varchar(255) | SIM | - | NULL | - |
| 46 | quantidade_pessoas | int | SIM | - | NULL | - |
| 47 | quantidade_comandas | int | SIM | - | NULL | - |
| 48 | tipo_lancamento | varchar(50) | NAO | - | VENDA | - |
| 49 | orcamento_id | int | SIM | - | NULL | - |
| 50 | orcamento_competencia | date | SIM | - | NULL | - |
| 51 | numero_pre_venda | varchar(50) | SIM | - | NULL | - |
| 52 | cliente_nome | varchar(255) | NAO | - | NULL | - |
| 53 | cliente_tipo_cliente_id | int | NAO | - | NULL | - |
| 54 | vendedor_nome | varchar(255) | NAO | - | NULL | - |
| 55 | venda_empresa_nome | varchar(50) | NAO | - | NULL | - |
| 56 | venda_empresa_nome_fantasia | varchar(255) | NAO | - | NULL | - |
| 57 | venda_empresa_razao_social | varchar(255) | NAO | - | NULL | - |
| 58 | tipo_comissao | enum('PRODUTO','VENDEDOR') | NAO | - | VENDEDOR | - |
| 59 | venda_item_id | int | NAO | - | 0 | - |
| 60 | produto_empresa_grade_id | int | NAO | - | NULL | - |
| 61 | produto_venda_quantidade | decimal(15,4) | NAO | - | 1.0000 | - |
| 62 | produto_venda_preco | decimal(15,4) | NAO | - | 0.0000 | - |
| 63 | comissao | decimal(15,2) | SIM | - | 0.00 | - |
| 64 | desconto_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 65 | acrescimo_valor_item | decimal(15,4) | NAO | - | 0.0000 | - |
| 66 | item_cancelado | timestamp | SIM | - | NULL | - |
| 67 | atendente_item | int | SIM | - | NULL | - |
| 68 | comissao_atendente | decimal(15,2) | SIM | - | NULL | - |
| 69 | comissao_carta_produto | decimal(15,4) | SIM | - | NULL | - |
| 70 | comissao_carta_produto_tipo | enum('VALOR','PERCENTUAL') | SIM | - | PERCENTUAL | - |
| 71 | cobrar_taxa_servico | tinyint | SIM | - | NULL | - |
| 72 | data_venda | date | SIM | - | NULL | - |
| 73 | data_hora_venda | datetime | SIM | - | NULL | - |
| 74 | caixa_data | date | SIM | - | NULL | - |
| 75 | turno | tinyint unsigned | SIM | - | NULL | - |
| 76 | operador_id | int unsigned | SIM | - | NULL | - |
| 77 | indicador_nome | varchar(255) | SIM | - | NULL | - |
| 78 | produto_id | int | SIM | - | 0 | - |
| 79 | produto_nome | varchar(255) | SIM | - | NULL | - |
| 80 | produto_tipo_produto | varchar(50) | SIM | - | PRODUTO | - |
| 81 | produto_servico | int | SIM | - | NULL | - |
| 82 | produto_nome_completo | varchar(511) | SIM | - | NULL | - |
| 83 | produto_grade_descricao | varchar(255) | SIM | - | NULL | - |
| 84 | produto_grade_estoque | decimal(15,4) | SIM | - | 0.0000 | - |
| 85 | produto_empresa_id | int | SIM | - | NULL | - |
| 86 | produto_grade_deleted_at | timestamp | SIM | - | NULL | - |
| 87 | grupo_id | int | SIM | - | 0 | - |
| 88 | grupo_nome | varchar(255) | SIM | - | NULL | - |
| 89 | fabricante_id | int | SIM | - | 0 | - |
| 90 | fabricante_nome | varchar(50) | SIM | - | NULL | - |
| 91 | mes_venda | varchar(2) | SIM | - | NULL | - |
| 92 | ano_venda | varchar(4) | SIM | - | NULL | - |
| 93 | mes_ano_venda | varchar(7) | SIM | - | NULL | - |
| 94 | item_total | decimal(31,4) | SIM | - | NULL | - |
| 95 | item_total_real | decimal(33,4) | SIM | - | NULL | - |
| 96 | item_total_compra | decimal(31,4) | SIM | - | NULL | - |
| 97 | item_total_lucro | decimal(34,4) | SIM | - | NULL | - |
| 98 | item_total_desconto | decimal(25,4) | SIM | - | NULL | - |
| 99 | item_total_acrescimo | decimal(25,4) | SIM | - | NULL | - |

### Tabela: view_venda_financeiro (VIEW)
**Comentario:** VIEW
**Linhas aprox:** 0 | **Colunas:** 5

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | venda_id | int | SIM | - | NULL | - |
| 2 | valor_parcela | decimal(37,4) | SIM | - | NULL | - |
| 3 | valor_parcela_corrigido | decimal(37,4) | SIM | - | NULL | - |
| 4 | valor_pago | decimal(37,4) | NAO | - | 0.0000 | - |
| 5 | valor_pendente | decimal(38,4) | SIM | - | NULL | - |

### Tabela: vinculos_fiscais (BASE TABLE)
**Linhas aprox:** 8 | **Colunas:** 10

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | nome_vinculo | varchar(255) | NAO | - | NULL | - |
| 3 | tipo_item | varchar(255) | SIM | - | NULL | - |
| 4 | tipo_vinculo | enum('PRODUTO','SERVICO') | NAO | - | PRODUTO | - |
| 5 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 6 | updated_at | timestamp | SIM | - | NULL | - |
| 7 | deleted_at | timestamp | SIM | - | NULL | - |
| 8 | indicador_finalidade | varchar(1) | SIM | - | NULL | - |
| 9 | vinculo_padrao | tinyint(1) | NAO | - | 0 | - |
| 10 | vinculo_padrao_servico | tinyint(1) | NAO | - | 0 | - |

### Tabela: vinculos_fiscais_configuracoes (BASE TABLE)
**Linhas aprox:** 40 | **Colunas:** 58

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | vinculo_fiscal_id | int unsigned | NAO | - | NULL | - |
| 3 | grupo | varchar(255) | SIM | - | NULL | - |
| 4 | cfop_nfe_entrada | varchar(255) | SIM | - | NULL | - |
| 5 | cfop_nfce_saida | varchar(255) | SIM | MUL | NULL | - |
| 6 | cfop_nfe_saida | varchar(255) | SIM | MUL | NULL | - |
| 7 | cfop_nfce_entrada | varchar(255) | SIM | - | NULL | - |
| 8 | natureza | varchar(255) | SIM | - | NULL | - |
| 9 | uf_origem | enum('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | NAO | - | NULL | - |
| 10 | uf_destino | enum('TODAS','AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO') | SIM | - | TODAS | - |
| 11 | cst_csosn | varchar(255) | SIM | - | NULL | - |
| 12 | icms_modalidade_base | varchar(255) | SIM | - | NULL | - |
| 13 | icms_acrescimo | decimal(15,2) | SIM | - | 0.00 | - |
| 14 | icms_st_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 15 | icms_reducao | decimal(15,2) | SIM | - | 0.00 | - |
| 16 | icms_st_modalidade_base | varchar(255) | SIM | - | NULL | - |
| 17 | icms_st_mva | decimal(15,2) | SIM | - | 0.00 | - |
| 18 | icms_st_reducao | decimal(15,2) | SIM | - | 0.00 | - |
| 19 | ipi_saida | varchar(255) | SIM | - | NULL | - |
| 20 | ipi_saida_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 21 | ipi_saida_enquadramento | varchar(255) | SIM | - | NULL | - |
| 22 | pis_saida | varchar(255) | SIM | - | NULL | - |
| 23 | pis_saida_aliquota | decimal(16,3) | SIM | - | 0.000 | - |
| 24 | cofins_saida | varchar(255) | SIM | - | NULL | - |
| 25 | cofins_saida_aliquota | decimal(16,3) | SIM | - | 0.000 | - |
| 26 | icms_valor_pauta | decimal(15,2) | SIM | - | 0.00 | - |
| 27 | ipi_entrada | varchar(255) | SIM | - | NULL | - |
| 28 | ipi_entrada_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 29 | ipi_entrada_enquadramento | varchar(255) | SIM | - | NULL | - |
| 30 | pis_entrada | int | SIM | - | 0 | - |
| 31 | pis_entrada_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 32 | cofins_entrada | varchar(255) | SIM | - | NULL | - |
| 33 | cofins_entrada_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 34 | especifico | varchar(255) | SIM | - | NULL | - |
| 35 | nfe_natureza_operacao_texto_saida | text | SIM | - | NULL | - |
| 36 | nfce_natureza_operacao_texto_saida | text | SIM | - | NULL | - |
| 37 | icms_saida_origem | tinyint | SIM | - | NULL | - |
| 38 | icms_percentual_diferimento | decimal(5,2) | SIM | - | NULL | - |
| 39 | nfce_aliquota | decimal(15,2) | SIM | - | 0.00 | - |
| 40 | servico_iss_saida | decimal(15,2) | NAO | - | 0.00 | - |
| 41 | servico_csll_saida | decimal(15,2) | NAO | - | 0.00 | - |
| 42 | servico_inss_saida | decimal(15,2) | NAO | - | 0.00 | - |
| 43 | servico_ir_saida | decimal(15,2) | NAO | - | 0.00 | - |
| 44 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 45 | updated_at | timestamp | SIM | - | NULL | - |
| 46 | deleted_at | timestamp | SIM | - | NULL | - |
| 47 | regime_tributario | varchar(255) | SIM | - | NULL | - |
| 48 | modelo | int | NAO | - | 55 | - |
| 49 | icms_normal_aliquota | decimal(15,2) | NAO | - | 0.00 | - |
| 50 | icms_motivo_desoneracao | varchar(60) | SIM | - | NULL | - |
| 51 | icms_valor_desoneracao | decimal(13,2) | SIM | - | NULL | - |
| 52 | zerar_icms | smallint | NAO | - | 0 | - |
| 53 | ibs_cbs_cst | varchar(10) | SIM | - | NULL | - |
| 54 | ibs_cbs_cclass_trib | varchar(20) | SIM | - | NULL | - |
| 55 | ibs_aliquota | decimal(15,2) | SIM | - | NULL | - |
| 56 | cbs_aliquota | decimal(15,2) | SIM | - | NULL | - |
| 57 | ibs_cbs_cst_id | bigint unsigned | SIM | - | NULL | - |
| 58 | somar_ipi_icmsst_base | smallint | NAO | - | 0 | - |

### Tabela: vinculos_fiscais_ncm (BASE TABLE)
**Linhas aprox:** 7 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | vinculo_fiscal_id | int unsigned | NAO | MUL | NULL | - |
| 3 | ncm | varchar(20) | NAO | - | NULL | - |
| 4 | created_at | timestamp | SIM | - | NULL | - |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: vinculos_ncm (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 6

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | int unsigned | NAO | PRI | NULL | auto_increment |
| 2 | vinculo_id | int unsigned | NAO | - | NULL | - |
| 3 | ncm_codigo | int | NAO | - | NULL | - |
| 4 | created_at | timestamp | NAO | - | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| 5 | updated_at | timestamp | SIM | - | NULL | - |
| 6 | deleted_at | timestamp | SIM | - | NULL | - |

### Tabela: whatsapp_devices (BASE TABLE)
**Linhas aprox:** 0 | **Colunas:** 8

| # | Coluna | Tipo | Nulo | Chave | Padrao | Extra |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | id | bigint unsigned | NAO | PRI | NULL | auto_increment |
| 2 | device_id | varchar(255) | NAO | - | NULL | - |
| 3 | status | varchar(255) | NAO | - | connecting | - |
| 4 | last_updated_at | timestamp | NAO | - | NULL | - |
| 5 | data | text | SIM | - | NULL | - |
| 6 | created_at | timestamp | SIM | - | NULL | - |
| 7 | updated_at | timestamp | SIM | - | NULL | - |
| 8 | deleted_at | timestamp | SIM | - | NULL | - |

