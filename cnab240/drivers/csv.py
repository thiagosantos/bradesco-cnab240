import csv
import os

def exec (arquivo_entrada):

    contas = []
    arquivo_csv = open(arquivo_entrada, "r")
    sreader = csv.reader(arquivo_csv, delimiter=';', quotechar='"')
    for row in sreader:

        contas.append({
            'banco':row[0],
            'agencia':row[1],
            'agencia_dv':row[2],
            'conta':row[3],
            'conta_dv':row[4],
            'favorecido_nome':row[5],
            'valor_centavos':int(row[6]),
            'data_pagamento':row[7],
            'cpf':row[8]
        })

    return contas