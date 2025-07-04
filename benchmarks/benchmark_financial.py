import time
from mathsolver_pro import financial

print("Financial benchmarks")

# Black-Scholes pricing benchmark
S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
t0 = time.time()
for _ in range(10000):
    price = financial.black_scholes_call(S, K, T, r, sigma)
t1 = time.time()
print(f"10k Black-Scholes call prices: {t1-t0:.3f} s")

# Monte Carlo pricing benchmark
import numpy as np
t0 = time.time()
for _ in range(100):
    price = financial.monte_carlo_option(S, K, T, r, sigma, n_sim=10000)
t1 = time.time()
print(f"100 Monte Carlo (10k sim): {t1-t0:.3f} s") 