"""
Financial module usage example
=============================

Demonstrates Black-Scholes pricing, VaR, and mean-variance portfolio optimization.
"""
from mathsolver_pro import financial

# Black-Scholes call price
call = financial.black_scholes_call(100, 100, 1, 0.05, 0.2)
print(f"Black-Scholes call price: {call:.4f}")  # Expected: ~10.4506

# Historical VaR
returns = [0.01, -0.02, 0.03, -0.01]
var = financial.var_historical(returns, 0.95)
print(f"Historical VaR (95%): {var}")  # Expected: -0.02

# Mean-variance portfolio optimization
mu = [0.1, 0.12]
cov = [[0.01, 0.002], [0.002, 0.02]]
res = financial.portfolio_mean_variance(mu, cov)
print(f"Optimal weights: {res['weights']}, expected return: {res['return']}, risk: {res['risk']}") 