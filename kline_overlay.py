import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates
from matplotlib.ticker import MultipleLocator
from tigeropen.common.consts import BarPeriod

from lib.date import timestamp_2_date
from tiger.config import get_quote_client
import numpy as np

"""
K线叠加
https://matplotlib.org/gallery/text_labels_and_annotations/date.html
"""

if __name__ == '__main__':
    quant_client = get_quote_client()

    stocks = ['QQQ', 'TLT', 'SPY']
    data = quant_client.get_bars(symbols=stocks, period=BarPeriod.MONTH, begin_time='2009-02-18', end_time='2019-02-18')

    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time)
    df = pd.DataFrame(index=time)
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        temp = (stock_data['close'] - stock_data['close'].mean()) / stock_data['close'].std()
        df[stock] = temp.values

    g = sns.lineplot(data=df)
    # plt.xticks(rotation=90)
    # g.xaxis.set_major_locator(MultipleLocator(10))
    # g.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
    # g.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
    # g.xaxis.set_major_locator(dates.MonthLocator())

    years = dates.YearLocator()  # every year
    months = dates.MonthLocator()  # every month
    yearsFmt = dates.DateFormatter('%Y')

    # format the ticks
    g.xaxis.set_major_locator(years)
    g.xaxis.set_major_formatter(yearsFmt)
    g.xaxis.set_minor_locator(months)

    # round to nearest years...
    datemin = np.datetime64(time[0], 'Y')
    datemax = np.datetime64(time[-1], 'Y')
    # g.set_xlim(datemin, datemax)

    plt.show()

