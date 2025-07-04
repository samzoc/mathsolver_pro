"""
Algebra module
==============

Core algebraic tools: quadratic equations, determinants, dot products, and more.

Examples:
>>> from mathsolver_pro import algebra
>>> algebra.solve_quadratic(1, -3, 2)
(2.0, 1.0)
>>> import numpy as np
>>> algebra.determinant(np.array([[1,2],[3,4]]))
-2.0
>>> algebra.dot_product([1,2,3], [4,5,6])
32
"""
import numpy as np

def solve_quadratic(a, b, c):
    """Solve ax^2 + bx + c = 0. Returns real roots as a tuple."""
    disc = b**2 - c*4*a
    if disc < 0:
        raise ValueError("No real roots")
    r1 = (-b + np.sqrt(disc)) / (2*a)
    r2 = (-b - np.sqrt(disc)) / (2*a)
    return (float(r1), float(r2))

def determinant(A):
    """Compute the determinant of a matrix."""
    return float(np.linalg.det(A))

def dot_product(v1, v2):
    """Compute the dot product of two vectors."""
    return float(np.dot(v1, v2)) 