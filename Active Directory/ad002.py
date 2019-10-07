# import class and constants
from ldap3 import Server, Connection, ALL

# define the server
s = Server('RPW-DC03.crii.org', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema
print('\n<<<<<<<   Server:   >>>>>>>\n',s)
# define the connection
c = Connection(s)  # define an ANONYMOUS connection
print('\n<<<<<<<   Connections:   >>>>>>>\n',c)
print('\n<<<<<<<   c.bind   >>>>>>>\n',c.bind)
print('\n<<<<<<<<<<<<<>>>>>>>>>>>>>\n')
# perform the Bind operation
if not c.bind():
    print('error in bind', c.result)
    exit()

