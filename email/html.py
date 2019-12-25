#! /usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendHTMLemail(toEmail, fromEmail, subject, body):
    # me == my email address
    # you == recipient's email address
    if fromEmail == None:
        fromEmail = "steve.blake@nationwidechildrens.org"
    if toEmail == None:
        toEmail = "steve.blake@nationwidechildrens.org"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = toEmail

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
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

SendHTMLemail(  toEmail=    '16144778613@vtext.com', 
                fromEmail=  'steve.blake@nationwidechildrens.org', 
                subject=    'Test email', 
                body=       '<strong><font color=blue>Welcome</font></strong> to this world.'
            )
