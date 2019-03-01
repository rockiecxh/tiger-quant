import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tigeropen.common.consts import BarPeriod

from lib.chart import subplot_num
from lib.date import timestamp_2_date, get_today, date_delta
from lib.quant import log_yield_rate
from tiger.config import get_bars_from_cache, get_quote_client


def yield_rate_plot(data: pd.DataFrame, stocks: []):
    """
    收益率图表
    :param data: 数据
    :param stocks: 股票
    :return:
    """
    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time.tolist())

    m, n = subplot_num(len(stocks))
    fig = plt.figure()
    idx = 1

    for stock in stocks:
        stock_data = data.loc[(data['symbol'] == stock)]

        normal_return_rate = list(stock_data['close'].pct_change().dropna())
        ln_return_rate = log_yield_rate(list(stock_data['close']))

        stock_normal = '{0}_normal'.format(stock)
        stock_log = '{0}_log'.format(stock)

        df = pd.DataFrame(index=time[1:])
        df[stock_normal] = np.cumsum(normal_return_rate)
        df[stock_log] = np.cumsum(ln_return_rate)

        ax = fig.add_subplot(m, n, idx)
        ax.plot(df)
        ax.legend([stock_normal, stock_log])

        idx += 1

    # X轴刻度设置
    # g.format_xdata = dates.AutoDateFormatter(dates.MonthLocator())
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()
    stocks = ['SCHB', 'QQQ', 'TLT', 'IAU']

    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.DAY,
                               begin_time=date_delta(-52 * 5), end_time=get_today())
    yield_rate_plot()

