from pyad.adquery import ADQuery as ADQuery
from pyad import *

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
    for row in results:
        if str(row["cn"])[:charLength] == groupName:
            Members = row["member"]
            for member in Members:
                cleanup = member.replace(",CN=Users,DC=CRII,DC=ORG", "")
                cleanup = cleanup.replace("\\","")
                cleanup = cleanup.replace("CN=","")
                Return cleanup
