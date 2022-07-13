# nao quebra linha, continua com "Qual seu nome?"
print('Hello World!', end='')
nome = input('Qual seu nome? ')
x = int(input('Digite o primeiro valor'))
y = int(input('Digite o segundo valor'))
a = input('Digite outro numero')
s = x+y
print(s, ' <--- Aqui foi o valor de S')  # Simplesmente imprime o valor de s
print(x+y, '<-- Aqui a soma de x e y')  # Simplesmente imprime a soma de x e y
print('O resultado da soma de x e y é: {}'.format(s))
# como utilizado no C %i para incrementar o valor de um inteiro formatado, nesse caso utilizamos o {}

print("""A soma entre {0} e {1} equivale a {2}.
\nDesenhando: {0}+{1}={2}""".format(x, y, s))  # imprime o tipo da variavel s
print(type(s), '<-- Aqui imprime o tipo de primitivo da variavel S')
# retornar com TRUE ou FALSE se o valor de a(linha 5) for numero.
print(a.isnumeric())
print(a.isalpha())  # Retorna TRUE ou FALSE se o valor é letra
print(a.isalnum())  # Retorna se a é alfanumerico

# resultado floar até 3 casas decimais
print('Divisao em float é {:.3f}'.format(s))
print(x**y, 'potencia')  # imprime o resultado de x elevado a y
print(x//y, 'divisor int')  # imprime resultado da divisão somente o valor int
# o bom e velho resto de divisao, para saber se o numero é primo
print(x % y, 'resto da divisoa')

# Hierarquia de operações
# 1- ()
# 2- **
# 3- *   /   //   %
# 4- + -

print('Bem vindo {:20} .' .format(nome))  # nome ocupa 20 char
# nome ocupa 20 char porém todo a direita
print('Bem vindo {:>20} .' .format(nome))
# nome ocupa 20 char mas todo a esquerda
print('Bem vindo {:<20} .' .format(nome))
# nome ocupa 20 char mas centralizado
print('Bem vindo {:^20} .' .format(nome))
# nome ocupa 20 char porém centralizado e com = preenchidos nos vazios
print('Bem vindo {:=^20} .' .format(nome))
