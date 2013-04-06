"""
Edit email screen.
A pop-up similar to inputting a new email, but just alters data previously entered
Author: Kristen Nielsen <kristen.e.nielsen@gmail.com>
"""

from tkinter import *
import tkMessageBox as MsgBox
import tkSimpleDialog

class EditEmail(tkSimpleDialog.Dialog):

    def body(self, master=None, currentEmail):
        self._imageOnlyStr = "N"
		  
	Label(master, text="Email:").grid(row=0, sticky=W)
	self._emailEntered = StringVar()
	self._emailEntered.set(currentEmail)
	self._emailEntry = Entry(master, width = 40,
                                 textvariable=self._emailEntered)
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
        if ((len(self._emailEntered.get()) >= 6) and ("@" in self._emailEntered.get())
            return 1
        else:
            MsgBox.showwarning(
                "Invalid email",
                "Please reenter email address")
            return 0

    def apply(self):
        self.result = str(self._emailEntered.get() + " " + self.imageOnlyStr)

    def get(self):
        return self.result
