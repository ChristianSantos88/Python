from biblio import interface, arquivo
from time import sleep

arq = 'Pessoas.txt'

if not arquivo.arquivo_existe(arq):
    arquivo.criar_arquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        arquivo.ler_arquivo(arq)
    elif resposta == 2:
        interface.header('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.header('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
    sleep(2)
