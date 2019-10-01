# 4 * ( (1/1)-(1/3)+(1/5)-(1/7)...)
import math
import time

denominator = []
iterations = 1000000
performAdd = False
bucket = 0.0
Start = time.perf_counter()

i = 0
while i <= iterations:
    i += 1
    denominator.append(i)
    i += 1

for i in denominator:
    if performAdd == False:
        bucket = bucket + (1/i)
        performAdd = True
    else:
        bucket = bucket - (1/i)
        performAdd = False

pi = 4 * bucket
print(pi)
print(math.pi)
print('Execution Time: ', str(time.perf_counter()-Start))

