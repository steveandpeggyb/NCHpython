from csb_pi import CalcPi
# from csb_navigate import calcVector
# from csb_plot import *
import csv
from datetime import datetime
import time
import multiprocessing
from decimal import *

<<<<<<< HEAD
print(datetime.now(), 'Please wait.  Calculating pi()...')
pi=CalcPi(100000)
=======

start = time.perf_counter()

DesiredDigits = Decimal(70000000/1)

print('\n{}\tPlease wait... Calculating {:,} digits of Pi()...'.format(datetime.now(), DesiredDigits))
pi=CalcPi(DesiredDigits)
>>>>>>> b6fc77b908db56cda78bb0110cbd6170c23e1155

# Save the results of PI()
writeFile = open('C:\\Temp\\PiDigits.txt', 'w+t')
writer = csv.writer(writeFile)
writer.writerow([pi])
writeFile.close()

# print(datetime.now(), 'Please wait.  vectoring pi()...')
# output = calcVector(pi)

# # Save the vector for each digit of PI()
# writeFile = open('C:\\Temp\\OutputCSVfile.csv', 'w+t')
# writer = csv.writer(writeFile)
# writer.writerow([output])
# writeFile.close()

# print(datetime.now(), 'Please wait.  plotting pi()...')
# # build scope
# # dest = 'save'
# # dest = 'plot'
# dest = 'both'

<<<<<<< HEAD
plotHeatMap(output, dest)
=======
# plotHeatMap(output, dest)
>>>>>>> b6fc77b908db56cda78bb0110cbd6170c23e1155
# plotDots(output, dest)
# plotDensity(output, dest)
# plotDensity2(output, dest)

finish = time.perf_counter()
print(datetime.now(), '\tFile is located at: C:\\Temp\\PiDigits.txt')

if finish-start < 60:
    t=str(round(finish-start, 3)) + ' seconds.'
else:
    t=str(round((finish-start)/60, 3)) + ' minutes.'

#  print results
print("Calculated and saved, {0:,} digits of Pi() in {1}\n".format(DesiredDigits, t))