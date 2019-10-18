# from csb_pi import CalcPi
import numpy as np
import pandas as pd
             
def calcVector(sPi):
    print(sPi)
     # recalculated navigation coordinates
    xDict = {0: 0, 1: 1.7633558, 2: 2.8531695, 3: 2.8531695, 4: 1.7633558, 5: 0, 6: -1.7633558, 7: -2.8531695, 8: -2.8531695, 9: -1.7633558}
    yDict = {0: 3, 1: 2.427051, 2: 0.927051, 3: -0.927051, 4: -2.427051, 5: -3, 6: -2.427051, 7: -0.927051, 8: 0.927051, 9: 2.427051}

    yRaw = []
    xRaw = []

    # sPi = '0'+str(p.replace('\n', ''))
    sPi = sPi.replace('.','')

    for index in range(0, len(sPi)):       #   Build the plot series
        if index == 0:
            xRaw.append(0)
            yRaw.append(0)
        else:
            xRaw.append(float(xDict[int(sPi[index])]) + xRaw[index-1])
            yRaw.append(float(yDict[int(sPi[index])]) + yRaw[index-1])

    # df = pd.DataFrame()


    # for x in range(len(xRaw)-1):
    #     data = {'xRaw':[xRaw[x]], 'yRaw':[yRaw[x]]}
    #     df = pd.DataFrame(data)

    return xRaw,yRaw