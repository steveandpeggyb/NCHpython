from GroupMembers import GetMembersByName
# from GroupMembers import GetMembersByEmail

target = ( "GDNCHDataBaseAdmins",
            "GDSQLDatabaseAdmins",
            "GGSQLDatabaseAdmins",
            "BCR Informatics Database Admins",
            "GDDBAdmins",
            "GGDBAdmins",
            "RISDBA",
            "RISDBAAdmins")

for grp in target:
    Members = GetMembersByName(grp)

    print(grp + ':\n\t------------------------------------------------------------')

    if Members == None:
        print('\tNothing returned!')
        print('\t------------------------------------------------------------\n')
        continue

    individuals = []
    groups = []

    for member in Members:
        cleanup = member
        if cleanup.find('Users') > 0:
            cleanup = member.replace(",OU=Users-Admin Accounts", "")
            cleanup = cleanup.replace(",OU=Users-NCHRI", "")
            cleanup = cleanup.replace(",OU=Users-ServiceAccounts", "")
            cleanup = cleanup.replace(",DC=CRII","")
            cleanup = cleanup.replace(",DC=ORG","")
            cleanup = cleanup.replace(",CN=Users", "")
            cleanup = cleanup.replace("\\","")
            cleanup = cleanup.replace("CN=","")
            individuals.append(cleanup)
            # print('User: ',cleanup)
            continue
        elif cleanup.find('Users,') < 0:
            cleanup = member.replace("CN=","")
            cleanup = cleanup[:cleanup.find(',')]
            groups.append(cleanup)
            # print('Group:', cleanup)
            continue

    index = 1
    if len(individuals) > 0:
        print('Users:')
        for line in individuals:
            print('\t', index, line)
            index += 1

    index = 1
    if len(groups) > 0:
        print('\n' + 'Groups:')
        for line in groups:
            print('\t', index, line)
            index += 1
    print('\t------------------------------------------------------------\n')


