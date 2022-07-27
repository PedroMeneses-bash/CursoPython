from random import randint
from operator import itemgetter

# rpg = list()
# player = dict()
# dado = 0
ranking = dict()

# for i in range(0,4):
#     dado = randint(1,6)
#     player['Jogador'] = i+1
#     player['Dado'] = dado
#     rpg.append(player.copy())
#     print(f'Jogador {player["Jogador"]} tirou: {player["Dado"]} ')

# ranking = sorted(player.items(), key=itemgetter(1))

jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6),
        'jogador4': randint(1, 6), 'jogador5': randint(1, 6), 'jogador6': randint(1, 6)}

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
