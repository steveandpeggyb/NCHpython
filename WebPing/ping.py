import csv
import subprocess

# read file in

f=open('./WebPing/hosts.csv', 'r')
reader = csv.reader(f)

print('\r\n..........Process Beginning..........\r\n')
for row in reader:
    if row[0] == 'IPaddress':
        pass
    else:
        (output, error) = subprocess.Popen((['ping', row[0], '-w', '2']), stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
        print("{}\tOutput: {}\r\nError: {}".format(row[1],output, error))
print('\r\n..........Process completed..........')      