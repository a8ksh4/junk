#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DEBUG = True # set to false for production

smtp_user = 'jstrickpython'
smtp_pwd = 'python(monty)'

sender = 'jstrick@mindspring.com'
recipient = 'jstrickler@gmail.com'

msg = MIMEMultipart('Here is your attachment')
msg['Subject'] = 'Testing email attachments from python class.'

with open('../DATA/parrot.txt') as PARROT:
    attachment_data = PARROT.read()

attachment = MIMEText(attachment_data)
attachment.add_header(
    'Content-Disposition', 'attachment', filename='parrot.txt'
)

msg.attach(attachment)

smtpserver = smtplib.SMTP("smtpcorp.com", 2525)
smtpserver.login(smtp_user, smtp_pwd)
smtpserver.set_debuglevel(DEBUG) # show communication with the server

try:
    smtpserver.sendmail(
        sender,
        recipient,
        msg.as_string()
    )
finally:
    smtpserver.quit()