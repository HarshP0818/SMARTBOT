import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd
import Alpaca
from TradingData import change_Quantity, change_Position, data_POS


def get_data(stock_ticker_symbol, start_date, end_date):
    frame = pd.DataFrame(yf.download(stock_ticker_symbol, start_date, end_date))
    frame = frame.iloc[:, :6]
    frame.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    frame[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = frame[['Open', 'High', 'Low',
                                                                            'Close', 'Adj Close',
                                                                            'Volume']].astype(float)
    return frame


def apply_Fast_Slow(stock, start_date, end_date, qty, stock_data, last_row, position_data=data_POS):
    if last_row.FastSMA > last_row.SlowSMA:
        order = Alpaca.Alpaca_Trade(Alpaca.API_KEY, Alpaca.SECRET_KEY, stock)
        change_Position(stock, buy=True)
        while True:
            try:
                amount = int(input("Please input the quantity of stock you would like to buy: "))
            except ValueError:
                print("Sorry, invalid input")
                continue
            else:
                break
        change_Quantity(stock, amount, buy=True)
        order.submit_order(amount)

    else:
        print(f'Not in position {stock} but Condition not fulfilled')

    if last_row.FastSMA < last_row.SlowSMA:
        order = Alpaca.Alpaca_Trade(Alpaca.API_KEY, Alpaca.SECRET_KEY, stock)
        while True:
            amount = input("Please choose how many shares you would like to sell")
            if amount > qty:
                print(f'Sorry, you only have {qty} shares to sell')
                continue
            else:
                break
        change_Quantity(stock, amount, buy=False)
        if data_POS.loc[data_POS.Stock == stock, 'Quantity'] == 0:
            change_Position(stock, buy=False)
        order.submit_order(amount)
