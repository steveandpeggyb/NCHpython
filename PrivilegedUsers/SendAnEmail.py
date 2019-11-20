from email.mime.text import MIMEText
import smtplib

def send_email(subject, body, to):
    s = smtplib.SMTP('xmail.nationwidechildrens.org')
    mime = MIMEText(body)
    mime['Subject'] = subject
    mime['To'] = to
    s.sendmail('steve.blake@nationwidechildrens.org', to, mime.as_string())

subj = 'This is a subject line'
text = 'This is the body of the email and should be written in <HTML> so that <br> should work.'
send_to = 'steve.blake@nationwidechildrens.org'

send_email(subj, text, send_to)
