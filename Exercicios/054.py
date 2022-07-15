from datetime import date


def calculoIdade(dataNascimento):
    today = date.today()
    idade = today.year - dataNascimento.year - \
        ((today.month, today.day) < (dataNascimento.month, dataNascimento.day))

    return idade


contadorMaiorIdade = 0
contadorMenorIdade = 0

for i in range(0, 8):
    data = input('Informe sua data de nascimento: ')

    dia = int(data[:(data.find('/'))])
    mes = int(data[data.find('/')+1:data.rfind('/')])
    ano = int(data[data.rfind('/')+1:])

    idade = calculoIdade(date(ano, mes, dia))

    if idade <= 18:
        contadorMaiorIdade += 1

    else:
        contadorMenorIdade += 1

print('{} são maior de idade.\n{} são menores de idade.' .format(
    contadorMaiorIdade, contadorMenorIdade))
