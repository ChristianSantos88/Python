# Faça um programa que leia 05 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

numbers = list(int(input('Digite um valor: ')) for n in range(0, 5))

print(f'Os valores digitados foram: {numbers}')

print(f'O maior valor digitado foi {max(numbers)} nas posições: ', end='')
for c, n in enumerate(numbers):
    if n == max(numbers):
        print(f'{c}... ', end='')

print(f'\nO menor valor digitado foi {min(numbers)} nas posições: ', end='')
for c, n in enumerate(numbers):
    if n == min(numbers):
        print(f'{c}... ', end='')

