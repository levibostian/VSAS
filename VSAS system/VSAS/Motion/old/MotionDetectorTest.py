from VideoCapture import Device
from VideoRecorder import *
import time
from Motion import *
from cv2 import *
import numpy
import threading

class MotionDetectorTest(): 
    def __init__(self): #not using video recorder as of now
        self._cam            = Device()
        self._detectedImages = []
        self._currentImage   = Image.open( "VSAS logo.jpg" )
        self._recording      = False
        self._videoRecorder  = self.newRecorder()
        self._recorded       = False

    def __call__(self):
        self.detect()

    def newRecorder(self):
        videoRecorder = cv.CreateVideoWriter( "testing-vsas.avi", 
                                               cv.CV_FOURCC('I','4','2','0'), 
                                               2.0, 
                                               (640,480), 
                                               1)
        return videoRecorder

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
            initialImage.save('image.jpg')
            time.sleep(.75)
        return initialImage

    # def convertImagesToCv( self, images ):
    #     newImages = []
    #     for index in xrange(len(images)):
    #         pilImage = images[index].save( "pilchange.jpg" )
    #         openCvImage = cv.LoadImage( "pilchange.jpg" )
    #         newImages.append(openCvImage)
    #     return newImages

    def overThreshold( self, greenImage, thresholdByPx ):
        amtChanged = self.totalChange( greenImage )
        return amtChanged > thresholdByPx

    def convertPilToCV( self, pilImage ):
        pilImage.save( "convert.jpg" )
        cvImage = cv.LoadImage( "convert.jpg")
        return cvImage

    def captureImages( self, fps ):
        #nothing here
        print

    def getMostCurrentImage( self ):
        return self._cam.getImage()

    def writeToVideo(self, pilImage):
        cvImage = self.convertPilToCV( pilImage )
        cv.WriteFrame( self._videoRecorder, cvImage )
        self._recorded = True
    # def recordImage(self, pilImage):
    #     cvImage = self._videoRecorder.convertPil( pilImage )
    #     self._videoRecorder.writeToVideo( cvImage )

    # def recordOutToVideo(self):
    #     cvImages = self.convertImagesToCv( self._detectedImages )
    #     frame = cvImages[0]
    #     cv.SaveImage("comparison.jpg", frame)
    #     video_out = cv.CreateVideoWriter( "testing-vsas.avi", 
    #                                       cv.CV_FOURCC('I','4','2','0'), 
    #                                       2.0, 
    #                                       cv.GetSize(frame), 
    #                                       1)
    # #     # cv.CV_FOURCC('I','4','2','0')
    #     for item in cvImages:
    #         frame = item
    #         cv.WriteFrame( video_out, frame )


    def detect( self ):
        #"Getting initial image, and adjusting camera..."
        initialImage = self.adjustCamera( self._cam )
        initialImage.save('initialImage.jpg')
        #"initial image saved and webcam adjusted..."

        while True:
            time.sleep(.01) #to slow it down...might not be needed

            self._currentImage = self._cam.getImage()
            compared           = compare_images( initialImage, 
                                                 self._currentImage, 
                                                 70, 
                                                 ANY_2RGB )
            if not self._recording and self._recorded:#self._videoRecorder.videoWritten(): #len(self._detectedImages) > 0:#self._videoRecorder.videoWritten(): #had just stopped recording
                # self._detectedImages[len(self._detectedImages)/2].save("detected.jpg")
                # self.recordOutToVideo()
                # self._detectedImages = []
                # print "!!!finishedRecording..."
                self._videoRecorder = self.newRecorder()
                self._recorded = False
                #clear memory
            elif self.overThreshold( compared, 20000 ): #recording
                print "recording..."
                self._recording = True
                # self._detectedImages.append( self._currentImage )
                # print "!!!recorded image to video..."
                self.writeToVideo( self._currentImage )
                # compared.save('recording.jpg')#' + str(imgNum) + '.jpg')
            else: #not recording
                print "not recording..."
                self._recording = False
                # compared.save('notRecording.jpg')
            
            # self._currentImage.save("currentImage.jpg")



