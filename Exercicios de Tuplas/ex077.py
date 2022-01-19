'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('caneta', 'lapiseira', 'forceps', 'cabelo', 'baqueta', 'apagador', 'remedio', 'vislumbre', 'datilografia')

for p in palavras:
    print(f'Na palavra {p.upper()} temos: ', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
