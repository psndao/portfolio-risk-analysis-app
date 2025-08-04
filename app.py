import streamlit as st
from datetime import datetime, timedelta
from core.data_fetch import fetch_stock_data
from core.performance import calculate_metrics
from core.risk import calculate_var, calculate_cvar, calculate_beta, calculate_max_drawdown, calculate_sortino_ratio
from core.optimization import optimize_portfolio_strategy, calculate_efficient_frontier
from core.visuals import plot_returns, plot_correlation_heatmap, plot_cvar_distribution, plot_pie_charts, plot_portfolio_performance, plot_efficient_frontier
import numpy as np
import pandas as pd

# App config
st.set_page_config(page_title="Portfolio Analyzer", layout="wide")

# Sidebar - Portfolio Configuration
st.sidebar.header("Portfolio Configuration")
portfolio_value = st.sidebar.number_input("Portfolio Value (USD)", 10000.0)
n = st.sidebar.slider("Number of Stocks", 1, 10, 2)

stock_names, weights = [], []
for i in range(n):
    col1, col2 = st.sidebar.columns(2)
    with col1:
        stock = st.text_input(f"Ticker {i+1}", key=f"ticker_{i}")
    with col2:
        weight = st.number_input(f"Weight % {i+1}", 0.0, 100.0, 100.0 if i==0 else 0.0, key=f"weight_{i}")
    stock_names.append(stock)
    weights.append(weight)

total_weight = sum(weights)
if total_weight > 100:
    st.sidebar.error("Total weight > 100%")
elif total_weight < 100:
    st.sidebar.warning("Total weight < 100%")

# Dates
end_date = datetime.today()
start_date = end_date - timedelta(days=365)
start_date = st.sidebar.date_input("Start Date", start_date)
end_date = st.sidebar.date_input("End Date", end_date)

# Fetch data
if st.sidebar.button("Fetch Data"):
    if abs(total_weight - 100) > 0.01:
        st.sidebar.error("Weights must sum to 100%")
    else:
        returns_dict, portfolio_returns = {}, []
        min_len = None

        for i, ticker in enumerate(stock_names):
            prices, err = fetch_stock_data(ticker, start_date, end_date)
            if prices is not None:
                returns = np.diff(prices) / prices[:-1]
                min_len = len(returns) if min_len is None else min(min_len, len(returns))
                returns_dict[ticker] = returns
                portfolio_returns.append(returns * (weights[i] / 100))
            else:
                st.error(err)
                break

        if returns_dict:
            aligned_returns = {k: v[:min_len] for k, v in returns_dict.items()}
            portfolio_returns = [r[:min_len] for r in portfolio_returns]
            st.session_state['portfolio_returns'] = np.sum(portfolio_returns, axis=0)
            st.session_state['all_returns'] = aligned_returns
            st.success("Data fetched successfully")

# Metrics & Risk Analysis
if st.button("Calculate Metrics"):
    if 'portfolio_returns' in st.session_state:
        r = st.session_state['portfolio_returns']
        mean_r, std_r, sharpe = calculate_metrics(r)
        st.metric("Mean Return", f"{mean_r:.4f}")
        st.metric("Volatility", f"{std_r:.4f}")
        st.metric("Sharpe Ratio", f"{sharpe:.4f}")

        method = st.selectbox("VaR Method", ["Historical", "Variance-Covariance", "Monte Carlo"])
        confidence = st.slider("Confidence Level", 90, 99, 95)
        var = calculate_var(r, confidence, method, portfolio_value)
        cvar = calculate_cvar(r, confidence, method, portfolio_value)
        st.write(f"**VaR**: {var:.2f}, **CVaR**: {cvar:.2f}")

        plot_returns(r)
        plot_cvar_distribution(r, var / portfolio_value, cvar / portfolio_value)
        plot_correlation_heatmap(st.session_state['all_returns'])

        market = st.text_input("Market Index (e.g. SPY)", "SPY")
        market_data, _ = fetch_stock_data(market, start_date, end_date)
        if market_data is not None:
            mkt_returns = np.diff(market_data) / market_data[:-1]
            mkt_returns = mkt_returns[:len(r)]
            beta = calculate_beta(r, mkt_returns)
            drawdown = calculate_max_drawdown(np.cumsum(r))
            sortino = calculate_sortino_ratio(r, 0.02)
            st.write(f"**Beta**: {beta:.4f}, **Max Drawdown**: {drawdown:.4f}, **Sortino Ratio**: {sortino:.4f}")

# Optimization
st.sidebar.header("Optimization")
if st.sidebar.checkbox("Run Portfolio Optimization"):
    if 'all_returns' in st.session_state:
        strategy = st.sidebar.selectbox("Strategy", ["sharpe", "min_volatility", "max_return"])
        all_r = st.session_state['all_returns']
        optimized_weights = optimize_portfolio_strategy(all_r, strategy)
        results, _ = calculate_efficient_frontier(all_r)

        df = pd.DataFrame(all_r)
        mu, cov = df.mean(), df.cov()
        ret_opt = np.dot(optimized_weights, mu)
        vol_opt = np.sqrt(np.dot(optimized_weights.T, np.dot(cov, optimized_weights)))

        init_weights = np.array([w / 100 for w in weights])
        plot_pie_charts(init_weights, optimized_weights, stock_names)
        plot_efficient_frontier(results, ret_opt, vol_opt)
        r_before = np.dot(df.values, init_weights)
        r_after = np.dot(df.values, optimized_weights)
        plot_portfolio_performance(r_before, r_after)
