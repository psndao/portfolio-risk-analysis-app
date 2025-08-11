## Portfolio Risk & Performance Analyzer

<p align="center">
  <img src="demo.gif" width="700" alt="Démonstration de l'application été affichée ici"/>
</p>

<p align="center">
  <a href="https://psndao-portfolio-risk-analysis-a-analyse-du-portefeuille-xqrw6r.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀 Tester l'app Streamlit - Portfolio Analyzer-purple?style=for-the-badge" alt="Lancer l'application Streamlit">
  </a>
</p>

### Introduction

Une application développée avec **Streamlit** permettant d’analyser la performance, le risque et l’optimisation d’un portefeuille d’investissement.

...

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