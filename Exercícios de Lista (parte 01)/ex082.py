# Crie um programa que vai ler os vários números e colocá-los em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre os conteúdos das
# três listas geradas.

lista_geral = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input('Digite um valor: '))
    lista_geral.append(numero)

    pergunta = input('Quer continuar? ')
    if pergunta == 'n':
        break

for n in lista_geral:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)



print(f'A lista completa é: {lista_geral}')
print(f'A lista de pares é: {lista_pares}')
print(f'A lista de ímpares é: {lista_impares}')
