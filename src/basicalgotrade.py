# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Andrew Zhang"
__date__ = "$Jul 15, 2016 8:48:50 PM$"


import pandas as pnd
import matplotlib.pyplot as plt

def plot_selected(df, start_index, end_index, columns):
    plot_data(df.ix[start_index:end_index, columns])

def get_data(symbols, dates):
    df = pnd.DataFram(index=dates)
    for symbol in symbols:
        #loops through and parses the dates in the columns, using them as an index, and joins it to the main dataframe.
        df_temp=read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates="True", usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp=df_temp.rename(columns={"Adj Close": symbol})
        df=df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])
            
    return df

def normalize_data(df):
    #normalizes the data for a common starting point
    return df/df.ix[0,:]
    
#plots the data into a graph with proper parameters
def plot_data(df, title):
    df.plot(title)
    df.set_xlabel("Date")
    df.set_ylabel("Price")
    plt.show()


def test_run():
    dates = pnd.date_range('2010-01-01','2010-12-31')
    symbols=['GOOG', 'IBM', 'GLD', 'SPY']
    get_data(symbols, dates)
    
if __name__ == "__main__":
    test_run()
