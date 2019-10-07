from ldap3 import Server, Connection, SUBTREE, ALL, Tls
import ssl

total_entries = 0
tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1)
server = Server('RPW-DC03.crii.org', get_info=ALL, use_ssl=True, tls=tls)  # define an unsecure LDAP server, requesting info on DSE and schema
c = Connection(server)
c.search(search_base = 'CN=Users',
         search_filter = '(objectClass=inetOrgPerson)',
         search_scope = SUBTREE,
         attributes = ['cn', 'givenName'],
         paged_size = 5)
# total_entries += len(c.response)
# for entry in c.response:
#     print(entry['dn'], entry['attributes'])
# cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
# while cookie:
#     c.search(search_base = 'o=test',
#              search_filter = '(objectClass=inetOrgPerson)',
#              search_scope = SUBTREE,
#              attributes = ['cn', 'givenName'],
#              paged_size = 5,
#              paged_cookie = cookie)
#     total_entries += len(c.response)
#     cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
#     for entry in c.response:
#         print(entry['dn'], entry['attributes'])
# print('Total entries retrieved:', total_entries)

# # paged search wrapped in a generator
# total_entries = 0
# entry_generator = c.extend.standard.paged_search(search_base = 'o=test',
#                                                  search_filter = '(objectClass=inetOrgPerson)',
#                                                  search_scope = SUBTREE,
#                                                  attributes = ['cn', 'givenName'],
#                                                  paged_size = 5,
#                                                  generator=True)
# for entry in entry_generator:
#     total_entries += 1
#     print(entry['dn'], entry['attributes'])
# print('Total entries retrieved:', total_entries)