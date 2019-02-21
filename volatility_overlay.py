from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels import regression
import numpy as np

from lib.pandas import beta

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
"""

df1 = pdr.get_data_yahoo('VMW', start='2018-02-21', end='2019-02-21')
df2 = pdr.get_data_yahoo('QQQ', start='2018-02-21', end='2019-02-21')

return_goog = df1.Close.pct_change()[1:]
return_spy = df2.Close.pct_change()[1:]

plt.figure(figsize=(20, 10))
return_goog.plot()
return_spy.plot()
plt.ylabel('Daily return of GOOG and SPY')
plt.legend()
plt.show()



"""
alpha 与 beta 计算
"""


def linreg(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    x = sm.add_constant(x)
    model = regression.linear_model.OLS(y, x).fit()

    # x = x[:, 1]
    return model.params[0], model.params[1]


# 以SPY为基准计算alpha, beta
# alpha, beta = linreg(return_spy, return_goog)
# print('alpha:' + str(alpha))
# print('beta:' + str(beta))


alpha = beta(return_spy, return_goog)
print('alpha:' + str(alpha))

