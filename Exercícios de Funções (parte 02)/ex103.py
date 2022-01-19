# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaqz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome, g):
    if nome:
        if g and g.isnumeric():
            return f'O jogador {nome} fez {g} gols no campeonato.'
        else:
            return f'O jogador {nome} fez 0 gols no campeonato.'
    if not nome:
        if g and g.isnumeric():
            return f'O jogador <desconhecido> fez {g} gols no campeonato.'
        else:
            return f'O jogador <desconhecido> fez 0 gols no campeonato.'


jogador = input('Digite o nome do jogador: ')
gols = str(input('Número de gols: '))
print(ficha(jogador, gols))
