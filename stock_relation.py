import logging

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tigeropen.common.consts import BarPeriod
import numpy as np
from lib.chart import subplot_num
from lib.date import get_today, date_delta, timestamp_2_date, date_2_month
from lib.quant import alpha_beta
from tiger.config import get_quote_client, get_bars_from_cache

"""
获取指定代码的相关系数并以热力图的方式展现
https://www.jianshu.com/p/139f06a14916
"""

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.INFO)

plt.rc('font', family='simhei')


def correlation_coefficient_plot(data: pd.DataFrame, stocks: []):
    """
    计算关联系数
    :param data:
    :param stocks:
    :return:
    """
    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time.tolist())
    min_date = time[0]
    max_date = time[-1]

    df = pd.DataFrame()
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        df[stock] = stock_data['close'].values

    corr = df.corr()

    plt.figure(figsize=(12, 10))
    foo = sns.heatmap(corr, vmax=0.6, square=True, annot=True)
    plt.show()


def linear_regression_plot(data: pd.DataFrame, stocks: [], base_stock: str):
    """
    线性回归图
    :param data: 数据
    :param stocks: 票代码
    :return: 基准票代码
    """
    spy_data = data.loc[(data['symbol'] == base_stock)]
    return_spy = spy_data['close'].pct_change().dropna()

    time = timestamp_2_date(spy_data['time'].tolist())
    min_date = time[0]
    max_date = time[-1]

    m, n = subplot_num(len(stocks) - 1)
    fig = plt.figure()
    idx = 1
    for stock in stocks:
        if stock == base_stock:
            continue

        stock_data = data.loc[(data["symbol"] == stock)]

        logging.info("%s data size %s", stock, len(stock_data))

        return_stock = list(stock_data['close'].pct_change().dropna())
        alpha_spy, beta_spy = alpha_beta(return_spy, return_stock)

        x2 = np.linspace(return_spy.min(), return_spy.max(), 100)
        y_hat = x2 * beta_spy + alpha_spy

        ax = fig.add_subplot(m, n, idx)
        ax.scatter(list(return_spy), return_stock, alpha=0.3)
        ax.plot(x2, y_hat, alpha=0.9)

        plt.xlabel('{0} Return'.format(base_stock))
        plt.ylabel('{0} Return'.format(stock))

        idx += 1

    plt.title('以{0}为基准的线性回归({1} - {2})'.format(base_stock, date_2_month(min_date), date_2_month(max_date)))
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()

    base_stock = 'SPY'
    stocks = ['QQQ', 'SPY', 'TLT', 'WTI', 'IAU']

    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.MONTH,
                               begin_time=date_delta(-52 * 10), end_time=get_today())
    linear_regression_plot(data, stocks, base_stock)

