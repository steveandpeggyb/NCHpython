import pyad.adquery, pyad.aduser

username = "BCRInformatics"
username = "csb003"

q = pyad.adquery.ADQuery()
q.execute_query(
                # attributes = ["givenName", "sn", "mail", "title", "sAMAccountType", "memberOf"][::-1],
                attributes = ["cn", "sAMAccountType", "member"][::-1],
                where_clause = "SamAccountName = '{}'".format(username),
                base_dn = "CN=users, DC=crii, DC=org"
                )

userObject = {} #   Create Dictionary of information

allResults=q.get_results()
if allResults.gi_yieldfrom == None:
    print(allResults)

# print(allResults)

for row in q.get_results():
    if row == None:
        print('No Results returned!')
    for key in row:
        userObject[key] = row[key]
        print("Key: ", key, '\t', userObject[key])