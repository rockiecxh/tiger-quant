import hashlib
import logging
import os
import tempfile
import pandas as pd
from lib.date import timestamp_2_month


logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.INFO)


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


def offset_by_date(df: pd.DataFrame, stocks: []):
    """
    FIXME 清洗数据，使每只票的总数据条数都能相等
    :param df:
    :param stocks:
    :return:
    """
    tmp = df[['symbol']].groupby(['symbol']).size()
    tmp = tmp.sort_values(ascending=True)
    min_count_stock = tmp.index[0]

    min_data = df.loc[(df["symbol"] == min_count_stock)]

    merged_data = pd.DataFrame(index=min_data['time'])
    for stock in stocks:
        current_data = df.loc[(df["symbol"] == stock)]
        logging.info('Length: %s %s', stock, len(current_data))

        tmp = pd.merge(min_data, current_data, on='time')
        merged_data = merged_data.concat(tmp)

    return merged_data


