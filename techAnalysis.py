import matplotlib.pyplot as plt
import pandas as pd
import datetime
import quandl
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot




def bollingerLines(initdata):
    data = initdata.copy()
    data['30 Day MA'] = data['adj_close'].rolling(window=20).mean()
    data['30 Day STD'] = data['adj_close'].rolling(window=20).std()
    data['Upper Band'] = data['30 Day MA'] + (data['30 Day STD'] * 2)
    data['Lower Band'] = data['30 Day MA'] - (data['30 Day STD'] * 2)
    data[['adj_close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(24,12))
    plt.title('30 Day Bollinger Band ')
    plt.ylabel('Price (USD)')

    plt.show();
    return data



def bollingerBand(initData):
    data = initData.copy()
    data['30 Day MA'] = data['adj_close'].rolling(window=20).mean()
    data['30 Day STD'] = data['adj_close'].rolling(window=20).std()
    data['Upper Band'] = data['30 Day MA'] + (data['30 Day STD'] * 2)
    data['Lower Band'] = data['30 Day MA'] - (data['30 Day STD'] * 2)

    plt.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(24,12))
    ax = fig.add_subplot(111)

    # Get index values for the X axis for facebook DataFrame
    x_axis = data.index.get_level_values(0)

    # Plot shaded 21 Day Bollinger Band for Facebook
    ax.fill_between(x_axis, data['Upper Band'], data['Lower Band'], color='grey')

    # Plot Adjust Closing Price and Moving Averages
    ax.plot(x_axis, data['adj_close'], color='blue', lw=2)
    ax.plot(x_axis, data['30 Day MA'], color='black', lw=2)

    # Set Title & Show the Image
    ax.set_title('30 Day Bollinger Band')
    ax.set_xlabel('Date (Year/Month)')
    ax.set_ylabel('Price(USD)')
    ax.legend()
    plt.show();
    return data


def mostCorrelatedEquities(input_data, target, n = 10):
    record = pd.DataFrame()
    for col in input_data.columns:
        record[col] = pd.Series(input_data[target].corr(input_data[col]))
    record.iloc[0].nlargest(12)
    return record.iloc[0].nlargest(n)
        
def leastCorrelatedEquities(input_data, target, n = 10):
    record = pd.DataFrame()
    for col in input_data.columns:
        record[col] = pd.Series(input_data[target].corr(input_data[col]))
    return record.iloc[0].nsmallest(n)

def mostIncreasedEquities(data, window = 100, n = 10):
    
    increase_percent = ((data.iloc[-1] - data.iloc[-window])/data.iloc[-1-window]).nlargest(n)
    increase_percent = toPercentage(increase_percent, 2)
    return increase_percent, data.index[-window], data.index[-1]

def mostDecreasedEquities(data, window = 100, n = 10):
    increase_percent = ((data.iloc[-1] - data.iloc[-window])/data.iloc[-1-window]).nsmallest(n)
    increase_percent = toPercentage(increase_percent, 2)
    return increase_percent, data.index[-window], data.index[-1]

def mostVolatile(data, window = 20, n = 10):
    volatility = data[-window:].rolling(window=window).std().iloc[-1].nlargest(n)
    return volatility

def leastVolatile(data, window = 20, n = 10):
    volatility = data[-window:].rolling(window=window).std().iloc[-1].nsmallest(n)
    return volatility

def toPercentage(data, digit = 2):
    target_format = "{0:." + str(digit) + "f}%"
    return pd.Series(["{0:.2f}%".format(val * 100) for val in data], index = data.index)

def getBigIncreaseSlice(data, ratio = 0.1, before = 2, after = 20) :
    gd = data.pct_change()
    judge = (data.pct_change() > ratio)
    array = []
    i = 0
    while (i < len(judge)):
        if (judge[i]):
            array.append((gd[i-before:i+after]))
            i += after - 1
        i += 1
    return array


def getBigDecreaseSlice(data, ratio = -0.1, before = 2, after = 20) :
    gd = data.pct_change()
    judge = (data.pct_change() < ratio)
    array = []
    i = 0
    while (i < len(judge)):
        if (judge[i]):
            array.append((gd[i-before:i+after]))
            i += after - 1
        i += 1
    return array



def volumeAndPriceChange(input_data, volume_window = 20, volume_change = 2, pct_change_low = -1, pct_change_high = 1, after = 20, before = 2):
    volume_MA = input_data['adj_volume'].rolling(window=volume_window).mean()
    volume = input_data['adj_volume']
    expand = (volume / volume_MA.shift(-1))
    pct = input_data['adj_close'].pct_change()
    i = 0
    array = []
    profit = []
    while (i < len(expand)):
        if (expand[i] > volume_change and pct[i] < pct_change_high and pct[i] > pct_change_low):
            frame = pd.DataFrame((input_data['adj_close'][i-before:i+after]))
            frame['adj_volume'] = input_data['adj_volume'][i-before:i+after]
            if (i+after < len(input_data['adj_close'])):
                profit.append(input_data['adj_close'][i+after]/input_data['adj_close'][i])
            array.append(frame)
            i += after - 1
        i += 1
    return array, profit

