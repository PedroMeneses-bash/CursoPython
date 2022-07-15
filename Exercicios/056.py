mediaIdade = 0
maiorIdade = 0
contadorMulheresMenosVinte = 0

for i in range(1, 5):

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Sexo:\n<1>Feminino\n<2>Masculino'))

    mediaIdade += idade/i

    if idade > maiorIdade and sexo == 2:
        nomeIdadeMaior = nome
        maiorIdade = idade

    if sexo == 1 and idade < 20:
        contadorMulheresMenosVinte += 1

print('Média Idade: {:.2f}'.format(mediaIdade))
print('{} é o homem mais velho.' .format(nomeIdadeMaior))
print('{} mulheres tem menos de 20.' .format(contadorMulheresMenosVinte))
