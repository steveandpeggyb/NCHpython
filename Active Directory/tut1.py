from ldap3 import Server, Connection, MODIFY_ADD, MODIFY_REPLACE, ALL_ATTRIBUTES
from ldap3.utils.dn import safe_rdn

server = Server('ipa.demo1.freeipa.org')
conn = Connection(server, 'uid=admin, cn=users, cn=accounts, dc=demo1, dc=freeipa, dc=org', 'Secret123', auto_bind=True)
# print(0, conn.extend.standard.who_am_i())

# print(server.schema)
# print(server.info)
# print(server.schema.object_classes['inetorgperson'])
# print(server.schema.object_classes['organizationalperson'])
# print(server.schema.object_classes['person'])
# print(server.schema.object_classes['top'])

# conn.search('dc=demo1, dc=freeipa, dc=org', '(&(objectclass=person)(uid=admin))', attributes=['sn', 'krbLastPwdChange', 'objectclass'])
# entry = conn.entries[0]

# print(entry)

conn.add('ou=ldap3-tutorial, dc=demo1, dc=freeipa, dc=org', 'organizationalUnit')

# conn.delete('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
# from ldap3.protocol.rfc4527 import pre_read_control, post_read_control
# print(1, conn.last_error)
# conn.add('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Beatrix', 'sn': 'Young', 'departmentNumber': 'DEV', 'telephoneNumber': 1111})
# print(2, conn.modify('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_ADD, ['Smyth'])]}, controls=[pre_read_control('sn'), post_read_control('sn')]))
# print(3, conn.result['controls'])
# print(4, conn.modify('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_REPLACE, ['Smith'])]}))
# print(5, conn.result)

# conn.add('cn=j.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'John', 'sn': 'Smith', 'departmentNumber': 'DEV', 'telephoneNumber': 2222})
# conn.add('cn=m.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Marianne', 'sn': 'Smith', 'departmentNumber': 'QA',  'telephoneNumber': 3333})
# conn.add('cn=quentin.cat,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Quentin', 'sn': 'Cat', 'departmentNumber': 'CC', 'telephoneNumber': 4444})
# conn.modify_dn('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.smith')
# conn.add('ou=moved, ou=ldap3-tutorial, dc=demo1, dc=freeipa, dc=org', 'organizationalUnit')
# conn.modify_dn('cn=b.smith,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.smith', new_superior='ou=moved, ou=ldap3-tutorial, dc=demo1, dc=freeipa, dc=org')
# print(safe_rdn('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org'))
# conn.search('ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=b.smith)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
# print(0)
# print(conn.entries)
# from ldap3 import MODIFY_ADD, MODIFY_DELETE, MODIFY_REPLACE
# print(conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_ADD, ['Smyth'])]}))
# #print(conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_REPLACE, ['Smith'])]}))
# print(conn.last_error)
# conn.search('ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=b.smith)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
# print(1)
# print(conn.entries)
#
# print(conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_DELETE, ['Young'])]}))
# print(conn.last_error)
# conn.search('ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=b.smith)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
# print(2)
# print(conn.entries)
#
# print(conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_REPLACE, ['Smith'])]}))
# print(conn.last_error)
# conn.search('ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=b.smith)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
# print(3)
# print(conn.entries)
#
# print(conn.modify('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', {'sn': [(MODIFY_ADD, ['Young', 'Johnson']), (MODIFY_DELETE, ['Smith'])], 'givenname': [(MODIFY_REPLACE, ['Mary', 'Jane'])]}))
# print(conn.last_error)
# print(4)
# conn.search('ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=b.smith)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
# print(conn.entries)
#
# print(conn.compare('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'departmentNumber', 'DEV'))
# print(conn.compare('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'departmentNumber', 'QA'))
#
# entries = conn.extend.standard.paged_search('dc=demo1, dc=freeipa, dc=org', '(objectClass=person)', attributes=['cn', 'givenName'], paged_size=5)
#
# for entry in entries:
#     print(entry)
#
#
# total_entries = 0
# cookie = "new_cookie"
# while cookie:
#    conn.search('dc=demo1, dc=freeipa, dc=org', '(objectClass=Person)', attributes=['cn', 'givenName'], paged_size=5, paged_cookie=cookie)
#    total_entries += len(conn.response)
#    cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
#    print (cookie)
#    for entry in conn.response:
#        print(entry['dn'], entry['attributes'])
# print('Total entries retrieved:', total_entries)
