"""
VSAS main screen mock-up using existing gif image.
Author: Kristen Nielsen  kristen.e.nielsen@gmail.com
References: pythonware.com
"""

from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox as MsgBox
from EmailScreen import EmailSettings
from TestVideo import VideoSettings
# from MotionDetector import *

root = Tk()
class Application():
    def displayAbout(self):
        text = "VSAS\n(C) 2013\nGroup Delta\nAbu Audu, Levi Bostian,\nTaylor Brown, Kyle Mueller,\nKristen Nielsen"
        MsgBox.showinfo(title="VSAS - About", message = text)
        
    def displayHelp(self, event=None):
        helpText = open("MainScreenHelp.txt", 'r').read()
        MsgBox.showinfo(title="VSAS - Help", message = helpText)

    def displayEmailSettings(self):
        EmailSettings(self._master)

    def displayVideoSettings(self):
        VideoSettings(self._master)

    def buildMenu(self):
        menuBar=Menu(self._master)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='Adjust Camera')
        fileMenu.add_command(label='Video Settings', command=self.displayVideoSettings)
        fileMenu.add_command(label='Email Settings', command=self.displayEmailSettings)
        fileMenu.add_command(label='View Previous Recordings')
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.closeWindow)
        menuBar.add_cascade(label="File", menu=fileMenu)

        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About", command=self.displayAbout)
        helpMenu.add_command(label="Help - F1", command=self.displayHelp)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        self._master.config(menu=menuBar)

    def closeWindow(self, event=None):
        if MsgBox.askokcancel("Quit", "Do you really want to quit?"):
            self._motion.end()
            self._master.destroy()

    def updateImage(self):
        image = self._motion.getMostCurrentImage()
        self._photo = ImageTk.PhotoImage(image)
        self._label.image = self._photo
        self._label.configure( image=self._photo )
        root.after(10, self.updateImage)

    def __call__(self):#this is ran when a Thread is created
        root.after(10, self.updateImage)    
        root.mainloop()

    def __init__(self, motionDetector, master=None):
        self._master = master

        self._motion = motionDetector

        self._master.title("VSAS")
        self._frame = Frame(self._master, height=600,width=800)
        self._frame.pack()
        self._frame.pack_propagate(0)

        self.buildMenu()
        
        self._master.bind("<F1>", self.displayHelp)
        self._master.bind("<Escape>", self.closeWindow)
        self._master.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self._imgCanvas = Canvas(self._frame)
        self._imgCanvas.pack()

        image = Image.open("VSAS logo.jpg")
        # image file must be in same folder as this program. Otherwise
        # you have to import os and sys.
        photo = ImageTk.PhotoImage(image)

        self._label = Label(self._imgCanvas,image=photo)
        self._label.image = photo
        self._label.pack()

        self._btnCanvas = Canvas(self._frame)
        self._btnCanvas.pack()

        adjustCameraButton = Button(self._btnCanvas, text= "Adjust Camera")
        adjustCameraButton['bg'] = 'red'
        adjustCameraButton.pack(side=TOP,padx=4,pady=4)
        # adjustCameraButton['command']

        emailButton = Button(self._btnCanvas, text='Email Settings')
        emailButton.pack(side=LEFT,padx=4,pady=4)
        emailButton['command']=self.displayEmailSettings

        videoButton = Button(self._btnCanvas, text='Video Settings')
        videoButton.pack(side=LEFT,padx=4,pady=2)
        videoButton['command']=self.displayVideoSettings

        logButton = Button(self._btnCanvas, text='View Previous Events')
        logButton.pack(side=LEFT,padx=4,pady=4)
        # logButton['command']=logChoices

        helpButton = Button(self._btnCanvas, text='Help')
        helpButton.pack(side=LEFT,padx=4,pady=4)
        helpButton['command']=self.displayHelp

        #self._master.mainloop()# removed due to __call__ method. 
        
        

##app = Application(root)
