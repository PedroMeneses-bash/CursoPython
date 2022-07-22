palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for i in palavras:
    print(f'\nNa palavra {i.upper()} temos:', end=' ')

    for letra in i:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
