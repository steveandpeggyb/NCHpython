from pyad import adquery
from pyad import aduser
from email.mime.text import MIMEText
import smtplib
import csv

def send_email(subject, body, to):
    s = smtplib.SMTP('xmail.nationwidechildrens.org')
    mime = MIMEText(body)
    mime['Subject'] = subject
    mime['To'] = to
    s.sendmail('steve.blake@nationwidechildrens.org', to, mime.as_string())
def ShowData():

    print("User List:")
    users.sort()
    for u in users:
        print("\t",u)
def EmailData():
    body_text = 'The following users have privileged user access to the BCR Data warehouse.  These user may have direct access or access through an Active Directory "Group".\r\n\r\n'
    for u in users:
        body_text = body_text + '\t' + u + '\r\n'
    subj = 'Privileged User Audit'
    send_to = 'steve.blake@nationwidechildrens.org'
    send_email(subj, body_text, send_to)
def QryUser(username='csb003'):                 #   Query AD username (sAMAccountName)
    q = adquery.ADQuery()
    q.execute_query(
        attributes = ["cn", "member", "sAMAccountType", "sAMAccountName", "displayName", "name"],
        where_clause=("sAMAccountName = '" + username + "'"),
    )
    allRestuls = ()
    allResults = q.get_results
    return allResults()
def QryName(name='Bateman, Thomas (Admin ID)'): #   Query AD by name (name)
    q = adquery.ADQuery()
    q.execute_query(
        attributes = ["cn", "member", "sAMAccountType", "sAMAccountName", "displayName", "name"],
        where_clause=("name = '" + name + "'"),
    )
    allRestuls = ()
    allResults = q.get_results
    return allResults()
def UserData():                                 #   Load the data within the CSV file.
    with open ("R:/RESBCR/FISMA/PrivilegedUserAudits/PrivilegedUserAudit.csv") as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data = []
        for row in reader:                      #   Read each line of the CSV file.
            if len(row)>0:                      #   Transform loaded CSV information
                # data.append(row)
                sandbox = row[0]
                sandbox = sandbox.lower()
                sandbox = sandbox.replace("research\\","")
                sandbox = sandbox.strip()
                data.append(sandbox)
        return data

#   Process the collect usernames
# body_text = ''
group = []                                      #   Known groups
users = []                                      #   Known Users from a group or singular
members = []
IDgroups = []

list = UserData()
InitialPass = True

while len(list)>0:
    for username in list:                       #   Process CSV rows
        if InitialPass == True:                 #   Initial pass (True) will look at AD attribute "sAMAccountName"
            results = QryUser(username)
        else:                                   #   Initial pass (False) looks at AD attribute "name"
            results = QryName(username)
        for r in results:                                   #   process all CSV items
            if r['displayName'] == None:
                NAME = r['name']
            else:
                NAME = r['displayName']
            MEMBER = r['member']
            sAMAccountType = r['sAMAccountType']
            sAMAccountName = r['sAMAccountName']
            if sAMAccountType == 268435456:                 #   Process group
                if sAMAccountName not in group:             #   Log real groups
                    group.append(r['sAMAccountName'])
                    if MEMBER == None:                      #   This group has no members
                        print('# No member in this group!')
                    else:                                   #   Process group members
                        for index in range(len(MEMBER)):
                            sandbox = MEMBER[index]
                            sandbox = sandbox.replace('CN=','')
                            sandbox = sandbox.split(',OU')[0]
                            sandbox = sandbox.split(',Users')[0]
                            sandbox = sandbox.replace('\\','')
                            if sandbox not in members:
                                members.append(sandbox)
            else:                                           #   Process Users
                if NAME not in users:                       #   Log real users
                    users.append(NAME)
    del list[:]
    for m in members:
        list.append(m)
    del members[:]
    del group[:]
    InitialPass = False

ShowData()
EmailData()

