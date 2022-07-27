from random import randint

apostas= []

qtdApostas = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0,qtdApostas):
    
    while len(apostas) != 6:
        number = randint(1,60)
        if number not in apostas:
            apostas.append(number)

    apostas.sort()    
    print(f'Jogo {i+1}: {apostas}', end='\n')
    apostas.clear()