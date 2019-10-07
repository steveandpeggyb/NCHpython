from pyad.adquery import ADQuery as ADQuery
from pyad import *
# import numpy

def GetMembers(group):
    pyad.set_defaults(ldap_server = 'RPW-DC03.crii.org')
    # user=pyad.aduser.ADUser.from_cn('Blake, Steve (csb003)')

    # print(user.get_attribute("sAMAccountName"))

    q = ADQuery()

    q.execute_query(
        attributes = ["mail", "givenName", "cn", "member"],
        where_clause = "objectClass = '*'"
    )
    results = q.get_results()
    charLength = len(group)
    for row in q.get_results():
        if str(row["mail"])[:charLength] == group:
            print(row["member"])
            output = row["member"]
            return output

Members = GetMembers("BCRInformaticsDatabaseTeam@nationwidechildrens.org")

print()
for member in Members:
    print(member)
print()