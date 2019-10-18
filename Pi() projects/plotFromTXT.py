from csb_navigate import calcVector
import matplotlib.pyplot as plt

filename = 'C:\\Users\\csb003\\Documents\\NCHpython\\Pi() projects\\100-PiDigits.txt'
file = open(filename, mode='r')
piTxt = file.read()
file.close()
piTxt = piTxt.rstrip()

xRaw, yRaw = calcVector(piTxt)

# Plot the x and y values
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(xRaw, yRaw, label='Legend Title', color='b', marker='.', s = 50)
plt.title('Interesting plot')
plt.legend()
plt.show()