import matplotlib.dates as mdate
import matplotlib.pyplot as plt
from tigeropen.common.consts import BarPeriod
from lib.date import timestamp_2_date_str
from tiger.config import get_quote_client
import seaborn as sns
import pandas as pd

"""
K线叠加
"""

if __name__ == '__main__':
    quant_client = get_quote_client()

    stocks = ['QQQ', 'TLT', 'SPY']
    data = quant_client.get_bars(symbols=stocks, period=BarPeriod.MONTH, begin_time='2009-02-18', end_time='2019-02-18')

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # for index, stock in stocks:
    y1 = data.loc[(data["symbol"] == stocks[0])]
    # normalize
    data1 =(y1['close']-y1['close'].mean())/y1['close'].std()
    x_time = timestamp_2_date_str(y1['time'].values)
    ax.plot(x_time, data1, color='red', label=stocks[0])
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m'))

    y2 = data.loc[(data["symbol"] == stocks[1])]
    # normalize
    data2 = (y2['close'] - y2['close'].mean()) / y2['close'].std()
    ax2 = ax.twinx()
    ax2.plot(x_time, data2, color='green', label=stocks[1])
    # ax2.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m'))
    # ax.autoscale_view()
    # ax.grid(True)
    # plt.yticks([])
    plt.legend()
    plt.show()

    df = pd.DataFrame()
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        df[stock] = (stock_data['close'] - stock_data['close'].mean()) / stock_data['close'].std()
        df['date'] = stock_data['time'].values

    cc = sns.lineplot(data=df)
    plt.show()

