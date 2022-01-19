from .. import interface
import sys


def arquivo_existe(file):
    try:
        a = open('Pessoas.txt', 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(file):
    a = open(file, 'wt+')
    a.close()
    print(f'Arquivo {file} criado com sucesso!')


def ler_arquivo(file):
    interface.header('CADASTRO DE PESSOAS')
    a = open(file, 'rt')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    print(a.read())
    a.close()


def cadastrar(arq, nome, idade):
    a = open(arq, 'at')
    a.write(f'{nome};{idade}\n')
    print(f'Novo registro de {nome} adicionado!')
    a.close()
