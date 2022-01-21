#
# LISTAS (PARTE 01)
#

# Adicionando elementos ao final da lista
lista = ['caneta', 'lapiseira', 'mochila']
lista.append('estojo')
print(lista)

# Adicionando elementos em qualquer posição da lista
lista.insert(1, 'tesoura')
print(lista)

# Eliminando elementos de uma lista
del lista[2]
lista.pop(3)  # normalmente, utilizando para apagar o último elemento da lista
lista.remove('caneta') # indicar o valor, e não o índice
lista.pop()  # sem argumentos, elimina o último elemento da lista
print(lista)

lista = ['caneta', 'lapiseira', 'mochila']

# Confirmando se um elemento existe na lista antes de removê-lo
if 'lapiseira' in lista:
    lista.remove('lapiseira')
print(lista)

# Criando uma lista utilizando a função "range"
valores = list(range(5, 12))
print(valores)

# Ordenando elementos de uma lista
valores2 = [5, 8, 1, 3, 9, 7]
valores2.sort()
print(valores2)
valores2.sort(reverse=True)  # Ordem decrescente
print(valores2)

# Tamanho de uma lista
print(len(valores2))

# Maneira correta de se fazer a cópia de uma lista
valores = valores2.copy()
#  valores = valores2[:]  ==> Alternativa que também dá certo
print(valores)

