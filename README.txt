# Blue-Chip Stock Supervising App

A Python-based tool for monitoring 100 leading blue-chip stocks and identifying potential buy opportunities based on historical price analysis.

This application retrieves live market data from the Yahoo Finance API, analyses the past 90 days of performance for each ticker, and flags when a stock is trading at less than 85% of its 90-day high — a potential indicator of undervaluation.

---

## Features

- **Live Market Data** – Automatically fetches the latest stock prices from Yahoo Finance.
- **Historical Analysis** – Evaluates 90 days of past performance for each ticker.
- **Customisable Ticker List** – Swap in or out stocks based on your own watchlist.
- **Automated Buy Signals** – Flags stocks trading significantly below recent highs.
- **Efficient Screening** – Quickly narrows focus to potentially undervalued blue-chip companies.

---

## Requirements

- Python 3.8 or later
- `yfinance` library
- `pandas` library

Install dependencies via:
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
yfinance
pandas
```

---

## Usage

1. **Clone this repository**
```bash
git clone https://github.com/YOUR-USERNAME/stock-supervisor.git
cd stock-supervisor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python stock_supervisor.py
```

4. **Interpret results**
- If the script finds qualifying stocks, it will print a table showing:
  - Ticker symbol
  - Current price
  - 90-day high, low, and average price
  - Date of analysis
- If no stocks meet the criteria, you’ll see:
```
No buy signals found today.
```

---

## Customisation

- Modify the `tickers` list in `stock_supervisor.py` to track your own preferred stocks.
- Adjust `buy_signal_threshold` to change the undervaluation percentage (default is `0.85`).

---

## Example Output

```
Fetching data...
Generating buy signals...

Suggested Buy Opportunities:

   Ticker  Current Price  90-day High  90-day Low  90-day Avg        Date
3   INTC         32.450        42.000       30.500      36.000  2025-08-07
7   PFE          34.120        50.000       33.500      41.220  2025-08-07
```

---

## Disclaimer

This application is for **educational purposes only**.  
It is **not financial advice**. Always conduct your own research before making investment decisions.

---

