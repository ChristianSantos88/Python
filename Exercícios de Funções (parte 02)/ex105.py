# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
# as seguintes informações:
# - quantidade de notas;
# - a maior nota;
# - a menor nota;
# - a média da turma;
# - a situação (aprovado, reprovado, recuperação) (opcional)
# Obs.: adicione também as docstrings da função.


# Jeito Christian idiota de fazer
'''
def boletim_escolar(*notas, situacao=False):
    dicio = dict()
    maior = menor = soma_notas = 0
    qtde_notas_digitadas = 0
    for n in range(0, len(notas)):
        qtde_notas_digitadas += 1
        dicio['Total'] = qtde_notas_digitadas
        soma_notas += notas[n]
        if n == 0:
            maior = notas[n]
            menor = notas[n]
            dicio['Maior nota'] = maior
            dicio['Menor nota'] = menor
        if notas[n] > maior:
            maior = notas[n]
            dicio['Maior nota'] = maior
        if notas[n] < menor:
            menor = notas[n]
            dicio['Menor nota'] = menor
        media = soma_notas / qtde_notas_digitadas
        dicio['Média da turma'] = float(f'{media:.1f}')
        if situacao:
            if 6 <= media <= 7:
                dicio['Situação da turma'] = 'Boa'
            elif media <= 6:
                dicio['Situação da turma'] = 'Ruim'
            else:
                dicio['Situação da turma'] = 'Ótima'

    return dicio
'''


# Jeito decente de fazer
def boletim_escolar(*notas, situacao=False):
    dicio = dict()
    dicio['Total de notas cadastradas'] = len(notas)
    dicio['Maior nota da turma'] = max(notas)
    dicio['Menor nota da turma'] = min(notas)
    dicio['Média da turma'] = float(f'{(sum(notas) / len(notas)):.1f}')
    if situacao:
        if 6 <= dicio['Média da turma'] <= 8:
            dicio['Situação da turma'] = 'BOA'
        elif dicio['Média da turma'] >= 8:
            dicio['Situação da turma'] = 'ÓTIMA'
        else:
            dicio['Situação da turma'] = 'RUIM'
    return dicio


print(boletim_escolar(7, 9.5, 10, 6.5, situacao=True))
