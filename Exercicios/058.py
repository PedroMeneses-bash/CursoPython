import random

i = 1
contadorPalpites = 0

while i > 0:

    numeroAleatorio = random.randint(0, 10)
    numeroPessoa = int(input('Digite sua aposta de número: '))

    if numeroPessoa == numeroAleatorio:
        print('Cagada da pohha, acertô miserávi!')
        i = 0
    else:
        print('Como diz Faustão: \n"ERROOOOOOU!"\nO número foi : {}' .format(
            numeroAleatorio))

        contadorPalpites += 1

print('Você fez {} palpites.' .format(contadorPalpites))
