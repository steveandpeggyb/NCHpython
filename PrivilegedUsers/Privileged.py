from tQueryADlibrary import SearchAD
import pprint

username = "bcr"

results = SearchAD(username)
i=1
for r in results:
    i += 1
    CN = r['cn']
    MEMBER = r['member']
    sAMAccountType = r['sAMAccountType']
    sAMAccountName = r['sAMAccountName']

print('\r\nCN:            \t',CN)
print('sAMAccountType:\t',sAMAccountType)
print('sAMAccountName:\t',sAMAccountName)
print('Member of Group:')
if MEMBER == None:
    print('\tGroup has no members.')
else:
    for index in range(len(MEMBER)):
        print ('\t',index, MEMBER[index].replace('CN=',''))
print()
