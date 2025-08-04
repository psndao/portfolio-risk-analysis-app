# Portfolio Risk Analysis App

## Overview
The Portfolio Risk Analysis App is a comprehensive tool designed to analyze investment portfolios. Built using Streamlit, this application allows users to input portfolio details, retrieve historical stock data, and analyze various risk and performance metrics. The tool also includes portfolio optimization features and advanced risk analysis capabilities.

## Features
- **Portfolio Configuration**: Users can input the total portfolio value, select the number of stocks, and specify their tickers and weights.
- **Historical Data Retrieval**: Fetches historical stock data for the specified date range.
- **Performance Indicators**: Calculates key metrics such as Compound Annual Growth Rate (CAGR), volatility, and Sharpe ratio for individual stocks and the overall portfolio.
- **Correlation Heatmap**: Visualizes the correlation between the returns of different stocks in the portfolio.
- **Portfolio Optimization**: Offers strategies to maximize the Sharpe ratio, minimize volatility, or maximize returns.
- **Risk Analysis**: Provides detailed risk measures, including Value at Risk (VaR) and Conditional Value at Risk (CVaR).
- **Monte Carlo Simulation**: Simulates future portfolio returns to evaluate potential outcomes.
- **Stress Testing**: Analyzes the impact of extreme market scenarios on portfolio performance.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd portfolio-risk-analysis-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command in your terminal:
```
streamlit run src/app.py
```
Once the application is running, you can configure your portfolio, retrieve data, and perform analyses through the user interface.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.