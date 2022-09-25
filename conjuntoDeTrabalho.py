#IMPLEMENTAÇÃO DO CONJUNTO DE TRABALHO

def TratamentoArquivo(arquivo):
    for linha in range(len(arquivo)):
        arquivo[linha] = arquivo[linha].replace('\r\n','')
        arquivo[linha] = int(arquivo[linha])
    return arquivo


def PagForaConjTrabalho(moldura, limiar, tempoVirtualAtual):
    tempo_min = float('inf')
    listaPagMaisAntiga = []
    for pag in range(0, len(moldura)):
        if moldura[pag][1] == True:
            moldura[pag][2] = tempoVirtualAtual
        else:
            idadePag = tempoVirtualAtual - moldura[pag][2]
            if idadePag > limiar:
                return moldura[pag]
            else:
                listaPagMaisAntiga.append(moldura[pag])
    for pagina in range(0, len(listaPagMaisAntiga)):
        if listaPagMaisAntiga[pagina][2] < tempo_min:
            tempo_min = listaPagMaisAntiga[pagina][2]
            pagAntiga = listaPagMaisAntiga[pagina]

    return pagAntiga

def AtualizaReferencia(moldura, referencias, refAtual):
    for pag in range(0,len(moldura)):
        if moldura[pag][0] == referencias[refAtual]:
            moldura[pag][1] = True
            moldura[pag][2] = refAtual
    return


def ConjuntoDeTrabalho(dados):
    print('\n--Algoritmo Conjunto de Trabalho--\n')
    dados = TratamentoArquivo(dados)
    #Quantidade de molduras de páginas na RAM.
    qntd_molduras = dados[0]
    #Limiar
    limiar = (qntd_molduras/2)+1
    #Sequencia de referências feitas às páginas de memória.
    referencias = dados[1:]
    #Faltas de páginas.
    faltasPagina = 0
    #Moldura de páginas
    moldura = []    #[PROCESSO, BIT R, ULTIMO USO]

    for ref in range(0, len(referencias)):
        print('REFERENCIA: ',referencias[ref])
        print('MOLDURA: ', moldura)
        if ref % 4 == 0 and ref != 0:
            for indice in range(0, len(moldura)):
                moldura[indice][1] = False
            print('ZERANDO BITR: ', moldura)

        if len(moldura) < qntd_molduras:
            adicionados = [mold[0] for mold in moldura]
            print('ADICIONADOS NA MOLDURA: ',adicionados)
            if referencias[ref] not in adicionados:
                moldura.append([referencias[ref], True, ref])
                faltasPagina +=1
                print('MOLDURA APOS ADIÇÃO: ', moldura)
            else:
                print('JA ESTÁ NA MOLDURA: ', moldura)
                AtualizaReferencia(moldura, referencias, ref)
                print('APOS ATUALIZAÇÃO DA MOLDURA: ', moldura)
        else:
            print('TAMANHO DA MOLDURA TA NO MAXIMO: ', moldura)
            adicionados = [mold[0] for mold in moldura]
            print('ADICIONADOS NA MOLDURA: ',adicionados)
            if referencias[ref] not in adicionados:
                fora_conj = PagForaConjTrabalho(moldura, limiar, ref)
                print('MOLDURA FORA DO CONJ DE TRABALHO: ', fora_conj)
                moldura.remove(fora_conj)
                print('REMOVENDO ESSA MOLDURA: ', moldura)
                moldura.append([referencias[ref], True, ref])
                print('ADICIONANDO A MOLDURA NOVA: ', moldura)
                faltasPagina+=1
            else:
                print('JA ESTÁ NA MOLDURA: ', moldura)
                AtualizaReferencia(moldura, referencias, ref)
                print('APOS ATUALIZAÇÃO DA MOLDURA: ', moldura)

    return faltasPagina


