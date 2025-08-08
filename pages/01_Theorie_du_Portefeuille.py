import streamlit as st

st.set_page_config(page_title="Théorie de la Gestion de Portefeuille", layout="wide")

st.title("Théorie de la Gestion de Portefeuille")

st.markdown("""

La gestion de portefeuille est une discipline centrale de la finance moderne, combinant mathématiques, statistiques et économie comportementale. Son but principal est d’optimiser l’allocation d’actifs en équilibrant le rendement espéré et le risque pris.

En effet, avec la démocratisation des outils numériques, il devient essentiel de connecter les concepts théoriques à des applications concrètes. Cette documentation présente les bases académiques de la gestion de portefeuille et leur mise en œuvre dans notre application Streamlit interactive.

Proposée par **Harry Markowitz** en 1952, la MPT est la pierre angulaire de la gestion d'actifs moderne. 
Elle postule que, pour un niveau de risque donné, il existe une combinaison optimale d'actifs qui maximise le rendement.

La MPT repose en effet sur trois principes clés :

- Le **risque** d'un portefeuille ne se résume pas à la somme des risques individuels mais dépend des **corrélations** entre actifs.
- La **diversification** permet de réduire le risque total sans sacrifier le rendement.
- L’investisseur rationnel opère un **arbitrage rendement / risque**, en fonction de ses préférences.

Elle introduit le concept de **frontière efficiente**, représentant les portefeuilles offrant le meilleur rendement pour un niveau de risque donné.
            
> **À retenir** : les actifs ne doivent pas être sélectionnés isolément, mais en fonction de leur **interaction dans un portefeuille**.

Ce document propose une synthèse rigoureuse et pédagogique de la théorie du portefeuille et de ses applications pratiques dans un outil d'analyse interactif développé en Streamlit.


""")


st.markdown("""
####  Mise en Pratique : Application Streamlit 

Notre application "Portfolio Risk & Performance Analyzer" concrétise ces concepts via une interface intuitive et interactive. 
Elle permet à tout utilisateur débutant comme expert de configurer un portefeuille, d’analyser ses performances, d’évaluer les risques et de simuler des optimisations selon différents objectifs.
""")

st.markdown("""

""")

st.markdown("""

""")

st.markdown("""
### Conclusion

La gestion de portefeuille repose sur un équilibre entre **rendement espéré**, **volatilité**, **corrélations** et **préférences individuelles**.

Cette application permet de visualiser ces effets **en temps réel**, comparer différents portefeuilles et adopter une approche rationnelle basée sur des métriques solides.

> 🎓 Ce projet constitue un excellent outil pédagogique pour comprendre, tester et appliquer la théorie de Markowitz, le ratio de Sharpe, la VaR/CVaR et l’optimisation de portefeuille.

---

**Projet réalisé dans le cadre du Master 2 Big Data & Data Science en Finance — ESG Finance Paris**  
**Développé avec** : Python, Streamlit, NumPy, Pandas, Plotly, SciPy
""")
