import collections
import cnab240.core.header_arquivo as ha
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
odict['arquivo_data_geracao'] =''
odict['arquivo_hora_geracao'] =''
odict['arquivo_nsa'] ='000001'
odict['arquivo_layout'] ='089'
odict['arquivo_densidade'] =''                
odict['reservado_banco'] =''
odict['reservado_empresa'] =''
odict['cnab_24'] =''   


bla = dict()
bla['header_arquivo'] = odict

print ( rp.generate(bla) ) 
 
 