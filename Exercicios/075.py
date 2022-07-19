
tuplaNumeros = (int(input('Informe um número: ')), int(input('Informe o segundo número: ')), int(input(
    'Informe o terceiro número: ')), int(input('Informe o quarto número: ')))
print(f'Tem {tuplaNumeros.count(9)} números 9 na tupla.')

if 3 in tuplaNumeros:
    print(f'O primeiro 3 foi encontrado na posição {tuplaNumeros.index(3)}')

print('Pares: ', end=' ')
for i in tuplaNumeros:
    if i % 2 == 0:
        print(i, end=' ')
