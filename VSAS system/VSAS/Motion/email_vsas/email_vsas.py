"""  
File: email_vsas.py
Author: Levi Bostian (bostianl@uni.edu)
Description: Class for sending emails.
             ***NOTE***
             Can only send with 1 email address. 
             
             Following commands to get to work:
             emailObj = SendEmail()
             emailObj.setRecipient("test@test.com")
             emailObj.setSubject("test subject")
             #set as RED, YELLOW, or ORANGE
             emailObj.setAlertLevel("RED")
             emailObj.setDbPhotoLink("dropbox.com/photo/link/")
             emailObj.setDbVidLink("vsassoftware.com/videoInfoHere")
             emailObj.setDuration("2 min 34 sec")
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
        self.alertLevel = ""
        self.dbPhotoLink = ""
        self.duration = ""
        self.dbVidLink = ""
        self.emailBody = ""
        self.date = ""
        self.setUp()
        
    def setRecipient(self, emailAddress):
        self.recipient = emailAddress
    def setAlertLevel(self, level):
            self.alertLevel = level
    def setDbPhotoLink(self, link):
            self.dbPhotoLink = link
    def setDbVidLink(self, link):
            self.dbVidLink = link
    def setDuration(self, length):
            self.duration = length
    def setDate(self, date):
            self.date = date
    
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
        except:
            print "Error: unable to send email"
                  
    def openEmailBody(self):
        self.body = MIMEMultipart('alternative')
        self.body['Subject'] = self.subject
        self.body['From'] = self.SENDER
        self.body['To'] = self.recipient
        self.setUpEmail()
        self.body.attach(MIMEText(self.emailBody, 'html'))
       
    def getPassword(self):
        # receive encrypted email password from password file
        # passwordFile = open("email_p.txt", "r")
        self.password = "teamPassword1"
        #passwordFile.close()
        
    def setConnection(self):
        self.emailConnection = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
        self.emailConnection.ehlo()
        self.emailConnection.starttls()
        self.emailConnection.ehlo()
        self.emailConnection.login(self.SENDER, self.password)

    def setUpEmail(self):
        self.emailBody = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <style type="text/css">
                body {
                    margin: 0 auto;
                    padding: 0;
                    width: 600px;
                    height: 100%;
                    background-color: #FFFFFF;
                    text-align: center;
                }
                #container {
                                    height: 100%;
                                    width: 600px;
                            }
                    </style>
        </head>
        <body>
        <h1 style="color:"""+self.alertLevel.lower()+"""; font-size: 50px;">"""+self.alertLevel+""" ALERT</h1>
            <h3>VSAS Motion Detected</h3>
            <img src="""+self.dbPhotoLink+" width=\"500px;\" height=\"400px;\" />"+"""
            <table border=0 style="margin: 0 auto;">
                        <tr>
                                <th colspan=3>-Motion Details-</th>
                        </tr>
                        <tr>
                            <th>Date:</th>
                                <td colspan=2>"""+self.date+"</td>"+"""
                                </tr>
                        <tr><td colspan=3></td></tr>
                        <tr>
                                <th colspan=3>Video Footage Link</th>
                        </tr>
                        <tr>
                            <td colspan=3><a href="""+self.dbVidLink+">"+self.dbVidLink+"</a></td>"+"""
                            </tr>
                    </table>
                    <h1> </h1>
        </body>
        </html>"""
