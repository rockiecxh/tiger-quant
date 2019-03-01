import logging

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import dates
from tigeropen.common.consts import BarPeriod

from lib.date import timestamp_2_date, get_today, date_delta, date_2_month
from lib.quant import log_yield_rate
from tiger.config import get_bars_from_cache, get_quote_client


plt.rc('font', family='simhei')


def yield_rate_plot(data: pd.DataFrame, stocks: []):
    """
    收益率图表
    :param data: 数据
    :param stocks: 股票
    :return:
    """
    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time.tolist())
    min_date = time[0]
    max_date = time[-1]

    df = pd.DataFrame(index=time[1:])

    for stock in stocks:
        stock_data = data.loc[(data['symbol'] == stock)]
        logging.info('%s data size %s', stock, len(stock_data))
        ln_return_rate = log_yield_rate(list(stock_data['close']))
        df[stock] = np.cumsum(ln_return_rate)

    g = sns.lineplot(data=df)
    # X轴刻度设置
    g.format_xdata = dates.AutoDateFormatter(dates.MonthLocator())

    plt.legend()
    plt.title('各ETF累计收益率({0} - {1})'.format(date_2_month(min_date), date_2_month(max_date)))
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()
    stocks = ['QQQ', 'SPY', 'TLT', 'IAU', 'WTI']

    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.WEEK,
                               begin_time=date_delta(-52 * 10), end_time=get_today())
    yield_rate_plot(data, stocks)

