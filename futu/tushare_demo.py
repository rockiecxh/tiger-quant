import tushare as ts


if __name__ == '__main__':
    ts.set_token("cc9a7209a1ddb53eeeb8232b0064eede3f7a196f3a488f7d0b6d211b")
    pro = ts.pro_api()

    # 获取单一股票行情
    df = pro.us_daily(ts_code='AAPL', start_date='20190101', end_date='20190904')

    # 获取某一日所有股票
    df = pro.us_daily(trade_date='20190904')