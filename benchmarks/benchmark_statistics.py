import numpy as np
import time
from mathsolver_pro import statistics

print("Statistics benchmarks")

# Mean benchmark
arr = np.random.rand(10**7)
t0 = time.time()
mean = statistics.mean(arr)
t1 = time.time()
print(f"Mean of 10M elements: {t1-t0:.3f} s")

# Std benchmark
t0 = time.time()
std = statistics.std(arr)
t1 = time.time()
print(f"Std of 10M elements: {t1-t0:.3f} s")

# Correlation benchmark
x = np.random.rand(10**6)
y = np.random.rand(10**6)
t0 = time.time()
corr = statistics.correlation(x, y)
t1 = time.time()
print(f"Correlation of 1M elements: {t1-t0:.3f} s") 