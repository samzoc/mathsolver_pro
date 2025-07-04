"""
Algebra module usage example
===========================

Demonstrates solving a quadratic equation, computing a determinant, and a dot product.
"""
from mathsolver_pro import algebra
import numpy as np

# Solve a quadratic equation
roots = algebra.solve_quadratic(1, -3, 2)
print(f"Roots of x^2 - 3x + 2 = 0: {roots}")  # Expected: (2.0, 1.0)

# Compute the determinant of a matrix
A = np.array([[1, 2], [3, 4]])
det = algebra.determinant(A)
print(f"Determinant of A: {det}")  # Expected: -2.0

# Compute the dot product of two vectors
v1 = [1, 2, 3]
v2 = [4, 5, 6]
dot = algebra.dot_product(v1, v2)
print(f"Dot product: {dot}")  # Expected: 32.0 