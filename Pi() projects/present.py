# from numpy import zeros

f = open("C:\\Users\\csb003\\Documents\\NCHpython\\Pi() projects\\10k-DigitsPi.txt", "r")
piData = f.read()
f.close()

# recalculated navigation coordinates
xDict = {'0': 0, '1': 1.7633558, '2': 2.8531695, '3': 2.8531695, '4': 1.7633558, '5': 0, '6': -1.7633558, '7': -2.8531695, '8': -2.8531695, '9': -1.7633558}
yDict = {'0': 3, '1': 2.427051, '2': 0.927051, '3': -0.927051, '4': -2.427051, '5': -3, '6': -2.427051, '7': -0.927051, '8': 0.927051, '9': 2.427051}

Output = []
NewX = 0
NewY = 0

for digit in piData:
    if digit not in ('.', '\n'):
        NewX = xDict[digit]+NewX
        NewY = yDict[digit]+NewY
        Output.append([NewX, NewY])

# for e in a:
#     print(e)

print("All Done!")