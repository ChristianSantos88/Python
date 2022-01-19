# Reescreva a função leia_int() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leia_float() com a mesma funcionalidade.


def leia_int(n):
    while True:
        try:
            num = int(input(n))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse valor.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        else:
            return num


def leia_float(n):
    invalido = True
    num = 0
    while invalido:
        try:
            num = float(input(n))
            invalido = False
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse valor.\033[m')
            invalido = False
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número real válido.')
    return num


numero = leia_int('Digite um número inteiro: ')
numero_real = leia_float('Digite um número real: ')
print(f'O número inteiro digitado foi {numero} e o número real digitado foi {numero_real}.')