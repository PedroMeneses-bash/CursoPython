def calculoIdade(data):
    from datetime import date

    dia = int(data[:(data.find('/'))])
    mes = int(data[data.find('/')+1:data.rfind('/')])
    ano = int(data[data.rfind('/')+1:])

    dataNascimento = date(ano, mes, dia)

    today = date.today()
    idade = today.year - dataNascimento.year - \
        ((today.month, today.day) < (dataNascimento.month, dataNascimento.day))

    return idade


#data = input('Informe sua data de nascimento: ')
#print(calculoIdade(data), "anos")
