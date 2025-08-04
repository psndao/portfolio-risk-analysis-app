import numpy as np

def calculate_metrics(returns):
    mean_return = np.mean(returns)
    std_dev = np.std(returns)
    sharpe_ratio = mean_return / std_dev if std_dev != 0 else 0
    return mean_return, std_dev, sharpe_ratio
