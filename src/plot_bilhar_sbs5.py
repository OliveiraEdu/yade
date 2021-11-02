import pandas as pd
import pylab as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

data = pd.read_csv('~/Documents/repo/yade/data/dados_pos.csv', delimiter=',', header=None)
data = data.rolling(7).mean()

fig = plt.figure()
sns.lineplot(data=data, x=0,y=1, palette="tab10",  linewidth= 2, color="g")
plt.legend(labels=["speed(m/s)"])


ax2 = plt.twinx()
sns.lineplot(data=data, x=0,y=2, palette="tab10",  linewidth= 2, color="r")

plt.legend(labels=["position(m)"])

plt.show()
