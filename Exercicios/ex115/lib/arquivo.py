from lib.home import *


def arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        print ('Arquivo não encontrado.')
        a = open(nome, 'wt+')
        a.close()
        print('ARQUIVO CRIADO.')
    else:
        print('Arquivo carregado.')

def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERROR ao ler arquivo.')
    else:
        titulo('LISTA DE PESSOAS')
        for i in a:
            dados = i.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:.<25}{dados[1]:>3} anos')
    finally:
        a.close()
