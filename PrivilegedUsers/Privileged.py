from datetime import datetime
from email.mime.text import MIMEText
import smtplib
import pyad.adquery as adquery
import pprint

def SearchAD(username='csb003'):

    q = adquery.ADQuery()
    q.execute_query(
        attributes = ["cn", "member", "sAMAccountType", "sAMAccountName"],
        where_clause=("sAMAccountName = '" + username + "'"),
    )

    return q.get_results()

def send_email(subject, body, to):
    s = smtplib.SMTP('xmail.nationwidechildrens.org')
    mime = MIMEText(body)
    mime['Subject'] = subject
    mime['To'] = to
    s.sendmail('steve.blake@nationwidechildrens.org', to, mime.as_string())

def siphon(usernames):
    print("seperate the users in one list then extract all group member and add to the first list.")
    print("Return a tuple of all users.")
    return usernames

subj = 'Privileged User Access - ' + str(datetime.today())
send_to = 'steve.blake@nationwidechildrens.org'

username = "bpc"
list = ('bcr', 'csb003', 'bpc', 'txb053', 'cra030')
usernames = siphon(list)

body_text = ''
for index in range(len(usernames)):
    username = usernames[index]

    results = SearchAD(username)
    i=1
    for r in results:
        i += 1
        CN = r['cn']
        MEMBER = r['member']
        sAMAccountType = r['sAMAccountType']
        sAMAccountName = r['sAMAccountName']

    body_text = body_text + '\r\nCN:\t\t\t'+ CN + '\r\n'
    body_text = body_text + 'sAMAccountType:\t'+str(sAMAccountType) + '\r\n'
    body_text = body_text + 'sAMAccountName:\t'+sAMAccountName + '\r\n'
    body_text = body_text + 'Member of Group:\r\n'
    if MEMBER == None:
        body_text = body_text + '\tNo group member assigned.\r\n'
    else:
        for index in range(len(MEMBER)):
            body_text = body_text + '\t' + str(index+1) + '\t' + MEMBER[index] + '\r\n'

    body_text = body_text.replace('CN=','')
    body_text = body_text.replace(',DC=CRII,DC=ORG','')
    body_text = body_text.replace(',OU=CRI DLs,OU=ExchangeMigration','')
    body_text = body_text.replace(',OU=BCR','')
    body_text = body_text.replace(',OU=BPC','')
    body_text = body_text.replace(',Users','')
    body_text = body_text.replace('\,',',')

# send_email(subj, body_text, send_to)
print("\r\n" + body_text.replace('\t\t\t','\t\t') + "\r\n")