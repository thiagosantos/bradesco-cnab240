import cnab240.core.header_arquivo as ha
import cnab240.core.header_lote as hl
import cnab240.core.trailer_arquivo as ta

def generate(odict_entrada):

    
    str_header = ha.header_arquivo( odict_entrada['header_arquivo'] )    
    str_header_lote = hl.header_lote( odict_entrada['header_lote'] )
    #str_trailer = ta.trailer_arquivo( odict_entrada['trailer_arquivo'])
    _str = str_header+"\n"+str_header_lote

    return _str
  