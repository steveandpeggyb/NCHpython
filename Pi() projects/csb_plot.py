import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb; sb.set()
from datetime import datetime
import scipy.ndimage as sp
from matplotlib.figure import Figure
from scipy.stats import kde

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def plotDots(d, dest='plot'):
    xRaw = d[0]
    yRaw = d[1]

    DataBuckets = 10    #   Number of colors plotted
    
    x = split_list(xRaw, wanted_parts = DataBuckets)
    y = split_list(yRaw, wanted_parts = DataBuckets)
    
    ColorMap = {0: ['#1f77b4'], 
                1: ['#ff7f0e'], 
                2: ['#2ca02c'], 
                3: ['#d62728'], 
                4: ['#9467bd'], 
                5: ['#8c564b'], 
                6: ['#e377c2'], 
                7: ['#7f7f7f'], 
                8: ['#bcbd22'], 
                9: ['#17becf']}

    left, width = 0.05, 0.90
    bottom, height = 0.05, 0.95
    rect_scatter = [left, bottom, width, height]

    title = "\nScatter Plot of {:,} digits of PI()".format(len(d[0])-2) 
    
    # plt.title(title, fontsize=20, fontweight=0, color='purple', loc='left', style='italic')

    axScatter = plt.axes(arg=rect_scatter, frameon = False, aspect='auto')
    plt.axis('off')

    for i in range(DataBuckets):
        if i == 0:
            axScatter.scatter(x[i], y[i], s=1, marker=',', linestyle='-', c=ColorMap[i])
        else:
            xdata = [x[i-1][len(x[i-1])-1]] + x[i]
            ydata = [y[i-1][len(y[i-1])-1]] + y[i]
            axScatter.scatter(xdata, ydata, s=1, marker=',', linestyle='-', c=ColorMap[i])

    if dest == 'both':
        plt.show()
        plt.savefig('C:\\Temp\\PIplotOutput.jpg', type='jpg', dpi=300)
        print(datetime.now(), 'Plot Saved to "C:\\Temp\\PIplotOutput.jpg" and Displayed.')
    if dest == 'plot':
        plt.show()
        print(datetime.now(), 'Only Plot Displayed')
    if dest == 'save':
        plt.plot(x,y, 'b,', markersize=1)
        plt.savefig('C:\\Temp\\PIplotOutput.jpg', type='jpg', dpi=300)
        print(datetime.now(), 'Plot Saved to "C:\\Temp\\PIplotOutput.jpg".')

def plotDensity(d, dest='plot'):

    # https://python-graph-gallery.com/
    x = d[0]
    y = d[1]

    # Create a figure with 6 plot areas
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(21, 5))
    
    # Everything sarts with a Scatterplot
    ax[0].set_title('Scatterplot')
    ax[0].plot(x, y, 'ko')
    # As you can see there is a lot of overplottin here!
    
    # Thus we can cut the plotting window in several hexbins
    nbins = 20
    ax[1].set_title('Hexbin')
    ax[1].hexbin(x, y, gridsize=nbins, cmap=plt.cm.BuGn_r)
    
    # # 2D Histogram
    # ax[2].set_title('2D Histogram')
    # ax[2].hist2d(x, y, bins=nbins, cmap=plt.cm.BuGn_r)
    
    # # # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
    # k = kde.gaussian_kde([x,y])
    # xi, yi = np.mgrid[min(x):max(x):nbins*1j, min(y):max(y):nbins*1j]
    # zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    
    # # plot a density
    # ax[3].set_title('Calculate Gaussian KDE')
    # ax[3].pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.cm.BuGn_r)
    
    # # add shading
    # ax[4].set_title('2D Density with shading')
    # ax[4].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.BuGn_r)
    
    # contour
    ax[5].set_title('Contour')
    ax[5].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.BuGn_r)
    ax[5].contour(xi, yi, zi.reshape(xi.shape))

    plt.tight_layout()
    plt.show()    

def plotHeatMap(d, dest='plot'):
    # https://python-graph-gallery.com/
    x = d[0]
    y = d[1]

    plt.style.use('seaborn')
 
    # Dataset:
    df=pd.DataFrame({'x': np.random.normal(10, 1.2, 20000), 'y': np.random.normal(10, 1.2, 20000), 'group': np.repeat('A',20000) })
    tmp1=pd.DataFrame({'x': np.random.normal(14.5, 1.2, 20000), 'y': np.random.normal(14.5, 1.2, 20000), 'group': np.repeat('B',20000) })
    tmp2=pd.DataFrame({'x': np.random.normal(9.5, 1.5, 20000), 'y': np.random.normal(15.5, 1.5, 20000), 'group': np.repeat('C',20000) })
    df=df.append(tmp1).append(tmp2)
    
    # Plot with transparency
    plt.plot( 'x', 'y', data=df, linestyle='', marker='o', markersize=3, alpha=0.05, color="purple")
    
    # plot
    plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
    plt.xlabel('Value of X')
    plt.ylabel('Value of Y')
    plt.title('Overplotting looks like that:', loc='left')

def plotDensity2(d, dest='plot'):
    
    # https://python-graph-gallery.com/
    x = d[0]
    y = d[1]

    X = sp.filters.gaussian_filter(x, sigma = 2, order = 0)
    Y = sp.filters.gaussian_filter(y, sigma = 2, order = 0)

    title = "Heatmap of {:,} digits of PI()".format(len(d[0])-2)
    plt.title(title)

    heatmap, xedges, yedges = np.histogram2d(X, Y, bins=150)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    # https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html?highlight=ylorrd
    plt.imshow(heatmap, extent=extent, cmap='hot')
    plt.colorbar()
    plt.show()    