salario = float(input('Qual seu salário ?'))
if salario > 1250.00:
    print('Seu salario teve um aumento de 10%: R${}\nSalário total: R${}'.format(
        salario*0.10, salario*1.10))  # primeiro o calculo do aumento e depois o total com o aumento
else:
    print('Seu salário teve um aumento de 15%: R${}\nSalário total: R${}'.format(
        salario*0.15, salario*1.15))
