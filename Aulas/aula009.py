#Tratamento de cadeia de caracter

frase='Curso em Vídeo Python'


#-----FATIAMENTO
print(frase[9])#imprime somente o char da posição 9
print(frase[9:13])#caracter da posição 9 até 13, lembrando que da posição 13 não mostra
print(frase[9:21])#da posição 9 até 21
print(frase[9:21:2])# da posição 9 até 21 porém de 2 em 2
print(frase[:5])#seria o mesmo que [0:5], então da posição 0 até 5
print(frase[15:])#da posição 15 até o final, seja qual a posição for
print(frase[9::3])#da posição 9 até o final, porém de 3 em 3

#-------CONTAGEM
print(len(frase))#imprime o comprimento da cadeia de caracteres em frase
print(frase.count('o'))#imprime quantos caracteres 'o'(minusculo) tem na frase
print(frase.upper().count('o'),'-----------------')
print(frase.upper().count('O'),'-----------------')
print(frase.count('o',0,13))#Quantos char de 0 até 13 tem 'o'
print(frase.find('deo'))# EM que posição começa 'deo'
print(frase.find('Android'))#Ele retorna -1 quando não existe uma string na cadeia a ser pesquisada
print('Curso' in frase)#caso tenha a string na variavel, ele retorna TRUE senão FALSE
print(frase.replace('Python', 'Android'))#substitui no momento da impressão somente
print(frase)#como prova que não altera a variavel
print(frase.upper())#tudo maiusculo
print(frase.lower())#tudo minusculo
print(frase.capitalize())#somente a primeira maiuscula
print(frase.title())#ele coloca a primeira letra de cada palavra em maiusculo

frase002='   Aprenda Python  '
print(frase002+'.')
print(frase002.strip()+'.')#Ele remove os espaço inusteis, tipo esse do começo e no final
print(frase002.rstrip()+'.')#Remove somente os ultimos espaços
print(frase002.lstrip()+'.')#remove somente os espaços iniciais

frase003=frase.split()#aqui separa a string e por palavras e atribuiu a frase003
print(frase003)
print(frase003[0])#imprime a primeira parte após fatiamento
print(frase003[3][1])#imprime da 4 parte da divisão o segundo caracter
frase003=' '.join(frase003)#aqui juntou as palavras separadas
print(frase003)
