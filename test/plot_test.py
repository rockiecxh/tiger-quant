from lib.pandas import read_pd_from_cache
from month_line_overlay import month_line_overlay_plot
from stock_beta import alpha_beta_plot
from stock_relation import correlation_coefficient_plot, linear_regression_plot
from yield_rate import yield_rate_plot


def month_line_overlay_plot_test():
    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = read_pd_from_cache('5b55eaf8428de1427b80842878b28a73')

    month_line_overlay_plot(data, stocks)


def correlation_coefficient_plot_test():
    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = read_pd_from_cache('5b55eaf8428de1427b80842878b28a73')
    correlation_coefficient_plot(data, stocks)


def test_alpha_beta_plot():
    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = read_pd_from_cache('5b55eaf8428de1427b80842878b28a73')

    alpha_beta_plot(data, stocks)


def test_linear_space_plot():
    data = read_pd_from_cache('4b83ce6d6941c0272dd1225343b268da')
    # base_stock = 'SCHB'
    base_stock = 'WTI'
    stocks = ['SCHB', 'QQQ', 'SPY', 'TLT', 'WTI', 'IAU']

    linear_regression_plot(data, stocks, base_stock)


def test_yield_rate_plot():
    stocks = ['QQQ', 'TLT', 'IAU', 'SPY']
    data = read_pd_from_cache('5b55eaf8428de1427b80842878b28a73')
    yield_rate_plot(data, stocks)


if __name__ == '__main__':
    test_yield_rate_plot()

