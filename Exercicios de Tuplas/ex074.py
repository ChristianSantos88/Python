'''
Crie um programa que vai gerar cinco números aleatórios e coloque-os em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint, sample

# 3 formas diferentes de fazer essa tupla com cinco números aleatórios
num_aleat = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
aleat = tuple(randint(0, 100) for c in range(0, 5))
aleat2 = tuple(sample(range(100), k=5))  # Nesta, os números aleatórios não se repetem.

print(f'Números gerados: {aleat2}')
print(f'Maior número gerado: {max(aleat2)}')
print(f'Menor número gerado: {min(aleat2)}')

