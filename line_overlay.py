import logging

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates
from tigeropen.common.consts import BarPeriod

from lib.chart import PlotDateType
from lib.date import date_delta, get_today, timestamp_2_date, timestamp_2_month, date_2_month
from lib.quant import normalize
from tiger.config import get_quote_client, get_bars_from_cache

"""
K线叠加
https://matplotlib.org/gallery/text_labels_and_annotations/date.html
"""

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.INFO)

plt.rc('font', family='simhei')
plt.rcParams['axes.unicode_minus'] = False


def onpick(event):
    if event.inaxes is not None:
        # logging.info('event')
        x = event.xdata
        y = event.ydata
        # event.inaxes.plot(x, y, 'ro')
        # event.canvas.draw()


def line_overlay_plot(data: pd.DataFrame, stocks: [], plotDateType: PlotDateType):
    """
    拆线叠加图
    :param data:
    :param stocks:
    :param plotDateType:
    :return:
    """
    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time.tolist())
    min_date = time[0]
    max_date = time[-1]

    df = pd.DataFrame(index=time)
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        # logging.info(timestamp_2_month(stock_data['time']))
        stock_data = list(normalize(stock_data, 'close'))

        logging.info('%s %s', stock, len(stock_data))

        df[stock] = stock_data

    g = sns.lineplot(data=df)

    # X轴刻度设置
    date_locator = None
    if plotDateType == PlotDateType.MONTH:
        date_locator = dates.AutoDateFormatter(dates.MonthLocator())
    elif plotDateType == PlotDateType.WEEK:
        date_locator = dates.AutoDateFormatter(dates.WeekdayLocator())
    elif plotDateType == PlotDateType.DAY:
        date_locator = dates.AutoDateFormatter(dates.DateLocator())

    g.format_xdata = date_locator
    # 鼠标hover 事件
    # plt.gcf().canvas.mpl_connect('motion_notify_event', onpick)
    plt.title('ETF价格叠加图({0} - {1})'.format(date_2_month(min_date), date_2_month(max_date)))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()

    stocks = ['QQQ', 'SPY', 'WTI', 'IAU']
    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.MONTH,
                               begin_time=date_delta(-52 * 14), end_time=get_today())

    line_overlay_plot(data, stocks, PlotDateType.MONTH)


