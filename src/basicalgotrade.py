# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Andrew Zhang"
__date__ = "$Jul 15, 2016 8:48:50 PM$"


import pandas as pnd

def test_run():
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates = pnd.date_range(start_date, end_date)
    df1 = pnd.DataFrame(index=dates)
    
    symbols=['GOOG', 'IBM', 'GLD', 'SPY']
    for symbol in symbols:
        df_temp=read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates="True", usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp=df_temp.rename(columns={"Adj Close": symbol})
        df1=df1.join(df_temp)
    print(df1)
    
if __name__ == "__main__":
    test_run()
