import hashlib
import os
import tempfile
import pandas as pd


def hash_code(tp: tuple):
    text = ''
    for i in tp:
        text = text + str(i)

    # code = hash(text)
    # code = code if code > 0 else -code
    text = text.strip()  # or new.split()[index]
    code = hashlib.md5(text.encode()).hexdigest()
    return code


def read_pd_from_cache(hcode: str):
    """
    根据MD5文件名从缓存中读取Pandas DataFrame 文件
    :param hcode: Hash code
    :return: pandas.DataFrame
    """
    cache_dir = os.path.join(tempfile.gettempdir(), 'tiger_quant')
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    cache_file = os.path.join(cache_dir, str(hcode) + '.h5')

    if not os.path.isfile(cache_file):
        return None

    df = pd.read_hdf(cache_file, key='data')
    return df


def write_pd_2_cache(df: pd.DataFrame, hcode: int):
    """
    将DataFrame 缓存成文件
    :param df: 要缓存的DataFrame
    :param hcode: 文件名hash_code
    """
    cache_dir = os.path.join(tempfile.gettempdir(), 'tiger_quant')
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    cache_file = os.path.join(cache_dir, str(hcode) + '.h5')

    if os.path.isfile(cache_file):
        return

    store = pd.HDFStore(cache_file, complevel=4, complib='blosc')
    store.append('data', df)
