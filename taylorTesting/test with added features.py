from VideoCapture import Device
import time
from Motion import *
import cv2
import numpy

def totalChange( greenScaleImage ):
    count = 0
    for pixel in greenScaleImage.getdata():
        if pixel != (0, 255, 0, 0):
            count += 1
    return count

def convertImagesToCv( images ):
    newImages = []
    for index in xrange(len(images)):
        pilImage = images[index].convert('RGB')
        openCvImage = numpy.array(pilImage)
        openCvImage = openCvImage[:, :, ::-1].copy()
        newImages.append(openCvImage)
    return newImages

def main():
    
    cam = Device()
    time.sleep(1)
    print "3..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "1..."
    time.sleep(1)
    print "SMILE!"
    initialImage = cam.getImage()
    time.sleep(1)
    initialImage = cam.getImage()
    initialImage.save('image.jpg')

    images = [initialImage]
    end = False
    count = 0
    while not end:
        time.sleep(.5)
        newImage = cam.getImage()

        compared = compare_images( initialImage, newImage )
##        size = compared.size
        print "not recording..."
        while totalChange( compared ) > 30000:
            print "Recording..."
            count += 1
            images.append( newImage )
            time.sleep(1)
            compared = compare_images( initialImage, newImage )
            print 
            newImage = cam.getImage()
            compared.save('letshope' + str(count) + '.jpg')
            end = True
        compared.save('letshope.jpg')
    print images
        
    cvImages = convertImagesToCv( images )
    frame = cvImages[0]
    video_out = cv.CreateVideoWriter( "testing", cv.CV_FOURCC('M','J','P','G'), capture.fps, frame.size(), 1)
    for item in cvImages:
        frame = item
        cv.WriteFrame( video_out, frame )



main()
