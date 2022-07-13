from datetime import date

anoNascimento = int(input('Em que ano você nasceu ?'))

anoHoje = date.today().year

idadePessoa = anoHoje-anoNascimento

if idadePessoa < 18:
    print('Ainda não precisa de alistar, daqui {} anos você poderá.' .format(
        18-idadePessoa))
elif idadePessoa == 18:
    print('Você deverá se alistar esse ano.')
else:
    print("""Caso não tenha se alistado, deverá se alistar o mais cedo possivel.
Seu alistamento esta atrasado há {} anos. """ .format(idadePessoa-18))
