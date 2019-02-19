from tigeropen.common.consts import Market
from tigeropen.quote.quote_client import QuoteClient

from tiger.config import get_client_config


def get_symbol_names():
    """
    获取所有股票代码和名称
    :return: 代码与名称数组
    """
    config = get_client_config()
    quant_client = QuoteClient(config)
    symbols = quant_client.get_symbol_names(market=Market.ALL)

    return symbols
