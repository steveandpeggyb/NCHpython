from pyad.adquery import ADQuery as ADQuery
from pyad import *
# import numpy

def GetMembers(groupEmail):
    pyad.set_defaults(ldap_server = 'RPW-DC03.crii.org')
    # user=pyad.aduser.ADUser.from_cn('Blake, Steve (csb003)')

    # print(user.get_attribute("sAMAccountName"))

    q = ADQuery()

    q.execute_query(
        attributes = ["mail", "givenName", "cn", "member"],
        where_clause = "objectClass = '*'"
    )
    results = q.get_results()
    charLength = len(groupEmail)
    for row in q.get_results():
        if str(row["mail"])[:charLength] == groupEmail:
            print(row["member"])
            output = row["member"]
            return output

Members = GetMembers("BCRInformaticsDatabaseTeam@nationwidechildrens.org")

print()
for member in Members:
    cleanup = member.replace(",CN=Users,DC=CRII,DC=ORG", "")
    cleanup = cleanup.replace("\\","")
    cleanup = cleanup.replace("CN=","")
    print(cleanup)
print()