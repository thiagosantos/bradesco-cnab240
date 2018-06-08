import collections
from datetime import datetime 

def header_arquivo(dic_header):

    #merge
    merged_dict = dic_header# default_header_arquivo().update( dic_header )
    header_str = '{:<3.3}{:0>4.4}{:<1.1}{:<9.9}{:<1.1}{:0>14.14}{:<20.20}{:0>5.5}{:0<1.1}{:0>12.12}{:<1.1}{:<1.1}{:<30.30}{:<30.30}{:<10.10}{:0>1.1}{:0>8.8}{:0>6.6}{:0>6.6}{:0>3.3}{:0>5.5}{:<20.20}{:<20.20}{:<29.29}'
    
    return header_str.format(*merged_dict.values())

def default_header_arquivo():
    
    odict = collections.OrderedDict()
    datetime_now = datetime.now()

    odict['banco'] = '237' #G001
    odict['lote'] = '0000' #G002
    odict['registro'] = '0' #G003
    odict['cnab_04'] = '         ' 
    odict['empresa_inscricao_tipo'] ='2' #1 Pessoa Fisica, 2 Pessoa Juridica
    odict['empresa_inscricao_numero'] =''
    odict['empresa_convenio'] =''
    odict['empresa_conta_corrente_agencia'] = ''
    odict['empresa_conta_corrente_agencia_codigo'] =''
    odict['empresa_conta_corrente_agencia_dv'] =''
    odict['empresa_conta_corrente_conta_numero'] =''
    odict['empresa_conta_corrente_conta_dv'] =''
    odict['empresa_nome'] =''
    odict['nome_banco'] =''
    odict['cnab_15'] = '          '
    odict['arquivo_codigo'] ='1' #código de remessa 1 (cliente banco), retorno 2 (banco cliente)
    odict['arquivo_data_geracao'] = datetime_now.strftime("%d%m%Y")
    odict['arquivo_hora_geracao'] = datetime_now.strftime("%H%M%f")
    odict['arquivo_nsa'] ='000001'
    odict['arquivo_layout'] ='089'
    odict['arquivo_densidade'] ='01600'                
    odict['reservado_banco'] =''
    odict['reservado_empresa'] =''
    odict['cnab_24'] =''    


    

    return odict


    

