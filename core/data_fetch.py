import pandas as pd
import requests
from datetime import datetime

API_KEY = '0uTB4phKEr4dHcB2zJMmVmKUcywpkxDQ'

def fetch_stock_data(ticker, start_date, end_date):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start_date}&to={end_date}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'historical' not in data or not data['historical']:
            return None, f"No data for {ticker}"
        df = pd.DataFrame(data['historical'])
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        return df['close'].values, None
    except Exception as e:
        return None, str(e)