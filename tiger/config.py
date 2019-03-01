import logging
import os
import numpy as np
from properties.p import Property
from tigeropen.common.consts import Language, BarPeriod, QuoteRight
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.tiger_open_config import TigerOpenClientConfig

from lib.pandas import read_pd_from_cache, tuple_2_md5, write_pd_2_cache

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.DEBUG)


def get_client_config():
    """
    https://www.itiger.com/openapi/info 开发者信息获取
    :return:
    """
    # Load tiger account information
    prop = Property()
    prop_loader = prop.load_property_files(os.path.expanduser('~/config/env.properties'))
    tiger_id = prop_loader.get('tiger_id')
    tiger_account = prop_loader.get('tiger_account')

    is_sandbox = False
    client_config = TigerOpenClientConfig(sandbox_debug=is_sandbox)
    client_config.private_key = read_private_key(os.path.expanduser('~/.ssh/tigerbroker_rsa_private_key.pem'))
    client_config.tiger_id = tiger_id
    client_config.account = tiger_account
    client_config.language = Language.en_US

    return client_config


def get_quote_client():
    """
    获取 QuoteClient
    :return: QuoteClient
    """
    config = get_client_config()
    quote_client = QuoteClient(config)

    return quote_client


def get_bars_from_cache(quote_client: QuoteClient, symbols, period=BarPeriod.DAY,
                        begin_time=-1, end_time=-1, right=QuoteRight.BR, limit=10000, lang=None):
    """
    走文件缓存，加快多次访问速度
    :param quote_client:
    :param symbols:
    :param period:
    :param begin_time:
    :param end_time:
    :param right:
    :param limit:
    :param lang:
    :return:
    """
    md5 = tuple_2_md5([symbols, period, begin_time, end_time, right, limit, lang])

    # 从文件缓存获取数据
    data = read_pd_from_cache(md5)

    if data is not None:
        return data

    # 调用API获取
    if data is None:
        data = quote_client.get_bars(symbols=symbols, period=period,
                                     begin_time=begin_time, end_time=end_time, limit=limit)

        if not data.empty:
            write_pd_2_cache(data, md5)

    # data = offset_by_date(data)
    return data

