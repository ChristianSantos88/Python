# Crie um programa no qual o usuário possa digitar 07 valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem CRESCENTE.

'''
#numeros = list(int(input('Digite um valor: ')) for c in range(0, 3))
numeros = [[], []]

for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    if valor % 2 != 0:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f'Valores pares digitados: {numeros[0]}')
print(f'Valores ímpares digitados: {numeros[1]}')
'''

par_impar = [[], []]

for v in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par_impar[0].append(n)
    else:
        par_impar[1].append(n)

par_impar[0].sort()
par_impar[1].sort()

print(f'Valores pares digitados: {par_impar[0]}')
print(f'Valores ímpares digitados: {par_impar[1]}')

