import collections
import cnab240.core.header_arquivo as ha
import cnab240.remessa_pagamento as rp



bla = dict()
bla['header_arquivo'] = ha.default_header_arquivo()

print ( rp.generate(bla) )