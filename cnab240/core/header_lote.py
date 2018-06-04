import collections

def header_lote(dic_lote):

    #merge
    merged_dict = dic_lote# default_header_arquivo().update( dic_header )
    header_str = '{:<3.3}{:<3.4}{:<1.1}{:<1.1}{:<2.2}{:<2.2}{:<3.3}{:<1.1}{:<1.1}{:<14.14}{:<20.20}{:<5.5}{:<1.1}{:<12.12}{:<1.1}{:<1.1}{:<30.30}{:<40.40}{:<30.30}{:<5.5}{:<15.15}{:<20.20}{:<5.5}{:<3.3}{:<2.2}{:<2.2}{:<6.6}{:<10.10}'
    
    return header_str.format(*merged_dict.values())

def default_header_lote():
    
    odict = collections.OrderedDict()

    odict['banco'] = '237'
    odict['lote'] = '0000'
    odict['registro'] = '1' #tipo de registro #G003
    odict['operacao'] = 'C' #tipo da operacao #G028
    odict['servico'] = '' #tipo do servico #G025
    odict['forma_lancamento'] = '' #tipo do servico #G029 --01
    odict['versao_layout_lote'] = '045' #tipo do servico #G030
    odict['cnab_081'] = ''
    odict['empresa_inscricao_tipo'] ='1'
    odict['empresa_inscricao_numero'] =''
    odict['empresa_convenio'] =''
    
    odict['empresa_conta_corrente_agencia_codigo'] =''
    odict['empresa_conta_corrente_agencia_dv'] =''
    odict['empresa_conta_corrente_conta_numero'] =''
    odict['empresa_conta_corrente_conta_dv'] =''
    odict['empresa_conta_corrente_digito_verificador'] =''    
    odict['empresa_nome'] =''
    odict['mensagem'] =''

    odict['empresa_endereco_logradouro'] =''
    odict['empresa_endereco_numero'] =''
    odict['empresa_endereco_complemento'] =''
    odict['empresa_endereco_cidade'] =''
    odict['empresa_endereco_cep'] =''
    odict['empresa_endereco_cep_complemento'] =''
    odict['empresa_endereco_estado'] =''
    odict['indicativo_forma_pagamento_servico'] = '01' #P014
    odict['cnab_271'] = '' #G004
    odict['codigo_ocorrencias_retorno'] = '' #G059

    return odict