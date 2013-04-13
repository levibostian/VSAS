"""  
File: email.py
Author: Levi Bostian (bostianl@uni.edu)
Description: Class for sending emails.
             ***NOTE***
             Can only send with 1 email address. 
             
             Following commands to get to work:
             emailObj = SendEmail()
             emailObj.setRecipient("test@test.com")
             emailObj.setSubject("test subject");
             emailObj.sendEmail()

References: http://www.tutorialspoint.com/python/python_sending_email.htm
            http://segfault.in/2010/12/sending-gmail-from-python/
            http://docs.python.org/2/library/email-examples.html#email-examples  <--- use this one
"""
import bz2 # used for really bad password "encyption" (it actually just compresses it). Better then nothing
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:
    
    def __init__(self):
        self.SMTP_SERVER = 'smtp.gmail.com'
        self.SMTP_PORT = 587 # or 465
        self.SENDER = 'team4.cs2720@gmail.com'
        self.subject = ""
        self.recipient = ""
        self.header = []
        self.emailConnection = ""
        self.setUp()
        
    def setRecipient(self, emailAddress):
        self.recipient = emailAddress
    
    def setUp(self):
        self.getPassword()
        self.setConnection()
        
    def setSubject(self, subject = "subject"):
        #expecting String
        self.subject = subject
        
    def sendEmail(self):
        self.openEmailBody()
        try:
            self.emailConnection.sendmail(self.SENDER, self.recipient, self.body.as_string())
            self.emailConnection.quit()
            print "success"
        except:
            print "Error: unable to send email"
                  
    def openEmailBody(self):
        self.body = MIMEMultipart('alternative')
        self.body['Subject'] = self.subject
        self.body['From'] = self.SENDER
        self.body['To'] = self.recipient
        try:
            self.bodyFile = open('email_body.html', 'r')
        except:
            print "Error opening email_body.html"
        self.body.attach(MIMEText(self.bodyFile.read(), 'html'))
        self.bodyFile.close()
       
    def getPassword(self):
        # receive encrypted email password from password file
        passwordFile = open("email_p.txt", "r")
        self.password = bz2.decompress(passwordFile.read())
        passwordFile.close()
        
    def setConnection(self):
        self.emailConnection = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
        self.emailConnection.ehlo()
        self.emailConnection.starttls()
        self.emailConnection.ehlo()
        self.emailConnection.login(self.SENDER, self.password)
