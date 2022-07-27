aluno = dict()
aluno['Aluno'] = input('Informe o nome do aluno: ')
aluno['Média'] = float(input('Informe a média do aluno: '))

if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
