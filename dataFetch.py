from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import quandl
#KB7ZyJpPrzE1zPpBX7xu



def prices(tickers, end_date = datetime.datetime.today().strftime('%Y-%m-%d'), start_date = "2015-01-01"):
    return quandl.get_table('SHARADAR/SEP', 
                            ticker = tickers, 
                            date={'gte':start_date, 'lte':end_date},
                            api_key='KB7ZyJpPrzE1zPpBX7xu')


