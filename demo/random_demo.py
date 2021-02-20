import numpy as np
np.random.seed(19680801)
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
for color in ['tab:green']:
    dot_count = 5000
    x, y = np.random.rand(2, dot_count)
    dot_size = 3
    # * np.random.rand(n)
    ax.scatter(x, y, c=color, s=dot_size, label=color, alpha=0.7, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
