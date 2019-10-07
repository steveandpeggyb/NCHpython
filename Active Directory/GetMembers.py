from GroupMembers import GetMembersByName

Members = GetMembersByName("BCR Informatics Database Team")

print()
for member in Members:
    cleanup = member.replace(",CN=Users,DC=CRII,DC=ORG", "")
    cleanup = cleanup.replace("\\","")
    cleanup = cleanup.replace("CN=","")
    print(cleanup)
print()