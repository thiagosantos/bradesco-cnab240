import collections
import cnab240.core.util as util

def parse(dic_trailer):

    odict = util.merge( default(), dic_trailer) #default_trailer_arquivo().update(dic_trailer)

    trailer_str = '{:0>3.3}{:0>4.4}{:0>1.1}{:>9.9}{:0>6.6}{:0>18.18}{:0>18.18}{:0>6.6}{:<165.165}{:<10.10}'

    return trailer_str.format(*odict.values())

def default():
    
    odict = collections.OrderedDict()

    odict['banco'] = '237'
    odict['lote'] = '0000'
    odict['registro'] = '5'
    odict['cnab_045'] = '' #nove espacos em branco
    odict['quantidade_registro_lote']  = '1' #G049
    odict['somatoria_valores']  = '0' #P007
    odict['somatoria_quantidade_moeda_valores']  = '0' #G058
    odict['numero_aviso_debito']  = '0' #G066    
    odict['cnab_095'] = '' #165 espacos em branco #G004
    odict['codigo_ocorrencia_retorno']  = '' #G058

    return odict