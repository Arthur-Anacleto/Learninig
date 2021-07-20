from random import shuffle
p1 = input('Digite o 1° nome. ')
p2 = input('Digite o 2° nome. ')
p3 = input('Digite o 3° nome. ')
p4 = input('Digite o 4° nome. ')
p5 = input('Digite o 5° nome. ')
lista = [p1, p2, p3, p4, p5]
shuffle(lista)
print('A ordem sorteada é {}.'.format(lista))
