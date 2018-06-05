import collections

def parse(dic_lote):

    #merge
    merged_dict = dic_lote# default_header_arquivo().update( dic_header )
    header_str = '{:<3.3}{:0>4.4}{:<1.1}{:0>5.5}{:<1.1}{:<1.1}{:<2.2}{:<3.3}{:<3.3}{:0>5.5}{:<1.1}{:0>12.12}{:<1.1}{:<1.1}{:<30.30}{:<20.20}{:<8.8}{:<3.3}{:0>15.15}{:0>15.15}{:<20.20}{:<8.8}{:<15.15}{:<40.40}{:<2.2}{:<5.5}{:<2.2}{:<3.3}{:<1.1}{:<10.10}'
    
    return header_str.format(*merged_dict.values())

def default():

    odict = collections.OrderedDict()
    

    odict['banco'] = '237' #G001
    odict['lote'] = '' #G002
    odict['registro'] = '3' #G003
    odict['sequencial_registro_lote'] = '1' #G038
    odict['codigo_segmento_registro_detalhe'] = 'A' #G039
    odict['servico_movimento_tipo'] = '0' #G060 - 0 inclusao, 1 consulta, 3 estorno, 5 alteracao, 7 liquidacao, 9 exclusao
    odict['servico_movimento_codigo'] = '00' #G061 - 00 inclusao de registro detalhe liberado
    odict['favorecido_camara'] = '018' #P001 - 018 TED (STR, CIP), 700 DOC (COMPE) e 888 - TED (STR/CIP) *mais info no P001
    odict['favorecido_banco'] = '000' #P002
    odict['favorecido_conta_corrente_agencia_codigo'] = '' #G008
    odict['favorecido_conta_corrente_agencia_dv'] = '' #G009
    odict['favorecido_conta_corrente_conta_numero'] = '' #G010
    odict['favorecido_conta_corrente_conta_dv'] = '' #G011
    odict['favorecido_conta_corrente_dv'] = '' #G012
    odict['favorecido_nome'] = '' #G013

    odict['credito_seu_numero'] = '' #G064 - numero atribuido pela empresa para esse registro de pagamento
    odict['credito_data_pagamento'] = '' #P009
    odict['credito_tipo_moeda'] = 'BRL' #G040
    odict['credito_quantidade_moeda'] = '' #G041
    odict['valor_pagamento'] = '' #P010
    odict['credito_nosso_numero'] = '' #G043

    odict['credito_data_real'] = '' #P003 - preenchido somente no arquivo de retorno
    odict['credito_valor_real'] = '' #P004 - preenchido somente no arquivo de retorno

    odict['informacao2'] = '' #P031
    odict['codigo_finalidade_doc'] = ''
    odict['codigo_finalidade_ted'] = ''
    odict['codigo_finalidade_complementar'] = ''
    odict['cnab_283a'] = ''
    odict['aviso'] = '0' #P006 - 0 nao emite aviso,'2' emite aviso somente remetente, '5' emite aviso somente ao favorecido, 
                         #'6' emite aviso favorecido e remetente, '7' emite aviso ao favorecido e duas vias para o remetente
    odict['ocorrencias'] = ''

    return odict