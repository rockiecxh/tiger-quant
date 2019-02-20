import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


index = pd.date_range("1 1 2000", periods=100, freq="m", name="date")
data = np.random.randn(100, 4).cumsum(axis=0)
wide_df = pd.DataFrame(data, index, ["a", "b", "c", "d"])
ax = sns.lineplot(data=wide_df)
plt.show()
