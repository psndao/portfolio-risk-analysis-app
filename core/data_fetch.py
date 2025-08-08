import pandas as pd
import requests
from datetime import datetime
from typing import Tuple, Optional

API_KEY = '0uTB4phKEr4dHcB2zJMmVmKUcywpkxDQ'

def fetch_stock_data(ticker: str, start_date: datetime, end_date: datetime) -> Tuple[Optional[pd.Series], Optional[str]]:
    """
    Récupère les prix de clôture quotidiens pour un ticker entre deux dates.
    
    Args:
        ticker (str): Le symbole boursier (ex: 'AAPL').
        start_date (datetime): Date de début.
        end_date (datetime): Date de fin.

    Returns:
        Tuple: (série des prix de clôture, message d'erreur ou None)
    """
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}"
    params = {
        "from": start_date.strftime("%Y-%m-%d"),
        "to": end_date.strftime("%Y-%m-%d"),
        "apikey": API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'historical' not in data or not data['historical']:
            return None, f"Aucune donnée pour le ticker : {ticker}"

        df = pd.DataFrame(data['historical'])
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')

        return df['close'].values, None

    except Exception as e:
        return None, f"Erreur lors de la récupération de {ticker} : {str(e)}"
