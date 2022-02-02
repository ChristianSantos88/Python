# Faça um exercício que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

dic = {}
dic['Nome'] = input('Digite o nome do aluno: ')
dic['Média'] = float(input(f'Digite a média de {dic["Nome"]}: '))
if dic['Média'] > 7:
    dic['Situação'] = 'Aprovado'
else:
    dic['Situação'] = 'Reprovado'

for k, v in dic.items():
    print(f'{k} é igual a {v}.')
