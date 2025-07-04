import numpy as np
import time
from mathsolver_pro import calculus

print("Calculus benchmarks")

# Numeric derivative benchmark
f = lambda x: np.sin(x) + np.log(x+10)
t0 = time.time()
der = calculus.numeric_derivative(f, 1000)
t1 = time.time()
print(f"Numeric derivative at x=1000: {t1-t0:.5f} s")

# Numeric integral benchmark
t0 = time.time()
I = calculus.numeric_integral(np.sin, 0, 100, n=100000)
t1 = time.time()
print(f"Numeric integral on [0,100]: {t1-t0:.3f} s")

# Minimization benchmark
t0 = time.time()
xmin, fmin = calculus.minimize(lambda x: np.sin(x)+0.1*x**2, 2)
t1 = time.time()
print(f"Minimization: {t1-t0:.3f} s, x_min={xmin:.2f}") 