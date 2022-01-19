#
# LISTAS (PARTE 02)
#

# Lista dentro de lista
'''
lista = ['Pedro', 32]
print(lista)
# pessoas = []
# pessoas.append(lista[:])
pessoas = [lista[:]]  # ou pessoas = [lista.copy]
print(pessoas)

cadastro = [['Pedro', 35], ['Maria', 45], ['Gabriel', 20]]
print(cadastro)
print(cadastro[0][0])  # Vai mostrar o índice 0 dentro do índice 0 da lista 'cadastro' (Pedro)
print(cadastro[0][0:2])  # Vai mostrar os índices 0 e 1 dentro do índice 0 da lista 'cadastro' (Pedro, 35)
print(cadastro[1])  # Mostra todos os índices dentro do índice 1 da listra 'cadastro' (Maria, 45)

for p in cadastro:
    print(*p, sep=', ', end=' / ')
print()
for p in cadastro:
    print(p[0], end=' / ')
print()
for p in cadastro:
    print(f'{p[0]} tem {p[1]} anos.')
'''

# Inserindo dados dentro de uma lista aninhada
pessoas = list()
dados = list()  # Lista temporária

for c in range(0, 3):
    dados.append(input('Digite um nome: '))
    dados.append(int(input('Digite uma idade: ')))
    pessoas.append(dados[:])
    dados.clear()

print(pessoas)

# Mostrar apenas as pessoas que tenham mais de 21 anos
for p in pessoas:
    if p[1] >= 21:
        print(p)