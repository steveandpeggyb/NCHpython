#   Using random darts (Monte Carlo) to calculate pi
#   https://www.youtube.com/watch?v=JjfrNc-G-zA

import matplotlib as qt5
from numpy import random
import numpy as np
import matplotlib.pyplot as plt


N = 10000000 # darts thrown

circlex = []
circley = []

squarex = []
squarey = []

i = 1
while i<=N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2 <=1):
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
    i += 1

pi =  4*len(circlex)/float(N)
print('PI() is approximately: ', pi)
print('')
print('PI() actually is: ', str(np.pi))

plt.plot(circlex, circley, 'b.')
plt.plot(squarex, squarey, 'g.')
plt.grid()
plt.show()