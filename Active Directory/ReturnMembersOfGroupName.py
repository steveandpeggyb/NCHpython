from pyad.adquery import ADQuery as ADQuery
from pyad import *
# import numpy

def GetMembersByName(groupName):
    pyad.set_defaults(ldap_server = 'RPW-DC03.crii.org')
    # user=pyad.aduser.ADUser.from_cn('Blake, Steve (csb003)')

    # print(user.get_attribute("sAMAccountName"))

    q = ADQuery()

    q.execute_query(
        attributes = ["mail", "givenName", "cn", "member"],
        where_clause = "objectClass = '*'"
    )
    results = q.get_results()
    charLength = len(groupName)
    for row in q.get_results():
        if str(row["cn"])[:charLength] == groupName:
            print(row["member"])
            return row["member"]

Members = GetMembersByName("BCR Informatics Database Team")

print()
for member in Members:
    cleanup = member.replace(",CN=Users,DC=CRII,DC=ORG", "")
    cleanup = cleanup.replace("\\","")
    cleanup = cleanup.replace("CN=","")
    print(cleanup)
print()