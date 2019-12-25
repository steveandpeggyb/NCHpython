import sys
import time
import psutil
import win32service
import win32serviceutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def SendHTMLemail(toEmail, fromEmail, subject, body):

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = toEmail

    # Create the body of the message (a plain-text and an HTML version).
    text = 'Windows Service Monitor'
    html = """\
    <html>
    <head></head>
    <body>"""
    html = html + body
    html = html + """</body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('xmail.nationwidechildrens.org')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(fromEmail, toEmail, msg.as_string())
    s.quit()
def getService(name): 
        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service
def service_info(action, machine, target):
    if action == 'stop': 
        win32serviceutil.StopService(target, machine)
        print('%s stopped successfully' % service)
    elif action == 'start': 
        win32serviceutil.StartService(target, machine)
        print('%s started successfully' % service)
    elif action == 'restart': 
        win32serviceutil.RestartService(target, machine)
        print('%s restarted successfully' % service)
    elif action == 'status':
        if win32serviceutil.QueryServiceStatus(target, machine)[1] == 4:
            print("%s is running normally" % target )
        else:
            print("%s is *not* running" % target)

STOPPED = 1
now=datetime.now()
ActionTimestamp = now.strftime("%Y%m%d-%H%M%S")

target = 'ReportServer$DEVSERVER'
machine = 'resd9-gzmmmr2'
action = 'start'

# In Windows Services, double-click the service. In the dialog box, use the "Service name:"
service = getService(target)

# Open log file to record all activity
f = open("C:\\NightlyJobs\\MonitorService.log", "a+")
f.write(now.strftime("%Y%m%d-%H%M%S") + '\tThe "' + target + '" service is ' +  service['status'] + '.\r')

if service['status'] == 'stopped':
    SendTo = SendFrom = 'steve.blake@nationwidechildrens.org'
    subject = 'WINDOWS SERVICE: ' + service['display_name'] + ' seems to be OFF!'
    body = '<p>WINDOWS SERVICE: <strong><font color=blue>' + service['display_name'] + '</font></strong> seems to be OFF!<p>'
    f.write(now.strftime("%Y%m%d-%H%M%S") + '\tAn Email has been sent to document service failure. Attempting a restart process.\r')
    body = body + '<p>Attempting to restart the service.'
    service_info('restart', machine, target)
    service = getService(target)
    time.sleep(10) # delays for 10 seconds
    if service['status'] == 'stopped':
        body = body + '<p>Attempt to restart the service failed.'
        body = body + '<p>On the server, open <i>"windows services"</i> and restart the service.'
        f.write(now.strftime("%Y%m%d-%H%M%S") + '\tFailed to restart service')
    else:
        body = body + '<p>Attempt to restart the service was successful. No further action is required.'
        f.write(now.strftime("%Y%m%d-%H%M%S") + '\tService was restarted.')
    SendHTMLemail(SendTo, SendFrom, subject, body)

f.close()