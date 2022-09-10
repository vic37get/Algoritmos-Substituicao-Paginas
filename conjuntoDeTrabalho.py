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


def ConjuntoDeTrabalho(dados):
    dados = TratamentoArquivo(dados)
    qtdMolduras = dados[0]
    limiar = (qtdMolduras/2)+1
    referencias = dados[1:]
    instante = 0
    molduras = []
    tempoVirtualAtual = 0
    bitRPaginas = [0 for i in range(qtdMolduras)]

    for indice, referencia in enumerate(referencias):
        if indice %4 == 0:
            bitRPaginas =  [0 for i in range(qtdMolduras)]

        if referencia not in molduras:
            falta_paginas+=1

        if len(molduras) == qtdMolduras:
            #implementar o conj de trabalho, tempo virtual atual
            pass
        molduras.append(referencia)
        bitRPaginas[len(molduras)-1] = indice




    return



dados = OpenFile()
falta_pagina = ConjuntoDeTrabalho(dados)
print('CT %d' %(falta_pagina))
