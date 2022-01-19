# Faça um programa que leia NOME e PESO de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) Uma listagem com as pessoas mais pesadas;
# C) Uma listagem com as pessoas mais leves.

'''
temp = list()  # Lista temporária
cadastro = list()
pesados = []
leves = []
c = 0

while True:
    temp.append(input('Nome da pessoa: '))
    temp.append(int(input('Peso da pessoa: ')))
    cadastro.append(temp.copy())
    c += 1
    temp.clear()

    resp = input('Gostaria de continuar cadastrando pessoas? [s/n] ')
    if resp in 'Nn':
        break

for p in cadastro:
    if p[1] >= 90:
        pesados.append(p)
    elif p[1] <= 75:
        leves.append(p)

print(f'Total de pessoas cadastradas: {c}')
print(f'Lista completa: {cadastro}')
print(f'Lista dos mais pesados: {pesados}')
print(f'Lista dos mais leves: {leves} ')
'''

'''
pessoas = [[], []]
c = 0

while True:
    nome = input('Digite um nome: ')
    peso = float(input(f'Digite o peso de {nome}: '))
    if peso >= 100:
        pessoas[0].append(nome)
        pessoas[0].append(peso)
    elif peso <= 75:
        pessoas[1].append(nome)
        pessoas[1].append(peso)
    c += 1
    resp = input('Gostaria de continuar cadastrando pessoas? ')
    if resp in 'Nn':
        break

print(f'Total de pessoas cadastradas: {c}')

print('Pessoas mais pesadas: ', end='')
print(*pessoas[0], sep=', ')
print(f'Pessoas mais leves: ', end='')
print(*pessoas[1], sep=', ')
'''

temp = []
princ = list()
c = 0

while True:
    temp.append(input('Digite um nome: '))
    temp.append(float(input('Digite um peso: ')))
    princ.append(temp.copy())
    temp.clear()
    c += 1

    resp = input('Quer continuar? ')
    if resp in 'Nn':
        break

print(f'Total de pessoas cadastradas: {c}')

print('As pessoas mais pesadas da lista são: ', end='')
for p in princ:
    if p[1] >= 100:
        print(p, end=', ')

print()

print('As pessoas mais leves da lista são: ', end='')
for p in princ:
    if p[1] <= 75:
        print(p, end=', ')




