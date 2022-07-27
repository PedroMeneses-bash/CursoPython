from datetime import date


def calculoIdade(dataNascimento):
    today = date.today()
    idade = today.year - dataNascimento.year - \
        ((today.month, today.day) < (dataNascimento.month, dataNascimento.day))

    return idade


trabalhador = dict()

trabalhador['Nome'] = input('Informe o nome do trabalhador: ')
data = input('Informe sua data de nascimento: ')
dia = int(data[:(data.find('/'))])
mes = int(data[data.find('/')+1:data.rfind('/')])
ano = int(data[data.rfind('/')+1:])
trabalhador['Idade'] = calculoIdade(date(ano, mes, dia))

trabalhador['CTPS'] = int(input('Carteira de Trabalhao (0 não tem): '))
if trabalhador['CTPS'] != 0:

    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + 35

print(trabalhador)


for k, v in trabalhador.items():
    print(f'{k} é igual a {v}.')
