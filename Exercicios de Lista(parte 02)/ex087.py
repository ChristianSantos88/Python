# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados;
# B) A soma dos valores da terceira coluna;
# C) O maior valor da segunda linha.


matriz = []
temp = []
cont = line = 1
pos = soma = soma_col3 = maior_valor = 0

#  Inserindo os elementos na matriz
while cont <= 3:
    for col in range(0, 3):
        temp.append(int(input(f'Digite um valor para [{line},{col + 1}]: ')))
    matriz.append(temp.copy())
    cont += 1
    line += 1
    temp.clear()

#  Lendo a matriz
for line in range(0, 3):
    soma_col3 += matriz[line][2]
    print()
    for col in range(0, 3):
        print(f'[{matriz[line][col]:^5}]', end=' ')
        if matriz[line][col] % 2 == 0:
            soma += matriz[line][col]

print()

# soma de todos os valores pares digitados
print(f'\nSoma dos elementos pares: {soma}')

# soma dos valores da terceira coluna
print(f'\nSoma dos elementos da terceira coluna: {soma_col3}')

# maior valor da segunda linha
for m in matriz[1]:
    if m > maior_valor:
        maior_valor = m
print(f'\nMaior valor da segunda linha: {maior_valor}')

'''
for m in range(0, len(matriz)):
    print(f'[{matriz[m][pos]}]', end=' ')
    pos += 1
'''

'''
matriz = list()
temp = list()
coluna3 = []
cont = 0
soma = soma_col3 = 0

#  Inserindo os valores na matriz
for e in range(0, 3):
    for m in range(0, 3):
        temp.append(int(input(f'Digite um valor para [{e+1},{m+1}]: ')))

#  Lendo a matriz
for line in range(0, 3):
    print()
    for col in range(0, 3):
        print(f'[{matriz[line]}]', end=' ')

print()
print(matriz)

for m in range(2, len(matriz), 3):
    soma_col3 += matriz[m]

print()

#  for m in range(0, len(matriz)):
#   print(f'[{matriz[m]:^5}]', end=' ')
#   cont += 1
#   if cont == 3:
#       print()
#       cont = 0

#   if matriz[m] % 2 == 0:
#       soma += matriz[m]

print(f'A soma dos valores pares digitados é igual a: {soma}')
print(f'A soma dos valores da terceira coluna é igual a: {soma_col3}')
'''




