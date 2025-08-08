## Portfolio Risk & Performance Analyzer
#  Portfolio Risk & Performance Analyzer

<p align="center">
  <img src="demo.gif" width="700" alt="Démonstration de l'application été affichée ici"/>
</p>

<p align="center">
  <a href="https://psndao-portfolio-risk-analysis-app-analyse-portefeuille--ddptrb.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀 Tester l'app Streamlit - Portfolio Analyzer-purple?style=for-the-badge" alt="Lancer l'application Streamlit">
  </a>
</p>

## 1. Introduction

Cette application interactive, réalisée en Streamlit, permet d’analyser, d’optimiser et de visualiser la gestion d’un portefeuille financier en temps réel.

👉 [Clique ici pour tester l'application en ligne](https://psndao-portfolio-risk-analysis-app-analyse-portefeuille--ddptrb.streamlit.app/)

...


Une application interactive développée avec **Streamlit** permettant d’analyser la performance, le risque et l’optimisation d’un portefeuille d’investissement.

### Objectifs

- Simuler des portefeuilles personnalisés avec des poids sur différents actifs
- Calculer automatiquement les **indicateurs de performance** (Sharpe, Sortino, Beta…)
- Évaluer les **risques financiers** via VaR, CVaR, Drawdown
- Optimiser le portefeuille selon la théorie de Markowitz (MPT)
- Visualiser les résultats de façon interactive

---


### Configuration utilisateur
- Nombre d’actifs : de 1 à 10
- Tickers personnalisés (ex : AAPL, MSFT…)
- Période d’analyse (glissante)
- Pondérations (%) ajustables
- Valeur du portefeuille (ex : 100 000 \$)

### Indicateurs calculés
- **Statistiques** :
  - Rendement moyen
  - Volatilité
  - Ratio de Sharpe
  - Sortino Ratio
  - Coefficient Beta
- **Risque** :
  - Value at Risk (VaR) : 3 méthodes (historique, paramétrique, Monte Carlo)
  - Conditional VaR (CVaR)
  - Maximum Drawdown

### Optimisation
- Méthodes disponibles :
  - Maximiser Sharpe Ratio
  - Minimiser volatilité
  - Maximiser rendement
- Résultats : nouvelle allocation optimale (SLSQP), camemberts, performances comparées

### Visualisations 
- Graphiques de rendements cumulés
- Carte de corrélation entre actifs
- Histogrammes des pertes (VaR / CVaR)
- Frontière efficiente
- Pie charts d’allocation (avant/après optimisation)

---

### Lancer l'application

### Installation des dépendances

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

pip install -r requirements.txt
