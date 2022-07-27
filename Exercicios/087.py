matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaColunaTres = 0
maiorValor = 0

#Entrada Matriz
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Informe valor: '))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        
        if c == 2:
            somaColunaTres += matriz[l][c]

        if l == 1:
            if matriz[l][c] > maiorValor:
                maiorValor = matriz[l][c]






#Saida Matriz
for l in range(0,3):
    print('')
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')

print(f'\nSoma dos pares: {somaPares}')
print(f'Soma da coluna 3: {somaColunaTres}')
print(f'O maior valor da linha 2: {maiorValor}')