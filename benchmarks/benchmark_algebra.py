import numpy as np
import time
from mathsolver_pro import algebra

print("Algebra benchmarks")

# Determinant benchmark
A = np.random.rand(500, 500)
t0 = time.time()
det = algebra.determinant(A)
t1 = time.time()
print(f"Determinant of 500x500 matrix: {t1-t0:.3f} s")

# Dot product benchmark
v1 = np.random.rand(1000000)
v2 = np.random.rand(1000000)
t0 = time.time()
dot = algebra.dot_product(v1, v2)
t1 = time.time()
print(f"Dot product of 1M elements: {t1-t0:.3f} s") 