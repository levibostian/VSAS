"""
Test of an Email Screen
Author: Kristen Nielsen  kristen.e.nielsen@gmail.com
Modeled after tkSimpleDialog.py from pythonware.com
"""

from Tkinter import *
import tkMessageBox as MsgBox
from multilistbox import MultiListbox
from emailInputNew import EmailInput

class EmailOptions(Toplevel):

    def __init__(self, parent):
    	Toplevel.__init__(self, parent, height=400, width=700)
    	self.pack_propagate(0)
    	self.transient(parent)
    	self.title("VSAS - Email Settings")

    	self._parent = parent

    	self._emailList = []

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
    	# create canvas to hold scrollbar and listbox objects
    	emailListCanvas = Canvas(master, width=350, height=400)
    	emailListCanvas.config(scrollregion=emailListCanvas.bbox(ALL))
    	emailListCanvas.grid(column=0, sticky=W)
    	
    	# create multiListbox to hold email list
    	self._emailListbox = MultiListbox(emailListCanvas,
                                          (('Email', 40), ('Image Only', 10)))
    	self._emailListbox.grid(column = 0, sticky=W)
        # create canvas to hold admin email information
        adminEmailCanvas = Canvas(master)
        adminEmailCanvas.grid(column=1)
    	
    def buttonBox(self):
    	pass

    def addEmail(self):
        email = EmailInput(self, title="Add Email").get()
        email = email.split()
        email = email.tuple()
        self._emailListbox.insert(END, email)

    def deleteEmail(self):
        pass

    def editEmail(self):
        pass

    def cancel(self, event=None):
    	if MsgBox.askokcancel("Quit", "Are you sure you want to quit?"):
	    self._parent.focus_set()
    	    self.destroy()

