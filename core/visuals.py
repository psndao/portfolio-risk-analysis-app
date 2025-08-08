import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def plot_returns(returns, cumulative=False):
    """
    Affiche les rendements journaliers ou cumulés du portefeuille.
    """
    y = np.cumsum(returns) if cumulative else returns
    title = "Rendements cumulés" if cumulative else "Rendements journaliers"
    fig = go.Figure(go.Scatter(y=y, mode='lines'))
    fig.update_layout(
        title=title,
        xaxis_title="Jours",
        yaxis_title="Rendement (%)"
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_correlation_heatmap(all_returns):
    """
    Affiche une heatmap de corrélation Plotly, compacte, lisible et stylée.
    """
    df_corr = pd.DataFrame(all_returns).corr()

    fig = go.Figure(
        data=go.Heatmap(
            z=df_corr.values,
            x=df_corr.columns,
            y=df_corr.columns,
            zmin=-1,
            zmax=1,
            colorscale="RdBu",
            colorbar=dict(title="Corrélation"),
            text=df_corr.round(2).values,
            hovertemplate="Corrélation %{x} / %{y} : %{z:.2f}<extra></extra>",
        )
    )

    fig.update_layout(
        title="Corrélation entre les actifs",
        xaxis=dict(title="Actifs", tickangle=0),
        yaxis=dict(title="Actifs"),
        autosize=True,
        width=600,  # ⬅️ moins large
        height=500,  # ⬅️ moins haut
        margin=dict(l=50, r=50, t=50, b=50),
    )

    st.plotly_chart(fig, use_container_width=False)


def plot_pie_charts(initial_w, optimized_w, tickers):
    """
    Affiche deux camemberts : poids initiaux vs poids optimisés.
    """
    df_init = pd.DataFrame({'Stock': tickers, 'Weight': initial_w * 100})
    df_opt = pd.DataFrame({'Stock': tickers, 'Weight': optimized_w * 100})

    df_init['Weight'] /= df_init['Weight'].sum()
    df_opt['Weight'] /= df_opt['Weight'].sum()

    fig1 = px.pie(df_init, names='Stock', values='Weight', title="Poids initiaux")
    fig2 = px.pie(df_opt, names='Stock', values='Weight', title="Poids optimisés")

    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)

def plot_portfolio_performance(before, after):
    """
    Compare la performance cumulée du portefeuille avant et après optimisation.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=np.cumsum(before), name="Avant", mode='lines'))
    fig.add_trace(go.Scatter(y=np.cumsum(after), name="Après", mode='lines'))
    fig.update_layout(
        title="Performance cumulée du portefeuille",
        xaxis_title="Jours",
        yaxis_title="Cumul des rendements"
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_efficient_frontier(results, opt_return, opt_volatility):
    """
    Affiche la frontière efficiente et le portefeuille optimal.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=results[1], y=results[0],
        mode='markers',
        marker=dict(color=results[2], colorscale='Viridis'),
        name='Portefeuilles simulés'
    ))
    fig.add_trace(go.Scatter(
        x=[opt_volatility], y=[opt_return],
        mode='markers',
        marker=dict(color='red', size=10),
        name='Portefeuille optimal'
    ))
    fig.update_layout(
        title="Frontière efficiente",
        xaxis_title="Volatilité (%)",
        yaxis_title="Rendement attendu (%)"
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_cvar_distribution(returns, var, cvar):
    """
    Affiche la distribution des rendements avec les lignes VaR et CVaR.
    """
    fig = go.Figure()

    # Histogramme des rendements
    fig.add_trace(go.Histogram(
        x=returns,
        nbinsx=50,
        name="Rendements",
        marker_color='steelblue',
        opacity=0.7
    ))

    # Lignes VaR et CVaR
    fig.add_vline(
        x=var,
        line_color="red",
        line_dash="dash",
        annotation_text="VaR",
        annotation_position="top right"
    )
    fig.add_vline(
        x=cvar,
        line_color="orange",
        line_dash="dash",
        annotation_text="CVaR",
        annotation_position="top right"
    )

    fig.update_layout(
        title="Distribution des rendements – VaR & CVaR",
        xaxis_title="Rendement",
        yaxis_title="Fréquence",
        bargap=0.05,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)
