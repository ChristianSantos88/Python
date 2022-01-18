'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

names_and_prices = ('Caneta', 1.50, 'Borracha', 0.75, 'Lapiseira', 1.20, 'Mochila', 89.90)
produto = 0

for p in range(1, len(names_and_prices), 2):
    print(f'{names_and_prices[produto]:<10}.......... R${names_and_prices[p]}')
    produto += 2
