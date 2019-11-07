import csv
import subprocess

# read file in

f=open('./WebPing/hosts.csv', 'r')
reader = csv.reader(f)

for row in reader:
    if row[0] == 'IPaddress':
        pass
    else:
        (output, error) = subprocess.Popen((['ping', row[0], '-c', '2']), stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
        print("Output: {}\r\nError: {}".format(output, error))
print('Process completed..........')      