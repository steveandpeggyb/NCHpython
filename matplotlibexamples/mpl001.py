# run the "data_gen.py" script from the command line.  This will automatically add a new data point every second to the
# csv file.  Then, run this script and see an automated update of that csv file data.
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.available[:26]

loop = len(plt.style.available[:])
for x in range(loop):
    plt.style.use(plt.style.available[x:x+1])

    x_vals = []
    y_vals = []

    index = count()


    def animate(i):
        data = pd.read_csv('c:\\TEMP\\data.csv')
        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']

        plt.cla()

        plt.plot(x, y1, label='Channel 1')
        plt.plot(x, y2, label='Channel 2')

        plt.legend(loc='upper left')
        plt.tight_layout()


    ani = FuncAnimation(plt.gcf(), animate, interval=500)

    plt.tight_layout()
    plt.show()


