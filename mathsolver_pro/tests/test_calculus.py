import numpy as np
import sympy as sp
from mathsolver_pro import calculus

def test_derivative():
    x = sp.symbols('x')
    assert calculus.derivative(x**2 + 2*x) == 2*x + 2

def test_numeric_derivative():
    f = lambda x: x**2
    assert np.isclose(calculus.numeric_derivative(f, 2), 4, atol=1e-4)

def test_integral():
    x = sp.symbols('x')
    assert calculus.integral(x**2) == x**3/3

def test_definite_integral():
    x = sp.symbols('x')
    res = calculus.definite_integral(x, 0, 2)
    assert np.isclose(float(res), 2.0)

def test_numeric_integral():
    f = lambda x: x
    assert np.isclose(calculus.numeric_integral(f, 0, 2), 2.0, atol=1e-3)

def test_limit():
    x = sp.symbols('x')
    assert calculus.limit(sp.sin(x)/x, 0) == 1

def test_numeric_limit():
    f = lambda x: np.sin(x)/x if x != 0 else 1
    assert np.isclose(calculus.numeric_limit(f, 0), 1, atol=1e-3)

def test_minimize():
    f = lambda x: (x-2)**2
    x_min, f_min = calculus.minimize(f, 0)
    assert np.isclose(x_min, 2, atol=1e-2)

def test_maximize():
    f = lambda x: -(x-2)**2
    x_max, f_max = calculus.maximize(f, 0)
    assert np.isclose(x_max, 2, atol=1e-2)

def test_solve_ode():
    fun = lambda t, y: -y
    t, y, success = calculus.solve_ode(fun, (0, 1), [1.0], t_eval=[0, 1])
    assert np.isclose(y[0][0], 1.0)
    assert success 