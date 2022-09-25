import numpy as np


def TratamentoArquivo(arquivo):
    for linha in range(len(arquivo)):
        #arquivo[linha] = arquivo[linha].replace('\r\n','')
        arquivo[linha] = int(arquivo[linha])
    return arquivo

def ReferenciaMaisAntiga(moldura, refAtual):
    naoReferenciadas = []
    tempo_min = float('inf')
    moldura = (sorted(moldura, key = lambda x: x[2]))
    
    for pag in range(0,len(moldura)):
        if moldura[pag][1] == True:
            moldura[pag][1] = False
            moldura[pag][2] = refAtual 
        else:
            naoReferenciadas.append(moldura[pag])

    for pagina in naoReferenciadas:
        if pagina[2] < tempo_min:
            tempo_min = pagina[2]
            pagAntiga = pagina
    
    return pagAntiga

def AtualizaReferencia(moldura, referencias, refAtual):
    for pag in range(0,len(moldura)):
        if moldura[pag][0] == referencias[refAtual]:
            moldura[pag][1] = True
    return

def SegundaChance(dados):
    print('\n--Algoritmo Segunda chance--\n')
    dados = TratamentoArquivo(dados)
    falta_paginas = 0
    #Quantidade de molduras de páginas na RAM.
    qntd_molduras = dados[0]
    #Sequencia de referências feitas às páginas de memória.
    referencias = dados[1:]
    #Moldura de páginas
    moldura = []    #[PROCESSO, BIT R, ULTIMO USO]
    
    for indice, referencia in enumerate(referencias):
        print('Referencia: ', referencia)
        if indice %4 == 0 and indice != 0:
            print('Quatro referencias á memória!')
            for pg in range(0, len(moldura)):
                moldura[pg][1] = False
            print('Zerando BITR: ', moldura)
        
        if len(moldura) < qntd_molduras:
            adicionados = [mold[0] for mold in moldura]
            print('Adicionados: ',adicionados)
            if referencia not in adicionados:
                falta_paginas+=1
                print('Referencia nao está na moldura: ', moldura)
                moldura.append([referencia, True, indice])
                print('Moldura após inserção da página: ', moldura)
            else:
                print('Já está na moldura: ', moldura)
                AtualizaReferencia(moldura, referencias, indice)
                print('Apos atualização da moldura: ', moldura)

        else:
            print('Moldura está cheia: ', moldura)
            adicionados = [mold[0] for mold in moldura]
            print('Adicionados: ',adicionados)
            if referencia not in adicionados:
                falta_paginas+=1
                ref_antiga = ReferenciaMaisAntiga(moldura, indice)
                print('Referencia mais antiga: ', ref_antiga)
                moldura.remove(ref_antiga)
                print('Apos remover a referencia mais antiga: ', moldura)
                moldura.append([referencia, True, indice])
                print('Apos atualização da moldura: ', moldura)
            else:
                print('Já está na moldura: ', moldura)
                AtualizaReferencia(moldura, referencias, indice)
                print('Apos atualização da moldura: ', moldura)
        print('Falta Paginas: ', falta_paginas)
        
    return falta_paginas
