import matplotlib.finance as f
from matplotlib.mlab import normpdf
from matplotlib.pyplot import hist, plot
from numpy import mean, std

sp = f.quotes_historical_yahoo_ohlc('^GSPC', '2018-01-01', '2018-12-31',
                         asobject=True, adjusted=True)
returns = (sp.open[1:] - sp.open[:-1])/sp.open[1:]
[n,bins,patches] = hist(returns, 100)
mu = mean(returns)
sigma = std(returns)
x = normpdf(bins, mu, sigma)
plot(bins, x, color='red', lw=2)