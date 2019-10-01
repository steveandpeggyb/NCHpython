import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb; sb.set()

def plotit(d):
    x = d[0]
    y = d[1]

    pvalues = [x,y]

    def checkx(TheList, min, max): 
        result = 0      
        # traverse in the list 
        for x in TheList: 
    
            # compare with all the values 
            # with val 
            if (x >= min) and (x <= max): 
                result += 1 

        return result
    def checky(TheList, min, max): 
        result = 0      
        # traverse in the list 
        for x in TheList: 
    
            # compare with all the values 
            # with val 
            if (x >= min) and (x <= max): 
                result += 1 

        return result

    title = "Scatter Plot of {:,} digits of PI()".format(len(pvalues[0])-2)

        # character description
        # '-'       solid line style
        # '--'      dashed line style
        # '-.'      dash-dot line style
        # ':'       dotted line style
        # '.'       point marker
        # ','       pixel marker
        # 'o'       circle marker
        # 'v'       triangle_down marker
        # '^'       triangle_up marker
        # '<'       triangle_left marker
        # '>'       triangle_right marker
        # '1'       tri_down marker
        # '2'       tri_up marker
        # '3'       tri_left marker
        # '4'       tri_right marker
        # 's'       square marker
        # 'p'       pentagon marker
        # '*'       star marker
        # 'h'       hexagon1 marker
        # 'H'       hexagon2 marker
        # '+'       plus marker
        # 'x'       x marker
        # 'D'       diamond marker
        # 'd'       thin_diamond marker
        # '|'       vline marker
        # '_'       hline marker

    # plt.scatter(x,y)    #, s=0, label='',c='w', alpha=0.7)    #, linestyle='--')
    # plt.plot(x,y)
    # plt.xlabel('')
    # plt.ylabel('')
    plt.title(title)
    # plt.legend()

    # Use Seaborn to do the scatter plot and heatmap
    # ax = sb.scatterplot(x=x, y=y, x_bins=10, y_bins=10)
    # ax = sb.heatmap(pvalues, cbar=True)

    # z = f(x,y)
    # ax = sb.heatmap(z, xticklabels = 50, cmap = 'RdYlGn' ,yticklabels=50, vmin = -5, vmax=5)
    # ax.invert_yaxis()

    # Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2) # calcul du tableau des valeurs de Z

    # plt.imshow(np.transpose(Z), extent=[0,4.2,0,48000], cmap='jet',
    #        vmin=-100, vmax=0, origin='lowest', aspect='auto')
    # plt.pcolor(x, y, Z)
    # plt.colorbar()
    # plt.show()

    # x = np.linspace(-3, 3, 51)
    # y = np.linspace(-2, 2, 41)
    X, Y = np.meshgrid(x, y)

    # Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2) # calcul du tableau des valeurs de Z
    
    Z=[]
    scope = 10
    index = 0
    for index in range(len(x)-1):
        print('Index =', index)
        print('x count: ', checkx(x, x[index]-scope, x[index]+scope))
        print('y count: ', checkx(y, y[index]-scope, y[index]+scope))
        Z(index) = checkx(x, x[index]-scope, x[index]+scope) + checky(y, y[index]-scope, y[index]+scope)
    
    plt.pcolor(X, Y, Z)



    plt.plot(x,y, 'wo', markersize=1)
    plt.colorbar()
    plt.show()