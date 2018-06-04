import cnab240.core.header_arquivo as ha
import cnab240.core.header_lote as hl
import cnab240.core.trailer_arquivo as ta
import cnab240.core.segmento_a as sega

def generate(odict_entrada):

    
    str_header = ha.header_arquivo( odict_entrada['header_arquivo'] )    
    str_header_lote = hl.header_lote( odict_entrada['header_lote'] )

    list_segmento_a = []
    for conta in odict_entrada['segmento_a_contas']:
        odic_sega = sega.default()


        odic_sega['favorecido_banco'] = conta['banco'] #P002
        odic_sega['favorecido_conta_corrente_agencia_codigo'] = conta['agencia'] #G008    
        odic_sega['favorecido_conta_corrente_conta_numero'] = conta['conta'] #G010
        odic_sega['favorecido_conta_corrente_conta_dv'] = conta['conta_dv'] #G011    
        odic_sega['favorecido_nome'] = conta['favorecido_nome'] #G013

        odic_sega['credito_data_pagamento'] = conta['data_pagamento'] #P009
        odic_sega['valor_pagamento'] = conta['valor_centavos'] #P010
        print (odic_sega )
        exit()
        list_segmento_a.append( sega.parse(odic_sega) )

    str_segmento = '\n'.join(list_segmento_a)
    #str_trailer = ta.trailer_arquivo( odict_entrada['trailer_arquivo'])
    _str = str_header+"\n"+str_header_lote+str_segmento

    return _str
  