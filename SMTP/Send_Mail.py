import smtplib

def xmitEmail(FROM, TO, SUBJECT, MESSAGE):

    HOST = 'xmail.nationwidechildrens.org'
    BODY = "From: %s" % FROM + "\nTo: %s" % TO + "\nSubject: %s" % SUBJECT + "\n" + MESSAGE + "\r\n"
    try:
        server = smtplib.SMTP(HOST)
        server.sendmail(FROM, [TO], BODY)
        return "Email sent successfully."
    except Exception:
        return "Error: unable to send email"

    server.quit()