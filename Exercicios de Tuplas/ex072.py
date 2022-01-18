'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso (zero a vinte). Pergunte ao cliente
se ele gostaria de repetir o processo ou não?
'''


def int_para_ext(num):
    numeros_extensos = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco')
    return numeros_extensos[num]


while True:
    numero = int(input('Digite um número entre 0 e 5: '))
    if numero < 0 or numero > 5:
        print('ERRO!', end=' ')
    else:
        resultado = int_para_ext(numero)
        print(f'O número {numero} por extenso é igual a "{resultado}".')
        resposta = input('Gostaria de continuar? [s/n] ')
        if resposta == 'n':
            break

print('FIM DO PROGRAMA')


'''
num = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco'

while True:
    n = int(input('Digite um número entre 0 e 5: '))
    if 0 <= n <= 5:
        print(f'{n} e {num[n]}')
        resp = input('Gostaria de continuar? ')
        if resp == 'n':
            break
    else:
        print('Tente novamente. ', end='')
'''












































