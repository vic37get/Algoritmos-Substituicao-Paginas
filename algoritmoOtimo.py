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

def AlgoritmoOtimo(dados):
    dados = TratamentoArquivo(dados)
    falta_paginas = 0
    qntd_molduras = dados[0]
    referencias = dados[1:]
    paginas = []

    for indice, referencia in enumerate(referencias):
        print('A referencia {} chegou'.format(referencia))
        if referencia not in paginas:
            print('A referencia {} não está na moldura: {}'.format(referencia, paginas))
            falta_paginas+=1
            print('Falta de páginas: {}'.format(falta_paginas))
            if len(paginas) == qntd_molduras:
                print('O número de páginas é igual a quantidade de molduras!!')
                print('Moldura: {}'.format(paginas))
                pagMaiorRotulo = PaginaComMaiorRotulo(indice, paginas, referencias)
                print('A pagina com maior rótulo é: {}'.format(pagMaiorRotulo))
                paginas.remove(pagMaiorRotulo)
                print('A pagina com maior rotulo foi removida! Moldura: {}'.format(paginas))
            paginas.append(referencia)
            print('A referencia {} foi adicionada!'.format(referencia))
            print('Moldura após adicionar a referencia {}: {}'.format(referencia,paginas))
        else:
            print('A referencia {} já estava na moldura!'.format(referencia))
        print('\n')
    return falta_paginas

dados = OpenFile()
falta_pagina = AlgoritmoOtimo(dados)
print('OTM %d' %(falta_pagina))
