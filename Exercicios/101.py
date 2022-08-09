def calculoIdade(data):
    from datetime import date

    dia = int(data[:(data.find('/'))])
    mes = int(data[data.find('/')+1:data.rfind('/')])
    ano = int(data[data.rfind('/')+1:])

    dataNascimento = date(ano, mes, dia)

    today = date.today()
    idade = today.year - dataNascimento.year - \
        ((today.month, today.day) < (dataNascimento.month, dataNascimento.day))

    print(f'{idade} anos.')
    if idade >= 18:
        print('Voto OBRIGATÓRIO.')
    elif idade < 18 and idade >= 16:
        print('Voto OPICIONAL')
    else:
        print('Voto Negado')

    return idade


data = input('Informe sua data de nascimento: ')
calculoIdade(data)
