import math

valor_a = int(input('Valor de A: '))
valor_b = int(input('Valor de B: '))
valor_c = int(input('Valor de C: '))

#y = (valor_a * (x**2)) + (valor_b * x) + (valor_c)

delt = valor_b**2 - 4*valor_a*valor_c
print(delt)

num = ((valor_b**2)-4*valor_a*valor_c)
raiz = math.sqrt(num)

x1 = (-(valor_b) + raiz) / (2*valor_a)
x2 = (-(valor_b) - raiz) / (2*valor_a)

print(x1)
print(x2)
