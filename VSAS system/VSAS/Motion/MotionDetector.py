from VideoCapture import Device
import time
from Motion import *
from cv2 import *
import numpy
import threading
import datetime
from dropbox.dropbox_vsas import DropboxUploader
from email_vsas.email_vsas import SendEmail
import subprocess

class MotionDetector(): 
    def __init__(self):
        self._cam              = Device()
        self._detectedImages   = []
        self._currentImage     = ""#Image.open( "VSAS logo.jpg" )
        self._recording        = False
        self._defaultTimeLimit = 5 * 60 #make sure to change back to 5 min
        self._stopRecording    = False
        self._timeStamp        = ""
        self._date             = ""

    def __call__(self):
        self.detect()

    def getCurrentImage(self):
        return self._currentImage

    def isRecording(self):
        return self._recording

    def totalChange( self, greenScaleImage ):
        count = 0
        for pixel in greenScaleImage.getdata():
            if pixel != (0, 255, 0, 0):
                count += 1
        return count

    def adjustCamera( self, cam ):
        for x in xrange(10):
            time.sleep(.75)
            initialImage = cam.getImage()
            time.sleep(.75)
        return initialImage

    def convertImagesToCv( self, images ):
        newImages = []
        for index in xrange(len(images)):
            pilImage = images[index].save( "pilConversion.jpg" )
            openCvImage = cv.LoadImage( "pilConversion.jpg" )
            newImages.append(openCvImage)
        return newImages

    def overThreshold( self, greenImage, thresholdByPx ):
        amtChanged = self.totalChange( greenImage )
        return amtChanged > thresholdByPx

    def getMostCurrentImage( self ):
        return self._cam.getImage()

    def recordOutToVideo(self):
        cvImages = self.convertImagesToCv( self._detectedImages )
        frame = cvImages[0]
        ts = time.time()
        self._timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H:%M:%S')+".avi"
        self._timeStamp = self._timeStamp.replace(":", "-")
        self._timeStamp = "videos/" + self._timeStamp
        video_out = cv.CreateVideoWriter( self._timeStamp, #make it add to subfolder..
                                          cv.CV_FOURCC('I','4','2','0'), 
                                          2.0, 
                                          cv.GetSize(frame), 
                                          1 )
        for item in cvImages:
            frame = item
            cv.WriteFrame( video_out, frame )

    def overTimeLimit(self, initialTime):
        (time.time() - initialTime) > self._defaultTimeLimit

    def end(self):
        self._stopRecording = True

    def aboveTimeLimit(self, startTime):
        if startTime == 0: 
            return False
        # print time.time() - startTime
        return (time.time() - startTime) > self._defaultTimeLimit

    def detect( self ):
        initialImage = self.adjustCamera( self._cam )
        # initialImage.save('initialImage.jpg')
        intialMotion = self.getMostCurrentImage()
        startTime = 0

        while True:
            # print str(time.time() - startTime) + " => " + str(self._defaultTimeLimit)
            self._currentImage = self._cam.getImage()
            compared           = compare_images( initialImage, 
                                                 self._currentImage, 
                                                 70, 
                                                 ANY_2RGB )
            # print self.aboveTimeLimit(startTime)
            if self._stopRecording:
                del self._detectedImages
                break
            elif (not self._recording and len(self._detectedImages) > 0) or self.aboveTimeLimit(startTime): 
            #this could look better
                print "\n\nEND RECORDING!\n\n"
                self.recordOutToVideo()
                initialMotionName = "initImage-" + str(self._timeStamp[7:-4]) + ".jpg"
                initialMotion.save( initialMotionName )
                self._detectedImages = []

                command = 'ffmpeg -i ' + str(self._timeStamp) + ' -acodec libmp3lame -ab 192 ' + str(self._timeStamp)[:-4] + '.mov'
                p = subprocess.Popen(command.split())
                p.wait()
                #video is now .mov
                self._timeStamp = self._timeStamp[:-4] + ".mov"

                #dropbox uploading done here
                dropboxPic = DropboxUploader()
                dropboxVid = DropboxUploader()

                dropboxPic.authenticate()
                dropboxVid.authenticate()

                picLocation = initialMotionName
                dropboxPic.uploadFile( picLocation )
                dropboxVid.uploadFile( self._timeStamp )

                picURL = dropboxPic.getDBLink( picLocation )
                vidURL = dropboxVid.getVSASLink( self._timeStamp )

                #email done here
                emailSender = SendEmail()
                emailSender.setRecipient( "tbrown@uni.edu" )
                emailSender.setSubject("VSAS Motion Detected!")
                emailSender.setAlertLevel("RED")
                emailSender.setDbPhotoLink( picURL )
                emailSender.setDbVidLink( vidURL )
                # emailSender.setDuration("not available")#str(int(time.time() - startTime)) + " secs")
                # emailSender.setDuration("not available")#str(int(time.time() - startTime)) + " secs")
                self._date = datetime.datetime.now().strftime("%Y-%m-%d")
                emailSender.setDate(self._date)
                emailSender.sendEmail()


                #clear memory
                startTime = 0
                self._recording = False 

            elif self.overThreshold( compared, 20000 ): #recording
                if len(self._detectedImages) == 1:
                    initialMotion = self.getMostCurrentImage()
                print "recording..."
                if startTime == 0:
                    startTime = time.time()
                self._recording = True
                self._detectedImages.append( self._currentImage )
            else: #not recording
                print "not recording..."
                self._recording = False
            



