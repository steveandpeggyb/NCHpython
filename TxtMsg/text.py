import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendText(number, message):
    # https://automatetheboringstuff.com/chapter16/
    username = "steve.blake1nch@gmail.com"
    password = ""

    number = number + "@vtext.com"
    message = "this is the message to be sent"

    msg = """From: %s
    To: %s
    Subject: text-message
    %s""" % (username, number, message)

    # server = smtplib.SMTP('smtp.gmail.com',587)
    server = smtplib.SMTP('xmail.nationwidechildrens.org')
    server.starttls()
    # server.login(username,password)
    server.sendmail(username, number, msg)
    server.quit()

def sendTxtMsg(number, body):
    
    # https://dev.to/mraza007/sending-sms-using-python-jkd
    
    email = os.environ.get('exyz')
    pas = os.environ.get('pxyz')

    sms_gateway = number + '@vtext.com'
    # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
    # and port is also provided by the email provider.
    smtp = "smtp.gmail.com" 
    port = 587
    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    # Make sure you add a new line in the subject
    msg['Subject'] = "You can insert anything\n"
    # Make sure you also add new lines to your body
    body = "You can insert message here\n"
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email,sms_gateway,sms)

    # lastly quit the server
    server.quit()

sendTxtMsg('6144778613', 'This is a test text message')