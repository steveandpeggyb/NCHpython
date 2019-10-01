import numpy as np
import decimal, time
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

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
DigitCount =  1000
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

y = []
x = []
sPi = '0'+str(pi)
sPi = sPi.replace('.','')

# create plot

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
print(EndTime, '\t\tPI() Plot Completed')
print(EndTime - StartTime, '\t\tTotal Plot Time\r\n')
answer = input('Plot? ')
answer = answer.lower()

if answer.startswith('y'):
#   Plot the image
    trace1 = go.Heatmap([(x),(y)])
    data=[trace]
    py.iplot(data)
