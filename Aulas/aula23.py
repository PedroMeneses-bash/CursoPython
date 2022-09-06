try:
    a = int(input('Informe o numerador: '))
    b = int(input('Informe o denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Não foi possível realizar a divisão. ERROR')
except ZeroDivisionError:
    print('Impossivel dividir por zero')
except KeyboardInterrupt:
    print('O usuario preferiunão informar os dados.')
else:
    print(f'O resultado foi: {r:.2f}')
finally:
    print('Código finalizado.')
