#!/usr/bin/python
#import os, sys, string
import smtplib
import string

HOST = "smtp.exmail.qq.com"
SUBJECT = "Test email from Python"
TO = "itmanager@dglpay.com"
FROM = "idler@imobpay.com"
text = "Python rules them all!"
BODY = string.join((
         "From: %s" % FROM,
         "To: %s" % TO,
         "Subject: %s" % SUBJECT,
         "",
         text
         ), "\r\n")
print BODY
server = smtplib.SMTP()
server.connect(HOST, "25")
#server.starttls()
server.login("idler@imobpay.com", "fei123")
server.sendmail(FROM, [TO], BODY)
server.quit()
