import sys

import algoritmoOtimo as otm
import conjuntoDeTrabalho as ct
import segundaChance as sc


def OpenFile():
    arquivo = sys.stdin
    try:
        dados = arquivo.readlines()
        return dados
    except:
        print('Arquivo não encontrado!')
        exit(0)

dados = OpenFile()

falta_sc = sc.SegundaChance(dados)
falta_otm = otm.AlgoritmoOtimo(dados)
falta_ct = ct.ConjuntoDeTrabalho(dados)

print('SC %d' %(falta_sc))
print('OTM %d' %(falta_otm))
print('CT %d' %(falta_ct))
