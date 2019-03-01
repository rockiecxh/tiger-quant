import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import dates
from tigeropen.common.consts import BarPeriod

from lib.date import timestamp_2_date, get_today, date_delta
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

    df = pd.DataFrame(index=time[1:])

    for stock in stocks:
        stock_data = data.loc[(data['symbol'] == stock)]

        ln_return_rate = log_yield_rate(list(stock_data['close']))
        df[stock] = np.cumsum(ln_return_rate)

    g = sns.lineplot(data=df)
    # X轴刻度设置
    g.format_xdata = dates.AutoDateFormatter(dates.MonthLocator())

    plt.legend()
    plt.title('累计收益率')
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()
    stocks = ['SCHB', 'QQQ', 'TLT', 'IAU', 'WTI']

    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.DAY,
                               begin_time=date_delta(-52 * 5), end_time=get_today())
    yield_rate_plot()

