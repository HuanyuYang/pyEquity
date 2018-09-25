import matplotlib.pyplot as plt
import pandas as pd
import datetime
import quandl
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot



def plotCandleGraph(data, height = 1200, width =1200):
    trace = go.Candlestick(x=data.index,
                           open=data.adj_open,
                           high=data.adj_high,
                           low=data.adj_low,
                           close=data.adj_close)
    data = [trace]
    layout = go.Layout(
        showlegend=True,
        height=1200,
        width=1200,
    )

    fig = dict( data=data, layout=layout )
    iplot(fig)


def plotStrategy(initdata, strategy):
    data = initdata.copy()
    data['Market'] = np.log(data['adj_close'] / data['adj_close'].shift(1))
    data['Strategy'] = data['Regime'].shift(1) * data['Market']
    data[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True,
                                                             figsize=(16, 10))


