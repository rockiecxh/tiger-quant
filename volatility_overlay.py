import cmath
import logging

import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas_datareader import data as pdr
from statsmodels import regression
from tigeropen.common.consts import BarPeriod

from lib.date import date_delta, get_today
from lib.quant import beta, alpha_beta
from tiger.config import get_bars_from_cache, get_quote_client
import pandas as pd
import numpy as np


"""
波动率计算
https://blog.csdn.net/CoderPai/article/details/82868280

beta 计算
https://blog.csdn.net/thfyshz/article/details/83443783

贝塔系数衡量了个股或基金相对于整个股市的波动情况。
β范围	含义
β=1	    股票或基金的风险收益率与市场平均风险收益率相同
β>1	    股票或基金的风险相较于市场平均更大
β<1	    股票或基金的风险相较于市场平均更小

df1 = pdr.get_data_yahoo('VMW', start='2015-02-21', end='2019-02-21')
df2 = pdr.get_data_yahoo('QQQ', start='2015-02-21', end='2019-02-21')

return_goog = df1.Close.pct_change()[1:]
return_spy = df2.Close.pct_change()[1:]
    
plt.figure(figsize=(20, 10))
return_goog.plot()
return_spy.plot()
plt.ylabel('Daily return of GOOG and SPY')
plt.legend()
plt.show()
"""


logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.DEBUG)


def alpha_beta_plot(data: pd.DataFrame, stocks: []):
    """
    Alpha, Beta 展示
    :param data: 数据
    :param stocks: 股票
    :return:
    """

    spy_data = data.loc[(data["symbol"] == 'SPY')]
    qqq_data = data.loc[(data["symbol"] == 'QQQ')]

    return_qqq = list(qqq_data['close'].pct_change().dropna())
    return_spy = list(spy_data['close'].pct_change().dropna())

    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]

        return_stock = list(stock_data['close'].pct_change().dropna())

        # 以SPY为基准计算alpha, beta
        alpha_spy, beta_spy = alpha_beta(return_spy, return_stock)

        alpha_qqq, beta_qqq = alpha_beta(return_qqq, return_stock)

        logging.info('SPY basics %s alpha: %s, beta: %s', stock, str(alpha_spy), str(beta_spy))

        logging.info('QQQ basics %s alpha: %s, beta: %s', stock, str(alpha_qqq), str(beta_qqq))


def subplot_num(total: int):
    """

    :param index:
    :return:
    """
    sqrt = cmath.sqrt(total).real
    if sqrt.real.is_integer():
        return sqrt, sqrt
    else:
        return int(sqrt) + 1, int(sqrt)


def linear_space_plot(data: pd.DataFrame, stocks: []):
    """
    线性回归图
    :param data: 数据
    :param stocks: 票
    :return:
    """

    spy_data = data.loc[(data["symbol"] == 'SPY')]
    # qqq_data = data.loc[(data["symbol"] == 'QQQ')]

    return_spy = spy_data['close'].pct_change().dropna()

    m, n = subplot_num(len(stocks))
    fig = plt.figure()
    idx = 1
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]

        return_stock = list(stock_data['close'].pct_change().dropna())
        alpha_spy, beta_spy = alpha_beta(return_spy, return_stock)

        x2 = np.linspace(return_spy.min(), return_spy.max(), 100)
        y_hat = x2 * beta_spy + alpha_spy

        # plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(m, n, idx)
        ax.scatter(list(return_spy), return_stock, alpha=0.3)
        # ax.xlabel('SPY Daily Return')
        # ax.ylabel('{0} Daily Return'.format(stock))
        ax.plot(x2, y_hat, alpha=0.9)

        idx += 1

    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()

    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.DAY,
                               begin_time=date_delta(-52 * 5), end_time=get_today())

    alpha_beta_plot(data, stocks)

