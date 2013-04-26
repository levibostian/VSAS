"""
Video display tester
Author: Kristen Nielsen
This code will display multiple images in a Tkinter window.
File must be in same folder as this program.
Code modified from http://code.activestate.com/recipes/521918-pil-and-tkinter-to-display-images/
and
effbot.org/tkinterbook/photoimage.htm
""""

from Tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open("VSAS Edit Video.gif")
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.image = photo
# This keeps a reference to the image so it isn't garbage collected.
label.pack()
