from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import pylab as plt
import numpy as np

data = pd.read_csv('~/Documents/repo/yade/data/dados_pos.csv', delimiter=',', header=None)
#data = data.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(data[1], data[2], data[3], c='skyblue', s=60)
ax.plot3D(data[1], data[2], data[3], 'gray')
ax.scatter3D(data[1], data[2], data[3], c=data[3], cmap='Greens')
#ax.view_init(30, 185)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(data[1], data[2], data[3], c='skyblue', s=60)
ax.plot3D(data[4], data[5], data[6], 'gray')
ax.scatter3D(data[4], data[5], data[6], c=data[6], cmap='Blues')
#ax.view_init(30, 185)

plt.show()
