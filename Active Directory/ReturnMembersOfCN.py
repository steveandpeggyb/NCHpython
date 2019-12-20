from pyad.adquery import ADQuery as ADQuery
from pyad import *

def GetMembersByCNname(CNname):
    pyad.set_defaults(ldap_server = 'RPW-DC03.crii.org')
    # user=pyad.aduser.ADUser.from_cn('Blake, Steve (csb003)')

    # print(user.get_attribute("sAMAccountName"))

    q = ADQuery()

    q.execute_query(
        attributes = ["name", "cn", "member"],
        where_clause = "CN='CNname'",
        base_dn="DC=crii,DC=org"
    )
    results = q.get_results()
    charLength = len(CNname)
    for row in q.get_results():
        if str(row["cn"])[:charLength] == CNname:
            print(row["member"])
            output = row["member"]
            return output

Members = GetMembersByCNname("bcrinformatics")

print()
for member in Members:
    cleanup = member.replace(",CN=Users,DC=CRII,DC=ORG", "")
    cleanup = cleanup.replace("\\","")
    cleanup = cleanup.replace("CN=","")
    print(cleanup)
print()