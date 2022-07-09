largura=float(input('Qual a largura da parede?'))
altura=float(input('E qual a altura ?'))
areaParede=largura*altura
custoTinta=areaParede/2
print('Para pintar {:.2f}m² de parede será necessário {:.2f}L de tinta.'.format(areaParede,custoTinta))