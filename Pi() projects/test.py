import numpy as np

from bokeh.plotting import figure, show, output_file

N = 10
x = np.random.random(size=N) * 100
print('x = ' + str(x))
y = np.random.random(size=N) * 100
print('y = ' + str(y))
radii = np.random.random(size=N) * 1.5
print('radii = ' + str(radii))
colors = ["#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)]
print('colors = ' + str(colors))