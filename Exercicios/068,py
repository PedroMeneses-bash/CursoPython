from random import randint

contTriunfo = 0

while True:
    escolha = input('Par ou impar ?').upper()
    numeroJogador = int(input('Qual número de 1 a 100: '))

    numeroMaquina = randint(1, 100)

    somaNumero = numeroJogador+numeroMaquina

    if somaNumero % 2 == 0 and escolha == 'PAR':
        contTriunfo += 1
        print('Ganhou essa!')
        print(f'Player: {numeroJogador}\nMachine: {numeroMaquina}')
        print(f'Soma: {somaNumero} ----> {escolha}')
    elif somaNumero % 2 != 0 and escolha == 'IMPAR':
        contTriunfo += 1
        print('Ganhou essa!')
        print(f'Player: {numeroJogador}\nMachine: {numeroMaquina}')
        print(f'Soma: {somaNumero} ----> {escolha}')
    else:
        print('You lost it!')
        print(f'Player: {numeroJogador}\nMachine: {numeroMaquina}')
        print(f'Soma: {somaNumero}')
        break
print('GAME OVER')
print(f'Total de triunfos : {contTriunfo}')
