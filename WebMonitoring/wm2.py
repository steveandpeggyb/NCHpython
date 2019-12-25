#!/usr/bin/env python

from threading import Thread
import requests ## pip install requests
import time
import smtplib

## email sending function

def SendHTMLemail(toEmail, fromEmail, subject, body):
    # me == my email address
    # you == recipient's email address
    if fromEmail == None:
        fromEmail = "steve.blake@nationwidechildrens.org"
    if toEmail == None:
        toEmail = "steve.blake@nationwidechildrens.org"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = toEmail

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
        <head>
        </head>
    <body>"""
    html = html + body
    html = html + """</body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('xmail.nationwidechildrens.org')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(fromEmail, toEmail, msg.as_string())
    s.quit()

## list of sites to track along with email address to send the alert
fromEmails = {"http://resd9-gzmmmr2/reports/browse/" :"steve.blake@nationwidechildrens.org",
              "https://r1pwbcrssrs01/Reports/browse/":"steve.blake@nationwidechildrens.org"}

## temporary dictionary used to do separate monitoring when a site is down
temp_dic = {}

## site 'up' function
def site_up():
    ''' function to monitor up time '''
    while True:
        for fromEmail, email in fromEmails.items():
            try:
                r = requests.get(fromEmail)
                if r.status_code == 200:
                    print(fromEmail, 'Site ok')
                    time.sleep(60) ## sleep for 1 min
                else:
                    print(fromEmail, 'Site first registered as down - added to the "site down" monitoring')
                    temp_dic[fromEmail]=email
                    del fromEmails[fromEmail]
            except requests.ConnectionError:
                print(fromEmail, 'Site first registered as down - added to the "site down" monitoring')
                temp_dic[fromEmail]=email
                del fromEmails[fromEmail]

## site 'down' function
def site_down():
    ''' function to monitor site down time '''
    while True:
        time.sleep(900) ## sleeps 15 mins
        for fromEmail, email in temp_dic.items():
            try:
                r = requests.get(fromEmail)
                if r.status_code == 200:
                    print(fromEmail, 'Site is back up!!')
                    SendHTMLemail('Site back up!! ', email, fromEmail)
                    fromEmails[fromEmail]=email
                    del temp_dic[fromEmail]
                else:
                    SendHTMLemail('Site down!! ', email, fromEmail)
                    print(fromEmail, 'Site Currently down - email sent')
            except requests.ConnectionError:
                SendHTMLemail('Site down!! ', email, fromEmail)
                print(fromEmail, 'Site Currently down - email sent')
            
t1 = Thread(target = site_up)
t2 = Thread(target = site_down)
t1.start()
t2.start()