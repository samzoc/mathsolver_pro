import numpy as np
from mathsolver_pro import algebra

def test_solve_quadratic():
    r = algebra.solve_quadratic(1, -3, 2)
    assert set(np.round(r, 2)) == {1.0, 2.0}

def test_determinant():
    A = np.array([[1,2],[3,4]])
    assert np.isclose(algebra.determinant(A), -2.0)

def test_dot_product():
    assert algebra.dot_product([1,2,3], [4,5,6]) == 32.0 