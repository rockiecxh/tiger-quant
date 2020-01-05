from datetime import timedelta

import matplotlib.pyplot as plt
import pandas as pd
from tweetfeels import TweetFeels
from twieet_sentimental import principle


trump_feels = TweetFeels(principle(), tracking=['trump'])

data1 = {s.end: s.value for s in trump_feels.sentiments(delta_time=timedelta(minutes=15), nans=True)}
data2 = {s.end: s.volume for s in trump_feels.sentiments(delta_time=timedelta(minutes=15), nans=True)}
df1 = pd.DataFrame.from_dict(data1, orient='index')
df2 = pd.DataFrame.from_dict(data2, orient='index')
fig, axes = plt.subplots(nrows=2, ncols=1)
fig.set_size_inches(15, 5)
plt.subplot(211).axes.get_xaxis().set_visible(False)
df1[0].plot(kind='line', title='Tesla Sentiment')
plt.subplot(212)
df2[0].plot(kind='area', title='Volume')
plt.show()