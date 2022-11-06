# # https://blog.quantinsti.com/historical-market-data-python-api/
# STEP 1: Getting the dataset. For this we use yahoo finance
# Import yfinance and matplotlib
import numpy
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

import Patterns
import pandas as pd
import Alpaca


# Get the data for the SPY ETF by specifying the stock ticker, start date, and end date


# Plot the close prices


#
# # Get the data for the SPY (an ETF on the S&P 500 index) and the stock Apple by specifying the stock ticker,
# # start date, and end date
# data = yf.download(['SPY', 'AAPL'], '2020-01-01', '2020-12-06')
# # Plot the adjusted close prices
# data["Adj Close"].plot()
# plt.show()
#
# # Get the data for the stock Apple by specifying the stock ticker, start date, and end date
# data = yf.download(['BTC-USD', 'EURUSD=X', 'AAPL210115C00018750', 'CL=F', 'ARKK', '^TNX'], '2020-01-01', '2020-12-31')
# data["Adj Close"].tail()
#
# data = yf.download(
#     tickers=['BTC-USD'],
#     # use "period" instead of start/end
#     # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#     # (optional, default is '1mo')
#     period="5d",
#     # fetch data by interval (including intraday if period < 60 days)
#     # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#     # (optional, default is '1d')
#     interval="1m")
# # Plot the close prices
# data.Close.plot()
# plt.show()


# function to change the position of our current portfolio

# @param stock is used to define which stock to use. insert string
# @start_date and end_date are also strings. Use this format: '0000-00-00', year-month-date
from TradingData import data_POS


def trader(stock, start_date, end_date, position_data=data_POS):
    qty = position_data[position_data.Stock == stock].Quantity.values[0]
    stock_data = Patterns.get_data(stock, start_date, end_date)
    stock_data['FastSMA'] = stock_data.Close.rolling(7).mean()
    stock_data['SlowSMA'] = stock_data.Close.rolling(25).mean()
    last_row = stock_data.iloc[-1]
    Patterns.apply_Fast_Slow(stock, start_date, end_date, qty, stock_data, last_row)


trader('SPY', '2000-01-01', '2020-01-01')
