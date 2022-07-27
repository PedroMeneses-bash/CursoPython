jogador = dict()
partidas = list()
totalGols = 0

jogador['Nome'] = input('Informe o nome do Jogador: ')
totalPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))

for i in range(0, totalPartidas):
    partidas.append(int(input(f'Quantos gols na partida {i}? ')))
    totalGols += partidas[i]

jogador['Gols'] = partidas[:]
jogador['Total de Gols'] = totalGols

for k, v in jogador.items():
    print(f'{k} é igual a {v}.')

print(f'O jogador {jogador["Nome"]} jogou {totalPartidas} partidas: ')
for c, v in enumerate(jogador['Gols']):
    print(f'     => Na partida {c}, fez {v} gols.')
