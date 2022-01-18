'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.
'''

num = tuple(int(input('Digite um valor: ')) for c in range(0, 4))
cont_nove = 0
pos_tres = 0

print(f'Números gerados: {num}')

if 9 in num:
    print(f'O número 09 apareceu {num.count(9)} vez(es).')

if 3 in num:
    pos_tres = num.index(3)
    print(f'O número 03 aparece pela primeira vez na {pos_tres + 1}ª posição.')

print(f'Número(s) par(es) gerado(s): ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

