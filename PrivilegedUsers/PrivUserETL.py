from pyad import adquery
from pyad import aduser
import csv

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
body_text = ''
group = []                                      #   Known groups
users = []                                      #   Known Users from a group or singular
members = []                                    #   Known Members of a group

for username in UserData():                             #   Process CSV rows
    results = QryUser(username)
    i=1
    for r in results:                                   #   process all CSV items
        i += 1
        if r['displayName'] == None:
            NAME = r['name']
        else:
            NAME = r['displayName']
        MEMBER = r['member']
        sAMAccountType = r['sAMAccountType']
        sAMAccountName = r['sAMAccountName']
        if sAMAccountType == 268435456:                 #   Process group
            if sAMAccountName not in group:             #   Log real groups
                group.append(sAMAccountName)
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

groups = []                                             #   Restart the 'Group' list
for m in members:                                       #   process groups in groups
    results = QryName(m)
    for r in results:                                   #   process AD returned information
        if r['sAMAccountType'] == 268435456:            #   Log real groups
            if r['sAMAccountName'] not in group:
                group.append(r['sAMAccountName'])
        else:                                           #   Process Users
            if r['sAMAccountName'] not in users:
                users.append(r['sAMAccountName'])

print("Group List:")
for g in group:
    print("\t",g)
print("User List:")
for u in users:
    print("\t",u)
print("Members List:")
for m in members:
    print("\t",m)

print()
# send_email(subj, body_text, send_to)
# print("\r\n" + body_text.replace('\t\t\t','\t\t') + "\r\n")