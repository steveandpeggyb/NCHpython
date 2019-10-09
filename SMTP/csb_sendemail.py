#!/usr/bin/python3

import smtplib
import base64

def SendEmailMsg(sender, receivers, subject, body, filename):
#    sender = 'steve.blake@nationwidechildrens.org'
#    receivers = 'steve.blake@nationwidechildrens.org'   # multiple emails are seperated by comma (',')
   smtpServer = 'xmail.nationwidechildrens.org'
   # filename = "C:\\DBfiles\\60million-PiDigits.txt" # 58.6 Mb is to large.  Maximum size is: 
#    filename = "C:\\DBfiles\\OutputCSVfile.csv"
   marker = "AUNIQUEMARKER"

   # Read a file and encode it into base64 format
   fo = open(filename, "rb")
   filecontent = fo.read()
   encodedcontent = base64.b64encode(filecontent)  # base64

#    body ="""
#    This is a test email to send an attachement.
#    """
   # Define the main headers.
   part1 = """From: Steve Blake <steve.blake@nationwidechildrens.org>
   To: Charles Blake <steve.blake@nationwidechildrens.org>
   Subject: Sending Attachement
   MIME-Version: 1.0
   Content-Type: multipart/mixed; boundary=%s
   --%s
   """ % (marker, marker)

   # Define the message action
   part2 = """Content-Type: text/plain
   Content-Transfer-Encoding:8bit

   %s
   --%s
   """ % (body,marker)

   # Define the attachment section
   part3 = """Content-Type: multipart/mixed; name=\"%s\"
   Content-Transfer-Encoding:base64
   Content-Disposition: attachment; filename=%s

   %s
   --%s--
   """ %(filename, filename, encodedcontent, marker)
   message = part1 + part2 + part3

   try:
      smtpObj = smtplib.SMTP(smtpServer, 25)
      smtpObj.sendmail(sender, receivers, message)
      return "Successfully sent email"
   except Exception:
      return "Error: unable to send email"