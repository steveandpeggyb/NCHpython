import smtplib



sender = 'steve.blake@nationwidechildrens.org'
receivers = 'steve.blake@nationwidechildrens.org'

message =           "From: Steve Blake <'" + sender + "'>\n"
message = message + "To: Steve Blake <'" + sender + "'>\n"
message = message + "Subject: SMTP e-mail test\n"
message = message + "This is a test e-mail message.\n"

try:
    smtpObj = smtplib.SMTP('xmail.nationwidechildrens.org' , 25)
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
