import numpy as np
import pandas as pd

from lib.pandas import write_pd_2_cache, read_pd_from_cache, hash_code

RULE_TUPLE = ('test_write_pd_2_cache', 1234, 45454)


def test_hash_str():
    for i in range(100):
        hstr = hash_code(RULE_TUPLE)
        print(hstr)


def test_write_pd_2_cache():
    a = np.random.standard_normal((900000, 4))
    df = pd.DataFrame(a)

    hstr = hash_code(RULE_TUPLE)
    write_pd_2_cache(df, hstr)


def test_read_pd_from_cache():
    hstr = hash_code(RULE_TUPLE)
    df = read_pd_from_cache(hstr)
    print(df)
