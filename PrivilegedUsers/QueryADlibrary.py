import pyad.adquery as adquery
import pprint

def SearchAD(username='csb003'):
    print('Running SearchAD("'+username+'")')
    r = adquery.ADQuery()

    r.execute_query(
        attributes = ["member", "sAMAccountType", "sAMAccountName"],
        where_clause=("sAMAccountName = '" + username + "'"),
    )

    results = r.get_results()
    print(results)

    for row in results:
        pprint.pprint( row )

    return results