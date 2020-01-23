# when you start e-mail marketing , You need opt-in email address list. You have opt-in list. You are using email client software and If you can export your list from your email client, You will have good list.

# Now I am trying to explain my codes to write all emails into test file from your outlook profile.

# First you should import win32com.client, You need to install pywin32

# pip install pywin32
# We should connect to Outlook by MAPI

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
# Then we should get all accounts in your outlook profile.

accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts;
# Then You need to get emails from inbox folder that is named emailleri_al.

def emailleri_al(folder):
    messages = folder.Items
    a=len(messages)
    if a>0:
        for message2 in messages:
             try:
                sender = message2.SenderEmailAddress
                if sender != "":
                    print(sender, file=f)
             except:
                print("Steve Blake")
                print(account.DeliveryStore.DisplayName)
                pass

             try:
                message2.Save
                message2.Close(0)
             except:
                 pass


# You should go to all account and get inbox folder and get emails

for account in accounts:
    global inbox
    inbox = outlook.Folders(account.DeliveryStore.DisplayName)
    print("****Account Name**********************************",file=f)
    print(account.DisplayName,file=f)
    print(account.DisplayName)
    print("***************************************************",file=f)
    folders = inbox.Folders

    for folder in folders:
        print("****Folder Name**********************************", file=f)
        print(folder, file=f)
        print("*************************************************", file=f)
        emailleri_al(folder)
        a = len(folder.folders)

        if a>0 :
            global z
            z = outlook.Folders(account.DeliveryStore.DisplayName).Folders(folder.name)
            x = z.Folders
            for y in x:
                emailleri_al(y)
                print("****Folder Name**********************************", file=f)
                print("..."+y.name,file=f)
                print("*************************************************", file=f)

# All Code is as the following

import win32com.client
import win32com
import os
import sys

f = open("testfile.txt","w+")

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts;

def emailleri_al(folder):
    messages = folder.Items
    a=len(messages)
    if a>0:
        for message2 in messages:
             try:
                sender = message2.SenderEmailAddress
                if sender != "":
                    print(sender, file=f)
             except:
                print("Error")
                print(account.DeliveryStore.DisplayName)
                pass

             try:
                message2.Save
                message2.Close(0)
             except:
                 pass

for account in accounts:
    global inbox
    inbox = outlook.Folders(account.DeliveryStore.DisplayName)
    print("****Account Name**********************************",file=f)
    print(account.DisplayName,file=f)
    print(account.DisplayName)
    print("***************************************************",file=f)
    folders = inbox.Folders

    for folder in folders:
        print("****Folder Name**********************************", file=f)
        print(folder, file=f)
        print("*************************************************", file=f)
        emailleri_al(folder)
        a = len(folder.folders)

        if a>0 :
            global z
            z = outlook.Folders(account.DeliveryStore.DisplayName).Folders(folder.name)
            x = z.Folders
            for y in x:
                emailleri_al(y)
                print("****Folder Name**********************************", file=f)
                print("..."+y.name,file=f)
                print("*************************************************", file=f)

print("Finished Succesfully")