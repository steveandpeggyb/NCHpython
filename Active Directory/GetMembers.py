# from GroupMembers import GetMembersByName
from GroupMembers import GetMembersByEmail

Members = GetMembersByEmail("BCRInformaticsDatabaseTeamPagers@nationwidechildrens.org")
print('\n------------------------------------------------------------')
# print(Members)
# print('------------------------------------------------------------')

if Members == None:
    print('Nothing returned!')
    print('------------------------------------------------------------\n')
    exit()
individuals = []
groups = []

for member in Members:
    cleanup = member
    if cleanup.find('Users,') > 0:
        cleanup = member.replace(",CN=Users", "")
        cleanup = cleanup.replace(",DC=CRII","")
        cleanup = cleanup.replace(",DC=ORG","")
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
print('------------------------------------------------------------\n')


