
def contador(x, y, z):

    if y > x:
        cont = x
        while cont <= y:
            print(cont, end=' ')
            cont += z
    else:
        print()
        cont = x
        while cont >= y:
            print(cont, end=' ')
            cont += z


contador(1, 10, 1)
contador(10, 0, -1)

print()
a = int(input('Informe o valor inicial: '))
b = int(input('Informe o valor final: '))
c = int(input('Informe o intervalo: '))
contador(a, b, c)
