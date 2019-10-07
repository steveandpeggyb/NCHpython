from pyad.adquery import ADQuery as ADQuery
from pyad import *

pyad.set_defaults(ldap_server = 'RPW-DC03.crii.org')
# user=pyad.aduser.ADUser.from_cn('Blake, Steve (csb003)')

# print(user.get_attribute("sAMAccountName"))

q = ADQuery()

q.execute_query(
    attributes = ["distinguishedName", "description"],
    where_clause = "objectClass = '*'"
)
results = q.get_results()
# print(results)

for row in q.get_results():
    print(row["distinguishedName"])