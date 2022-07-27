matrizPessoa = [[0, 0, 0 ], [0, 0, 0 ], [0, 0, 0 ]]

for l in range(0,3):
    for c in range(0,3):
        matrizPessoa[l][c] = int(input('Informe valor: '))

for l in range(0,3):
    print('')
    for c in range(0,3):
        print(f'[{matrizPessoa[l][c]}]', end='')