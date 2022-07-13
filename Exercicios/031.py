distancia = float(input('Digite a distância da viagem: '))
if distancia > 200:
    valorPassagem = distancia*0.45
    print('Valor da passagem: R${:.2f}'.format(valorPassagem))
else:
    valorPassagem = distancia*0.50
    print('Valor da passagem: R${:.2f}' .format(valorPassagem))
