import Quandl
import numpy as np
from datetime import date, timedelta
import pdb

def getMultiDay(ticker, duration):
    curr = date.today()  # Today's date
    past = curr - timedelta(days=duration)  # get a past date

    # Craft the Quandl Request
    data = Quandl.get(('WIKI/' + ticker),
                      authtoken='xxxxxxxxxxxxxx',
                      trim_start=str(past),
                      trim_end=str(curr),
                      exclude_headers='true',
                      returns='numpy',
                      sort_order='desc',
                      transformation = 'None')

    return data
    # Returns stock data for interval specified by duration for a stock (ident = ticker).

def getTotalDiff(ticker, duration):

    data = getMultiDay(ticker, duration)
    sz = data.size
    return (data[0][4] - data[sz-1][4])

def getPercDiff(ticker, duration):

    data = getMultiDay(ticker, duration)
    sz = data.size
    return ((data[0][4] - data[sz-1][4]) / data[sz-1][4])

if __name__ == "__main__":
    pdb.set_trace()
    data = getTotalDiff("MSFT", 5)
    print(data)


