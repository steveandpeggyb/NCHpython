from csb_navigate import calcVector
import matplotlib.pyplot as plt
import time

filename = 'C:\\Users\\csb003\\Documents\\NCHpython\\Pi() projects\\01m-PiDigits.txt'
file = open(filename, mode='r')
piTxt = file.read()
file.close()
piTxt = piTxt.rstrip()

xRaw, yRaw = calcVector(piTxt)




# Plot the x and y values
plt.xlabel('X')
plt.ylabel('Y')

start = time.perf_counter()
plt.scatter(xRaw, yRaw, label='Legend Title', color='b', marker='.', s = 1)
# plt.plot(xRaw, yRaw, label='Legend Title', color='b', marker='.', markersize = 1, linestyle=':')
plt.title('Interesting plot')

plt.legend()
plt.show()
finish = time.perf_counter()

if finish-start < 60:
    t=str(round(finish-start, 3)) + ' seconds.'
else:
    t=str(round((finish-start)/60, 3)) + ' minutes.'

print("Plotted {0:,} digits of Pi() in {1}\n".format(len(xRaw)-1, t))