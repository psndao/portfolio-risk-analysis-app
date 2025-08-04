import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

def plot_returns(returns):
    fig = go.Figure(go.Scatter(y=returns, mode='lines'))
    fig.update_layout(title="Portfolio Returns", xaxis_title="Days", yaxis_title="Returns")
    st.plotly_chart(fig)

def plot_correlation_heatmap(all_returns):
    corr = pd.DataFrame(all_returns).corr()
    fig = go.Figure(go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns, colorscale='viridis'))
    st.plotly_chart(fig)

def plot_cvar_distribution(returns, var, cvar):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=returns, nbinsx=50))
    fig.add_vline(x=var, line_color="red", name="VaR")
    fig.add_vline(x=cvar, line_color="orange", name="CVaR")
    fig.update_layout(title="VaR & CVaR Distribution")
    st.plotly_chart(fig)

def plot_pie_charts(initial_w, optimized_w, tickers):
    df_init = pd.DataFrame({'Stock': tickers, 'Weight': initial_w * 100})
    df_opt = pd.DataFrame({'Stock': tickers, 'Weight': optimized_w * 100})
    fig1 = px.pie(df_init, names='Stock', values='Weight', title="Initial Weights")
    fig2 = px.pie(df_opt, names='Stock', values='Weight', title="Optimized Weights")
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

def plot_portfolio_performance(before, after):
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=np.cumsum(before), name="Before"))
    fig.add_trace(go.Scatter(y=np.cumsum(after), name="After"))
    fig.update_layout(title="Portfolio Performance", yaxis_title="Cumulative Return")
    st.plotly_chart(fig)

def plot_efficient_frontier(results, opt_r, opt_vol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=results[1], y=results[0], mode='markers', marker=dict(color=results[2], colorscale='Viridis'), name='Portfolios'))
    fig.add_trace(go.Scatter(x=[opt_vol], y=[opt_r], mode='markers', marker=dict(color='red', size=10), name='Optimized'))
    fig.update_layout(title="Efficient Frontier", xaxis_title="Volatility", yaxis_title="Return")
    st.plotly_chart(fig)
