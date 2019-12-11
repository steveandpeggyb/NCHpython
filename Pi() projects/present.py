# from numpy import zeros
import matplotlib.pyplot as plt
import pandas

f = open("C:\\Users\\csb003\\Documents\\NCHpython\\Pi() projects\\10k-PiDigits.txt", "r")
piData = f.read()
f.close()

# recalculated navigation coordinates
xDict = {'0': 0, '1': 1.7633558, '2': 2.8531695, '3': 2.8531695, '4': 1.7633558, '5': 0, '6': -1.7633558, '7': -2.8531695, '8': -2.8531695, '9': -1.7633558}
yDict = {'0': 3, '1': 2.427051, '2': 0.927051, '3': -0.927051, '4': -2.427051, '5': -3, '6': -2.427051, '7': -0.927051, '8': 0.927051, '9': 2.427051}

x, y = [0],[0]
NewX = 0
NewY = 0
pip
for digit in piData:
    if digit not in ('.', '\n'):
        NewX = xDict[digit]+NewX
        NewY = yDict[digit]+NewY
        x.append(NewX)
        y.append(NewY)

#   Plot the data

fig, ax = plt.subplots()

# https://www.w3schools.com/colors/colors_xkcd.asp
ax.plot(x, y, 'xkcd:indigo')

Title = "{:,}".format(len(x)-1) + " Digits of PI()"

ax.set_axis_off()
ax.set(title= Title)
ax.grid(False)

fig.savefig("C:\\Users\\csb003\\Documents\\NCHpython\\Pi() projects\\test.png")

plt.show() 

print("All Done!")