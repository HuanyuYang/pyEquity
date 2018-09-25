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






