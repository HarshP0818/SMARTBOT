import Patterns
import pandas as pd
import alpaca_trade_api as tradeapi

API_KEY = 'PKSGUNX7W09T07707ZOO'
SECRET_KEY = 'KUase87nfaRiPjA2kRJepBRQ5DcZkbWIu0YqjI8T'


class Alpaca_Trade():

    def __init__(self, API_KEY, SECRET_KEY, ticker):
        self.key = API_KEY
        self.secret = SECRET_KEY
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint, api_version='v2')
        self.symbol = ticker

        account = self.api.get_account()
        print(account.status)

        try:
            self.position = int(self.api.get_position(self.symbol().qty))
        except:
            self.position = 0
        print(f' Current Holding {self.position} {self.symbol} stocks')

    def submit_order(self, amount):
        delta = self.position

        if delta >= 0:
            buy_quantity = amount
            print(f' buying {buy_quantity} {self.symbol} shares')

            self.order = self.api.submit_order(
                symbol=self.symbol,
                qty=buy_quantity,
                type='market',
                side='buy',
                time_in_force='day'
            )
        elif delta < 0:
            sell_quantity = abs(delta)
            print(f' Selling {sell_quantity} {self.symbol} shares')

            self.order = self.api.submit_order(
                symbol=self.symbol,
                qty=sell_quantity,
                type='market',
                side='sell',
                time_in_force='day'
            )
        print("Success!")


aapl = Alpaca_Trade(API_KEY, SECRET_KEY, 'SPY')