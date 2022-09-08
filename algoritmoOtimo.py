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
    dados = TratamentoArquivo(dados)
    falta_paginas = 0
    qntd_molduras = dados[0]
    referencias = dados[1:]
    paginas = []

    for indice, referencia in enumerate(referencias):
        if referencia not in paginas:
            falta_paginas+=1
        if len(paginas) == qntd_molduras:
            pagMaiorRotulo = PaginaComMaiorRotulo(indice, paginas, referencias)
            print(referencia, pagMaiorRotulo)
            paginas.remove(pagMaiorRotulo)
        
        paginas.append(referencia)
    
    return falta_paginas


def PaginaComMaiorRotulo(indicepag, paginas, referencias):
    tempos = [-1 for i in range(len(paginas))]
    for indice, pagina in enumerate(paginas):
        for referencia in range(indicepag+1, len(referencias)):
            if referencias[referencia] != pagina:
                tempos[indice]+=1
            else:
                break
    maiorTempo = np.argmax(tempos)
    pagMaisDemorada = paginas[maiorTempo]
    
    return pagMaisDemorada

dados = OpenFile()
falta_pagina = AlgoritmoOtimo(dados)
print('OTM %d' %(falta_pagina))
