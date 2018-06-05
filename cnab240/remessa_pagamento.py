import cnab240.core.header_arquivo as ha
import cnab240.core.header_lote as hl
import cnab240.core.trailer_arquivo as ta
import cnab240.core.segmento_a as sega
import cnab240.core.trailer_lote as tl

def generate(odict_entrada):

    lote = '1'
    odict_entrada['header_arquivo']['lote'] = lote
    odict_entrada['header_lote']['lote'] = lote
    
    str_header = ha.header_arquivo( odict_entrada['header_arquivo'] )    
    str_header_lote = hl.header_lote( odict_entrada['header_lote'] )

    list_segmento_a = []
    somatoria_de_valores = 0 #inicial 0 centavos - #P0007
    sequencial_registro = 0
    for conta in odict_entrada['segmento_a_contas']:
        odic_sega = sega.default()

        odic_sega['lote'] = lote
        odic_sega['sequencial_registro_lote'] = str( sequencial_registro )
        odic_sega['favorecido_banco'] = conta['banco'] #P002
        odic_sega['favorecido_conta_corrente_agencia_codigo'] = conta['agencia'] #G008    
        odic_sega['favorecido_conta_corrente_conta_numero'] = conta['conta'] #G010
        odic_sega['favorecido_conta_corrente_conta_dv'] = conta['conta_dv'] #G011    
        odic_sega['favorecido_nome'] = conta['favorecido_nome'] #G013

        odic_sega['credito_data_pagamento'] = conta['data_pagamento'] #P009
        odic_sega['valor_pagamento'] = str(conta['valor_centavos']) #P010
       
        list_segmento_a.append( sega.parse(odic_sega) )
        sequencial_registro = sequencial_registro + 1
        somatoria_de_valores = somatoria_de_valores + conta['valor_centavos']
    

    odic_trailer_lote = tl.default()
    odic_trailer_lote['lote'] = lote
    odic_trailer_lote['somatoria_valores'] = somatoria_de_valores

    str_trailer_lote = tl.parse( odic_trailer_lote )


    odic_trailer = ta.default()
    odic_trailer['lote'] = lote
    #1 obrigatorio do header do arquivo
    #soma 1 obrigatorio do header do lote
    #soma 1 obrigatorio do trailer do lote
    #soma 1 obrigatorio do trailer do arquivo
    #soma sequencial do segmento a
    odic_trailer['quantidade_registros'] = 1 + 1 + 1 + 1 + sequencial_registro

    str_trailer_arquivo = ta.parse(odic_trailer)

    str_segmento = '\r\n'.join(list_segmento_a)
    #str_trailer = ta.trailer_arquivo( odict_entrada['trailer_arquivo'])
    _str = str_header+"\r\n"+str_header_lote+'\r\n'+str_segmento+'\r\n'+str_trailer_lote+'\r\n'+str_trailer_arquivo

    return _str
  