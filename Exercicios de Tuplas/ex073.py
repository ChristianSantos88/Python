'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colo-
cação. Depois, mostre:

a) apenas os 05 primeiros colocados;
b) Os últimos 04 colocados da tabela;
c) uma lista com os times em ordem alfabética;
d) em que posição na tabela está o time da Chapecoense.
'''

times = ('Flamengo', 'Fluminense', 'São Paulo', 'Chapecoense', 'Corinthians', 'Vasco', 'Palmeiras')

# a) Os três primeiros colocados
for time in range(0, 3):
    print(f'{time + 1}º colocado: {times[time]}')

print()

# b) Os últimos três colocados da tabela
for time in range(len(times) - 3, len(times)):
    print(f'{time + 1}º colocado: {times[time]}')

# c) Lista com os times em ordem alfabética
print(sorted(times))

# d) Em que posição se encontrar o time da Chapecoense
print(f'Chapecoense se encontra na {times.index("Chapecoense") + 1}ª posição da tabela do campeonato.')


