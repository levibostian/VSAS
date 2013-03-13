"""
VSAS main screen mock-up using existing gif image.
Author: Kristen Nielsen  kristen.e.nielsen@gmail.com
References: pythonware.com
"""

from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox as MsgBox

root = Tk()
root.title("VSAS")
class Application():
    def displayAbout(self):
        text = "VSAS\n(C) 2013\nGroup Delta\nAbu Audu, Levi Bostian,\nTaylor Brown, Kyle Mueller,\nKristen Nielsen"
        MsgBox.showinfo(title="VSAS - About", message = text)
        
    def displayHelp(self, event=None):
        helpText = open("MainScreenHelp.txt", 'r').read()
        MsgBox.showinfo(title="VSAS - Help", message = helpText)


    def __init__(self, master=None):
        master.title("VSAS")
        self.frame = Frame(root, height=600,width=800)
        self.frame.pack()
        self.frame.pack_propagate(0)

        menuBar=Menu(master)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='Adjust Camera')
        fileMenu.add_command(label='Video Settings')
        fileMenu.add_command(label='Email Settings')
        fileMenu.add_command(label='View Previous Recordings')
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=master.destroy)
        menuBar.add_cascade(label="File", menu=fileMenu)

        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About", command=self.displayAbout)
        helpMenu.add_command(label="Help - F1", command=self.displayHelp)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        master.config(menu=menuBar)
        
        master.bind("<F1>", self.displayHelp)

        self.imgCanvas = Canvas(self.frame)
        self.imgCanvas.pack()

        image = Image.open("VSAS Edit Video.gif")
        # image file must be in same folder as this program. Otherwise
        # you have to import os and sys.
        photo = ImageTk.PhotoImage(image)

        self.label = Label(self.imgCanvas,image=photo)
        self.label.image = photo
        self.label.pack()

        self.btnCanvas = Canvas(self.frame)
        self.btnCanvas.pack()

        adjustCameraButton = Button(self.btnCanvas, text= "Adjust Camera")
        adjustCameraButton['bg'] = 'red'
        adjustCameraButton.pack(side=TOP,padx=4,pady=4)
        # adjustCameraButton['command']
        
        emailButton = Button(self.btnCanvas, text='Email Settings')
        emailButton.pack(side=LEFT,padx=4,pady=4)
        # emailButton['command']=emailSettingsScreen

        videoButton = Button(self.btnCanvas, text='Video Settings')
        videoButton.pack(side=LEFT,padx=4,pady=2)
        # videoButton['command']=videoSettingsScreen

        logButton = Button(self.btnCanvas, text='View Previous Events')
        logButton.pack(side=LEFT,padx=4,pady=4)
        # logButton['command']=logChoices

        helpButton = Button(self.btnCanvas, text='Help')
        helpButton.pack(side=LEFT,padx=4,pady=4)
        helpButton['command']=self.displayHelp

        master.mainloop()
        
        

app = Application(root)
