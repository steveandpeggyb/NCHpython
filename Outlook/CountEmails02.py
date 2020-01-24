from win32com.client import Dispatch
outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
root_folder = outlook.Folders.Item(1)

print (root_folder.Name)

count = 0

# folder = outlook(1)
ScopeFolder = root_folder.Folders("Inbox")


# for folder in root_folder.Folders:
print(ScopeFolder.Name)
for email in range(1, ScopeFolder.Items.count):
    print('\t'+ScopeFolder.Items(email).Subject)
    count += 1
    if count > 5: 
        break

# Below is the current functionality I've found based on reading other peoples code.
# The objects used above have the following functionality that I'm aware of:

# inbox -
#    .Folders
#    .Items
#    .Items.count

# messages -
#    .GetFirst()
#    .GetLast()
#    .GetNext()
#    .GetPrevious()
#    .Attachments

# message -
#    .Subject
#    .Body
#    .To
#    .Recipients
#    .Sender
#    .Sender.Address

#attachments -
#    .item()
#    .Count

# attachment -
#    .filename
