# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# Get your app key and secret from the Dropbox developer website
APP_KEY = 'y7cxubkm19o3f9b'
APP_SECRET = '8rguqnx7oqwjqtm'

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'

#sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

#request_token = sess.obtain_request_token()

#url = sess.build_authorize_url(request_token)

# Make the user sign in and authorize this token
#print "url:", url
#print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
#raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
#access_token = sess.obtain_access_token(request_token)

#you do not need any of the above if you run the request_dropbox_token.py application
token_file = open('dropbox_token.txt', 'r')
token_key,token_secret = token_file.read().split('|')
token_file.close()

sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE)
sess.set_token(token_key,token_secret)
client = client.DropboxClient(sess)
print "linked account:", client.account_info()

print
print "NOW READY TO UPLOAD!!!"
print

f = open('working-draft.txt')
response = client.put_file('/fileUploader_linkCreator/magnum-opus.txt', f)
print "uploaded:", response

print
print "FILE UPLOADED SUCCESSFULLY!!"
print "...NOW ONTO CREATING LINK"
print

link = client.share('/fileUploader_linkCreator/magnum-opus.txt')
print link


