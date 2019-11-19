import pyad.adquery as adquery
import pprint

q = adquery.ADQuery()

q.execute_query(
    attributes = ["member", "sAMAccountType", "sAMAccountName"],
    where_clause=("sAMAccountName = 'csb003'"),
)

for row in q.get_results():
    pprint.pprint( row )