# Crie um programa que vai ler vários números e colocá-los em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados;
# b) A lista de valores, ordenada de forma DECRESCENTE;
# c) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    perg = input('Gostaria de continuar? ')
    if perg == 'n':
        break

lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 05 foi digitado.')
else:
    print('O valor 05 não foi digitado.')