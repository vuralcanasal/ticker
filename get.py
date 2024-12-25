# Created by VA
# To get the some financial values of the tickers via yahoo finance API

import globalParameters
import datetime
from datetime import timedelta
import yfinance as yf
import insertDB

def getPrice(ticker, name):
    daily_prices = ticker.history(start=globalParameters.priceStartDate, end=datetime.datetime.today() - timedelta(days = 1))
    for date, row in daily_prices.iterrows():
        date_string = date.strftime("%Y-%m-%d") # Convert date to string
        open_price = row.get("Open", None)
        high_price = row.get("High", None)
        low_price = row.get("Low", None)
        close_price = row.get("Close", None)
        volume = row.get("Volume", None)


        print(date_string)
        print(open_price)
        print(high_price)
        print(low_price)
        print(close_price)
        print(volume)
        insertDB.insertPrice(name, date_string, open_price, high_price, low_price, close_price, volume)



if __name__=="__main__":
    name = "FROTO"
    ticker = yf.Ticker("FROTO.IS")
    
    getPrice(ticker, name)