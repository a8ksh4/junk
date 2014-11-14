#!/usr/bin/env python

import smtplib

DEBUG = True # set to false for production

smtp_user = 'jstrickpython'
smtp_pwd = 'python(monty)'

sender = 'bozo@circus.com'
recipients = ['jstrickler@gmail.com']
msg = '''Subject: Simple EMail example
Testing smtplib.
This is a test.
'''

smtpserver = smtplib.SMTP("smtpcorp.com", 2525)
smtpserver.login(smtp_user, smtp_pwd)
smtpserver.set_debuglevel(DEBUG) # show communication with the server

try:
    smtpserver.sendmail(
        sender,
        recipients,
        msg
    )
except Exception as e:
    print "Unable to send mail:", e
finally:
    smtpserver.quit()
