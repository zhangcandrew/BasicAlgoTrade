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
    
    dfSPY =pnd.read_csv("data/SPY.csv", index_col="Date", parse_dates="True", usecols=['Date', 'Adj Close'], na_values=['nan'])
    df1 = df1.join(dfSPY)
    print(df1)
    
if __name__ == "__main__":
    test_run()
