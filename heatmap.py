import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tigeropen.common.consts import BarPeriod
from tigeropen.quote.quote_client import QuoteClient
from common.Config import get_client_config

"""
https://www.jianshu.com/p/139f06a14916
"""

config = get_client_config()
quant_client = QuoteClient(config)

stocks = ['QQQ', 'SPY', 'TLT', 'USO']
data = quant_client.get_bars(symbols=stocks, period=BarPeriod.MONTH, begin_time='2009-02-18', end_time='2019-02-18')

# 构建新的 DataFrame 计算相关系数
df = pd.DataFrame()
for stock in stocks:
    stock_data = data.loc[(data["symbol"] == stock)]
    df[stock] = stock_data['close'].values

corr = df.corr()

plt.figure(figsize=(12, 10))
foo = sns.heatmap(corr, vmax=0.6, square=True, annot=True)
plt.show()
