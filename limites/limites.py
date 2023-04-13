"""
O código abaixo é um exemplo de como calcular o limite de uma função usando a biblioteca SymPy em Python.
Antes de importar biblioteca SymPy
se certifique de ter essa biblioteca instalada no ambiente em que o código está sendo executadao
"""
# Nesta linha, estamos importando a biblioteca SymPy e atribuindo a ela o alias "sp".
import sympy as sp

# Aqui estamos definindo a variável x como um símbolo usando a função Symbol da biblioteca SymPy.
x = sp.Symbol('x')

# Nesta linha, estamos definindo a função f como (x^2 - 1)/(x - 1).
f = (x**2 - 1)/(x - 1)

"""
Atenção:
Por padrão, o comando limit computa o limite lateral pela direita.
Vou mostrar abaixo como calcular para ambos lados que o x se do limite.  
"""
# limite da função f quando x se aproxima de 1 pelo lado direito (padrão).
lim_dir = sp.limit(f, x, 1)
# limite da função f quando x se aproxima de 1 pelo lado esquerdo.
lim_esq = sp.limit(f, x, 1, dir='-')
# Nesta linha, estamos calculando o limite da função f quando x se aproxima de 1 pelos dois lados.
lim_com = sp.limit(f, x, 1, dir='+-')

# Nesta linha, estamos imprimindo na tela os valores dos limites.
print("Limite pela direita:", lim_dir)
print("Limite pela esquerda:", lim_esq)
print("Limite comum:", lim_com)

"""
Resumindo, o código define uma função, uma variável e calcula o limite dessa função 
para um determinado valor da variável usando a biblioteca SymPy. O resultado é exibido no console.
"""
