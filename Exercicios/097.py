
def titulo(texto):
    print('-'*44)
    print(f'{texto:^44}')  # centralizado a 40 espaços
    print('-'*44)


tituloTexto = input('Qual o texto ?')
titulo(tituloTexto)
