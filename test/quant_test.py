from lib.quant import log_return_rate
from tiger.quote import get_symbol_names


def test_get_symbol_names():
    all_symbols = get_symbol_names()
    assert all_symbols is not None
    print(all_symbols)


def test_log_return_rate():
    return_rate = log_return_rate(100, 105)
    print(return_rate)

