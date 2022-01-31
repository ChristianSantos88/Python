#
# DICIONÁRIOS
#

"""
# Adicionando e lendo elementos
dados = {'nome': 'Pedro', 'idade': 23}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)

# Removendo elementos
del dados['idade']
print(dados)

# Identificando chaves, valores e itens
filmes = {'título': 'Jurassic Park',
          'ano': 1991,
          'diretor': 'Steven Spielberg'
          }

print(filmes.keys())
print(filmes.values())
for k, v in filmes.items():
    print(f'{k}: {v}')

# Colocando dicionários dentro de lista
locadora = [filmes]
print(locadora)
print(locadora[0]['ano'])
"""

# Praticando
brasil = list()
estado = dict()
for e in range(0, 2):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())

for e in brasil:  # Laço de fora: lista
    for k, v in e.items():  # Laço de dentro: dicionário
        print(f'{k}: {v}')

# Exercícios (30:00)

