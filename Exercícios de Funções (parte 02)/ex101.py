# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.


def voto(ano):
    from datetime import date
    idade_atual = date.today().year - ano_de_nascimento
    if idade_atual < 16:
        return f'Com {ano} anos, você não vota.'
    elif idade_atual >= 70 or 16 <= ano < 18:
        return f'Com {ano} anos, o voto é facultativo.'
    else:
        return f'Com {ano} anos, o voto é obrigatório.'


ano_de_nascimento = int(input('Em que ano você nasceu? '))
resposta = voto(ano_de_nascimento)
print(resposta)
