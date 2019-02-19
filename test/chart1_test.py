import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    # pdb.set_trace()
    # the histogram of the data
    # normed表示直方图规范化总面积为1，alpha表示透明度
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    # normpdf表示在bins的每个点上用mu，sigma参数画出对应的正态点

    y = mlab.normpdf(bins, mu, sigma)
    z = mlab.normpdf(bins, mu, 10)

    l = plt.plot(bins, y, 'r--', linewidth=1)
    v = plt.plot(bins, z, 'bo', linewidth=3)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)

    plt.show()
