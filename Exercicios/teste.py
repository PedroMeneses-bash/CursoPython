from datetime import date


def calculoIdade(dataNascimento):
    today = date.today()
    idade = today.year - dataNascimento.year - \
        ((today.month, today.day) < (dataNascimento.month, dataNascimento.day))

    return idade


def tratativaData(data):
    dia = int(data[:(data.find('/'))])
    mes = int(data[data.find('/')+1:data.rfind('/')])
    ano = int(data[data.rfind('/')+1:])

    return dia, mes, ano


print(calculoIdade(tratativaData('24/02/1996')))
