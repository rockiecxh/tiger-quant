import logging

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from tigeropen.common.consts import BarPeriod

from lib.date import date_delta, get_today, timestamp_2_date
from lib.pandas import normalize
from tiger.config import get_quote_client, get_bars_from_cache

"""
K线叠加
https://matplotlib.org/gallery/text_labels_and_annotations/date.html
"""

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.DEBUG)


def month_line_overlay_plot(data: pd.DataFrame, stocks: []):
    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time.tolist())

    df = pd.DataFrame(index=time)
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        stock_data = list(normalize(stock_data, 'close'))[0:len(time)]

        logging.info('%s %s', stock, len(stock_data))

        df[stock] = stock_data

    g = sns.lineplot(data=df)

    # X轴刻度设置
    g.format_xdata = dates.AutoDateFormatter(dates.MonthLocator())

    plt.legend()
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()

    stocks = ['QQQ', 'SPY', 'TLT', 'WTI', 'IAU']
    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.MONTH,
                               begin_time=date_delta(-52 * 14), end_time=get_today())

    month_line_overlay_plot(data, stocks)


