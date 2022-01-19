# Crie um programa que tenha a função leia_int(), que vai funcionar de forma semelhante à função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico.
# ex.: n = leia_int('Digite um número: ')


def leia_int(numero):
    numero = str(input(numero)).strip()
    while numero.isalpha() or numero == '':
        numero = str(input('\033[0;31mERRO!!!\033[m Digite um número inteiro válido: ')).strip()
    if numero.isnumeric():
        numero = int(numero)
    return numero


n = leia_int('Digite um número inteiro válido: ')
print(f'Você digitou o número {n}.')

