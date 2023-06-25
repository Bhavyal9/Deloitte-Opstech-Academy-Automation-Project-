from __future__ import print_function	# For Py2/3 compatibility
import eel
import yfinance as yf
import pandas as pd
from datetime import date


# Set web files folder
eel.init('web')


@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    enddate = pd.to_datetime(x) + pd.DateOffset(days=1)
    data = []

    with open('myList.csv', newline='') as f:
        lines = f.readlines()

        for line in lines[1:]:
            row = line.strip().split(',')
            data.append(row)

    data1 = pd.DataFrame(data)

    newData = data1[0]

    newData = newData[:]
    symbols = ' '.join(newData.astype(str))

    data1 = pd.DataFrame()
    for symbol in newData:
        try:
            ticker = yf.Ticker(symbol)
            tickerInfo = ticker.history(start=x, end = enddate, actions=False)
            tickerInfo['Symbol'] = symbol  # Add a 'Symbol' column to identify the ticker symbol
            tickerInfo.reset_index(inplace=True)  # Reset the index to include the 'Date' column
            data1 = data1._append(tickerInfo, ignore_index=True)  # Append the tickerInfo to the data1 DataFrame
        except IndexError:
            print(f"No data found for {symbol}. The symbol may be delisted or there is no data available for the specified date range.")

    print(data1)


    # data2 = data1.drop('Adj Close',axis=1)

    data1.set_index('Symbol', inplace = True)

    data1.to_csv("dataspread"+x+".csv")



eel.start('hello.html', size=(1000, 1000))    # Start