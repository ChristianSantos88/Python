# Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem cres-
# cente.

list_numbers = []

while True:
    number = int(input('Digite um valor: '))
    if number not in list_numbers:
        list_numbers.append(number)
    else:
        print('Número duplicado! Não irei cadastrá-lo nesta lista.')

    question = input('Gostaria de continuar cadastrando números? [s/n] ')
    if question == 'n':
        break



print(list_numbers)