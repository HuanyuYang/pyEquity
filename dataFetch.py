from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import quandl
#KB7ZyJpPrzE1zPpBX7xu



def getEquityData(tickers, qopts = { 'columns': ['ticker', 'date', 'adj_close', 'adj_open', 'adj_low', 'adj_high', 'adj_volume'] }, end_date = datetime.datetime.today().strftime('%Y-%m-%d'), start_date = "2015-01-01"):
    data = quandl.get_table('WIKI/PRICES', 
                            ticker = tickers, 
                            qopts = qopts, 
                            date={'gte':start_date, 'lte':end_date},
                            api_key='KB7ZyJpPrzE1zPpBX7xu')
    data = data.set_index('date')
    data = new[::-1]
    return new

