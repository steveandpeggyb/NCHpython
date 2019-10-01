import numpy as np
import decimal, time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import matplotlib.cm as cm

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

date_object = datetime.now()
start_clock = date_object.strftime('%H:%M:%S')


starttime=time.process_time()
DataBuckets = 10    #   Number of colors plotted
DigitCount =  1000 #   Number of Digits to Calculate

print('Decimal Places Calculated: \t\t{0:,d}'.format(DigitCount))
print('------------------------------------------------------------------------')
decimal.getcontext().prec = DigitCount + 1   #8751
pi = pi_gauss_legendre()
stoptime=time.process_time()
# print('\r\n-------\r\n' + str(pi) + '\r\n-------\r\n')
duration = stoptime - starttime
if duration == 0:
    duration = .0001    # if calculation take less than one second, this line will prevent a divide by zero error.
decimalPlaces = len(str(pi))-2
CharPerSec = decimalPlaces/(duration)

date_object = datetime.now()
stop_clock = date_object.strftime('%H:%M:%S')

# define the data
theTitle = "Plot " + format(DigitCount, ",d") + " digits of PI()"

xDict = {0: 0, 1: 1.2, 2: 2.4, 3: 2.4, 4: 1.2, 5: 0, 6: -1.2, 7: -2.4, 8: -2.4, 9: -1.2}
yDict = {0: 3, 1: 1.8, 2: 0.6, 3: -0.6, 4: -1.8, 5: -3, 6: -1.8, 7: -0.6, 8: 0.6, 9: 1.8}
ColorMap = {0: [128, 128, 128], 1: [255, 0, 0], 2: [128, 64, 255], 3: [0, 128, 0], 4: [128, 0, 255], 5: [128, 0, 128], 6: [0, 0, 255], 7: [255, 0, 255], 8: [128, 64, 64], 9: [255, 128, 0]}


y = []
x = []
sPi = '0'+str(pi)
sPi = sPi.replace('.','')

# create plot coordinates
StartTime = datetime.now()
print(StartTime, '\t\tBegin Plotting PI()')
for index in range(0, len(sPi)):       #   Build the plot series
    # print(sPi[index])
    if index == 0:
        x.append(0)
        y.append(0)
    else:
        x.append(float(xDict[int(sPi[index])]) + x[index-1])
        y.append(float(yDict[int(sPi[index])]) + y[index-1])
EndTime = datetime.now()
print(EndTime, '\tPI() Plot Completed')
print(EndTime - StartTime, '\t\tTotal Plot Time\r\n')
# answer = input('Plot? ')
# answer = answer.lower()
# if answer[:1] != 'n':
    #   Matplotlib code
nullfmt = NullFormatter()         # no labels

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left + width + 0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(12, 12))

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot:
yRaw = []
xRaw = []

#   split the data into 10 groups
x = split_list(xRaw, wanted_parts = DataBuckets)
y = split_list(yRaw, wanted_parts = DataBuckets)

for i in range(DataBuckets):
    print(ColorMap[i])
    if i == 0:
        axScatter.scatter(x[i], y[i], s=1, marker='.', linestyle='-', c=ColorMap[i])
    else:
        xdata = [x[i-1][len(x[i-1])-1]] + x[i]
        ydata = [y[i-1][len(y[i-1])-1]] + y[i]
        axScatter.scatter(xdata, ydata, s=1, marker='.', linestyle='-', c=ColorMap[i])

# now determine nice limits by hand:
binwidth = 0.25
xmax = int(np.max((x))*1.1)
xmin = int(np.min((x))*1.1)
ymax = int(np.max((y))*1.1)
ymin = int(np.min((y))*1.1)


axScatter.set_xlim((xmin, xmax))
axScatter.set_ylim((ymin, ymax))

xbins = np.arange(xmin, xmax + binwidth, binwidth)
ybins = np.arange(ymin, ymax + binwidth, binwidth)
axHistx.hist(x, bins=xbins, orientation='vertical')
axHisty.hist(y, bins=ybins, orientation='horizontal')

axHistx.set_xlim(axScatter.get_xlim())
axHisty.set_ylim(axScatter.get_ylim())

plt.show()
