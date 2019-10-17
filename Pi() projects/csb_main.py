from csb_pi import CalcPi
# from csb_navigate import calcVector
# from csb_plot import *
import csv
from datetime import datetime
import time
import multiprocessing

start = time.perf_counter()

DesiredDigits = 50000000

print('\n{}\tPlease wait... Calculating {:,} digits of Pi()...'.format(datetime.now(), DesiredDigits))
pi=CalcPi(DesiredDigits)
# pi=multiprocessing.Process(target=CalcPi)
# pi.start()

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

# plotHeatMap(output, dest)
# plotDots(output, dest)
# plotDensity(output, dest)
# plotDensity2(output, dest)

finish = time.perf_counter()
print(datetime.now(), 'Done!')

if finish-start < 60:
    t=str(round(finish-start, 3)) + ' seconds.'
else:
    t=str(round((finish-start)/60, 3)) + ' minutes.'

#  print results
print("Calculated and saved, {0:,} digits of Pi() in {1}\n".format(DesiredDigits, t))