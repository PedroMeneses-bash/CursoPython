def area(l, c):
    a = l * c
    print(f'Area do terreno {l}x{c} : {a}m²')


largura = float(input('Informe a largura do terreno: '))
comprimento = float(input('Informe o comprimento do terreno: '))

area(largura, comprimento)
