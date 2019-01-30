import os

import datetime
from tigeropen.common.consts import Language
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.tiger_open_config import TigerOpenClientConfig
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def get_client_config():
    """
    https://www.itiger.com/openapi/info 开发者信息获取
    :return:
    """
    is_sandbox = False
    client_config = TigerOpenClientConfig(sandbox_debug=is_sandbox)
    client_config.private_key = read_private_key(os.path.expanduser('~/.ssh/tigerbroker_rsa_private_key.pem'))
    client_config.tiger_id = '20150138'
    client_config.account = '20190130215629871'
    client_config.language = Language.en_US
    return client_config


def timestamp_2_str(arr):
    # convert = lambda a: datetime.utcfromtimestamp(a).strftime('%Y-%m-%d')
    temp = []
    for x in arr.tolist():
        temp.append(datetime.datetime.fromtimestamp(x / 1000.0).strftime('%Y-%m-%d'))
    return temp


if __name__ == '__main__':
    config = get_client_config()
    quant_client = QuoteClient(config)

    aapl = quant_client.get_bars(['AAPL'])
    # bars = QuoteClient.get_bars(['AAPL'], period=BarPeriod.DAY, begin_time=-1, end_time=-1, right=QuoteRight.BR, limit=251)
    print(aapl)

    x_time = timestamp_2_str(aapl['time'].values)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.figure(figsize=(10, 5))
    plt.plot(x_time, aapl['close'], color='red')
    plt.gcf().autofmt_xdate()
    plt.show()
