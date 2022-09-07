import sys

import numpy as np


def OpenFile():
    arquivo = sys.stdin
    try:
        dados = arquivo.readlines()
        return dados
    except:
        print('Arquivo não encontrado!')
        exit(0)

def TratamentoArquivo(arquivo):
    for linha in range(len(arquivo)):
        arquivo[linha] = arquivo[linha].replace('\r\n','')
        arquivo[linha] = int(arquivo[linha])
    return arquivo

def AlgoritmoOtimo(dados):
    return
