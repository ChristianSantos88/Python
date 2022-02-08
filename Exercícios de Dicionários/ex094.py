# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas;
# b) A média de idade do grupo;
# c) Uma lista com todas as mulheres;
# d) Uma lista com todas as pessoas com idade acima da média.

pessoas = dict()
cadastrados = list()
mulheres = []
acima_media = []
cont = media = soma_idade = 0

while True:
    pessoas['Nome'] = input('Digite o nome: ')
    pessoas['Sexo'] = input(f'Sexo de {pessoas["Nome"]} [m/f]: ').lower()
    pessoas['Idade'] = int(input(f'Idade de {pessoas["Nome"]}: '))
    cadastrados.append(pessoas.copy())
    cont += 1
    soma_idade += pessoas['Idade']
    media = soma_idade / cont

    if pessoas['Sexo'] == 'f':
        mulheres.append(pessoas.copy())

    perg = input('Gostaria de continuar cadastrando pessoas? [s/n] ')
    if perg == 's':
        pessoas.clear()
    else:
        break

for a in range(0, len(cadastrados)):
    if cadastrados[a]['Idade'] > media:
        acima_media.append(cadastrados[a].copy())


print(cadastrados)
print(f'Total de {cont} pessoas cadastradas.')
print(f'A média de idade dos cadastrados é de {media:.0f} anos.')

if len(mulheres) > 0:
    print(f'Mulheres cadastradas: {mulheres}')
else:
    print('Nenhuma mulher foi cadastrada.')

if len(acima_media) > 0:
    print(f'Pessoas com idade acima da média: {acima_media}')
else:
    print('Nenhuma pessoa com idade acima da média foi cadastrada.')

