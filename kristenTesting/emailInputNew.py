"""
Input box for email screen
Author: Kristen Nielsen  kristen.e.nielsen@gmail.com
Reference: pythonware.com
"""

from Tkinter import *
import tkMessageBox as MsgBox
import tkSimpleDialog

class EmailInput(tkSimpleDialog.Dialog):

    def body(self):

    	Label(master, text="Email:").grid(row=0, sticky=W)
    	self._emailEntry = Entry(master)
    	self._emailEntry.grid(row=0,column=1)
    	
    	return self._emailEntry
    
    def validate(self):
    	