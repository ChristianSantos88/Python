# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de zero, o dicionário também receberá o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar. (Considerese 35 anos de contribuição)

import datetime

dicio = {'Nome': input('Digite o nome: '), 'Ano': int(input('Ano de nascimento: ')), 'CTPS': int(input('Nº da CTPS: '))}
dicio['Idade'] = datetime.date.today().year - dicio['Ano']

if dicio['CTPS'] != 0:
    dicio['Admissão'] = int(input('Ano de admissão no trabalho: '))
    dicio['Salary'] = float(input('Salário: R$ '))
    aposentadoria = (dicio['Admissão'] - dicio['Ano'] + 35)
    print(dicio)
    print(f'{dicio["Nome"]} irá se aposentar com {aposentadoria} anos.')
else:
    print(dicio)


