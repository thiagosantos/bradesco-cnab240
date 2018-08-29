import argparse
import json
import os

import collections
import cnab240.core.header_arquivo as ha
import cnab240.remessa_pagamento as rp




def check_conf(conf):
    conf_file = "./cnab240/confs/"+conf+".prod.conf"
    if(not os.path.isfile(conf_file)):
        print ("Arquivo de configuracao passado não encontrado")
        return False

    arquivo_json = open(conf_file,"r")

    return json.load(arquivo_json)

def generate(conf=None, arquivo_processamento=None):

    conf_json = check_conf(conf)
    if( conf_json == False ):
        return

    print (conf_json)



parser = argparse.ArgumentParser()
parser.add_argument("-c", "--conf", help="nome do arquivo de configuracao antes do '.prod.conf'")
parser.add_argument("-a", "--arquivo", help="caminho do arquivo de entrada que será usado para processamento")
parser.add_argument("-d", "--driver", help="driver para tratar o arquivo de entrada", default="csv")
args = parser.parse_args()

if not args.conf:
    print ("Arquivo de configuracao é obrigatório")
    exit()

if not args.arquivo:
    print ("Arquivo de entrada é obrigatório")    
    exit()

generate(args.conf, args.arquivo)


#bla = dict()
#bla['header_arquivo'] = ha.default_header_arquivo()
#print ( rp.generate(bla) )