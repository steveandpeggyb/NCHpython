import pyad.adquery, pyad.aduser

def QryUser(username='csb003'):
    q = pyad.adquery.ADQuery()
    q.execute_query(
                    # attributes = ["givenName", "sn", "mail", "title", "sAMAccountType", "memberOf"][::-1],
                    attributes = ["cn", "sAMAccountType", "member"][::-1],
                    where_clause = "SamAccountName = '{}'".format(username),
                    base_dn = "CN=users, DC=crii, DC=org"
                    )

    userObject = {} #   Create Dictionary of information

    allResults=q.get_results()

    # print(allResults)

    for row in q.get_results():
        userObject[key] = row[key]
        print(key, '\t', userObject[key])
    
    return userObject

QryUser('csb003')