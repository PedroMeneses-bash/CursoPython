import random

i=1

while i > 0 :

    numeroAleatorio=random.randint(0,5)
    numeroPessoa=int(input('Digite sua aposta de número: '))

    if numeroPessoa == numeroAleatorio :
        print('Cagada da pohha, acertô miserávi!')
    else:
        print('Como diz Faustão: \n"ERROOOOOOU!"\nO número foi : {}' .format(numeroAleatorio))

    i=int(input('\nDeseja tentar de novo ? \n<1> para SIM\n<0> para NÃO\n'))