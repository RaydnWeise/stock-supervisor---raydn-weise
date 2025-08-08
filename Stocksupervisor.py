import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Ticker list
tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "JNJ", "V", "PG", "JPM", "UNH",
    "HD", "MA", "XOM", "ABBV", "PFE", "PEP", "KO", "AVGO", "MRK", "TMO",
    "LLY", "COST", "BAC", "WMT", "CVX", "ADBE", "ACN", "CSCO", "INTC", "MCD",
    "TXN", "DHR", "LIN", "UNP", "NEE", "PM", "NKE", "QCOM", "MDT", "AMGN",
    "HON", "UPS", "IBM", "BA", "MS", "GS", "RTX", "CAT", "BLK", "LMT",
    "SPGI", "AXP", "DE", "LOW", "SBUX", "ORCL", "GILD", "PLD", "ISRG", "CB",
    "TGT", "ADP", "MO", "AMAT", "BKNG", "ZTS", "EL", "CI", "MDLZ", "SYK", "ADI",
    "C", "MMC", "VRTX", "SO", "REGN", "APD", "CL", "BDX", "FISV", "PSA",
    "ECL", "AON", "FDX", "WM", "ADI", "TFC", "ITW", "EW", "ALL", "PGR",
    "AEP", "NSC", "COF", "BIIB", "STZ", "MCO", "EXC", "HCA", "D", "ED" "VTI"
]

# Parameters
days_of_history = 90  # 90 days to analyse
buy_signal_threshold = 0.85  # Buy when price is below 85% of 90 day high - context of course matters, do deeper analysis on why dips occur

def fetch_data(tickers):
    data = yf.download(tickers, period=f"{days_of_history}d", interval="1d", group_by='ticker', threads=True)
    return data

def generate_signals(data):
    buy_signals = []
    today = datetime.now().strftime('%Y-%m-%d')

    for ticker in tickers:
        try:
            stock_data = data[ticker]['Close'].dropna()
            current_price = stock_data.iloc[-1]
            high_90 = stock_data.max()
            low_90 = stock_data.min()
            avg_price = stock_data.mean()

            # Buy signal: if current price is under 85% of 90-day high
            if current_price < buy_signal_threshold * high_90:
                buy_signals.append({
                    'Ticker': ticker,
                    'Current Price': current_price,
                    '90-day High': high_90,
                    '90-day Low': low_90,
                    '90-day Avg': avg_price,
                    'Date': today
                })
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
    
    return pd.DataFrame(buy_signals)

def main():
    print("Fetching data...")
    data = fetch_data(tickers)
    print("Generating buy signals...")
    signals = generate_signals(data)
    if not signals.empty:
        print("\nSuggested Buy Opportunities:\n")
        print(signals.sort_values(by='Current Price'))
    else:
        print("No buy signals found today.")

if __name__ == '__main__':
    main()
