from QueryADlibrary import SearchAD
from datetime import datetime
# from logging import send_email
import pprint
from email.mime.text import MIMEText
import smtplib

def send_email(subject, body, to):
    s = smtplib.SMTP('xmail.nationwidechildrens.org')
    mime = MIMEText(body)
    mime['Subject'] = subject
    mime['To'] = to
    s.sendmail('steve.blake@nationwidechildrens.org', to, mime.as_string())

subj = 'Privileged User Access - ' + str(datetime.today())
text = 'This is the body of the email and should be written in <HTML> so that <br> should work.'
send_to = 'steve.blake@nationwidechildrens.org'
username = "csb003"

results = SearchAD(username)
i=1
body_text = ''
for r in results:
    i += 1
    CN = r['cn']
    MEMBER = r['member']
    sAMAccountType = r['sAMAccountType']
    sAMAccountName = r['sAMAccountName']

body_text = body_text + '\r\n             CN:\t'+CN
body_text = body_text + ' sAMAccountType:\t'+str(sAMAccountType)
body_text = body_text + ' sAMAccountName:\t'+sAMAccountName
body_text = body_text + 'Member of Group:'
if MEMBER == None:
    body_text = body_text + '\tGroup has no members.'
else:
    for index in range(len(MEMBER)):
        body_text = body_text + '\t'+index+1, '\t'+ MEMBER[index].replace('CN=','').replace(',DC=CRII,DC=ORG','').replace('\,','\t')
print()

send_email(subj, body_text, send_to)