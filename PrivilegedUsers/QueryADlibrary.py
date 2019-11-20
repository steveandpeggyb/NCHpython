import pyad.adquery as adquery
import pprint

def SearchAD(username='csb003'):
    # print('Running SearchAD("'+username+'")')
    r = adquery.ADQuery()

    r.execute_query(
        attributes = ["cn", "member", "sAMAccountType", "sAMAccountName"],
        where_clause=("sAMAccountName = '" + username + "'"),
    )

    return list(r.get_results())