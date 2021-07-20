km = float(input('Quantos km percorreu? '))
dia = int(input('Quatos dias alugou o carro? '))
print('Como percorreu {}km em {} dias, \n'
      'então o valor total a pagar é R${:.2f}'.format(km, dia, (km * 0.15 + dia * 60)))