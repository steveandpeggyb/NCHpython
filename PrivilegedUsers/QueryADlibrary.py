import pyad.adquery as adquery
import pprint

def SearchAD(username='csb003'):

    q = adquery.ADQuery()
    q.execute_query(
        attributes = ["cn", "member", "sAMAccountType", "sAMAccountName"],
        where_clause=("sAMAccountName = '" + username + "'"),
    )

    return q.get_results()