from win32com.client import Dispatch
outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
root_folder = outlook.Folders.Item(1)

print (root_folder.Name)

for folder in root_folder.Folders:
    print (folder.Name + ' has ' + str(folder.Items.count) + ' emails.')

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
