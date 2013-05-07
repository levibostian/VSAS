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

        self.result = ""
        
        #self._imageOnlyStr = "N"
        #self.adminStr = ""

    	Label(master, text="Email:").grid(row=0, sticky=W)
    	self._emailEntered = StringVar()
    	self._emailEntered.set("Enter email")
    	self._emailEntry = Entry(master, width = 40,
                                 textvariable=self._emailEntered)
    	self._emailEntry.grid(row=0,column=1)

        #self._imageOnlyCheckedVar = IntVar()
    	#self._imageOnlyCheckButton = Checkbutton(master, text="Image Only",variable=self._imageOnlyCheckedVar,command=self.isChecked)
    	#self._imageOnlyCheckButton.grid(row=1,column=0, sticky=W)
    	#self.adminCheckedVar = IntVar()
    	#self.adminCheckButton = Checkbutton(master, text="Administrator Email",
    	#variable=self.adminCheckedVar, command=self.adminIsChecked)
    	#self.adminCheckButton.grid(row=1, column=1, stick=W)


    	return self._emailEntry

    #def adminIsChecked(self, event=None):
     #   if self.adminCheckedVar:
      #     self.adminStr = "admin"
       # else:
        #   self.adminStr = ""

    #def isChecked(self, event=None):
     #   if self._imageOnlyCheckedVar:
      #      self._imageOnlyStr = "Y"
       # else:
        #    self._imageOnlyStr = "N"

    def validate(self):
        email = self._emailEntered.get()
        if ((len(email)>=6) and ("@" in email)):
            atIndex = email.index("@")
            addressPlace = email[atIndex: ]
            if "." in addressPlace:
               return 1
            else:
               MsgBox.showwarning(
                   "Invalid email",
                   "Please reenter email address")
               return 0
        else:
            MsgBox.showwarning(
                "Invalid email",
                "Please reenter email address")
            return 0

    def apply(self):
        self.result = ",".join([self._emailEntered.get()])#,"N"])

    def get(self):
        return self.result
