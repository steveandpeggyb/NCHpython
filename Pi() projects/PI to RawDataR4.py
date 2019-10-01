from __future__ import with_statement
import pandas as pd
import numpy as np
import decimal, time
from datetime import datetime
import csv

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
#   ==========================================================================================

DataBuckets = 10

date_object = datetime.now()
start_clock = date_object.strftime('%H:%M:%S')

starttime=time.process_time()
DigitCount =  1000
print('Decimal Places Calculated: \t\t{0:,d}'.format(DigitCount))
print('------------------------------------------------------------------------')
decimal.getcontext().prec = DigitCount - 1   #8751

#   Calculate xDigits of PI()
pi = pi_gauss_legendre()

writeFile = open('C:\\Users\\csb003\\Desktop\\PythonProjects\\Pi() projects\\PiDigits.txt', 'w+t')
writer = csv.writer(writeFile)
writer.writerow([pi])
writeFile.close()

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

yRaw = []
xRaw = []

sPi = '0'+str(pi)
sPi = sPi.replace('.','')

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

StartTime = datetime.now()
print(StartTime, '\t\tBegin Plotting PI()')

inilrow = {'xCol': [0.01], 'yCol': [0.01]}
PrepForOutput = pd.DataFrame(inilrow)

for x in range(len(xRaw)):
    new_row = {'xCol': xRaw[x], 'yCol': yRaw[x]}
    PrepForOutput = PrepForOutput.append(new_row, ignore_index = True)
    # PrepForOutput = np.append(PrepForOutput, ['\n' + str(xRaw[x]) + ', ' + str(yRaw[x])])

writeFile = open('C:\\Users\\csb003\\Desktop\\PythonProjects\\Pi() projects\\pidata.csv', 'w')
writer = csv.writer(writeFile)
writer.writerows([PrepForOutput])
writeFile.close()

EndTime = datetime.now()

print('\n\n--------------------------------------------------------------------------------------------------')
print(EndTime, '\t\tPI() Plot Completed')
print(EndTime - StartTime, '\t\tTotal Plot Time')

