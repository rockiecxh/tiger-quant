import matplotlib.dates as mdate
import matplotlib.pyplot as plt
from tigeropen.common.consts import BarPeriod
from lib.date import timestamp_2_date_str
from tiger.config import get_quote_client

"""
K线叠加
"""

if __name__ == '__main__':
    quant_client = get_quote_client()

    stocks = ['QQQ', 'TLT']
    data = quant_client.get_bars(symbols=stocks, period=BarPeriod.MONTH, begin_time='2009-02-18', end_time='2019-02-18')

    # years = mdates.YearLocator()  # every year
    # months = mdates.MonthLocator()  # every month
    # yearsFmt = mdates.DateFormatter('%Y')

    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # TODO normalize data range
    # ax1 = None
    # for index, stock in stocks:
    y1 = data.loc[(data["symbol"] == stocks[0])]
    # normalize
    y1 =(y1-y1.mean())/y1.std()
    x_time = timestamp_2_date_str(y1['time'].values)
    ax.plot(x_time, y1['close'], color='red', label=stocks[0])
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m'))

    y2 = data.loc[(data["symbol"] == stocks[1])]
    # normalize
    y2 = (y2 - y2.mean()) / y2.std()
    ax2 = ax.twinx()
    ax2.plot(x_time, y2['close'], color='green', label=stocks[1])
    ax2.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m'))

    # mondays = mdates.WeekdayLocator(mdates.MONDAY)  # major ticks on the mondays
    # alldays = mdates.DayLocator()  # minor ticks on the days
    # weekFormatter = mdates.DateFormatter('%Y-%m-%d')  # e.g., 2018-09-12; Jan 12
    # dayFormatter = mdates.DateFormatter('%d')  # e.g., 12

    # ax.xaxis.set_major_locator(mondays)
    # ax.xaxis.set_minor_locator(alldays)
    # ax.xaxis.set_major_formatter(weekFormatter)
    # ax.xaxis_date()
    ax.autoscale_view()
    # ax.grid(True)
    # plt.yticks([])
    plt.legend()
    plt.show()

