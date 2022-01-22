# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição corre-
# ta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
maior_num = 0

for v in range(0, 5):
    num = int(input('Digite um valor: '))
    if v == 0:
        maior_num = num
        lista.append(num)



