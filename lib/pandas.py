import hashlib
import logging
import os
import tempfile

import numpy as np
import pandas as pd


logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.DEBUG)


def tuple_2_md5(tp: tuple):
    """
    根据tuple生成md5
    :param tp:
    :return:
    """
    text = ''
    for i in tp:
        text = text + str(i)

    text = text.strip()  # or new.split()[index]
    code = hashlib.md5(text.encode()).hexdigest()
    return code


def read_pd_from_cache(md5: str):
    """
    根据MD5文件名从缓存中读取Pandas DataFrame 文件
    :param md5: 文件名
    :return: pandas.DataFrame
    """
    cache_dir = os.path.join(tempfile.gettempdir(), 'tiger_quant')
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    cache_file = os.path.join(cache_dir, md5 + '.h5')

    logging.info('Read from local cache: %s', cache_file)

    if not os.path.isfile(cache_file):
        return None

    df = pd.read_hdf(cache_file, key='data')
    return df


def write_pd_2_cache(df: pd.DataFrame, md5: str):
    """
    将DataFrame 缓存成文件
    :param df: 要缓存的DataFrame
    :param md5: 文件名md5
    """
    cache_dir = os.path.join(tempfile.gettempdir(), 'tiger_quant')
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    cache_file = os.path.join(cache_dir, md5 + '.h5')

    if os.path.isfile(cache_file):
        return

    store = pd.HDFStore(cache_file, complevel=4, complib='blosc')
    store.append('data', df)


def normalize(df: pd.DataFrame, column: str):
    """
    数据归一化
    :param df: DataFrame
    :param column: 列名
    :return:
    """
    # temp = (stock_data['close'] - stock_data['close'].mean()) / stock_data['close'].std()
    normalized_data = (df[column] - df[column].mean()) / df[column].std()
    normalized_data = normalized_data.values
    return normalized_data


def beta(market_returns, stock_returns):
    """
    计算 Beta 值
    :param market_returns:
    :param stock_returns:
    :return:
    """
    # np_array = df.values
    # m = np_array[:,0] # market returns are column zero from numpy array
    # s = np_array[:,1] # stock returns are column one from numpy array
    covariance = np.cov(stock_returns, market_returns)  # Calculate covariance between stock and market
    beta = covariance[0, 1] / covariance[1, 1]
    return beta


def offset_by_date(df: pd.DataFrame, stocks: []):
    """
    清洗数据，使每只票的总数据条数都能相等
    :param df:
    :param stocks:
    :return:
    """

    tmp = df[['symbol']].groupby(['symbol']).size()
    tmp = tmp.sort_values(ascending=True)
    min_count_stock = tmp.index[0]
    # min_data_count = tmp[0]

    min_data = df.loc[(df["symbol"] == min_count_stock)]
    std_time = min_data['time']

    for stock in stocks:
        cur_data = df.loc[(df["symbol"] == stock)]
        logging.info('Lenght: %s %s', stock, len(cur_data))

        current_time = cur_data['time']

        diff = list(set(std_time.values).difference(set(current_time.values)))
        logging.info(timestamp_2_month(current_time.values))

    return df


