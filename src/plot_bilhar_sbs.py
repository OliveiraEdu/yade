import pandas as pd
import pylab as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

data = pd.read_csv('~/Documents/repo/yade/data/dados_pos.csv', delimiter=',', header=None)
data = data.rolling(7).mean()

fig = plt.figure()
sns.lineplot(data=data, x=0,y=1, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=4, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=7, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=10, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=13, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=16, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=19, palette="tab10",  linewidth= 1.5)

fig = plt.figure()
sns.lineplot(data=data, x=0,y=2, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=5, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=8, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=11, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=14, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=17, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=20, palette="tab10",  linewidth= 1.5)

fig = plt.figure()
sns.lineplot(data=data, x=0,y=3, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=6, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=9, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=12, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=15, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=18, palette="tab10",  linewidth= 1.5)
sns.lineplot(data=data, x=0,y=21, palette="tab10",  linewidth= 1.5)



plt.show()
