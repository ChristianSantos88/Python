# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o MAIOR.

# Versão simplificada do programa
def maior(*numbers):
    print(f'Números digitados: {numbers}')
    print(f'Maior número digitado: {max(numbers)}')


# Versão complicada do programa
def maior_hard(*numbers):
    maior_number = 0
    for v in numbers:
        if v > maior_number:
            maior_number = v
    print(f'Números digitados: {numbers}')
    print(f'Maior número digitado: {maior_number}')


maior(5, 4, 8, 128, 11, 15)
maior_hard(5, 4, 8, 121, 11, 9, 13)
