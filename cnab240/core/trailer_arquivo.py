import collections

def trailer_arquivo(dic_trailer):

    odict = default_trailer_arquivo().update(dic_trailer)

    trailer_str = '{:>3.3}{:>4.4}{:>1.1}{:>9.9}{:>6.6}{:>6.6}{:>6.6}{:>205.205}'

    return trailer_str.format(*odict.values())

def default_trailer_arquivo():
    
    odict = collections.OrderedDict()

    odict['banco'] = '237'
    odict['lote'] = '0000'
    odict['registro'] = '2'
    odict['cnab_04'] = '         '
    odict['quantidade_lotes']  = '000000'
    odict['quantidade_registros']  = '000000'
    odict['quantidade_contas_conciliacao']  = '000000'

    return odict