diasAluguel=int(input('Por quantos dias o carro foi alugado ?'))
kmAndado=float(input('Quantos km foi percorrido com o carro ?'))
valorAluguel=(diasAluguel*60)+(kmAndado*0.15)
print('O valor do aluguel total foi de R${:.2f}' .format(valorAluguel))