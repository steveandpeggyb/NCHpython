import pyad.adquery
q = pyad.adquery.ADQuery()

q.execute_query(
    attributes = ["sn", "Blake"],
    where_clause = "objectClass = '*'",
    base_dn = "CN=users, DC=crii, DC=org"
)

for row in q.get_results():
    print(row["distinguishedName"])