from VideoCapture import Device
import time
from Motion import *
import cv2
import numpy
import threading


class MotionDetector(): 
    def __init__(self):
        self._cam            = Device()
        self._detectedImages = []
        self._currentImage   = Image.open( "VSAS Edit Video.gif" )
        self._recording      = False

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
            time.sleep(1)
            initialImage = cam.getImage()
            initialImage.save('image.jpg')
            time.sleep(1)
        return initialImage

    def convertImagesToCv( self, images ):
        newImages = []
        for index in xrange(len(images)):
            pilImage = images[index].convert('RGB')
            openCvImage = numpy.array(pilImage)
            openCvImage = openCvImage[:, :, ::-1].copy()
            newImages.append(openCvImage)
        return newImages

    def overThreshold( self, greenImage, thresholdByPx ):
        amtChanged = self.totalChange( greenImage )
        return amtChanged > thresholdByPx


    def detect( self ):
        
        print "Getting initial image, and adjusting camera..."
        
        initialImage = self.adjustCamera( self._cam )
        initialImage.save('initialImage.jpg')

        print "initial image saved and webcam adjusted..."

        start_time = time.time()
        while True:
            time.sleep(1.0/60.0)

            self._currentImage = self._cam.getImage()
            if (time.time() - start_time) % 1.0:
                continue

            compared = compare_images( initialImage, 
                                       self._currentImage, 
                                       70, 
                                       ANY_2RGB )

            # amtPxChanged = totalChange( compared )
            if self.overThreshold( compared, 20000 ):
                print "Recording..."
                # print amtPxChanged

                self._recording = True
                
                self._detectedImages.append( self._currentImage )
                # compared.save('recording.jpg')#' + str(imgNum) + '.jpg')
            else:
                self._recording = False
                print "not recording..."
                # compared.save('notRecording.jpg')
            # self._currentImage.save("currentImage.jpg")
    # cvImages = convertImagesToCv( recordedImages )
    # frame = cvImages[0]
    # video_out = cv2.VideoWriter( "testing", ('M','J','P','G'), 30.0, frame.size())
    # for item in cvImages:
    #     frame = item
    #     cv2.WriteFrame( video_out, frame )

