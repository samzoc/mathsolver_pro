"""
Financial Engineering module
===========================

Tools for derivatives pricing, risk management, portfolio optimization, stochastic simulation, and basic machine learning for finance.

Examples:
>>> from mathsolver_pro import financial
>>> financial.black_scholes_call(100, 100, 1, 0.05, 0.2)
10.4506...
>>> financial.var_historical([0.01, -0.02, 0.03, -0.01], 0.95)
-0.02
>>> financial.portfolio_mean_variance([0.1, 0.12], [[0.01, 0.002], [0.002, 0.02]])['weights']
[...]
"""
import numpy as np
import scipy.stats as stats
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S*stats.norm.cdf(d1) - K*np.exp(-r*T)*stats.norm.cdf(d2)

def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return K*np.exp(-r*T)*stats.norm.cdf(-d2) - S*stats.norm.cdf(-d1)

def binomial_option(S, K, T, r, sigma, N=100, kind='call'):
    dt = T/N
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    p = (np.exp(r*dt) - d) / (u - d)
    disc = np.exp(-r*dt)
    ST = S * u**np.arange(N, -1, -1) * d**np.arange(0, N+1, 1)
    if kind == 'call':
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)
    for _ in range(N):
        payoff = disc * (p*payoff[:-1] + (1-p)*payoff[1:])
    return payoff[0]

def monte_carlo_option(S, K, T, r, sigma, kind='call', n_sim=10000):
    Z = np.random.randn(n_sim)
    ST = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    if kind == 'call':
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)
    return np.exp(-r*T) * np.mean(payoff)

def var_historical(returns, alpha=0.95):
    returns = np.sort(returns)
    idx = int((1-alpha)*len(returns))
    return float(returns[idx])

def expected_shortfall(returns, alpha=0.95):
    returns = np.sort(returns)
    idx = int((1-alpha)*len(returns))
    if idx == 0:
        # If the slice is empty, return the worst loss (minimum return)
        return float(np.min(returns))
    return float(returns[:idx].mean())

def portfolio_mean_variance(mu, cov):
    mu, cov = np.array(mu), np.array(cov)
    n = len(mu)
    def obj(w):
        return w @ cov @ w
    cons = ({'type':'eq','fun':lambda w: w.sum()-1},)
    bounds = [(0,1)]*n
    res = minimize(obj, np.ones(n)/n, constraints=cons, bounds=bounds)
    w = res.x
    return {'weights': w, 'return': w@mu, 'risk': np.sqrt(w@cov@w)}

def simulate_gbm(S0, mu, sigma, T, N):
    dt = T/N
    t = np.linspace(0, T, N+1)
    W = np.cumsum(np.sqrt(dt)*np.random.randn(N))
    W = np.insert(W, 0, 0)
    S = S0 * np.exp((mu-0.5*sigma**2)*t + sigma*W)
    return t, S

def linear_regression(X, y):
    model = LinearRegression().fit(X, y)
    return model.coef_, model.intercept_ 