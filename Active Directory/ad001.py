from ldap3 import *
# from ldap3.utils.dn import safe_rdn

def main(snName):
    # Create the Server object with the given address.
    server = Server('RPW-DC03.crii.org')
    
    #Create a connection object, and bind with the given DN and password.
    try: 
        conn = Connection(server, auto_bind=True)
        print('\n<<<<<<<<<<<<<<<<<<<<<<<<<< LDAP Bind Successful. >>>>>>>>>>>>>>>>>>>>>>>>>>')
        
        # Perform a search for a pre-defined criteria.
        # Mention the search filter / filter type and attributes.
        conn.search('CN=Users,DC=CRII,DC=ORG', '(sn=Blake)')
        
        # Print the resulting entries.
        print(conn.entries) # print(conn.entries[0])
    
    except core.exceptions.LDAPBindError as e:
        
        # If the LDAP bind failed for reasons such as authentication failure.
        print('######################################################    LDAP Bind Failed: ', e) 


print(main('blake'))