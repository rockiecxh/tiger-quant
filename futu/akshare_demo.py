import akshare as ak

from lib.pandas import tuple_2_md5, read_pd_from_cache, write_pd_2_cache
from week_line_overlay import week_line_overlay_plot


def get_daily_from_cache(stock_code):
    md5 = tuple_2_md5([stock_code])
    # 从文件缓存获取数据
    data = read_pd_from_cache(md5)

    if data is None:
        data = ak.stock_us_daily(symbol=stock_code, adjust="")

        if not data.empty:
            write_pd_2_cache(data, md5)

    return data


def download_wrap(stock_code):
    data = get_daily_from_cache(stock_code=stock_code)
    # data.index.rename('date', 'time')
    data['symbol'] = stock_code
    data['time'] = data.index
    return data


if __name__ == '__main__':
    aapl = download_wrap('XLV')
    aapl = aapl.append(download_wrap('XLF'))
    aapl = aapl.append(download_wrap('XLK'))

    week_line_overlay_plot(aapl, ['XLV', 'XLF', 'XLK'])
