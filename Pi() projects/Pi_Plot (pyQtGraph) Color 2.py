from __future__ import with_statement
#   http://www.pyqtgraph.org/documentation/colormap.html
import numpy as np
import decimal, time
import pyqtgraph as pg
import pyqtgraph.exporters
from datetime import datetime

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def pi_gauss_legendre():
    StartTime = datetime.now()
    print(StartTime, '\t\tBegin Calculating PI().')
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2                
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1                
        pi = None
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            piold = pi
            pi    = (a + b) * (a + b) / (4 * t)
            if pi == piold:  # equal within given precision
                break
    EndTime = datetime.now()
    print(EndTime, '\t\tPI() is calculated.')
    print(EndTime-StartTime, '\t\tTotal Calc Time')
    return +pi

DataBuckets = 10
pg.setConfigOption('background', 'w')

date_object = datetime.now()
start_clock = date_object.strftime('%H:%M:%S')

starttime=time.process_time()
DigitCount =  10000
print('Decimal Places Calculated: \t\t{0:,d}'.format(DigitCount))
print('------------------------------------------------------------------------')
decimal.getcontext().prec = DigitCount + 1   #8751

#   Calculate xDigits of PI()
pi = pi_gauss_legendre()

#   Track time for reporting
stoptime=time.process_time()
duration = stoptime - starttime

if duration == 0:
    duration = .0001    # if calculation take less than one second, this line will prevent a divide by zero error.
decimalPlaces = len(str(pi))-2
CharPerSec = decimalPlaces/(duration)

date_object = datetime.now()
stop_clock = date_object.strftime('%H:%M:%S')

theTitle = 'Decimal Places Calculated: \t\t{0:,d}'.format(DigitCount)

# recalculated navigation coordinates
xDict = {0: 0, 1: 1.7633558, 2: 2.8531695, 3: 2.8531695, 4: 1.7633558, 5: 0, 6: -1.7633558, 7: -2.8531695, 8: -2.8531695, 9: -1.7633558}
yDict = {0: 3, 1: 2.427051, 2: 0.927051, 3: -0.927051, 4: -2.427051, 5: -3, 6: -2.427051, 7: -0.927051, 8: 0.927051, 9: 2.427051}
# ColorMap = {0: [128, 128, 128], 1: [255, 0, 0], 2: [128, 64, 255], 3: [0, 128, 0], 4: [128, 0, 255], 5: [128, 0, 128], 6: [0, 0, 255], 7: [255, 0, 255], 8: [128, 64, 64], 9: [255, 128, 0]}
ColorMap = {1: '808080', 2: 'FF0000', 3: '8040FF', 4: '000800', 5: '800FF', 6: '80080', 7: '0000FF', 8: 'FF00FF', 9: '804040', 10: 'FF8000'}

yRaw = []
xRaw = []
sPi = '0'+str(pi)
sPi = sPi.replace('.','')

# create plot
StartTime = datetime.now()
print(StartTime, '\t\tBegin Plotting PI()')
for index in range(0, len(sPi)):       #   Build the plot series
    # print(sPi[index])
    if index == 0:
        xRaw.append(0)
        yRaw.append(0)
    else:
        xRaw.append(float(xDict[int(sPi[index])]) + xRaw[index-1])
        yRaw.append(float(yDict[int(sPi[index])]) + yRaw[index-1])
        
#   split the data into 10 groups
x = split_list(xRaw, wanted_parts = DataBuckets)
y = split_list(yRaw, wanted_parts = DataBuckets)

EndTime = datetime.now()
print(EndTime, '\t\tPI() Plot Completed')
print(EndTime - StartTime, '\t\tTotal Plot Time')

plotWidget = pg.plot(title=theTitle)
answer = input('Plot? ')
answer = answer.lower()
if answer[:1] != 'n':
    for i in range(DataBuckets):
        if i == 0:
            plotWidget.plot(x[i], y[i], pen=pg.mkPen(RGB=ColorMap[i], width=.5))
        else:
            xdata = [x[i-1][len(x[i-1])-1]] + x[i]
            ydata = [y[i-1][len(y[i-1])-1]] + y[i]
            plotWidget.plot(xdata, ydata, pen=pg.mkPen(RGB=ColorMap[i], width=.5))

## Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
