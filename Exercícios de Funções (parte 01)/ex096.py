# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é igual a {area:.1f}m².')


print(f'{"CONTROLE DE TERRENOS":^10}')
print('-' * 20)
largura = float(input(f'LARGURA (m): '))
comprimento = float(input(f'COMPRIMENTO (m): '))

area(largura, comprimento)

