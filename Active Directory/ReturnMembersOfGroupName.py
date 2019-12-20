from pyad import *
from pyad.adquery import ADQuery as ADQuery


def GetMembersByName(groupName):
    pyad.set_defaults(ldap_server = 'RPW-DC03.crii.org')    #   Research
    # pyad.set_defaults(ldap_server = 'columbuschildrens.net')    #   Hospital
    # user=pyad.aduser.ADUser.from_cn('Blake, Steve (csb003)')

    q = ADQuery()

    q.execute_query(
        attributes = ["name", "cn", "member", "sAMAccountName", "sAMAccountType"],
        where_clause=("name = '" + groupName + "'"),
        # base_dn="OU=Hospital, DC=columbuschildrens,DC=net"
        base_dn="DC=CRII,DC=org"
    )
    results = q.get_results()
    i=1
    charLength = len(groupName)
    for row in results:
        if row["member"] != None:
            if str(row["cn"])[:charLength] == groupName:
                Members = row["member"]
                print('\n' + str(len(row["member"])) + ' member(s) found.\n')
                cleanup = ''
                for member in Members:
                    cleanup = cleanup + member
                    cleanup = cleanup.replace(",CN=Users,DC=CRII,DC=ORG", "")
                    cleanup = cleanup.replace(",OU=Users-Admin Accounts,OU=Users-NCHRI,DC=CRII,DC=ORG","")
                    cleanup = cleanup.replace(",OU=Users,OU=Hospital,DC=columbuschildrens,DC=net","")
                    cleanup = cleanup.replace(",OU=Global,OU=Security,OU=Groups,OU=Hospital,DC=columbuschildrens,DC=net","")
                    cleanup = cleanup.replace("\\","")
                    cleanup = cleanup.replace("CN=","")
                    cleanup = cleanup + '\n'
                    i += 1
                return cleanup
        else:
            return 'This group has no members!'
    

print(GetMembersByName('bcrInformatics'))
