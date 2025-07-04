import numpy as np
from mathsolver_pro import financial

def test_black_scholes_call():
    price = financial.black_scholes_call(100, 100, 1, 0.05, 0.2)
    assert np.isclose(price, 10.4506, atol=1e-3)

def test_black_scholes_put():
    price = financial.black_scholes_put(100, 100, 1, 0.05, 0.2)
    assert np.isclose(price, 5.5735, atol=1e-3)

def test_binomial_option():
    price = financial.binomial_option(100, 100, 1, 0.05, 0.2, N=100, kind='call')
    assert np.isclose(price, 10.45, atol=0.1)

def test_monte_carlo_option():
    price = financial.monte_carlo_option(100, 100, 1, 0.05, 0.2, kind='call', n_sim=10000)
    assert np.isclose(price, 10.45, atol=0.5)

def test_var_historical():
    returns = [0.01, -0.02, 0.03, -0.01]
    var = financial.var_historical(returns, 0.95)
    assert np.isclose(var, -0.02)

def test_expected_shortfall():
    returns = [0.01, -0.02, 0.03, -0.01]
    es = financial.expected_shortfall(returns, 0.95)
    assert es <= -0.015

def test_portfolio_mean_variance():
    mu = [0.1, 0.12]
    cov = [[0.01, 0.002], [0.002, 0.02]]
    res = financial.portfolio_mean_variance(mu, cov)
    assert np.isclose(res['weights'].sum(), 1)
    assert res['risk'] > 0

def test_simulate_gbm():
    t, S = financial.simulate_gbm(100, 0.05, 0.2, 1, 10)
    assert len(t) == len(S)

def test_linear_regression():
    X = np.array([[1],[2],[3]])
    y = np.array([2,4,6])
    coef, intercept = financial.linear_regression(X, y)
    assert np.isclose(coef[0], 2) 