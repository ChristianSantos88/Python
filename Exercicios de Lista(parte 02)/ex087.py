# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados;
# B) A soma dos valores da terceira coluna;
# C) O maior valor da segunda linha.

matriz = []
temp = []
cont = 1
pos = 0

while cont <= 3:
    for m in range(0, 3):
        temp.append(int(input('Digite um valor: ')))
    matriz.append(temp.copy())
    cont += 1
    temp.clear()

for m in range(0, len(matriz)):
    print(f'[{matriz[m][pos]}]', end=' ')
    pos += 1











'''
matriz = list()
coluna3 = []
cont = 0
soma = soma_col3 = 0

for e in range(0, 3):
    for m in range(0, 3):
        matriz.append(int(input(f'Digite um valor para [{e+1},{m+1}]: ')))

for m in range(2, len(matriz), 3):
    soma_col3 += matriz[m]

print()

for m in range(0, len(matriz)):
    print(f'[{matriz[m]:^5}]', end=' ')
    cont += 1
    if cont == 3:
        print()
        cont = 0

    if matriz[m] % 2 == 0:
        soma += matriz[m]

print(f'A soma dos valores pares digitados é igual a: {soma}')
print(f'A soma dos valores da terceira coluna é igual a: {soma_col3}')
'''




