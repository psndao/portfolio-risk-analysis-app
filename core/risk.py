import numpy as np
from scipy import stats

def calculate_var(returns, confidence_level, method, portfolio_value):
    if method == "Historical":
        var = np.percentile(returns, 100 - confidence_level)
    elif method == "Variance-Covariance":
        mu, sigma = np.mean(returns), np.std(returns)
        z = -stats.norm.ppf(1 - confidence_level / 100)
        var = -(mu + z * sigma)
    elif method == "Monte Carlo":
        mu, sigma = np.mean(returns), np.std(returns)
        sim = np.random.normal(mu, sigma, 10000)
        var = -np.percentile(sim, 100 - confidence_level)
    return var * portfolio_value

def calculate_cvar(returns, confidence_level, method, portfolio_value):
    var = calculate_var(returns, confidence_level, method, portfolio_value) / portfolio_value
    cvar = np.mean(returns[returns <= -var])
    return cvar * portfolio_value

def calculate_beta(portfolio_returns, market_returns):
    cov_matrix = np.cov(portfolio_returns, market_returns)
    return cov_matrix[0, 1] / cov_matrix[1, 1]

def calculate_max_drawdown(cumulative_returns):
    running_max = np.maximum.accumulate(cumulative_returns)
    drawdown = (cumulative_returns - running_max) / running_max
    return drawdown.min()

def calculate_sortino_ratio(returns, risk_free_rate=0.02, target=0):
    downside = np.std(returns[returns < target])
    mean_return = np.mean(returns)
    return (mean_return - risk_free_rate) / downside if downside != 0 else 0
