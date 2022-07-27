jogador = dict()
partidas = list()
time = list()

while True:

    jogador.clear()
    jogador['Nome'] = input('Informe o nome do Jogador: ')
    totalPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    partidas.clear()

    for i in range(0, totalPartidas):
        partidas.append(int(input(f'Quantos gols na partida {i}? ')))

    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas)
    time.append(jogador.copy())

    breakPrograma = input('Quer continuar? [S/N]').upper().strip()[0]
    if breakPrograma == 'N':
        break
print('-='*18)
print(f'{"Cod.":<7}{"Nome":<12}{"Gols":<12}{"Total":<12}')
print('--'*18)
for k, v in enumerate(time):
    print(f'{k:<7}', end='')
    for d in v.values():
        print(f'{str(d):<12}', end='')
    print()
print('-='*18)

while True:
    numero = int(input(f'Informe o indice para ver a nota de algum aluno: '))

    if numero == 999:
        print('Programa Finalizado!')
        break
    elif numero >= len(time):
        print('Aluno não encontrado.')
    else:
        print('-='*18)
        print(f'Informações do jogador {time[numero]["Nome"]}: ')
        for j, r in enumerate(time[numero]['Gols']):
            print(f'    -->No jogo {j+1} converteu {r} gols.')
    print('-='*18)
