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

def ReferenciaMaisAntiga(moldura):
    return np.argmin(moldura)

def SegundaChance(dados):
    dados = TratamentoArquivo(dados)
    falta_paginas = 0
    #Quantidade de molduras de páginas na RAM.
    qntd_molduras = dados[0]
    #Sequencia de referências feitas às páginas de memória.
    referencias = dados[1:]
    #Paginas
    paginas = []
    #Bit de referencia das páginas
    bitRPaginas = [float('inf') for i in range(qntd_molduras)]
    
    for indice, referencia in enumerate(referencias):
        if indice %4 == 0:
            bitRPaginas =  [float('inf') for i in range(qntd_molduras)]

        if referencia not in paginas:
            falta_paginas+=1

        if len(paginas) == qntd_molduras:
            del paginas[ReferenciaMaisAntiga(bitRPaginas)]
        paginas.append(referencia)
        bitRPaginas[len(paginas)-1] = indice
    
    return falta_paginas

dados = OpenFile()
falta_pagina = SegundaChance(dados)
print('SC %d' %(falta_pagina))
