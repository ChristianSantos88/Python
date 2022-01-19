#
# FUNÇÕES (PARTE 01)
#

def mostra_linha():
    print('-' * 30)


# Funções com parâmetros
def titulo(frase):
    print('-' * 30)
    print(f'{frase:^30}')
    print('-' * 30)


# Função para cálculos matemáticos com parâmetro
def operacao_matematica(a, b, operador):
    if operador == '+':
        soma = a + b
        print(soma)
    elif operador == '-':
        subtracao = a - b
        print(subtracao)
    elif operador == '*':
        multiplicacao = a * b
        print(multiplicacao)
    elif operador == '/':
        divisao = a / b
        print(divisao)
    else:
        print('Operador inválido!')


# "Empacotando" parâmetros
def contador_numeros(*num):  # Este símbolo é usado para "desempacotar" parâmetros
    print(f'No total, você digitou {len(num)} números.')


# Listas dentro de funções
def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [2, 5, 4, 8, 12]
dobra(valores)
print(valores)


# Função soma com empacotador
def soma(*num):
    s = pos = 0
    for v in range(0, len(num)):
        s += num[v]
        pos += 1
    print(f'Somando os números {num} temos {s}.')


soma(2, 3, 4, 8, 12, 3)


