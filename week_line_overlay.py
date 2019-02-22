import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates
from tigeropen.common.consts import BarPeriod

from lib.date import date_delta, get_today, timestamp_2_date
from lib.quant import normalize
from tiger.config import get_quote_client, get_bars_from_cache

"""
K线叠加
https://matplotlib.org/gallery/text_labels_and_annotations/date.html
"""


def week_line_overlay_plot(data: pd.DataFrame, stocks: []):
    time = data.loc[(data["symbol"] == stocks[0])]['time']
    time = timestamp_2_date(time)

    df = pd.DataFrame(index=time)
    for stock in stocks:
        stock_data = data.loc[(data["symbol"] == stock)]
        df[stock] = normalize(stock_data, 'close')

    g = sns.lineplot(data=df)

    # X轴刻度设置
    g.format_xdata = dates.AutoDateFormatter(dates.WeekdayLocator())

    plt.legend()
    plt.show()


if __name__ == '__main__':
    quote_client = get_quote_client()

    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = get_bars_from_cache(quote_client, symbols=stocks, period=BarPeriod.WEEK,
                               begin_time=date_delta(-52 * 5), end_time=get_today())

    week_line_overlay_plot(data, stocks)


