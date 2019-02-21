import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates
from matplotlib.ticker import MultipleLocator
from tigeropen.common.consts import BarPeriod

from lib.date import timestamp_2_date, date_delta, get_today
from tiger.config import get_quote_client
import numpy as np

"""
K线叠加
https://matplotlib.org/gallery/text_labels_and_annotations/date.html
"""


def month_line_overlay_plot(data: pd.DataFrame):
    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time)

    # df = pd.DataFrame(index=time)
    # for stock in stocks:
    #     stock_data = data.loc[(data["symbol"] == stock)]
    #     temp = (stock_data['close'] - stock_data['close'].mean()) / stock_data['close'].std()
    #     df[stock] = temp.values
    #
    # g = sns.lineplot(data=df)
    # plt.xticks(rotation=90)
    # g.xaxis.set_major_locator(MultipleLocator(10))
    # g.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
    # g.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
    # g.xaxis.set_major_locator(dates.MonthLocator())

    fig, ax = plt.subplots()
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        temp = (stock_data['close'] - stock_data['close'].mean()) / stock_data['close'].std()
        ax.plot(time, temp.values)

    years = dates.YearLocator()  # every year
    months = dates.MonthLocator()  # every month
    yearsFmt = dates.DateFormatter('%Y')

    # format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)

    # round to nearest years...
    datemin = np.datetime64(time[0], 'Y')
    datemax = np.datetime64(time[-1], 'Y')
    ax.set_xlim(datemin, datemax)

    ax.format_xdata = dates.DateFormatter('%Y-%m-%d')
    # ax.format_ydata = price
    ax.grid(True)
    fig.autofmt_xdate()

    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()

    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = quote_client.get_bars(symbols=stocks, period=BarPeriod.MONTH,
                                 begin_time=get_today(), end_time=date_delta(-52 * 10))

    month_line_overlay_plot(data)


