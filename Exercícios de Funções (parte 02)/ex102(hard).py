# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro indique o número a calcular e
# o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cál-
# culo do fatorial.


def func_fatorial(numero, show=False):
    f = 1
    for v in range(numero, 0, -1):
        if show and v > 1:
            print(f'{v} x ', end='')
        elif show and v == 1:
            print(f'{v} = ', end='')
        f *= v
    return f


# Programa principal
num = int(input('Gostaria de saber o fatorial de qual número? '))
print(func_fatorial(num, show=True))
