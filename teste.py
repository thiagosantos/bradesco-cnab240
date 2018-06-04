import collections
import cnab240.core.header_arquivo as ha
import cnab240.core.header_lote as hl
import cnab240.remessa_pagamento as rp


odict = ha.default_header_arquivo()
odict['banco'] = '237'
odict['lote'] = '0000'
odict['registro'] = '4'
odict['cnab_04'] = '' 
odict['empresa_inscricao_tipo'] ='1'
odict['empresa_inscricao_numero'] ='31449358000120'
odict['empresa_convenio'] ='335220'
odict['empresa_conta_corrente_agencia'] = '279'
odict['empresa_conta_corrente_agencia_codigo'] ='8'
odict['empresa_conta_corrente_agencia_dv'] ='8572'
odict['empresa_conta_corrente_conta_numero'] ='3'
odict['empresa_conta_corrente_conta_dv'] =''
odict['empresa_nome'] ='MK PUBLICITA PRODUCOES PUBLICIDADE E PROPAGANDA LTDA'
odict['nome_banco'] ='BRADESCO S/A'
odict['cnab_15'] = '          '
odict['arquivo_codigo'] ='' #código de remessa,
odict['arquivo_nsa'] ='000001'
odict['arquivo_layout'] ='089'
odict['arquivo_densidade'] =''                
odict['reservado_banco'] =''
odict['reservado_empresa'] =''
odict['cnab_24'] =''   

odict_hl = hl.default_header_lote()
odict_hl['empresa_inscricao_tipo'] ='1'
odict_hl['empresa_inscricao_numero'] ='31449358000120'
odict_hl['empresa_convenio'] ='335220'

odict_hl['empresa_conta_corrente_agencia_numero'] ='279'
odict_hl['empresa_conta_corrente_agencia_dv'] ='8'
odict_hl['empresa_conta_corrente_conta_numero'] ='8572'
odict_hl['empresa_conta_corrente_conta_dv'] ='3'
odict_hl['empresa_conta_corrente_digito_verificador'] =''   

odict_hl['empresa_nome'] ='MK PUBLICITA PRODUCOES PUBLICIDADE E PROPAGANDA LTDA'

odict_hl['empresa_endereco_logradouro'] ='RUA GOTEMBURGO'
odict_hl['empresa_endereco_numero'] ='211'
odict_hl['empresa_endereco_complemento'] =''
odict_hl['empresa_endereco_cidade'] ='RIO DE JANEIRO'
odict_hl['empresa_endereco_cep'] ='20941'
odict_hl['empresa_endereco_cep_complemento'] ='080'
odict_hl['empresa_endereco_estado'] ='RJ'

bla = dict()
bla['header_arquivo'] = odict
bla['header_lote'] = odict_hl

print ( rp.generate(bla) ) 
 
 