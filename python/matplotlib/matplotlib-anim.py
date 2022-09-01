import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)

fig = plt.figure()
ax = fig.add_subplot(111)
t = 0

while True:
    t += 0.1
    y = np.sin(x-0.2*t)
    ax.clear()
    ax.plot(x, y)
    plt.pause(0.1)