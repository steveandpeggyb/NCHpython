#! /usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

SendHTMLemail(  toEmail=    'steve.blake@nationwidechildrens.org', 
                fromEmail=  'steve.blake@nationwidechildrens.org', 
                subject=    'Test email', 
                body=       
                        """
                            <!doctype html>
                                <html>
                                    <style>
                                        span {background-color: #fdff00;}
                                    </style>                                    
                                    <body>
                                        <center><H1>This is a test HTML email</H1></center>
                                        <p>This <strong><font color=blue>email</font></strong> show examples of what can be utilized as an <strong><i><font color=red>HTML</font></i></strong> email.
                                        Here are some options for formatting text:
                                            <ul>
                                            <li>[b]&#8195;-&#8195;Bold <b>text</b></li>
                                            <li>[strong]&#8195;-&#8195;Important <strong>text</strong></li>
                                            <li>[i]&#8195;-&#8195;Italic <i>text</i></li>
                                            <li>[em]&#8195;-&#8195;Emphasized <em>text</em></li>
                                            <li>[small]&#8195;-&#8195;Small <small>text</small></li>
                                            <li>[del]&#8195;-&#8195;Deleted text</li>
                                            <li>[ins]&#8195;-&#8195;Inserted text</li>
                                            <li>[sub]&#8195;-&#8195;Subscript <sub>text</sub></li>
                                            <li>[sup]&#8195;-&#8195;Superscript <sup>text</sup></li>
                                            <li>[mark]&#8195;-&#8195;<mark>Marked</mark> Formatting</li>
                                            <li>[span]&#8195;-&#8195;format <span>text</span> as highlighted</li>
                                            <li>&#8195;&#8195;&#8195;&#8195;&#8195;[style]span {background-color: #fdff00;}[/style]</li>
                                            </ul>
                                        </p>
                                    </body>
                                </html>"""
                )
