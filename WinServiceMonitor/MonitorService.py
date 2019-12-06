import sys
import psutil
import win32service
import win32serviceutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

STOPPED = 1
target = 'ReportServer$DEVSERVER'

# In Windows Services, double-click the service. In the dialog box, use the "Service name:"
service = getService(target)
print('\r\nThe "' + target + '" service is ' +  service['status'] + '.')

if service['status'] == 'stopped':
    SendTo = SendFrom = 'steve.blake@nationwidechildrens.org'
    subject = 'WINDOWS SERVICE: ' + service['display_name'] + ' seems to be OFF!'
    body = '<p>WINDOWS SERVICE: <strong><font color=blue>' + service['display_name'] + '</font></strong> seems to be OFF!<p>'
    body = body + '<p> On the server, open "windows services" and restart the service.'
    SendHTMLemail(SendTo, SendFrom, subject, body)
    print('Email has been sent to document this ')

