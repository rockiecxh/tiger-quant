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
    :param df:
    :param stocks:
    :return:
    """

    spy_data = data.loc[(data["symbol"] == 'SPY')]
    qqq_data = data.loc[(data["symbol"] == 'QQQ')]

    return_qqq = qqq_data['close'].pct_change()[1:]
    return_spy = spy_data['close'].pct_change()[1:]

    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]

        return_stock = stock_data['close'].pct_change()[1:]

        # 以SPY为基准计算alpha, beta
        alpha_spy, beta_spy = alpha_beta(return_spy, return_stock)

        alpha_qqq, beta_qqq = alpha_beta(return_qqq, return_stock)

        logging.info('SPY alpha: %s, beta: %s', str(alpha_spy), str(beta_spy))

        logging.info('QQQ alpha: %s, beta: %s', str(alpha_qqq), str(beta_qqq))


if __name__ == '__main__':
    quote_client = get_quote_client()

    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.DAY,
                               begin_time=date_delta(-52 * 5), end_time=get_today())

    alpha_beta_plot(data, stocks)

