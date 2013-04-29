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
             fileURL = dropboxObj.getVSASLink("testFile.txt") #returns URL to file
             fileURL = dropboxOjb.getDBLink("testFile.txt") #for photo

print test

References: https://www.dropbox.com/developers 
"""
from dropbox import client, rest, session
import json
import pprint

class DropboxUploader:
    def __init__(self):
        self.APP_KEY = 'y7cxubkm19o3f9b'
        self.APP_SECRET = '8rguqnx7oqwjqtm'
        # ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
        self.ACCESS_TYPE = 'app_folder'
        self.url = ""
        self.fileName = ""

    def authenticate(self):
        token_file = "73gle25hzsesgzv|32q2n8eg4pmmd06"
        token_key,token_secret = token_file.split('|')
        # token_file.close()
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
        file = open(self.filePath, 'rb')
        self.getFileName(filePath)
        return self.connection.put_file('/fileUploader_linkCreator/'+self.fileName, file)

    def getFileName(self, filePath):
        split = filePath.split("/")
        self.fileName = split[-1]

    def getVSASLink(self, fileLocation):
        if fileLocation[0:1] == '/':
            fileLocation = fileLocation[1:]
        self.getFileName(fileLocation)
        try:
            jsonData = self.connection.media('/fileUploader_linkCreator/'+self.fileName)
            jsonDataString = json.dumps(jsonData)#encode JSON data
            jsonDataDecoded = json.loads(jsonDataString)#decode JSON data
            dropboxURL = jsonDataDecoded["url"]
            dropboxURLSplit = dropboxURL.split("/")
            self.url = "http://vsassoftware.com/video/index.php?id=" + dropboxURLSplit[5] + "&path=" + self.fileName
            return self.url
        except:
            return "filePath argument not found in Dropbox"

    def getDBLink(self, fileLocation):
        if fileLocation[0:1] == '/':
            fileLocation = fileLocation[1:]
        self.getFileName(fileLocation)
        try:
            jsonData = self.connection.media('/fileUploader_linkCreator/'+self.fileName)
            jsonDataString = json.dumps(jsonData)#encode JSON data
            jsonDataDecoded = json.loads(jsonDataString)#decode JSON data
            return jsonDataDecoded["url"]
        except:
            return "filePath argument not found in Dropbox"    

    def getAuthenticationURL(self):
        self.request_token = self.sess.obtain_request_token()
        return self.sess.build_authorize_url(self.request_token)
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

