import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb; sb.set()
from datetime import datetime

def plotHeatMap(d, dest):
    X = d[0]
    Y = d[1]

    heatmap, xedges, yedges = np.histogram2d(X, Y, bins=40)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    fig1 = plt.subplot(2,2,2)
    plt.imshow(heatmap, extent=extent)
    plt.colorbar()
    plt.title('Heatmap with smoothing')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()