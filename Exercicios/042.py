r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triangulo.')

    if r1 == r2 == r3:
        print('Triângulo Equilátero')
    elif r1 == r2 or r1 == r3:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')


else:
    print('Não forma um triângulo.')
