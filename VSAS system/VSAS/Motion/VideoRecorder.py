from cv2 import *
import PIL
import time
import Image

class VideoRecorder():
	def __init__(self, sizeOfFrames=(640,480)):
		self._sizeOfVideo = sizeOfFrames
		self._recorder = self.newRecorder()
		self._videoWritten = False


	def newRecorder(self):
		videoRecorder = cv.CreateVideoWriter( "testing-vsas.avi", 
                                         	   cv.CV_FOURCC('I','4','2','0'), 
                                               2.0, 
                                               self._sizeOfVideo, 
                                               1)
		return videoRecorder

	def videoWritten(self):
		return self._videoWritten

	def convertPil( self, pilImage ):
		pilImage.save( "convert.jpg" )
		cvImage = cv.LoadImage( "convert.jpg")
		return cvImage

	def writeToVideo( self, cvImage ):
		print "written frame"
		cv.WriteFrame( self._recorder, cvImage )
		self._videoWritten = True

	def finishRecording(self):
		# del self._recorder
		print cv.self._recorder.isOpened()
		self._recorder = self.newRecorder()
		self._videoWritten = False

# def convertPIL(pilImage):
#         cvImage = cv.CreateImageHeader(pilImage.size, cv.IPL_DEPTH_8U, 3)
#         r,g,b=pilImage.split()
#         pilImage2 = Image.merge("RGB",(b,g,r))
#         cv.SetData(cvImage, pilImage2.tostring())
#         cv.SaveImage("TESTINGHURRRRR.jpg", cvImage)
# 
# 

