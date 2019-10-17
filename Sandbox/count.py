import numpy as np
import time

start = time.perf_counter()

total = 0
f = 'C:\\Users\\csb003\\Documents\\NCHpython\\Pi() projects\\60m-PiDigits.txt'
file = open(f, 'r')
pi=file.read()
            
            

for i in range(10):
    sub = str(i)
    c = pi.count(sub)
    total += c
    print(i, c)

finish = time.perf_counter()
print("total numbers: ", total)
if finish-start < 60:
    t=str(round(finish-start, 3)) + ' seconds.'
else:
    t=str(round((finish-start)/60, 3)) + ' minutes.'

print('Processing Time: ', t)