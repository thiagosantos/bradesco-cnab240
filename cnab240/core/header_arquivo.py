import collections

def header_arquivo(dic_header):

    #@todo fazer o merge da entrada com o dicionario ordenado default
    merged_dict = default_header_arquivo()
   
    header_str = '{:.3}'
    header_str = header_str+ '{:.4}'
    header_str = header_str+ '{:.1}'
    header_str = header_str+ '{:.9}'
    header_str = header_str+ '{:.1}'
    header_str = header_str+ '{:.14}'
    header_str = header_str+ '{:.20}'
    header_str = header_str+ '{:.5}'
    header_str = header_str+ '{:.1}'
    header_str = header_str+ '{:.12}'
    header_str = header_str+ '{:.1}'
    header_str = header_str+ '{:.1}'
    header_str = header_str+ '{:.30}'
    header_str = header_str+ '{:.30}'
    header_str = header_str+ '{:.10}'
    header_str = header_str+ '{:.1}'
    header_str = header_str+ '{:.8}'
    header_str = header_str+ '{:.6}'
    header_str = header_str+ '{:.6}'
    header_str = header_str+ '{:.3}'
    header_str = header_str+ '{:.5}'
    header_str = header_str+ '{:.20}'
    header_str = header_str+ '{:.20}'
    header_str = header_str+ '{:.29}'

    header_str = header_str.format(*merged_dict.values())


    return header_str


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


    

