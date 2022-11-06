import pandas as pd


def change_Position(stock, buy=True):
    if buy:
        data_POS.loc[data_POS.Stock == stock, 'Position'] = 1
    else:
        data_POS.loc[data_POS.Stock == stock, 'Position'] = 0
    data_POS.to_csv('C:/Users/harsh/OneDrive/Desktop/position.csv', index=False)


def change_Quantity(stock, amount, buy=True):
    if buy:
        data_POS.loc[data_POS.Stock == stock, 'Quantity'] += amount
    else:
        data_POS.loc[data_POS.Stock == stock, 'Quantity'] += amount
    data_POS.to_csv('C:/Users/harsh/OneDrive/Desktop/position.csv', index=False)


data_POS = pd.read_csv("C:/Users/harsh/OneDrive/Desktop/position.csv")
