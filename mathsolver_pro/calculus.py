"""
Calculus module
==============

Symbolic and numeric calculus: derivatives, integrals, limits, optimization, ODEs, and plotting.

Examples:
>>> from mathsolver_pro import calculus
>>> import sympy as sp
>>> x = sp.symbols('x')
>>> calculus.derivative(x**2 + 2*x)
2*x + 2
>>> calculus.numeric_integral(lambda x: x, 0, 2)
2.0
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, integrate

def derivative(expr, var='x'):
    x = sp.symbols(var)
    return sp.diff(expr, x)

def numeric_derivative(f, x0, h=1e-5):
    return (f(x0 + h) - f(x0 - h)) / (2 * h)

def integral(expr, var='x'):
    x = sp.symbols(var)
    return sp.integrate(expr, x)

def definite_integral(expr, a, b, var='x'):
    x = sp.symbols(var)
    return sp.integrate(expr, (x, a, b))

def numeric_integral(f, a, b, n=1000):
    x = np.linspace(a, b, n)
    y = np.vectorize(f)(x)
    return np.trapz(y, x)

def limit(expr, x0, var='x', direction='+'):
    x = sp.symbols(var)
    return sp.limit(expr, x, x0, dir=direction)

def numeric_limit(f, x0, h=1e-5):
    return (f(x0 + h) + f(x0 - h)) / 2

def minimize(f, x0):
    res = optimize.minimize(f, x0)
    return res.x[0], res.fun

def maximize(f, x0):
    f_neg = lambda x: -f(x)
    res = optimize.minimize(f_neg, x0)
    return res.x[0], -res.fun

def solve_ode(fun, t_span, y0, t_eval=None, method='RK45'):
    from scipy.integrate import solve_ivp
    sol = solve_ivp(fun, t_span, y0, t_eval=t_eval, method=method)
    return sol.t, sol.y, sol.success

def plot_function(f, a, b, n=1000, label="f(x)", show=True):
    x = np.linspace(a, b, n)
    y = np.vectorize(f)(x)
    plt.plot(x, y, label=label)
    plt.xlabel("x")
    plt.ylabel(label)
    plt.legend()
    if show:
        plt.show()
    return x, y

def plot_derivative(f, a, b, n=1000, h=1e-5, show=True):
    def df(x):
        return (f(x + h) - f(x - h)) / (2 * h)
    x, y = plot_function(df, a, b, n, label="f'(x)", show=show)
    return x, y

def plot_integral(f, a, b, n=1000, show=True):
    x = np.linspace(a, b, n)
    y = np.vectorize(f)(x)
    y_int = np.cumsum(y) * (x[1] - x[0])
    plt.plot(x, y_int, label="integral")
    if show:
        plt.show()
    return x, y_int 