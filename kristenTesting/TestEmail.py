"""
Test of an Email Screen
Author: Kristen Nielsen  kristen.e.nielsen@gmail.com
Modeled after tkSimpleDialog.py from pythonware.com"""

from Tkinter import *
import tkMessageBox as MsgBox
import tkSimpleDialog

class EmailOptions(Toplevel):

    def __init__(self, parent):
    	Toplevel.__init__(self, parent, height=400, width=700)
    	self.pack_propagate(0)
    	self.transient(parent)
    	self.title("VSAS - Email Settings")

    	self._parent = parent

    	body = Frame(self)
    	self._initialFocus = self.body(body)
    	body.pack_propagate(0)
    	body.pack(padx=5,pady=5)

    	self.buttonBox()

    	self.grab_set()

    	if not self._initialFocus:
    	   self._initialFocus = self

    	self.protocol("WM_DELETE_WINDOW", self.cancel)

    	self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

    	self._initialFocus.focus_set()

    	self._parent.wait_window(self)


    def body(self, master):
    	pass

    def buttonBox(self):
    	pass

    def cancel(self, event=None):
    	if MsgBox.askokcancel("Quit", "Are you sure you want to quit?"):
	    self._parent.focus_set()
    	    self.destroy()

