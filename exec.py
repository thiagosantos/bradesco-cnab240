import argparse
import json
import os
import importlib

import collections
import cnab240.drivers as drivers
import cnab240.core.header_arquivo as ha
import cnab240.core.header_lote as hl
import cnab240.remessa_pagamento as rp


def check_conf(conf):
    """Verifica se o conf passado por parametro existe. Existindo retorna o conf, caso contrario retorna False.
    
    Keyword arguments:
    conf -- nome do arquivo de configuracao sem o ".prod.conf"
    """

    conf_file = "./cnab240/confs/"+conf+".prod.conf"
    if(not os.path.isfile(conf_file)):
        print ("Arquivo de configuracao passado não encontrado")
        return False

    return json.load(open(conf_file,"r"))



def generate(conf=None, arquivo_processamento=None, driver=None):
    """Organiza e gera a partir dos parametros enviados o arquivo de remessa.
    
    Keyword arguments:
    conf -- nome do arquivo de configuracao sem o ".prod.conf"    
    arquivo_processamento -- caminho para o arquivo que será processado
    driver -- driver que será utilizado para a leitura correta do arquivo_processamento (csv, default)
    """

    conf_json = check_conf(conf)
    if( conf_json == False ):
        return

    odict_ha = ha.default_header_arquivo()    
    odict_hl = hl.default_header_lote()
    
    #vamos iterar sobre o conf_json e alimentar o odict_ha e o odict_hl
    for indice in conf_json.keys():
        if(indice in odict_ha.keys()) :
            odict_ha[ indice ] = conf_json[ indice ]
        
        if( indice in odict_hl.keys() ):
            odict_hl[ indice ] = conf_json[ indice ]
    
    #vamos fazer a leitura das contas
    #carregamento automatico do modulo
    try:
        modname = "cnab240.drivers."+driver
        module = importlib.import_module( modname )
        contas = module.exec( arquivo_processamento )      

    except Exception as e:
        #Caso nao consiga carregar o modulo
        print ("Driver '"+driver+"' não encontrado")
        return


    bla = dict()
    bla['header_arquivo'] = odict_ha
    bla['header_lote'] = odict_hl
    bla['segmento_a_contas'] = contas

    #manda processar
    print ( rp.generate(bla), end='' ) 

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--conf",     help="nome do arquivo de configuracao antes do '.prod.conf'")
parser.add_argument("-a", "--arquivo",  help="caminho do arquivo de entrada que será usado para processamento")
parser.add_argument("-d", "--driver",   help="driver para tratar o arquivo de entrada", default="csv")
parser.add_argument("-l", "--list",     help="combinado com qualquer outro argumento lista os confs, drivers disponiveis e arquivo passado", default=None)
args = parser.parse_args()


#imprimir a lista de configuracoes, drivers e arquivo passado por parametro
#if args.list:
#    if parser.print_help
#    exit()

if not args.conf:
    print ("Arquivo de configuracao é obrigatório")
    exit()

if not args.arquivo:
    print ("Arquivo de entrada é obrigatório")    
    exit()


generate(args.conf, args.arquivo, args.driver)



