def fatorial(num, show=False):

    if show:

        totalFatorial = 1
        for i in range(num, 0, -1):
            totalFatorial *= i
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    else:

        totalFatorial = 1
        for i in range(num, 0, -1):
            totalFatorial *= i

    return totalFatorial


# Programa Main
print(fatorial(5))
print(fatorial(4, show=True))
