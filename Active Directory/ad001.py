from ldap3 import Server, Connection, Tls, SASL, GSSAPI, core
import ssl

# from ldap3.utils.dn import safe_rdn

def main(snName):
    tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1)
    # Create the Server object with the given address.
    server = Server('RPW-DC03.crii.org', use_ssl=True, tls=tls)

    #Create a connection object, and bind with the given DN and password.
    try:
        conn = Connection(server, auto_bind=True)
        print('\n<<<<<<<<<<<<<<<<<<<<<<<<<< LDAP Bind Successful. >>>>>>>>>>>>>>>>>>>>>>>>>>')
        
        # Perform a search for a pre-defined criteria.
        # Mention the search filter / filter type and attributes.
        # https://ldap3.readthedocs.io/tutorial_searches.html
        # https://github.com/cannatag/ldap3
        print('Connection Response:', conn.response)
        # r = conn.response[0]['raw_attributes']
        # r['search_base'] = 'DC='+r['dnsHostName'].split('.', maxsplit=1)[0]+','+r['rootDomainNamingContext']
        conn.search('', '(objectClass=*)')
        
        # Print the resulting entries.
        print('Search Results:', conn.entries) # print(conn.entries[0])

    except core.exceptions.LDAPBindError as e:
        
        # If the LDAP bind failed for reasons such as authentication failure.
        print('######################################################    LDAP Bind Failed: ', e) 
print('Returned information: ', main('Blake'), '\n')