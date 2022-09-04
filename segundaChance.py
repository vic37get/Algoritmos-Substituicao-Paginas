import sys

import numpy as np
import pandas as pd


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

def SegundaChance(dados):
    dados = TratamentoArquivo(dados)
    falta_paginas = 0
    molduras = dados[0]
    referencias = dados[1:]
    quadros = []
    for referencia in referencias:
        if referencia not in quadros:
            falta_paginas+=1
        if len(quadros) == molduras:
            del quadros[0]
        quadros.append(referencia)
        print(quadros)
    return falta_paginas

dados = OpenFile()
miss = SegundaChance(dados)
print(miss)
