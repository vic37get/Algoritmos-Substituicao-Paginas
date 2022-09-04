# Implementação de Algoritmos de Substituição de Páginas :page_facing_up:

## Execução:
`python3 [nomeDoArquivo].py < entrada.txt`

## Funcionamento:
O programa lê da entrada padrão um conjunto de números inteiros onde o primeiro número representa a quantidade de molduras de página disponíveis na RAM e os demais representam a sequência de referências às páginas, sempre um número por linha.

O programa imprime na saída o número de faltas de páginas obtido com a utilização de cada um dos algoritmos.

## Entrada:
A entrada é composta por uma série números inteiros, um por linha, indicando, primeiro a quantidade de quadros disponíveis na memória RAM e, em seguida, a sequência de referências à memória.

### Exemplo de entrada:
4
1
2
3
4
1
2
5
1
2
3
4
5

## Saída
A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade de faltas de página obtidas com a utilização de cada um deles.
### Exemplo de saída:
Algoritmo | Faltas de páginas
-- | --
SC | 7
OTM | 6
CT | 8
