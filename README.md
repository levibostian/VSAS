VSAS (Video Surveillance Alert System)
======================================

VSAS is	a personal video surveillance software built in Python 2.7 for Windows.

Motion is detected via webcam which triggers video recording. After video is recorded, video is uploaded to Dropbox cloud storage and email is sent to you with a (1) still image taken from the motion detected to quickly view if it was a false alarm or serious, (2) date and time of detected motion, (3) link to website to view the video footage. 

Project history
===============

VSAS was created for CS2720 Software Engineering Spring 2013 at the [University of Northern Iowa](www.uni.edu) by [Dr Stephen Hughes](http://www.uni.edu/sthughes/). 

### Team:
Abu Audu, Levi Bostian, Taylor Brown, Kyle Mueller, Kristen Nielsen

Files
=====
Project includes all docs created and used for semester project including:
* VSAS source code including random code used for various testing (___testing directories).
* Documentation including final SRS document. Whiteboard sessions, mockups, risk assessments, etc.
* Presentation documents for final presentation.
* Screenshots of program.
* vsassoftware.com source code files used for website to watch video footage.

Building
========
VSAS does work! You will have to hack away at the source code in some places to get it designed for you and you will need to install some libraries but besides that it is fully functional.
* Download source code here from GitHub.
* Install libraries mentioned below and Python2.7 with TkInter on your Windows Vista/7 machine (not tested on other versions of Windows but may work. Also, most libraries have ports of Mac or Linux so feel free to hack away and get it working. If you do, please take a sec and mention it to me!)
* Edit `dropbox_vsas.py` to your Dropbox API key and secret. Edit `email_vsas.py` to your email and password you wish to send email message to.
* Download website files for the VSAS website here in the GitHub repo and host it on your own web server. (Website written with PHP). You will then need to edit `dropbox_vsas.py` and `email_vsas.py` to match the web URL for your server instead of the vsassoftware.com it is currently setup as. 

VSAS takes advantage of many open source libraries to make our project a success and these libraries need to be installed in order for it to operate.  

The known software packages to install are:
* [PIL](http://www.pythonware.com/products/pil/)
* [OpenCV](http://opencv.org/downloads.html)
* [NumPy](https://pypi.python.org/pypi/numpy)
* [VideoCapture](http://videocapture.sourceforge.net/)
* [FFmpeg](http://ffmpeg.zeranoe.com/builds/)

Notes
=====
* Viewing the source code, you can find wonderful pieces of information such as the password to our email address used for the project and the API keys to upload docs to our Dropbox account but don't worry, the passwords have all been changed and the Dropbox keys are invalid so go ahead and edit those fields to your accounts. 
* This repo is not designed for extending. It is meant to represent an amazing team and an amazing semester. 
* A few of the documents have 2012 as the date on them. 2013 is accurate, I have no idea how this was not noticed before now.