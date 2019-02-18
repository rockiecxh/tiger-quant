from tigeropen.common.consts import Market
from tigeropen.quote.quote_client import QuoteClient

from common.Config import get_client_config


def get_symbol_names():
    """
    获取所有股票代码和名称
    :return:
    """
    config = get_client_config()
    quant_client = QuoteClient(config)
    symbols = quant_client.get_symbol_names(market=Market.ALL)

    return symbols


if __name__ == '__main__':
    all_symbols = get_symbol_names()
    print(all_symbols)