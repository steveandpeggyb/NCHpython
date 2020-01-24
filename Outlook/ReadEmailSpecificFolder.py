import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").Folders

folder = outlook(1)
inbox = folder.Folders("Inbox")
message = inbox.Items
messages = message.GetLast()
body_content = messages.body
print (body_content)