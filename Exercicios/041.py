from datetime import date


def calculoIdade(dataNascimento):
    today = date.today()
    idade = today.year - dataNascimento.year - \
        ((today.month, today.day) < (dataNascimento.month, dataNascimento.day))

    return idade


data = input('Informe sua data de nascimento: ')

dia = int(data[:(data.find('/'))])
mes = int(data[data.find('/')+1:data.rfind('/')])
ano = int(data[data.rfind('/')+1:])

idade = calculoIdade(date(ano, mes, dia))
print('-Natação-')

if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 20:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
