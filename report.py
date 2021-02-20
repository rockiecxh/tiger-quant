import FundamentalAnalysis as fa


if __name__ == '__main__':
    symbol = ['TSLA', 'AAPL', 'MSFT']

    balance_sheet = fa.balance_sheet(symbol)
    income_statement = fa.income_statement(symbol)
    cashflows = fa.cashflows(symbol)
    ratios = fa.ratios(symbol)
    stock_data = fa.stock_data(2019, 2021, symbol, include_returns=True)