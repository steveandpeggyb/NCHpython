from pyad.adquery import ADQuery as ADQuery
from pyad import *

def GetMembersByEmail(groupEmail):
    pyad.set_defaults(ldap_server = 'RPW-DC03.crii.org')
    # user=pyad.aduser.ADUser.from_cn('Blake, Steve (csb003)')

    # print(user.get_attribute("sAMAccountName"))

    q = ADQuery()

    q.execute_query(
        attributes = ["name", "cn", "member"],
        where_clause = "CN='groupEmail'"
    )
    results = q.get_results()
    charLength = len(groupEmail)
    for row in q.get_results():
        if str(row["cn"])[:charLength] == groupEmail:
            print(row["member"])
            output = row["member"]
            return output

Members = GetMembersByEmail("bcrinformatics")

print()
for member in Members:
    cleanup = member.replace(",CN=Users,DC=CRII,DC=ORG", "")
    cleanup = cleanup.replace("\\","")
    cleanup = cleanup.replace("CN=","")
    print(cleanup)
print()