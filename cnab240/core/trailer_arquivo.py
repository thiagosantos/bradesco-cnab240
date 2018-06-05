import collections
import cnab240.core.util as util

def parse(dic_trailer):

    odict = util.merge( default(), dic_trailer) #default_trailer_arquivo().update(dic_trailer)

    trailer_str = '{:0>3.3}{:0>4.4}{:0>1.1}{:>9.9}{:0>6.6}{:0>6.6}{:0>6.6}{:<205.205}'

    return trailer_str.format(*odict.values())

def default():
    
    odict = collections.OrderedDict()

    odict['banco'] = '237'
    odict['lote'] = '0000'
    odict['registro'] = '9'
    odict['cnab_049'] = '' #nove espacos em branco
    odict['quantidade_lotes']  = '1' #G049
    odict['quantidade_registros']  = '000000' #G056 - soma dos registros do tipo 0,1,3,5,9
    odict['quantidade_contas_conciliacao']  = '0'  #G037 - nada de consciliacao bancaria por agora
    odict['cnab_089'] = '' #205 espacos em branco

    return odict