from tigeropen.quote.quote_client import QuoteClient

from tiger.config import get_quote_client


def get_future_quote():
    # client_config = get_quote_client()
    # quote_client = QuoteClient(client_config)
    quote_client = get_quote_client()
    exchanges = quote_client.get_future_exchanges()
    print(exchanges)
    quote_client.get_future_bars(['CN1901'], begin_time=-1, end_time=1545105097358)
    quote_client.get_future_trade_ticks(['CN1901'])
    quote_client.get_future_contracts('CME')
    quote_client.get_future_trading_times('CN1901', trading_date=1545049282852)
    quote_client.get_future_brief(['ES1906', 'CN1901'])


def get_future_list():
    # client_config = get_quote_client()
    # quote_client = QuoteClient(client_config)
    quote_client = get_quote_client()
    # exchanges = quote_client.get_future_exchanges()
    future_contracts = quote_client.get_future_contracts(exchange='NYMEX')
    print(future_contracts)

    # data = quote_client.get_future_trading_times('GF1908')
    data = quote_client.get_future_trade_ticks(identifiers='GF1908')
    print(data)


if __name__ == '__main__':
    # get_future_quote()
    get_future_list()

