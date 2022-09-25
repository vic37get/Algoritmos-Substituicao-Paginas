import numpy as np


def TratamentoArquivo(arquivo):
    for linha in range(len(arquivo)):
        #arquivo[linha] = arquivo[linha].replace('\r\n','')
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
    print('\n---Algoritmo Ótimo---\n')
    dados = TratamentoArquivo(dados)
    #Faltas de páginas.
    falta_paginas = 0
    #Quantidade de molduras
    qntd_molduras = dados[0]
    #Sequencia de referências feitas às páginas de memória.
    referencias = dados[1:]
    #Moldura de páginas
    moldura = []    #[PROCESSO, BIT R, ULTIMO USO]

    for indice, referencia in enumerate(referencias):
        print('A referencia {} chegou'.format(referencia))
        if referencia not in moldura:
            print('A referencia {} não está na moldura: {}'.format(referencia, moldura))
            falta_paginas+=1
            print('Falta de páginas: {}'.format(falta_paginas))
            if len(moldura) == qntd_molduras:
                print('O número de páginas é igual a quantidade de molduras!!')
                print('Moldura: {}'.format(moldura))
                pagMaiorRotulo = PaginaComMaiorRotulo(indice, moldura, referencias)
                print('A pagina com maior rótulo é: {}'.format(pagMaiorRotulo))
                moldura.remove(pagMaiorRotulo)
                print('A pagina com maior rotulo foi removida! Moldura: {}'.format(moldura))
            moldura.append(referencia)
            print('A referencia {} foi adicionada!'.format(referencia))
            print('Moldura após adicionar a referencia {}: {}'.format(referencia,moldura))
        else:
            print('A referencia {} já estava na moldura!'.format(referencia))
        print('\n')
    return falta_paginas
