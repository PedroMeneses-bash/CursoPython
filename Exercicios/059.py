operacao = 1

while operacao != 5:
    number001 = int(input('Informe o primeiro número: '))
    number002 = int(input('Informe o segundo número: '))
    print('========================\n|     < 1 > Somar     |')
    print('========================\n| < 2 > Multiplicação |')
    print('========================\n|     < 3 > Maior     |')
    print('========================\n| < 4 > Novos Números |')
    print('========================\n|     < 5 > Sair      |')
    operacao = int(input('Informe a operação dos numeros: '))

    if operacao == 1:
        print(number001+number002)
    elif operacao == 2:
        print(number001*number002)
    elif operacao == 3:
        if number001 > number002:
            print('O primeiro número,{} é maior que o segundo número {}.' .format(
                number001, number002))
        else:
            print('O segundo número, {} é maior que o primeiro {}.' .format(
                number002, number001))
    elif operacao == 5:
        print(
            '========================\n| Programada Encerrado |\n========================')
    else:
        print('---------------------\nInforme novos números\n----------------------')
