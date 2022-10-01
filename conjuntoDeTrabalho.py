#IMPLEMENTAÇÃO DO CONJUNTO DE TRABALHO
import copy


def TratamentoArquivo(arquivo):
    dados = copy.deepcopy(arquivo)
    for linha in range(len(dados)):
        dados[linha] = dados[linha].replace('\r\n','')
        dados[linha] = int(dados[linha])
    return dados

#Ordena a moldura pelo instante do ultimo uso das páginas.
def OrdenaMoldura(moldura):
    return moldura.sort(key = lambda moldura: moldura[2])

#Busca a página que está fora do conjunto de trabalho.
def PagForaConjTrabalho(moldura, limiar, tempoVirtualAtual):
    for pag in range(0, len(moldura)):
        if moldura[pag][1] == True:
            moldura[pag][2] = tempoVirtualAtual
        else:
            idadePag = tempoVirtualAtual - moldura[pag][2]
            if idadePag > limiar:
                return moldura[pag]

    return moldura[0]

#Atualiza os dados da página quando referenciada, BITR e instante de ultimo uso.
def AtualizaReferencia(moldura, referencias, refAtual):
    for pag in range(0,len(moldura)):
        if moldura[pag][0] == referencias[refAtual]:
            moldura[pag][1] = True
            moldura[pag][2] = refAtual
    return

def ConjuntoDeTrabalho(dados):
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
    moldura = []    #[PAGINA, BIT R, ULTIMO USO]
    for ref in range(0, len(referencias)):
        #Zerar os BITR das páginas a cada 4 referencias a memória
        if ref % 4 == 0 and ref != 0:
            #Zerando BITR
            for indice in range(0, len(moldura)):
                moldura[indice][1] = False
        #Se a moldura ainda tem espaço.
        if len(moldura) < qntd_molduras:
            #Já adicionados na moldura.
            adicionados = [mold[0] for mold in moldura]
            #Se a pagina não está na moldura.
            if referencias[ref] not in adicionados:
                #Referencia adicionada na moldura.
                moldura.append([referencias[ref], True, ref])
                faltasPagina +=1
            #Se a pagina já está na moldura
            else:
                #Atualização do BITR da página para True e do instante do ultimo uso.
                AtualizaReferencia(moldura, referencias, ref)
                #Ordena a moldura pelo instante do ultimo uso das páginas.
                OrdenaMoldura(moldura)
        else:
            adicionados = [mold[0] for mold in moldura]
            #Se a pagina não está na moldura.
            if referencias[ref] not in adicionados:
                #Busca a página que está fora do conjunto de trabalho.
                fora_conj = PagForaConjTrabalho(moldura, limiar, ref)
                #Remove a página.
                moldura.remove(fora_conj)
                #Adiciona a nova página.
                moldura.append([referencias[ref], True, ref])
                faltasPagina+=1
            #Se a página já estiver na moldura.
            else:
                #Atualização do BITR da página para True e do instante do ultimo uso.
                AtualizaReferencia(moldura, referencias, ref)
                #Ordena a moldura pelo instante do ultimo uso das páginas.
                OrdenaMoldura(moldura)

    return faltasPagina

############
#Passo a passo

def ConjuntoDeTrabalhoPassoApasso(dados):
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
    moldura = []    #[PAGINA, BIT R, ULTIMO USO]
    print('Limiar: {}\n'.format(limiar))
    print('********************************************************\n')
    for ref in range(0, len(referencias)):
        print('--- Referência: {} ---\n'.format(referencias[ref]))
        print('- Instante {}\n'.format(ref))
        #Zerar os BITR das páginas a cada 4 referencias a memória
        if ref % 4 == 0 and ref != 0:
            print('--Quatro referências á memória!--\n')
            #Zerando BITR
            for indice in range(0, len(moldura)):
                moldura[indice][1] = False
            print('Zerando BITR... {}\n'.format(moldura))
        #Se a moldura ainda tem espaço.
        if len(moldura) < qntd_molduras:
            #Já adicionados na moldura.
            adicionados = [mold[0] for mold in moldura]
            #Se a pagina não está na moldura.
            if referencias[ref] not in adicionados:
                print('A referencia {} não está na moldura: {}'.format(referencias[ref], moldura))
                #Referencia adicionada na moldura.
                moldura.append([referencias[ref], True, ref])
                faltasPagina +=1
                print('Moldura após a inserção da página: ', moldura)
            #Se a pagina já está na moldura
            else:
                print('A referencia {} já está na moldura: {}'.format(referencias[ref], moldura))
                #Atualização do BITR da página para True e do instante do ultimo uso.
                AtualizaReferencia(moldura, referencias, ref)
                #Ordena a moldura pelo instante do ultimo uso das páginas.
                OrdenaMoldura(moldura)
                print('Apos atualização da moldura: ', moldura)
        else:
            adicionados = [mold[0] for mold in moldura]
            #Se a pagina não está na moldura.
            if referencias[ref] not in adicionados:
                print('\nA moldura está cheia: {}\n'.format(moldura))
                #Busca a página que está fora do conjunto de trabalho.
                fora_conj = PagForaConjTrabalho(moldura, limiar, ref)
                print('Página fora do conjunto de trabalho: ', fora_conj)
                #Remove a página.
                moldura.remove(fora_conj)
                print('Após remover a página: ', moldura)
                #Adiciona a nova página.
                moldura.append([referencias[ref], True, ref])
                print('Moldura após a inserção da página: ', moldura)
                faltasPagina+=1
            #Se a página já estiver na moldura.
            else:
                print('A referencia {} já está na moldura: {}'.format(referencias[ref], moldura))
                #Atualização do BITR da página para True e do instante do ultimo uso.
                AtualizaReferencia(moldura, referencias, ref)
                #Ordena a moldura pelo instante do ultimo uso das páginas.
                OrdenaMoldura(moldura)
                print('Após atualização da moldura: ', moldura)
        print('\nFaltas de páginas: ', faltasPagina)
        print('\n********************************************************\n')

    return faltasPagina


