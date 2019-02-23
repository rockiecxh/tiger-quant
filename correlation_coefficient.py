import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tigeropen.common.consts import BarPeriod

from lib.date import get_today, date_delta
from tiger.config import get_quote_client, get_bars_from_cache

"""
获取指定代码的相关系数并以热力图的方式展现

https://www.jianshu.com/p/139f06a14916
"""


def correlation_coefficient_plot(data: pd.DataFrame, stocks: []):
    # 构建新的 DataFrame 计算相关系数
    df = pd.DataFrame()
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        df[stock] = stock_data['close'].values

    corr = df.corr()

    plt.figure(figsize=(12, 10))
    foo = sns.heatmap(corr, vmax=0.6, square=True, annot=True)
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()

    stocks = ['QQQ', 'SPY', 'WTI', 'IAU']
    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.MONTH,
                               begin_time=date_delta(-52 * 14), end_time=get_today())

    correlation_coefficient_plot(data, stocks)

