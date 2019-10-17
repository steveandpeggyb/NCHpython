from pyad.adquery import ADQuery as ADQuery
from pyad import *
import time

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
            if Members == None:
                print("None!")
            else:
                for member in Members:
                    cleanup = member.replace(",CN=Users,DC=CRII,DC=ORG", "")
                    cleanup = cleanup.replace("\\","")
                    cleanup = cleanup.replace("CN=","")
                    return cleanup

def FixTime(finish, start):
    if finish-start < 60:
        t=str(round(finish-start, 3)) + ' seconds.'
    else:
        t=str(round((finish-start)/60, 3)) + ' minutes.'
    return t

Start = time.perf_counter()

Groups = ("GDNCHDataBaseAdmins", 
          "GDSQLDatabaseAdmins", 
          "GGSQLDatabaseAdmins", 
          "BCR Informatics Database Admins", 
          "GDDBAdmins", 
          "GGDBAdmins", 
          "RISDBA", 
          "RISDBAAdmins", 
          "MSSQLSERVER", 
          "SQLSERVERAGENT", 
          "SQLWriter", 
          "Winmgmt", 
          "SAP-BCRDB-SQL", 
          "SAP-BCRDB-SQLAGENT", 
          "sqlbutler")

for G in Groups:
    step = time.perf_counter()
    members = GetMembersByName(G)
    print(G, end='')
    print('\t', FixTime(time.perf_counter(), step))
    if members == None:
        print("\tNone")
        # continue()
    else:
        print('\t', members)
print("Completed")



