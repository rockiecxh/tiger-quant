from correlation_coefficient import correlation_coefficient_plot
from lib.pandas import read_pd_from_cache
from month_line_overlay import month_line_overlay_plot
from volatility_overlay import alpha_beta_plot, linear_space_plot


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
    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = read_pd_from_cache('5b55eaf8428de1427b80842878b28a73')
    linear_space_plot(data, stocks)


if __name__ == '__main__':
    test_linear_space_plot()

