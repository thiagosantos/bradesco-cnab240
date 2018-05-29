import collections

def header_arquivo(dic_header):

    #merge
    merged_dict = dic_header# default_header_arquivo().update( dic_header )
    header_str = '{:>3.3}{:>3.4}{:>1.1}{:>9.9}{:>1.1}{:>14.14}{:>20.20}{:>5.5}{:>1.1}{:>12.12}{:>1.1}{:>1.1}{:>30.30}{:>30.30}{:>10.10}{:>1.1}{:>8.8}{:>6.6}{:>6.6}{:>3.3}{:>5.5}{:>20.20}{:>20.20}{:>29.29}'
    
    return header_str.format(*merged_dict.values())

def default_header_arquivo():
    
    odict = collections.OrderedDict()

    odict['banco'] = '237'
    odict['lote'] = '0000'
    odict['registro'] = '2'
    odict['cnab_04'] = '         ' 
    odict['empresa_inscricao_tipo'] ='1'
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
    odict['arquivo_codigo'] ='' #código de remessa,
    odict['arquivo_data_geracao'] =''
    odict['arquivo_hora_geracao'] =''
    odict['arquivo_nsa'] ='000001'
    odict['arquivo_layout'] ='089'
    odict['arquivo_densidade'] =''                
    odict['reservado_banco'] =''
    odict['reservado_empresa'] =''
    odict['cnab_24'] =''    

    return odict


    

