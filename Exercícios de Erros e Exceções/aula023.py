try:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    c = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except KeyboardInterrupt:
    print('O usuário desistiu de continuar usando o programa.')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0!')
else:
    print(c)
finally:
    print('VOLTE SEMPRE!')