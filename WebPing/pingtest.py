import os
import csv

f=open('./WebPing/hosts.csv', 'r')
reader = csv.reader(f)

for row in reader:
    if row[0] == 'IPaddress':
        pass
    else:
        ping = os.system("Ping " + row[0])
        if ping ==0:
            print(row[1]+"(" + row[0]+ ")", " is Up")
        else:
            print(row[1]+"(" + row[0]+ ")", " is Down")
