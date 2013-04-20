##from VideoCapture import Device
import time
from Motion import *
import PIL
##import cv2

start_time = time.time()
for x in xrange(307000):
    if True == True:
        x = 4
print time.time() - start_time, "seconds to compare pixels range \n"

start_time = time.time()
for x in xrange(307000):
    if True == True:
        x = 4
print time.time() - start_time, "seconds to compare pixels xrange \n"

start_time = time.time()
count = 0
greenScaleImage = Image.open("image.jpg")
for pixel in greenScaleImage.getdata():
    if pixel != (0, 255, 0, 0):
        count += 1
print time.time() - start_time, "seconds to ACTUALLY compare pixels xrange \n"

start_time = time.time()
initialImage = Image.open( "initialImage.jpg" )
currentImage = Image.open( "currentImage.jpg" )
print time.time() - start_time, "seconds to compare open 2 images"

start_time = time.time()
initialImage.save( "initialImage.jpg" )
print time.time() - start_time, "seconds to save 1 image"
##
start_time = time.time()
compared = compare_images( initialImage, currentImage, 70, ANY_2RGB )
print time.time() - start_time, "seconds to do comparison with (compare_images)"


stop = input("Hacking dis shit")
