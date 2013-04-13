"""  
File: sessionUpload.py
Author: Levi Bostian (bostianl@uni.edu)
Description: Class uploading data to Dropbox
             ***NOTE***
             Linked to 1 Dropbox account. Not universal 
             
             Following commands to get to work:
             dropboxObj = DropboxUploader()
             dropboxObj.authenticate()
             dropboxObj.uploadFile("testFile.txt")
             fileURL = dropboxObj.getLink("testFile.txt")

print test

References: https://www.dropbox.com/developers 
"""
from dropbox import client, rest, session

class DropboxUploader:
    def __init__(self):
        self.APP_KEY = 'y7cxubkm19o3f9b'
        self.APP_SECRET = '8rguqnx7oqwjqtm'
        # ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
        self.ACCESS_TYPE = 'app_folder'

    def authenticate(self):
        token_file = open('dropbox_token.txt', 'r')
        token_key,token_secret = token_file.read().split('|')
        token_file.close()
        self.sess = session.DropboxSession(self.APP_KEY,self.APP_SECRET, self.ACCESS_TYPE)
        self.sess.set_token(token_key,token_secret)
        self.connection = client.DropboxClient(self.sess)
        
    def getAccountInfo(self):
        return self.connection.account_info()

    # uploads file you specify to Dropbox. Method returns response Dropbox returns when uploading
    def uploadFile(self, filePath):
        if filePath[0:1] == '/':
            self.filePath = filePath[1:]
        else:
            self.filePath = filePath
        file = open(self.filePath)
        return self.connection.put_file('/fileUploader_linkCreator/'+self.filePath, file)

    def getLink(self, filePath):
        if filePath[0:1] == '/':
            filePath = filePath[1:]
        try:
            return self.connection.media('/fileUploader_linkCreator/'+filePath)
        except:
            return "filePath argument not found in Dropbox"

    def getAuthenticationURL(self):
        self.request_token = self.sess.obtain_request_token()
        return self.sess.build_authorize_url(request_token)
        # This will fail if the user didn't visit the above URL and hit 'Allow'
        
    def saveToken(self):
        try:  
            access_token = self.sess.obtain_access_token(self.request_token)
        except:
            return "call getAuthencationURL() to get URL"
        #Okay, now we are ready to save the access_token
        tokensFileStr = 'dropbox_token.txt'
        tokenFile = open(tokensFileStr, 'w')
        tokenFile.write("%s|%s" % (access_token.key,access_token.secret))
        tokenFile.close()
