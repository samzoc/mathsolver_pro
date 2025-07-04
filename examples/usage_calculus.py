"""
Calculus module usage example
============================

Demonstrates symbolic derivative, numeric integral, limit, and minimization.
"""
from mathsolver_pro import calculus
import sympy as sp

x = sp.symbols('x')

# Symbolic derivative
expr = x**2 + 2*x
der = calculus.derivative(expr)
print(f"Derivative of x^2 + 2x: {der}")  # Expected: 2*x + 2

# Numeric integral
def f(x):
    return x
integral = calculus.numeric_integral(f, 0, 2)
print(f"Integral of x from 0 to 2: {integral}")  # Expected: 2.0

# Limit
lim = calculus.limit(sp.sin(x)/x, 0)
print(f"Limit of sin(x)/x as x->0: {lim}")  # Expected: 1

# Minimize a function
min_x, min_val = calculus.minimize(lambda x: (x-2)**2, 0)
print(f"Minimum of (x-2)^2: x={min_x}, value={min_val}")  # Expected: x=2, value=0 