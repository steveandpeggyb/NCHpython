from pyad.adquery import ADQuery as ADQuery
from pyad import *

def GetMembersByEmail(groupEmail):      # Input the group email to get the members
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

def GetMembersByName(groupName):      # Input the group name to get the members
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

