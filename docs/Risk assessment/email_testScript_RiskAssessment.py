"""  
File: email.py
Author: Levi Bostian (bostianl@uni.edu)
Description: TESTING ONLY for sending emails via Python

References: http://www.tutorialspoint.com/python/python_sending_email.htm
            http://segfault.in/2010/12/sending-gmail-from-python/  <--- use this one
"""

"""line below is for Linux only. Change for Windows"""
#!/usr/bin/python 

import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 #or 465
SENDER = 'team4.cs2720@gmail.com' #emails will be sent via this email address
PASSWORD = #email password here. Has been deleted for security reasons

recipient = #receiver's email address here.
subject = 'Python Test'

bodyFile = open('email_body.html', 'r') #body of email is able to be read from external dynamically created file
body = bodyFile.read()


headers = ["from: " + SENDER,
           "subject: " + subject,
           "to: " + recipient,
           "mime-version: 1.0",
           "content-type: text/html"]
headers = "\r\n".join(headers)

emailConnection = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
emailConnection.ehlo()
emailConnection.starttls()
emailConnection.ehlo()
emailConnection.login(SENDER, PASSWORD)

print "Sending Mail Now"
try:
   emailConnection.sendmail(SENDER, recipient, headers + "\r\n\r\n" + body)     
   emailConnection.quit()    
   print "Successfully sent email"
except:
#except SMTPException:
   print "Error: unable to send email"
