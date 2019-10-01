from csb_pi import CalcPi
from csb_navigate import calcVector
from csb_plot import plotHeatMap
from csb_plot import plotDots
import csv
from datetime import datetime

print(datetime.now(), 'Please wait.  Calculating pi()...')
pi=CalcPi(10000)

# Save the results of PI()
writeFile = open('C:\\Users\\csb003\\Desktop\\PythonProjects\\Pi() projects\\PiDigits.txt', 'w+t')
writer = csv.writer(writeFile)
writer.writerow([pi])
writeFile.close()

print(datetime.now(), 'Please wait.  vectoring pi()...')
output = calcVector(pi)

# Save the vector for each digit of PI()
writeFile = open('C:\\Temp\\OutputCSVfile.csv', 'w+t')
writer = csv.writer(writeFile)
writer.writerow([output])
writeFile.close()

print(datetime.now(), 'Please wait.  plotting pi()...')
# build scope
# dest = 'save'
# dest = 'plot'
dest = 'both'

# plotHeatMap(output)
plotDots(output, dest)

print(datetime.now(), 'Done!')