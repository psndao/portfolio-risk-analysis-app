import numpy as np
import scipy.optimize as sco
import pandas as pd


def optimize_portfolio_strategy(returns_dict, strategy='sharpe', rf=0.02):
    df = pd.DataFrame(returns_dict)
    mu = df.mean()
    cov = df.cov()
    n = len(mu)

    def negative_sharpe(w):
        ret = np.dot(w, mu)
        vol = np.sqrt(np.dot(w.T, np.dot(cov, w)))
        return -(ret - rf) / vol

    def min_vol(w):
        return np.sqrt(np.dot(w.T, np.dot(cov, w)))

    def neg_return(w):
        return -np.dot(w, mu)

    obj = negative_sharpe if strategy == 'sharpe' else min_vol if strategy == 'min_volatility' else neg_return

    cons = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = [(0, 1)] * n
    init_w = np.array(n * [1 / n])

    res = sco.minimize(obj, init_w, method='SLSQP', bounds=bounds, constraints=cons)
    return res.x

def calculate_efficient_frontier(returns_dict, rf=0):
    df = pd.DataFrame(returns_dict)
    mu = df.mean()
    cov = df.cov()
    n = len(mu)

    results = np.zeros((3, 10000))
    weights_list = []

    for i in range(10000):
        w = np.random.random(n)
        w /= np.sum(w)
        weights_list.append(w)
        r = np.dot(w, mu)
        vol = np.sqrt(np.dot(w.T, np.dot(cov, w)))
        sharpe = (r - rf) / vol
        results[0, i] = r
        results[1, i] = vol
        results[2, i] = sharpe

    return results, weights_list
