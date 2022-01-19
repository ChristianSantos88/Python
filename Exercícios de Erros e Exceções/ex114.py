# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

'''
import urllib
import urllib.request
try:
    resposta = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site do pudim não está acessível no momento.')
else:
    print('Consegui acessar o site do Pudim!')
'''

import requests

try:
    resposta = requests.get('http://www.pudim.com.br')
except Exception as erro:
    print(f'Não estou conseguindo acessar o site do pudim. \nMotivo do erro: {erro.__class__}')
else:
    print('Consegui acessar o site do pudim!')
