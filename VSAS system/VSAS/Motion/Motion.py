import Image, ImageFilter, ImageOps

import ImageChops
import ImageEnhance
import ImageStat
import ImageDraw
import ImageFilter

# Author Bogdan Marian
# email bamarian@gmail.com
# url http://bogdanmarian.com?section=motion

#import os
#print os.name # 'posix', 'nt', 'mac', 'os2', 'ce', 'java', 'riscos'.

# threshold computation
COMPUTE_THRESHOLD = 0
# compare_images dtype constants - determines how to apply threshold
ANY_RGB = 0
ANY_2RGB = 1
SUM_RGB = 2
# green_key mtype constants - determines how key mask is constructed
KEY_REG = 0
KEY_BLUR = 1
KEY_BLUR_BRIGHT = 2
KEY_BLUR_BRIGHT_MORE = 3

DEBUG = 0


# returns a tuple containing the difference of R,G,B bands between two images
def compare_pixels(pixel1,pixel2):
	r_diff = abs(pixel1[0] - pixel2[0])
	g_diff = abs(pixel1[1] - pixel2[1])
	b_diff = abs(pixel1[2] - pixel2[2])
	return (r_diff,g_diff,b_diff)


# computes threshold is one is not specified
def compute_threshold(imgwidth,maxwidth=1000,minwidth=200,upperlimit=80,lowerlimit=5):
	if(imgwidth < maxwidth):
		threshold = (maxwidth - imgwidth)/20
	elif(imgwidth < minwidth):
		threshold = upperlimit
	else:
		threshold = lowerlimit
	return threshold


# test for motion based on one of three comparisons (dtype)
# 1 ANY_RGB:  if either of the R,G,B bands exceed threshold
# 2 ANY_2RGB: if any two of the R,G,B bands exceed threshold
# 3 SUM_RGB:  if if the combined total of R,G,B bands exceeds threshold
def motion_detected(pixel1,pixel2,threshold,dtype=ANY_RGB):
	(r_diff,g_diff,b_diff) = compare_pixels(pixel1,pixel2)
	if((dtype == ANY_RGB) and (r_diff > threshold) or (g_diff > threshold) or (b_diff > threshold)) or \
		((dtype == ANY_2RGB) and ((r_diff > threshold and g_diff > threshold) or (r_diff > threshold and b_diff > threshold) or (g_diff > threshold and b_diff > threshold))) or \
		((dtype == SUM_RGB) and (abs(sum(pixel1) - sum(pixel2)) > threshold)):
		return True
	else:
		return False


# convert a pixel number to a x,y coordinate based on image width
def pixel2xy(pixelnumber,imgwidth):
	y = pixelnumber / imgwidth
	x = pixelnumber % imgwidth
	return (x,y)


# key out where green band is saturated (0,255,0) exposing canvas
def green_key(canvas,key_image,img_source,mtype=KEY_REG):
	s3 = key_image.split()
	mask = (s3[1].point(lambda i: (i > 254 or 256))) # cut out green area (overlay)
	if(mtype == KEY_BLUR or mtype == KEY_BLUR_BRIGHT or mtype == KEY_BLUR_BRIGHT_MORE):
		mask = mask.filter(ImageFilter.SMOOTH_MORE)
		mask = mask.filter(ImageFilter.BLUR)
		mask = mask.filter(ImageFilter.SMOOTH_MORE)
	if(mtype == KEY_BLUR_BRIGHT):
		mask = (mask.point(lambda k: (k*2)))	
	elif(mtype == KEY_BLUR_BRIGHT_MORE):
		mask = (mask.point(lambda k: k > 20 and (k*k)))
# 	mask.show()
# 	mask.save("images/saved/mask.jpg")
# 	canvas.convert("RGBA") # needed?

	if(canvas.size != img_source.size): # fix image size
		if(canvas.size < img_source.size):
			print "resizing canvas", canvas.size, img_source.size, key_image.size
			canvas = ImageOps.fit(canvas,img_source.size)
		else:
			print "resizing img_source and mask", canvas.size, img_source.size, key_image.size
			img_source = ImageOps.fit(img_source,canvas.size)
			mask = ImageOps.fit(mask,canvas.size)
	image = Image.composite(img_source,canvas,mask)
	return image


def compare_images(frame1, frame2, threshold=COMPUTE_THRESHOLD,dtype=KEY_REG):
	if not frame1 or not frame2: print "compare_image :: Bad image detected"; return False
	frame1_size = frame1.size
	frame2_size = frame2.size
	if (frame1_size != frame2_size): 
		print "compare_image :: Different image sizes"; return False

	if(threshold == COMPUTE_THRESHOLD): threshold = compute_threshold(frame1_size[0]);
	color = 0,255,0,0 # green screen
	frame1 = frame1.getdata()
	frame2 = frame2.getdata()
	key_img = Image.new("RGBA",frame1_size,color)
	total_pixels = frame1_size[0] * frame1_size[1]
	key_img_pixels = [color] * total_pixels

	for i in range(3,total_pixels - 1 ,3):
		if(motion_detected(frame1[i],frame2[i],threshold,dtype)):
			key_img_pixels[i] = frame2[i]
			# add quick flag to skip i-1,i+1 tests
			if(motion_detected(frame1[i-1],frame2[i-1],threshold,dtype)):
				key_img_pixels[i-1] = frame2[i-1]
			if(motion_detected(frame1[i+1],frame2[i+1],threshold,dtype)):
				key_img_pixels[i+1] = frame2[i+1]

	key_img.putdata(key_img_pixels)
	
	if DEBUG:
		print "Threshold : ",threshold," dtype ",dtype

	return key_img
