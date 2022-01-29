# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão ge-
# rados e vai sortear 06 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample, randint

pergunta = int(input('Quantas apostas gostaria de gerar? '))
apostas = [sample(range(1, 61), k=6) for c in range(0, pergunta)]

for a in range(0, pergunta):
    print(f'Aposta {a + 1}: {sorted(apostas)[a]}')

