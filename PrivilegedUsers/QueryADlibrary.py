import pyad.adquery as adquery
import pprint

def SearchAD(username='csb003'):
    r = adquery.ADQuery()

    r.execute_query(
        attributes = ["member", "sAMAccountType", "sAMAccountName"],
        where_clause=("sAMAccountName = 'csb003'"),
    )

    results = r.get_results()
    for row in results:
        pprint.pprint( row )

    return results