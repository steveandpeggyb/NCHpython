from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyad import adquery
from pyad import aduser
import smtplib
import csv


def ShowData():                                 #   Show the data on the terminal
    print("User List:")
    users.sort()
    for u in users:
        print("\t",u)
    print("\r\nGroups processed:")
    users.sort()
    for i in IDgroups:
        print("\t",i)
def EmailData():                                #   Construct the email content from provided details.
    body_text = '<strong>The following users have privileged user access to the BCR <span style="background-color: #FFFF00"><font color=#8B0E80>RPW-BCRSQL02</font></span> (Production).<p>'
    body_text = body_text +  "Privileged users are defined as, any individual or group that have 'Update', 'Delete', 'Insert' access to the data warehouse.<p>"
    body_text = body_text + 'These user may have direct access or access through an Active Directory "Group".</strong><p><p>'
    
    body_text = body_text + '<ul style="list-style-type:circle"><font color=#560494>'
    for u in users:
        body_text = body_text + '<li>' + u + '</li><p>'
    body_text = body_text + '</ul></font>'
    
    body_text = body_text + '<p><strong>The above users are potentially included in one or more of the following groups AND/OR have individual accesses:</strong><p><p>'

    body_text = body_text + '<ul style="list-style-type:circle"><font color=#560494>'
    for i in IDgroups:
        body_text = body_text + '<li>' + i + '</li><p>'   
    body_text = body_text + '</ul></font>'
    
    subj = 'Privileged User Audit'
    SendHTMLemail(subj, body_text, send_to)
def SendHTMLemail(subject, body, send_to):      #   Send out the email
    # me == my email address
    # you == recipient's email address
    fromEmail = "steve.blake@nationwidechildrens.org"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = send_to

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
    s.sendmail(fromEmail, send_to, msg.as_string())
    s.quit()
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
def QryGroup(name='BCRinformatics'):            #   Query AD by group (name)
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
group = []                                      #   groups to process
users = []                                      #   Known Users from a group or singular
members = []                                    #   Members of a group being processed
IDgroups = []                                   #   All distinct groups processed
HospitalList = []                               #   Raw Hospital users and groups
list = UserData()                               #   raw list to be processed
InitialPass = True                              #   First time through, processing

send_to = 'steve.blake@nationwidechildrens.org'

while len(list)>0:                              #   Process the users and Groups loaded from the CSV file.
    for username in list:                       #   Process user/groups
        if InitialPass == True:                 #   Initial pass (True) will look at AD attribute "sAMAccountName"
            results = QryUser(username)
        else:                                   #   Initial pass (False) looks at AD attribute "name"
            results = QryName(username)
        for r in results:                       #   process all CSV items
            if r['displayName'] == None:
                NAME = r['name']
            else:
                NAME = r['displayName']
            MEMBER = r['member']
            sAMAccountType = r['sAMAccountType']
            sAMAccountName = r['sAMAccountName']
            if sAMAccountType == 268435456:                 #   Process group
                if sAMAccountName not in IDgroups:          #   Keep track of all groups processed
                    IDgroups.append(r['sAMAccountName'] + '\t(' + str(len(r['member'])) + ') members.')
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
# EmailData()
# GGBCRQPReadOnly
