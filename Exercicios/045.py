from random import choice

partidasMaquina = 0
partidasJogador = 0
contador = 1

print('Vamos jogar JOKENPO!!!')
while contador == 1:

    a = 'PEDRA'
    b = 'PAPEL'
    c = 'TESOURA'
    escolhaMaquina = choice([a, b, c])

    print('Máquina {}x{} Você' .format(partidasMaquina, partidasJogador))
    escolhaJogador = input('Pedra, papel ou tesoura ?').strip().upper()

    if escolhaMaquina == 'PEDRA' and escolhaJogador == 'TESOURA':
        print('Maquina ganhou')
        partidasMaquina += 1
    elif escolhaMaquina == 'PAPEL' and escolhaJogador == 'PEDRA':
        print('Maquina Ganhou')
        partidasMaquina += 1
    elif escolhaMaquina == 'TESOURA' and escolhaJogador == 'PAPEL':
        print('Maquina ganhou')
        partidasMaquina += 1
    elif escolhaMaquina == escolhaJogador:
        print('Empate')
    else:
        print('Ponto pra você.')
        partidasJogador += 1

    if partidasJogador == 3 or partidasMaquina == 3:
        contador = 0

if partidasMaquina > partidasJogador:
    print('\nA maquina venceu no melhor de 3.')
    print('Máquina {}x{} Você' .format(partidasMaquina, partidasJogador))
else:
    print('\nVocê ganhou da máquina!')
    print('Máquina {}x{} Você' .format(partidasMaquina, partidasJogador))
