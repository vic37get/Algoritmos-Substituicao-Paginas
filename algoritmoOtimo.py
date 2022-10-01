#IMPLEMENTAÇÃO DO ALGORITMO ÓTIMO
import copy

import numpy as np


def TratamentoArquivo(arquivo):
    dados = copy.deepcopy(arquivo)
    for linha in range(len(dados)):
        dados[linha] = dados[linha].replace('\r\n','')
        dados[linha] = int(dados[linha])
    return dados

#Retorna a página que demorará mais para ser referenciada novamente.
def PaginaComMaiorRotulo(indicepag, paginas, referencias):
    #Tempos das páginas sendo setados para -1
    tempos = [-1 for i in range(len(paginas))]
    #Percorrendo as páginas
    for indice, pagina in enumerate(paginas):
        #Percorrendo as referencias, da proxima referencia até a ultima.
        for referencia in range(indicepag+1, len(referencias)):
            #Se a referencia não é a página
            if referencias[referencia] != pagina:
                #Incremento no tempo para ela ser refernciada novamente.
                tempos[indice]+=1
            #Se for a página, apenas volta.
            else:
                break
    #Retorna o indice da pagina que vai demorar mais tempo para ser referenciada.
    maiorTempo = np.argmax(tempos)
    #Pagina mais demorada
    pagMaisDemorada = paginas[maiorTempo]
    
    return pagMaisDemorada

def AlgoritmoOtimo(dados):
    dados = TratamentoArquivo(dados)
    #Faltas de páginas.
    falta_paginas = 0
    #Quantidade de molduras
    qntd_molduras = dados[0]
    #Sequencia de referências feitas às páginas de memória.
    referencias = dados[1:]
    #Moldura de páginas
    moldura = []    #[PAGINA]

    for indice, referencia in enumerate(referencias):
        #Se a referencia não está na moldura.
        if referencia not in moldura:
            falta_paginas+=1
            #Se a moldura estiver cheia.
            if len(moldura) == qntd_molduras:
                #Obtém a página que vai demorar mais para ser referenciada novamente.
                pagMaiorRotulo = PaginaComMaiorRotulo(indice, moldura, referencias)
                #Remove a página
                moldura.remove(pagMaiorRotulo)
            #Adiciona a nova referência de página na moldura
            moldura.append(referencia)
        #Se a página já estiver na moldura
        else:
            continue

    return falta_paginas

##################
#Passo a passo

def AlgoritmoOtimoPassoApasso(dados):
    print('\n---Algoritmo Ótimo---\n')
    dados = TratamentoArquivo(dados)
    #Faltas de páginas.
    falta_paginas = 0
    #Quantidade de molduras
    qntd_molduras = dados[0]
    #Sequencia de referências feitas às páginas de memória.
    referencias = dados[1:]
    #Moldura de páginas
    moldura = []    #[PAGINA]

    for indice, referencia in enumerate(referencias):
        print('--- Referência: {} ---\n'.format(referencia))
        #Se a referencia não está na moldura.
        if referencia not in moldura:
            print('A referencia {} não está na moldura: {}'.format(referencia, moldura))
            falta_paginas+=1
            #Se a moldura estiver cheia.
            if len(moldura) == qntd_molduras:
                print('\nA moldura está cheia: {}\n'.format(moldura))
                #Obtém a página que vai demorar mais para ser referenciada novamente.
                pagMaiorRotulo = PaginaComMaiorRotulo(indice, moldura, referencias)
                print('Próximas referências: {}'.format(referencias[indice+1:]))
                print('A pagina com maior rótulo é: {}'.format(pagMaiorRotulo))
                #Remove a página
                moldura.remove(pagMaiorRotulo)
                print('A pagina com maior rotulo foi removida! Moldura: {}'.format(moldura))
            #Adiciona a nova referência de página na moldura
            moldura.append(referencia)
            print('Referencia {} adicionada!'.format(referencia))
            print('Moldura após adicionar a referencia {}: {}'.format(referencia,moldura))
        #Se a página já estiver na moldura
        else:
            print('A referencia {} já está na moldura: {}'.format(referencia, moldura))
        print('\nFaltas de páginas: ', falta_paginas)
        print('\n********************************************************\n')

    return falta_paginas
