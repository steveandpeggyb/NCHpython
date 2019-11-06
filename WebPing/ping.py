import csv
import os

# read file in

f=open('./WebPing/hosts.csv', 'r')
reader = csv.reader(f)

for row in reader:
    if row[0] == 'IPaddress':
        pass
    else:
        ping_response = os.system("ping -c 1 row[0]")
        print("Pinging {}({}): {}".format(row[1], row[0], ping_response))
