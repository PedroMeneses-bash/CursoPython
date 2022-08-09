def jogador(nomeJogador='<desconhecido>', gols=0):
    print(f'O jogador {nomeJogador} fez {gols} gols(s) no campeonato.')


nome = input('Nome do jogador: ')
qtdGols = input('Número de Gols: ')
if qtdGols.isnumeric():
    gols = int(qtdGols)
else:
    qtdGols = 0
if nome.strip() == '':
    jogador(gols=qtdGols)
else:
    jogador(nome, qtdGols)
