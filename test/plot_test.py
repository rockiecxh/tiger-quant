from lib.pandas import read_pd_from_cache
from month_line_overlay import month_line_overlay_plot


def month_line_overlay_plot_test():
    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']
    data = read_pd_from_cache('5b55eaf8428de1427b80842878b28a73')

    month_line_overlay_plot(data, stocks)


if __name__ == '__main__':
    month_line_overlay_plot_test()

