import smtplib



sender = 'steve.blake@nationwidechildrens.org'
receivers = 'steve.blake@nationwidechildrens.org'

message = """From: Steve Blake <'steve.blake@nationwidechildrens.org'>
To: Steve Blake <'steve.blake@nationwidechildrens.org'>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('xmail.nationwidechildrens.org' , 25)
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
