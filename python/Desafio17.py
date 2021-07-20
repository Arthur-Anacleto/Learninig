from math import hypot
co = float(input('Digite o cateto oposto do triângulo retângulo. '))
ca = float(input('Digite o cateto adjacente do triângulo retângulo. '))
print('A hipotenusa é {:.2f}.'.format(hypot(co, ca)))
