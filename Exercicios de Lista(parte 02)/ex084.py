# Faça um programa que leia NOME e PESO de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) Uma listagem com as pessoas mais pesadas;
# C) Uma listagem com as pessoas mais leves.

pessoas = []
pesados = []
leves = []
mais_pesado = 0
mais_leve = 0
cadastrados = 0

while True:
    nome = input('Nome: ')
    peso = float(input(f'Peso de {nome}: '))
    pessoas.append(nome)
    pessoas.append(peso)

    if cadastrados == 0:
        mais_pesado = peso
        mais_leve = peso
    elif peso > mais_pesado:
        mais_pesado = peso
    elif peso < mais_leve:
        mais_leve = peso

    if peso >= 100:
        pesados.append(pessoas[:])

    elif peso <= 70:
        leves.append(pessoas[:])

    cadastrados += 1

    pessoas.clear()

    perg = input('Continuar? ')
    if perg == 'n':
        break


print(f'Total de pessoas cadastradas: {cadastrados}')

print(f'O maior peso foi de {mais_pesado}. Peso de: ', end='')
for p in range(0, len(pesados)):
    if pesados[p][1] == mais_pesado:
        print(f'[{pesados[p][0]}]', end=' ')

print(f'\nO menor peso foi de {mais_leve}. Peso de: ', end='')
for p in range(0, len(leves)):
    if leves[p][1] == mais_leve:
        print(f'[{leves[p][0]}]', end=' ')








