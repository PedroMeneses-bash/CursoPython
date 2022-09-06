from lib.home import *
from lib.cadastro import *
from lib.arquivo import *

arq = 'cadastros.txt'
arquivo(arq)

while True:
    titulo('MENU PRINCIPAL')
    num = menu(['Cadastrar Pessoa', 'Listar Pessoas', 'Sair do Programa'])

    if num == 1:
        titulo('CADASTRO DE PESSOA')
        cadastro('cadastros.txt')

    elif num == 2:
        lerArq(arq)
    elif num == 3:
        titulo('PROGRAMA FINALIZADO')
        break
    else:
        print('Digite uma opçao válida.')
