import pyad.adquery as adquery
import pprint

def SearchAD(username='BCRinformatic'):

    q = adquery.ADQuery()
    q.execute_query(
        attributes = ["cn", "member", "sAMAccountType", "sAMAccountName"],
        where_clause=("sAMAccountName = '" + username + "'"),
    )

    # for r in q.get_results():
    #         print("CN:             ",r['cn'])
    #         print("MEMBER:         ",r['member'])
    #         print("SAMAccountType: ",r['sAMAccountType'])
    #         print("sAMAccountName: ",r['sAMAccountName'])
    
    return q.get_results()

