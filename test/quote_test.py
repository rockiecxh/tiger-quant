from tiger.quote import get_symbol_names


def test_get_symbol_names():
    all_symbols = get_symbol_names()
    assert all_symbols is not None
    print(all_symbols)
