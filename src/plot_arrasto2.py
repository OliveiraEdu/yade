import pandas as pd
import pylab as plt



data = pd.read_csv('~/Documents/repo/yade/data/dados.csv', delimiter=',', header=None)

print (data)

data.plot(x =0, y=1, kind = 'line')

plt.xlabel("t(s)")
plt.ylabel("y(m)")
plt.grid(True)
plt.title("Drag")

data.plot(x =0, y=2, kind = 'line')



plt.xlabel("t(s)")
plt.ylabel("y(m)")
plt.grid(True)
plt.title("Drag - Terminal Velocity")


plt.show()
