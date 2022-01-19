# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma men-
# sagem com tamanho adaptável.
'''
--- input ---
escreva('Olá, Mundo!')

--- output ---
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
'''


def escreva(frase):
    tamanho = len(frase) + 4
    print('~' * tamanho)
    # print(' ', frase)
    print(frase.center(tamanho))
    print('~' * tamanho)


escreva('Você é muito inteligente, meus parabéns!')