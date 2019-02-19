from tiger.config import get_quote_client

quote_client = get_quote_client()
exchanges = quote_client.get_future_exchanges()
print(exchanges)