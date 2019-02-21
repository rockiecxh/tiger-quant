import numpy as np
import pandas as pd
from lib.pandas import write_pd_2_cache, read_pd_from_cache, tuple_2_md5


RULE_TUPLE = ('test_write_pd_2_cache', 1234, 45454)


def test_hash_str():
    for i in range(100):
        md5 = tuple_2_md5(RULE_TUPLE)
        print(md5)


def test_write_pd_2_cache():
    a = np.random.standard_normal((900000, 4))
    df = pd.DataFrame(a)

    md5 = tuple_2_md5(RULE_TUPLE)
    write_pd_2_cache(df, md5)


def test_read_pd_from_cache():
    md5 = tuple_2_md5(RULE_TUPLE)
    df = read_pd_from_cache(md5)
    print(df)
