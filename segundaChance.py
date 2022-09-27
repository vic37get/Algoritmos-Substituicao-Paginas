
def TratamentoArquivo(arquivo):
    for linha in range(len(arquivo)):
        arquivo[linha] = int(arquivo[linha])
    return arquivo

#Retorna a referencia mais antiga da moldura
def ReferenciaMaisAntiga(moldura):
    for pag in range(0,len(moldura)):
        if moldura[pag][1] == True:
            posicoes = [mold[2] for mold in moldura]
            proximo = max(posicoes)
            moldura[pag][1] = False
            moldura[pag][2] = proximo+1
        else:
            return moldura[pag]
    return moldura[0]

#Atualiza o BITR da página para True
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
        print('--- Referência: {} ---\n'.format(referencia))
        #Zerar os BITR das páginas a cada 4 referencias a memória
        if indice %4 == 0 and indice != 0:
            print('--Quatro referências á memória!--\n')
            #Zerando BITR
            for pg in range(0, len(moldura)):
                moldura[pg][1] = False
            print('Zerando BITR... {}\n'.format(moldura))
        #Se a moldura ainda tem espaço.
        if len(moldura) < qntd_molduras:
            #Já adicionados na moldura.
            adicionados = [mold[0] for mold in moldura]
            print('Moldura: ', adicionados)
            #Se a referencia não está na moldura.
            if referencia not in adicionados:
                falta_paginas+=1
                print('Essa referência não está na moldura: ', moldura)
                #Referencia adicionada na moldura.
                moldura.append([referencia, True, indice])
                print('Moldura após a inserção da página: ', moldura)
            else:
                print('Essa referência já está na moldura: ', moldura)
                #Atualização do BITR da página para True
                AtualizaReferencia(moldura, referencias, indice)
                print('Apos atualização da moldura: ', moldura)

        #Se a moldura estiver cheia
        else:
            adicionados = [mold[0] for mold in moldura]
            #Se a referencia não estiver na moldura.
            if referencia not in adicionados:
                print('Moldura está cheia: ', moldura)
                falta_paginas+=1
                #Retorna a referencia mais antiga com BITR = False
                ref_antiga = ReferenciaMaisAntiga(moldura)
                #Reordenando a moldura pela posição na fila.
                moldura.sort(key = lambda moldura: moldura[2])
                print('Referência mais antiga: ', ref_antiga)
                #Removendo a referencia mais antiga.
                moldura.remove(ref_antiga)
                print('Após remover a referência mais antiga: ', moldura)
                posicoes = [mold[2] for mold in moldura]
                proximo = max(posicoes)
                #Adicionando a nova referência na ultima posição da fila.
                moldura.append([referencia, True, proximo+1])
                print('Moldura após a inserção da página: ', moldura)
            else:
                print('Essa referência já está na moldura: ', moldura)
                #Atualização do BITR da página para True
                AtualizaReferencia(moldura, referencias, indice)
                print('Após a atualização da moldura: ', moldura)
        print('\nFaltas de páginas: ', falta_paginas)
        print('\n********************************************************\n')
        
    return falta_paginas
