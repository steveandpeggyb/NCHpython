from ldap3 import Server, Connection, Tls, core, ALL
import ssl

def main(snName):
    print('\n<<<<<<<<<<<<<<<<<<<<<<<<<< LDAP Setup >>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1)
    print('tls:',tls)

    # Create the Server object with the given address.
    server = Server('RPW-DC03.crii.org', use_ssl=True, tls=tls)
    print('Server:', server)
    
    #Create a connection object, and bind with the given DN and password.
    try:
        conn = Connection(server, auto_bind=True)
        print('\n<<<<<<<<<<<<<<<<<<<<<<<<<< LDAP Bind Successful. >>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        
        # Perform a search for a pre-defined criteria.
        # Mention the search filter / filter type and attributes.
        # https://ldap3.readthedocs.io/tutorial_searches.html
        # https://github.com/cannatag/ldap3
        print('Connection Response:', conn.response)

        # Enter the search criteria
        # conn.search('dc=Users,dc=CRII,dc=ORG', '(&(mail=*@nationwidechildrens.org)(CN=Blake*))')
        conn.search('', '(&(mail=*@nationwidechildrens.org)(CN=Blake*))')
        
        # Print the resulting entries.
        print('Search Results:', conn.entries) # print(conn.entries[0])

    except core.exceptions.LDAPBindError as e:
        
        # If the LDAP bind failed for reasons such as authentication failure.
        print('######################################################    LDAP Bind Failed: ', e)

print('Returned information: ', main('Blake'))
print('\n<<<<<<<<<<<<<<<<<<<<<<<<<< LDAP Bind Successful. >>>>>>>>>>>>>>>>>>>>>>>>>>\n')