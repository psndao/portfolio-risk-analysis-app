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
st.set_page_config(page_title="Analyse de Risque & Performance de Portefeuille", layout="wide")
st.title("Analyse de Risque & Performance de Portefeuille")
st.markdown("""
Bienvenue dans notre application d'optimisation de Portefeuille Multi-Actifs selon la MPT et Analyse des Risques développée avec **Streamlit**.

### Fonctionnalités principales :
- Configuration dynamique du portefeuille
- Récupération des données de marché en temps réel
- Calculs de **rendement**, **volatilité**, **Sharpe ratio**
- Analyse des risques : **VaR**, **CVaR**, **Drawdown**, **Beta**, **Sortino**
- Optimisation d’allocation selon la **théorie moderne des portefeuilles (MPT)**
- Visualisations : courbes, heatmaps, camemberts, frontière efficiente

> Cette application est conçue comme un outil pédagogique pour explorer les concepts clés de la gestion de portefeuille.

---
""")



# Sidebar - Portfolio Configuration
st.sidebar.header("Configuration du portefeuille")
portfolio_value = st.sidebar.number_input("Valeur du portefeuille (USD)", 10000.0)
n = st.sidebar.slider("Nombre d’actions", 1, 10, 2)

stock_names, weights = [], []
for i in range(n):
    col1, col2 = st.sidebar.columns(2)
    with col1:
        stock = st.text_input(f"Ticker {i+1}", key=f"ticker_{i}")
    with col2:
        default_weight = round(100.0 / n, 2)
        weight = st.number_input(f"Poids % {i+1}", 0.0, 100.0, default_weight, key=f"weight_{i}")
    stock_names.append(stock)
    weights.append(weight)

total_weight = sum(weights)
if total_weight > 100:
    st.sidebar.error("Total weight > 100%")
elif total_weight < 100:
    st.sidebar.warning("Total weight < 100%")
else:
    st.sidebar.success("Répartition correcte à 100%")


# Dates
end_date = datetime.today()
start_date = end_date - timedelta(days=365)
start_date = st.sidebar.date_input("Start Date", start_date)
end_date = st.sidebar.date_input("End Date", end_date)

# Fetch data
if st.sidebar.button("Extraction des données"):
    if abs(total_weight - 100) > 0.01:
        st.sidebar.error("Les poids doivent totaliser 100%")
    else:
        returns_dict, portfolio_returns = {}, []
        min_len = None

        for i, ticker in enumerate(stock_names):
            if not ticker:
                st.warning(f"Ticker {i+1} est vide — ignoré")
                continue

            prices, err = fetch_stock_data(ticker, start_date, end_date)
            if prices is not None and len(prices) > 1:
                returns = np.diff(prices) / prices[:-1]
                min_len = len(returns) if min_len is None else min(min_len, len(returns))
                returns_dict[ticker] = returns
                portfolio_returns.append(returns * (weights[i] / 100))
            else:
                st.error(f"Erreur pour {ticker}: {err or 'Pas assez de données'}")
                continue

        if returns_dict:
            aligned_returns = {k: v[:min_len] for k, v in returns_dict.items()}
            portfolio_returns = [r[:min_len] for r in portfolio_returns]

            st.session_state['portfolio_returns'] = np.sum(portfolio_returns, axis=0)
            st.session_state['all_returns'] = aligned_returns
            st.success("Extraction des données réussie.")
        else:
            st.error("Aucune donnée valide extraite.")

# Metrics & Risk Analysis

# --- Calcul des métriques ---
if st.button("Calcul métriques"):
    if 'portfolio_returns' in st.session_state:
        r = st.session_state['portfolio_returns']
        mean_r, std_r, sharpe = calculate_metrics(r)
        st.session_state['metrics'] = {
            'r': r,
            'mean_r': mean_r,
            'std_r': std_r,
            'sharpe': sharpe
        }

# --- Affichage uniquement si les métriques existent ---
if 'metrics' in st.session_state:

    # Créer les onglets ici
    tab1, tab2, tab3, tab4 = st.tabs(["Performance", "Risques", "Optimisation", "Lexique"])

    # === Onglet 1 : Performance ===
    with tab1:
        st.subheader("Indicateurs de Performance")
        r = st.session_state['metrics']['r']
        mean_r = st.session_state['metrics']['mean_r']
        std_r = st.session_state['metrics']['std_r']
        sharpe = st.session_state['metrics']['sharpe']

        col1, col2, col3 = st.columns(3)
        col1.metric("Rendement moyen", f"{mean_r:.4f}")
        col2.metric("Volatilité", f"{std_r:.4f}")
        col3.metric("Sharpe Ratio", f"{sharpe:.4f}")

        plot_returns(r)

    # === Onglet 2 : Risques ===
    with tab2:
        st.subheader("Analyse des Risques")
        r = st.session_state['metrics']['r']

        method = st.selectbox("Méthode VaR", ["Historical", "Variance-Covariance", "Monte Carlo"])
        confidence = st.slider("Niveau de confiance", 90, 99, 95)
        var = calculate_var(r, confidence, method, portfolio_value)
        cvar = calculate_cvar(r, confidence, method, portfolio_value)

        col4, col5 = st.columns(2)
        col4.metric(f"VaR ({confidence}%)", f"{var:.2f} USD")
        col5.metric("CVaR", f"{cvar:.2f} USD")

        plot_cvar_distribution(r, var / portfolio_value, cvar / portfolio_value)

        if st.checkbox("Afficher la matrice de corrélation (tableau)"):
            df_corr = pd.DataFrame(st.session_state['all_returns']).corr()
            st.dataframe(df_corr.style.format("{:.2f}").background_gradient(cmap='RdBu', axis=None, vmin=-1, vmax=1))

    # === Onglet 3 : Optimisation ===
    with tab3:
        st.subheader("Optimisation du portefeuille")

        if 'all_returns' in st.session_state:
            strategy = st.selectbox("Stratégie", ["sharpe", "min_volatility", "max_return"])
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

    #  === Onglet 4 : Lexique ===
    with tab4:
        st.subheader("Explication des indicateurs financiers")
        st.markdown("""
        #### Indicateurs de performance
        - **Rendement moyen** : moyenne des rendements journaliers du portefeuille.
        - **Volatilité** : écart-type des rendements → mesure du **risque total**.
        - **Ratio de Sharpe** : rendement excédentaire rapporté à la volatilité.

        #### Indicateurs de risque
        - **VaR (Value at Risk)** : perte maximale attendue avec un niveau de confiance donné.
        - **CVaR (Conditional VaR)** : perte moyenne au-delà de la VaR.

        #### Indicateurs avancés
        - **Bêta** : sensibilité du portefeuille aux variations du marché.
        - **Max Drawdown** : perte maximale depuis un sommet.
        - **Ratio de Sortino** : Sharpe ajusté des pertes uniquement.
        """)