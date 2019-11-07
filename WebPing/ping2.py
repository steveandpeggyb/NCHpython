import subprocess

def ping_ip(ip):
    (output, error) = subprocess.Popen((['ping', ip, '-w', '2']), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    #for windows use -n instead of -c after ping, ip.
    if b'Reply from ' in output:
        return "UP"
    elif b'Request timed out.' in output:
        return "Request timed out."
    elif error:
        return "DNS Error"
    else:
        return "UNKNOWN"

l = ''
with open('./WebPing/devices.txt') as f:
    for ip in f:
        ip = ip.strip('\n')
        response = ping_ip(ip)
        result = ('%s\t%s \n' % (response, ip))
        l = l+result

print(l)
file = open('output.txt', 'w')
file.write(l)
file.close()