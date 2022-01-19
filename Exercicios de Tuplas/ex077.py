'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('caneta', 'lapiseira', 'forceps', 'cabelo', 'baqueta', 'apagador', 'remedio', 'vislumbre', 'datilografia')

for p in palavras:
    print(f'Na palavra {p.upper()}, temos: ', end=' ')
    for letras in p:
        if letras in 'aeiou':
            print(letras, end=' ')
    print()

