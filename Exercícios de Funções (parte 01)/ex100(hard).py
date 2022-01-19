# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). A primeira fun-
# ção vai sortear 5 números aleatórios e os colocará dentro da lista, e a segunda função vai mostrar a soma entre todos
# os valores pares sorteados pela função anterior.

from random import randint, sample
from time import sleep

numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for v in range(0, 5):
        v = randint(0, 10)
        lista.append(v)
        sleep(0.3)
        print(v, end=' ', flush=True)
    sleep(0.3)
    print('PRONTO!')
    # lista = list(randint(0, 100) for c in range(0, 5))
    # lista2 = list(sample(lista, k=5))  # Usar "sample()" caso eu não queira números repetidos
    # print(f'Lista criada: {lista2}')


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia(numeros)
soma_par(numeros)
