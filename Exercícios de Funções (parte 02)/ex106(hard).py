# Faça um minissistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai apare-
# cer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Obs.: use cores!


def sistema_de_ajuda():
    from time import sleep
    sair = False

    while not sair:
        titulo = 'Sistema de Ajuda PyHELP'
        print('\033[0;30;42m', end='')
        print('~' * (len(titulo) + 4))
        print(titulo.center(len(titulo) + 4))
        print('~' * (len(titulo) + 4))
        print('\033[m', end='')


        comando = input('Função ou biblioteca > ')

        if comando == 'fim':
            final = 'ATÉ LOGO!'
            print('\033[0;30;41m', end='')
            print('~' * (len(final) + 4))
            print(final.center(len(final) + 4))
            print('~' * (len(final) + 4))
            print('\033[m', end='')
            sair = True
        else:
            subtitulo = f"Acessando o manual do comando '{comando}'"
            print('\033[0;30;44m', end='')
            print('~' * (len(subtitulo) + 4))
            print(subtitulo.center(len(subtitulo) + 4))
            print('~' * (len(subtitulo) + 4))
            print('\033[m', end='')
            sleep(0.5)

            print('\033[0;7;40m')
            help(comando)
            print('\033[m', end='')


sistema_de_ajuda()



