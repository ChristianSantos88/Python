# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo, e realize a
# contagem. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1;
# b) de 10 até 0, de 2 em 2;
# c) uma contagem personalizada.

from time import sleep


def contador():
    print('-=' * 30)
    print('Contagem de 01 até 10, de 1 em 1: ')
    for n in range(1, 11, 1):
        sleep(0.3)
        print(n, end=' ', flush=True)
    print()

    print('-=' * 30)
    print('Contagem de 10 até 0, de 2 em 2: ')
    for n in range(10, -1, -2):
        sleep(0.3)
        print(n, end=' ', flush=True)
    print()

    print('-=' * 30)
    print('Agora, é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}: ')
    if inicio < fim:
        if passo < 0:
            print('ERRO! Tente novamente.')
        if passo == 0:
            passo = 1
        for n in range(inicio, fim + 1, passo):
            sleep(0.3)
            print(n, end=' ', flush=True)
    elif inicio > fim:
        if passo > 0:
            passo = -passo
        if passo == 0:
            passo = -1
        for n in range(inicio, fim - 1, passo):
            sleep(0.3)
            print(n, end=' ')


contador()

