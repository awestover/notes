
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

p = 100

fig, ax = plt.subplots()
data = [0 for i in range(p)]
bars = plt.bar([i for i in range(p)], data, color='r')

def init():
    ax.set_xlim(0, p)
    ax.set_ylim(0, 100)
    return bars

def update(frame):
    data[(frame*1) % p] = np.random.randint(50)

    for bar, h in zip(bars, data):
        bar.set_height(h)

    return bars

ani = FuncAnimation(fig, update, frames=[i for i in range(1000)],
                    init_func=init, blit=True)
plt.show()
