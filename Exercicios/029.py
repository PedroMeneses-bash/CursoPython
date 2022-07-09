velocidade=int(input('Velocidade: '))
if velocidade > 80 :
    multa=float((velocidade-80)*7.00)
    print('Multa de R${:.2f}' .format(multa))