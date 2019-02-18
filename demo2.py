import os

import datetime
import random

from tigeropen.common.consts import Language
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.tiger_open_config import TigerOpenClientConfig
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def timestamp_2_str(arr):
    # convert = lambda a: datetime.utcfromtimestamp(a).strftime('%Y-%m-%d')
    temp = []
    for x in arr.tolist():
        temp.append(datetime.datetime.fromtimestamp(x / 1000.0).strftime('%Y-%m-%d'))
    return temp


def random_color():
    color_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    for i in range(6):
        color += color_arr[random.randint(0, 14)]
    return "#" + color


if __name__ == '__main__':
    config = get_client_config()
    quant_client = QuoteClient(config)

    stocks = ['QQQ', 'TLT']
    data = quant_client.get_bars(stocks)

    years = mdates.YearLocator()  # every year
    months = mdates.MonthLocator()  # every month
    yearsFmt = mdates.DateFormatter('%Y')

    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # ax1 = None
    # for index, stock in stocks:
    y1 = data.loc[(data["symbol"] == stocks[0])]
    x_time = timestamp_2_str(y1['time'].values)
    ax.plot(x_time, y1['close'], color='red', label=stocks[0])

    y2 = data.loc[(data["symbol"] == stocks[1])]
    ax2 = ax.twinx()
    ax2.plot(x_time, y2['close'], color='green', label=stocks[1])

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

