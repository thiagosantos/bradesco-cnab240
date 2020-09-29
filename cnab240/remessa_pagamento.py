from datetime import datetime
import cnab240.core.header_arquivo as ha
import cnab240.core.header_lote as hl
import cnab240.core.trailer_arquivo as ta
import cnab240.core.segmento_a as sega
import cnab240.core.segmento_b as segb
import cnab240.core.trailer_lote as tl

def generate(odict_entrada, codigo_banco=None):

    if(codigo_banco is None):
        print ("Código do banco é um campo obrigatorio")
        return None

    lote = '1'
    odict_entrada['header_lote']['lote'] = lote

    str_header = ha.header_arquivo( odict_entrada['header_arquivo'] )
    str_header_lote = hl.header_lote( odict_entrada['header_lote'] )

    list_segmento_a = []
    somatoria_de_valores = 0 #inicial 0 centavos - #P0007
    sequencial_registro = 0
    for conta in odict_entrada['segmento_a_contas']:
        odic_sega = sega.default()
        odic_sega['banco'] = codigo_banco
        odic_segb = segb.default()
        odic_segb['banco'] = codigo_banco

        odic_sega['lote'] = lote
        odic_sega['sequencial_registro_lote'] = str( sequencial_registro + 1 )
        odic_sega['favorecido_banco'] = conta['banco'] #P002
        odic_sega['favorecido_conta_corrente_agencia_codigo'] = conta['agencia'] #G008
        odic_sega['favorecido_conta_corrente_conta_numero'] = conta['conta'] #G010
        odic_sega['favorecido_conta_corrente_conta_dv'] = conta['conta_dv'] #G011
        odic_sega['favorecido_nome'] = conta['favorecido_nome'] #G013
        """
        Seu número crédito. 
        Número do documento atribuido pela empresa, serve para identificar o pagamento usando um
        identificador com 20 caracteres.
        Se o valor não for passado como parametro do arquivo de entrada, adotaremos o padrao a seguir:
        CPF (11 digitos) + ANO (com dois caracteres) + dia do ano (ex: 309, equivale a 5 de novembro para o ANO de 2018)
        + Hora (padrão 24 horas) + minutos (com dois digitos)

        00000000000 18 309 13 02
        00000000000183091302
        """
        seu_numero_complemento = str(datetime.now().strftime("%y")) + str( datetime.now().timetuple().tm_yday ) + str(datetime.now().strftime("%H%M"))
        if('credito_seu_numero' in conta.keys()):
            #forço ao limite de 20 caracteres para não atrapalhar a montagem dos arquivos
            odic_sega['credito_seu_numero'] = conta['credito_seu_numero'][0:20]
        else:
            odic_sega['credito_seu_numero'] = conta['cpf'] + seu_numero_complemento #G064

        odic_sega['credito_data_pagamento'] = conta['data_pagamento'] #P009
        odic_sega['valor_pagamento'] = str(conta['valor_centavos']) #P010

        #segmento b
        odic_segb['dados_complementares_favorecido_inscricao_tipo'] = '1' #G005
        odic_segb['dados_complementares_favorecido_inscricao_numero'] = conta['cpf'] #cpf ou cnpj


        #endereco da empresa
        odic_segb['lote'] = lote
        odic_segb['sequencial_registro_lote'] = str(sequencial_registro+2)
        odic_segb['dados_complementares_favorecido_logradouro'] = odict_entrada['header_lote']['empresa_endereco_logradouro'] #
        odic_segb['dados_complementares_favorecido_numero'] = odict_entrada['header_lote']['empresa_endereco_numero'] #
        odic_segb['dados_complementares_favorecido_complemento'] = odict_entrada['header_lote']['empresa_endereco_complemento'] #
        odic_segb['dados_complementares_favorecido_bairro'] = odict_entrada['header_lote']['empresa_endereco_bairro'] #
        odic_segb['dados_complementares_favorecido_cidade'] = odict_entrada['header_lote']['empresa_endereco_cidade'] #
        odic_segb['dados_complementares_favorecido_cep'] = odict_entrada['header_lote']['empresa_endereco_cep'] #
        odic_segb['dados_complementares_favorecido_cep_complemento'] = odict_entrada['header_lote']['empresa_endereco_cep_complemento'] #
        odic_segb['dados_complementares_favorecido_estado'] = odict_entrada['header_lote']['empresa_endereco_estado'] #

        list_segmento_a.append(sega.parse(odic_sega))
        list_segmento_a.append(segb.parse(odic_segb))

        sequencial_registro = sequencial_registro + 2
        somatoria_de_valores = somatoria_de_valores + conta['valor_centavos']


    odic_trailer_lote = tl.default()
    odic_trailer_lote['banco'] = codigo_banco
    odic_trailer_lote['lote'] = lote
    odic_trailer_lote['quantidade_registro_lote'] = sequencial_registro + 2 #1 para header do lote e 1 para trailer do lote
    odic_trailer_lote['somatoria_valores'] = somatoria_de_valores

    str_trailer_lote = tl.parse( odic_trailer_lote )


    odic_trailer_arquivo = ta.default()
    odic_trailer_arquivo['banco'] = codigo_banco
    odic_trailer_arquivo['lote'] = '9999'
    #1 obrigatorio do header do arquivo
    #soma 1 obrigatorio do header do lote
    #soma 1 obrigatorio do trailer do lote
    #soma 1 obrigatorio do trailer do arquivo
    #soma sequencial do segmento a
    odic_trailer_arquivo['quantidade_registros'] = 1 + 1 + 1 + 1 + sequencial_registro

    str_trailer_arquivo = ta.parse(odic_trailer_arquivo)

    str_segmento = '\r\n'.join(list_segmento_a)
    #str_trailer = ta.trailer_arquivo( odict_entrada['trailer_arquivo'])
    _str = str_header+"\r\n"+str_header_lote+'\r\n'+str_segmento+'\r\n'+str_trailer_lote+'\r\n'+str_trailer_arquivo

    return _str
  
