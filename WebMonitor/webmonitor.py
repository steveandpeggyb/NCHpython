import os
import smtplib
import requests

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def notify_user(SendTo):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)        # put username and password in environment variables so it is not in the source code.
        subject = 'YOUR WEBSITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up.'
        msg= f'Subject: [subject]\r\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, SendTo, msg)

def reboot_server():
    print('Rebooting server')

try:
    r=requests.get('https://google.com', timeout=5)
    if r.status_code != 200:
        notify_user('steve.blake@nationwidechildrens.org')
        reboot_server()
        # print('Status Code: ' + str(r.status_code))
        # print('\r\nText: ' + r.text)
        # print('\r\njson: ' + r.json)
except Exception as e:
    notify_user('steve.blake@nationwidechildrens.org')
    reboot_server()

# https://myaccount.google.com/lesssecureapps
# https://myaccount.google.com/apppasswords


    