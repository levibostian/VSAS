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

def adjustCamera( cam ):
    for x in xrange(3):
        initialImage = cam.getImage()
        initialImage.save('image.jpg')
        time.sleep(5)
    return initialImage

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

    print "Getting initial image, and adjusting camera..."
    
    initialImage = adjustCamera( cam )
    initialImage.save('initialImage.jpg')

    print "initial image saved and webcam adjusted..."


    recordedImages = [initialImage]
    end            = False

    while True:
        time.sleep(.2)

        newImage = cam.getImage()
        compared = compare_images( initialImage, newImage, 70, ANY_2RGB )

        amtPxChanged = totalChange( compared )
        if amtPxChanged > 20000:
            print "Recording..."
            print amtPxChanged

            # time.sleep(.2)
            
            recordedImages.append( newImage )
            compared.save('recording.jpg')#' + str(imgNum) + '.jpg')
            end = True
        elif not end:
            break
        else:
            print "not recording..."
            compared.save('notRecording.jpg')

    cvImages = convertImagesToCv( recordedImages )
    frame = cvImages[0]
    video_out = cv2.VideoWriter( "testing", cv.CV_FOURCC('M','J','P','G'), 30.0, (640, 580))
    for item in cvImages:
        frame = item
        cv2.WriteFrame( video_out, frame )

main()
