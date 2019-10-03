from ldap3 import Server, Connection, MODIFY_ADD, MODIFY_REPLACE, ALL_ATTRIBUTES
from ldap3.utils.dn import safe_rdn

def test_init(self):
        """Tests init logic."""
        admin_obj = admin.Admin(None, 'dc=test,dc=com')
        admin_obj.ldap = ldap3.Connection(ldap3.Server('fake'), client_strategy=ldap3.MOCK_SYNC)
        admin_obj.init()

        dn_list = [arg[0][0] for arg in admin_obj.ldap.add.call_args_list]

        self.assertTrue('dc=test,dc=com' in dn_list)
        self.assertTrue('ou=treadmill,dc=test,dc=com' in dn_list)
        self.assertTrue('ou=apps,ou=treadmill,dc=test,dc=com' in dn_list) 

print(test_init())