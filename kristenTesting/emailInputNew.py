"""
Input box for email screen
Author: Kristen Nielsen  kristen.e.nielsen@gmail.com
Reference: pythonware.com
"""

from Tkinter import *
import tkMessageBox as MsgBox
import tkSimpleDialog

class EmailInput(tkSimpleDialog.Dialog):

    def body(self, master):

        self._imageOnlyStr = "N"

    	Label(master, text="Email:").grid(row=0, sticky=W)
    	self._emailEntered = StringVar()
    	self._emailEntered.set("Enter email")
    	self._emailEntry = Entry(master, textvariable=self._emailEntered)
    	self._emailEntry.grid(row=0,column=1)

        self._checkedVar = IntVar()
    	self._imageOnlyCheckButton = Checkbutton(master, text="Image Only",
                                                 variable=self._checkedVar,
                                                 command=self.isChecked)
    	self._imageOnlyCheckButton.grid(row=1,columnspan=2, sticky=W)
    	
    	return self._emailEntry

    def isChecked(self, event=None):
        if self._checkedVar:
            self._imageOnlyStr = "Y"
        else:
            self._imageOnlyStr = "N"
    
    def validate(self):
        if ((len(self._emailEntered.get())>1) and ("@" in self._emailEntered.get())):
            return 1
        else:
            MsgBox.showwarning(
                "Invalid email",
                "Please reinput email address")
            return 0
        
    def apply(self):
        self.result = str(self._emailEntered.get()+ " "+ self._imageOnlyStr)

    def get(self):
        return self.result
