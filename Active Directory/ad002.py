def has_username(uid:str) -> bool:
    """
    Tells whether or not a uid is already used on the server.

    :param uid the uid being queried about
    :returns True if the uid exists, False otherwise
    """
    if uid in p.BLACKLIST:
        return True
    ldap_server = ldap3.Server(p.LDAP_HOST, get_info=ldap3.ALL)
    with ldap3.Connection(
                    ldap_server,
                    user=p.LDAP_USER,
                    password=p.LDAP_KEY,
                    auto_bind=True) as conn:
    
        return conn.search(
                    search_base="dc=netsoc,dc=co",
                    search_filter="(&(objectClass=account)(uid=%s))"%(
                            ldap3.utils.conv.escape_filter_chars(uid)),
                    attributes=["uid"],)
    return True 

print(has_username('csb003'))