import subprocess

def ping_ip(ip):
    (output, error) = subprocess.Popen((['ping', ip, '-w', '2']), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print(output)
    #for windows use -n instead of -c after ping, ip.
    if b'Reply from ' in output:
        return ("UP", 1)
    elif b'Request timed out.' in output:
        return ("Request timed out.", 0)
    elif error:
        return ("DNS Error",0)
    else:
        return ("UNKNOWN",0)

l = ''
with open('./WebPing/devices.txt') as f:
    for ip in f:
        ip = ip.strip('\n')
        response, t = ping_ip(ip)
        result = ('%s\t%i\t%s \n' % (ip, t, response))
        l = l+result

print('\r\n'+l)
file = open('./WebPing/output.txt', 'w')
file.write(l)
file.close()

print("Output.txt was created with these scanned results.")