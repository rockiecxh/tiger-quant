from tiger.config import get_quote_client
import seaborn as sns
import matplotlib.pyplot as plt
# quote_client = get_quote_client()
# exchanges = quote_client.get_future_exchanges()
# print(exchanges)

import numpy as np, pandas as pd
plt.close("all")
index = pd.date_range("1 1 2000", periods=100, freq="m", name="date")
data = np.random.randn(100, 4).cumsum(axis=0)
wide_df = pd.DataFrame(data, index, ["a", "b", "c", "d"])
ax = sns.lineplot(data=wide_df)
plt.show()
