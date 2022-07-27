# Dicionários

tuplas = ()
lista = []
dicionario = {}  # OU dicionario = dict()

filme = {'Título': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'}
print(filme.values())  # imprime os valores
print(filme.keys())  # imprime somente as palavras chaves do dicionario
print(filme.items())  # imprime values e keys
locadora = []
locadora.append(filme.copy())
filme['Título'] = 'Avengers'
filme['Ano'] = 2012
filme['Diretor'] = 'Joss Mhadon'
locadora.append(filme.copy())
filme['Título'] = 'Matrix'
filme['Ano'] = 1999
filme['Diretor'] = 'Machowski'
locadora.append(filme.copy())

for i in locadora:
    for k, v in i.items():
        print(f'{k}: {v}')


dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(f'O {dados["nome"]} tem {dados["idade"]} anos.')
dados['Sexo'] = 'M'  # criou uma nova key no dicionario "dados"
del dados['Sexo']  # Aqui deletamos ela
