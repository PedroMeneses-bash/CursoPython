contMaiorIdade = 0
contHomens = 0
contMulheresVinte = 0
repete = ' '


while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Informe o sexo M\F: ').strip().upper()[0]

    if idade > 18:
        contMaiorIdade += 1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulheresVinte += 1

    repete = ' '
    while repete not in 'SN':
        repete = input('Deseja repetir o processo ? S/N').upper().strip()

    if repete == 'N':
        break

print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
print(f'{contMaiorIdade} pessoas tem mais de 18 anos.')
print(f'{contHomens} homens foram cadastrados.')
print(f'{contMulheresVinte} mulheres tem menos de 20 anos.')
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
