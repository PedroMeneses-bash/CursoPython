nomeFuncionario=input('Qual seu nome ?')
salarioFuncionario=float(input('Qual seu salario ?'))
print('{} seu salario base é de R$ {} mas houve um aumento de 15%, então : R$ {:.2f}' .format(
    nomeFuncionario, salarioFuncionario, salarioFuncionario*1.15))