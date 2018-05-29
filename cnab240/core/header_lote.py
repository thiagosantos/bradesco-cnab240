import collections

def header_lote(dic_lote):

    #merge
    merged_dict = dic_header# default_header_arquivo().update( dic_header )
    header_str = '{:>3.3}{:>3.4}{:>1.1}{:>1.1}{:>2.2}{:>2.2}{:>3.3}{:>1.1}{:>1.1}{:>14.14}{:>20.20}{:>5.5}{:>1.1}{:>12.12}{:>1.1}{:>1.1}{:>30.30}{:>40.40}{:>30.30}{:>5.5}{:>15.15}{:>20.20}{:>5.5}{:>3.3}{:>2.2}{:>2.2}{:>6.6}{:>10.10}'
    
    return header_str.format(*merged_dict.values())

def default_header_arquivo():
    
    odict = collections.OrderedDict()

    odict['banco'] = '237'
    odict['lote'] = '0000'
    odict['registro'] = '1' #tipo de registro
    odict['operacao'] = '0000' #tipo da operacao
    odict['servico'] = '' #tipo da operacao