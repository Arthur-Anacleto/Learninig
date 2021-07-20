from random import choice
p1 = input('Digite o 1° nome. ')
p2 = input('Digite o 2° nome. ')
p3 = input('Digite o 3° nome. ')
p4 = input('Digite o 4° nome. ')
nomes = [p1, p2, p3, p4]
print('O escolhido para pagar o lanche é {}.'.format(choice(nomes)))

