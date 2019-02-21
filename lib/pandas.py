import hashlib
import os
import tempfile
import pandas as pd
import numpy as np


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
    normalized_data = (df[column] - df[column].mean()) / df[column].std().values()
    return normalized_data


def beta(market_returns, stock_returns):
    # np_array = df.values
    # m = np_array[:,0] # market returns are column zero from numpy array
    # s = np_array[:,1] # stock returns are column one from numpy array
    covariance = np.cov(stock_returns, market_returns)  # Calculate covariance between stock and market
    beta = covariance[0, 1] / covariance[1, 1]
    return beta