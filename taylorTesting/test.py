from VideoCapture import Device
import time
from Motion import *

cam = Device()
test = cam.getImage()
cam.saveSnapshot('image.jpg')

time.sleep(1)
test2 = cam.getImage()

compared = compare_images(test, test2)
compared.save('letshope.jpg')
