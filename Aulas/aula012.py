# ELIF
from datetime import date

nomePessoa = input('Qual seu nome ?')
dataNascimento = input('Qual data de nascimento ?')

charDataInicial = dataNascimento.rfind('/')+1
anoNascimento = int(dataNascimento[charDataInicial:])

anoHoje = date.today().year
idadePessoa = anoHoje-anoNascimento

if idadePessoa >= 18:
    print("""{} é maior de idade, tem {} anos de idade.\n
    -Documentos Obrigatorios:\n
    --Titulo Eleitoral\n
    --Reservista Militar\n
    -Documentos Opcionais:\n
    --Carteira Nacional de Habilitação""" .format(nomePessoa, idadePessoa))

elif idadePessoa >= 16:
    print("""{} tem {} anos de idade e tem direito a seguintes documentos: \n
    -Documentos Opcionais:\n
    --Titulo Eleitoral""" .format(nomePessoa, idadePessoa))

else:
    print("""{} tem {} anos de idade e não é obrigado a tirar nenhum documento.""" .format(
        nomePessoa, idadePessoa))
