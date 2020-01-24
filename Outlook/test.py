from tkinter import *
import win32com.client
import sys
import os.path
save_path = 'C:/temp/'
nGui=Tk() 
title=nGui.title('Production Accolation')
geo=nGui.geometry
def homepage():
    geo('250x150')
    title
    BtnSta=Button(text="Start", command=start,height=2,width=100,font = "Calibri 12 bold").pack()
    BtnRep=Button(text="Report",command=report,height=2, width=100,font = "Calibri 12 bold").pack()
    BtnExi=Button(text="Exit",fg="red",command=end, height=2,width=100,font = "Calibri 12 bold").pack()
    nGui.mainloop()
def start():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    # inbox = outlook.GetDefaultFolder(6)
    inbox = inbox.Folders.Item("Inbox")
    messages = inbox.Items
    message = messages.GetLast()
    subject=message.Subject
    emailcount=0
    corrcount=0
    misccount=0
    for m in messages:
        emailcount=emailcount+1
        if m.Subject=="production":
            corrcount=corrcount+1
            email="outlookparse"
            compemail=os.path.join(save_path, email+".txt")
            file1=open(compemail,"w")
            file1.write(message.body)
            file1.close()
        else:
            misccount=misccount+1
    print("Total Emails ",emailcount)
    print("Production Emails ",corrcount)
    print("Miscellaneous Emails ",misccount)
def report():
    print("ok")
def end():
    exit()
    
homepage()