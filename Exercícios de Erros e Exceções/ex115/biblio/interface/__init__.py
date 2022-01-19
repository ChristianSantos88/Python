def leia_int(n):
    while True:
        try:
            num = int(input(n))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse valor.\033[m')
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        else:
            return num


def linha(tam=42):
    return '-' * tam


def header(titulo):
    print(linha())
    print(titulo.center(42))
    print(linha())


def menu(lista):
    header('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leia_int('\033[33mSua opção:\033[m ')
    return opc
