# O código acima é um exemplo de como calcular o limite de uma função usando a biblioteca SymPy em Python. Vamos comentar cada linha:

import sympy as sp

x = sp.Symbol('x')
f = (x**2 - 1)/(x - 1)

lim = sp.limit(f, x, 1)
print(lim)

