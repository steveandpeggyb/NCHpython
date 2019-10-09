import smtplib
from Send_Mail import xmitEmail

sender = 'steve.blake@nationwidechildrens.org'
receivers = 'steve.blake@nationwidechildrens.org'
subject = "This is the subject line"
body = "This is the body of the email."
filename = "C:\\DBfiles\\OutputCSVfile.csv"

print(xmitEmail(sender, receivers, subject, body))