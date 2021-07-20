from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo para saber o seno, cosseno e tangente. '))
rad1 = radians(angulo)
print('O seno de {}° é {:.2f}.'.format(angulo, sin(rad1)))
print('O cosseno de {}° é {:.2f}.'.format(angulo, cos(rad1)))
print('A tangente de {}° é {:.2f}.'.format(angulo, tan(rad1)))
