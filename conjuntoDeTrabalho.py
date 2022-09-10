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
    qntd_molduras = dados[0]
    limiar = (qntd_molduras/2)+1
    referencias = dados[1:]
    falta_paginas = 0
    moldura = []#[PROCESSO, BIT R, ULTIMO USO]

    for indice, processo in enumerate(referencias):
        if (indice%4 == 0 and indice != 0): #se tiver sido 4 referencias a memória entao coloca o bit R de cada processo da moldura para False
            for k in moldura:
                k[1] = False
        if len(moldura) < qntd_molduras :#se a moldura tiver com vaga so add o processo
            try:#verifica se o processo já foi adicionado, se tiver sido, nao faz nada
                indiceNaMoldura = list(np.array(moldura)[:,0]).index(processo)
                print(processo)
                print(moldura)
                print(indiceNaMoldura)
                moldura[indiceNaMoldura][1] = True
                moldura[indiceNaMoldura][2] = indice+1
            except (ValueError, IndexError):
                moldura.append([processo,True,indice+1])#salva o processo, o bit de referencia e o tempo virtual atual
                falta_paginas+=1
        else:
            try:#ve se o processo está na com o status de bit R True alem de atualiza o tempo virtual atual do processo
                indiceNaMoldura = list(np.array(moldura)[:,0]).index(processo) #pega o indice do processo na moldura
                moldura[indiceNaMoldura][1] = True
                moldura[indiceNaMoldura][2] = indice+1
            except ValueError:#se nao tiver na moldura, entao será escolhido algum com o BIT R = 0
                indicesMolduraAux = []#irá guardar as paginas da moldura que devem ser deletadas
                for i in range(len(moldura)):
                    idade = moldura[i][2]
                    if (moldura[i][1] == False) and (idade > limiar):
                        indicesMolduraAux.append(moldura[i][0])
                    elif (moldura[i][1] == False) and (idade <= limiar):
                        moldura[i][0] = processo
                        moldura[i][1] = True
                        moldura[i][2] = indice + 1
                        falta_paginas+=1
                for i in indicesMolduraAux:#Exclui as paginas que possui a idade maior que o limiar
                    indiceNaMoldura = list(np.array(moldura)[:,0]).index(i)
                    del(moldura[indiceNaMoldura])#deleta o processo da moldura

                try:#verifica se o processo entrou na moldura, em alguma das ocasiÕes acima
                    list(np.array(moldura)[:,0]).index(processo)
                except:#se o processo não está na moldura depois disso td, entao adiciona
                    moldura.append([processo,True,indice+1])#salva o processo, o bit de referencia e o tempo virtual atual
                    falta_paginas+=1
    return falta_paginas



dados = OpenFile()
falta_pagina = ConjuntoDeTrabalho(dados)
print('CT %d' %(falta_pagina))
