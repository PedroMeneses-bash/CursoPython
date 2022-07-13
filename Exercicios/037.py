numeroEscolhido = int(input('Informe um numero :'))
baseNumerica = int(input(
    'Qual base numerica quer converter ?\nBinaria <1>\nOctal <2>\nHexadecimal <3>\n'))
if baseNumerica == 1:
    baseNumerica = bin(baseNumerica)
    print(baseNumerica)
elif baseNumerica == 2:
    baseNumerica = oct(baseNumerica)
    print(baseNumerica)
else:
    baseNumerica = hex(baseNumerica)
    print(baseNumerica)
