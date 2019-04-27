import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np



def plt_show():
  try:
    plt.show()
  except UnicodeDecodeError:
    plt_show()

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])
plt.savefig('myfilename.png')


