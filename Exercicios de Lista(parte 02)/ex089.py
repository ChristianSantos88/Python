# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada individualmente. (33'00)
# Dica: Fazer uma lista grande em que o NOME será o 1º elemento e as duas notas serão o 2º elemento.
# [[nomeA[nota1, nota2, media]], [nomeB[nota1, nota2, media]], [nomeC[nota1, nota2, media]]]

lista = []
lista_temp = []

while True:
    lista_temp.append(input('Nome do aluno: '))
    lista_temp.append(float(input(f'Primeira nota: ')))
    lista_temp.append(float(input(f'Segunda nota: ')))
    lista_temp.append((lista_temp[1] + lista_temp[2]) / 2)
    lista.append(lista_temp.copy())

    perg = input('Gostaria de continuar cadastrando? ')
    if perg == 'n':
        break

    lista_temp.clear()

print(lista)
print()

for aluno in range(0, len(lista)):
    print(f'{aluno + 1} --- {lista[aluno][0]} --- {lista[aluno][3]}')

print()

while True:
    perg = int(input('Gostaria de ver as notas de qual aluno? [999 finaliza o sistema] '))
    if perg == 999:
        break
    elif perg >= len(lista) + 1:
        print('Cadastro não encontrado. Tente novamente.\n')
    else:
        print(f'Notas de {lista[perg - 1][0]}: {lista[perg - 1][1:3]}\n')

print('FIM DO PROGRAMA')





