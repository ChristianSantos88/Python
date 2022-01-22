# Crie um programa em que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []

vazio = False

if expr == '' or expr.isspace():
    print('Expressão vazia!')
    vazio = True
else:
    for simb in expr:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:  # sinal de que a pilha não está vazia!
                pilha.pop() # remove o último elemento da lista
            else:
                pilha.append(')')  # se cair aqui, significa que há mais ')' do que '('
                break

if not vazio:
    if len(pilha) == 0:
        print('Sua expressão está válida!')
    else:
        print('Sua expressão está inválida!')