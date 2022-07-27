import os

dados = dict()
pessoas = list()
mulheres = list()
idadeAcimaMedia = list()
contPessoas = 0
somaIdade = 0
mediaIdade = 0
contMulher = 0
contAcimaMedia = 0

while True:

    dados['Nome'] = input('Nome: ').capitalize()
    dados['Sexo'] = input('Sexo [M/F]: ').upper().strip()[0]
    dados['Idade'] = int(input('Idade: '))

    contPessoas += 1
    somaIdade += dados['Idade']
    mediaIdade = somaIdade / contPessoas
    pessoas.append(dados.copy())

    if dados['Sexo'] == 'F':
        mulheres.append(dados.copy())
        contMulher += 1

    if dados['Idade'] >= mediaIdade:
        idadeAcimaMedia.append(dados.copy())
        contAcimaMedia += 1

    breakPrograma = input('Quer continuar? [S/N]').upper().strip()[0]
    if breakPrograma == 'N':
        break

os.system('cls')
print(f'Foram registradas {contPessoas} pessoas.')
print(f'A média de idade foi de {mediaIdade:.2f}')
print(f'Dentre as informadas {contMulher} são mulheres: ')
for c in mulheres:
    print(c["Nome"])
print(f'\nE foram registras {contAcimaMedia} acima da média de idade: ')
for i in idadeAcimaMedia:
    print(f'{i["Nome"]} com {i["Idade"]} anos de idade.')
