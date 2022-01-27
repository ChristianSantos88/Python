# Crie um programa que crie uma MATRIZ de dimensão 3x3 e preencha com os valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# Dessa forma:
# [1][2][3]
# [4][5][6]
# [7][8][9]

temp = []
matriz = []
cont = 0

for e in range(0, 3):
    for m in range(0, 3):
        matriz.append(int(input(f'Digite um valor para [{e + 1},{m + 1}]: ')))

for m in range(0, len(matriz)):
    print(f'[{matriz[m]:^5}]', end=' ')
    cont += 1
    if cont == 3:
        print()
        cont = 0
