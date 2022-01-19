#
# FUNÇÕES (PARTE 02)
#

# ==> 1) INTERACTIVE HELP
# help()
# help(print)
# print(print.__doc__)

# ==> 2) DOCSTRINGS
'''
def contador(i, f, p):
    """
    Faz uma contagem do início ao fim, pulando os números de acordo com o passo digitado.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passos
    :return: sem retorno
    """
    while i <= f:
        print(i, end='..')
        i += p
'''


# ==> PARÂMETROS OPCIONAIS (15:50)
def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')


# ==> ESCOPO DE VARIÁVEIS / ESCOPO DE DECLARAÇÕES
# Escopo: local onde a variável vai existir e também onde não vai existir
def teste(a):
    global b  # Transforma a variável "b" interna em global
    a += 5  # variável de escopo LOCAL
    b = 6  # apesar de ter uma variável 'b' global, agora também terei uma variável 'b' local
    c = 9  # variável de escopo LOCAL
    print(f'Dentro desta função, a variável "a" vale {a}')
    print(f'Dentro desta função, a variável "b" vale {b}.')
    print(f'Dentro desta função, a variável "c" vale {c}.')


b = 3  # variável de escopo GLOBAL
teste(b)
print(f'A variável "b" fora vale {b}')

# ==>  RETORNO DE VALORES
def somando(a=0, b=0, c=0):
    s = a + b + c
    return s


resp = somando(5, 8, 4)
resp2 = somando(8, 7)
resp3 = somando(9, 9, 15)
print(f'Resultado das somas: {resp}, {resp2}, {resp3}.')

# Exercícios (39:45)





