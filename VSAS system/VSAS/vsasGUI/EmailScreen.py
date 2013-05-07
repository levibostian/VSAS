"""
Test of an Email Screen
Author: Kristen Nielsen  kristen.e.nielsen@gmail.com
Modeled after tkSimpleDialog.py from pythonware.com
"""

from Tkinter import *
import tkMessageBox as MsgBox
from multilistbox import MultiListbox
from emailInputNew import EmailInput

class EmailSettings(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent, height=400, width=700)
        self.pack_propagate(0)
        self.transient(parent)
        self.title("VSAS - Email Settings")

        self._parent = parent

        self.adminEmail=""

        emailFile = open("vsasGUI/emailTester.txt","r")
        self.emailList = emailFile.readlines()
        emailFile.close()
        body = Frame(self, bg="black")
        self._initialFocus = self.body(body)
        #body.pack_propagate(0)
        body.pack(padx=5,pady=5)

        self.buttonBox()
        self.current=None
        self.grab_set()

        self.bind("<F1>",self.displayHelp)

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
                                          (('Email', 160),("",1)),
                                          command = self.deleteEmail)
        for item in self.emailList:
            item = item[ :-1]
            item = item.split(",")
            self._emailListbox.insert(END, (item[0],""))
        self._emailListbox.grid(column = 0,columnspan=3, sticky=W)
        addButton = Button(emailListCanvas, text="Add",command=self.addEmail)
        addButton.grid(row=1,column=0)

        deleteButton = Button(emailListCanvas, text="Delete",command=self.deleteEmail)
        deleteButton.grid(row=1,column=1)

        helpButton = Button(emailListCanvas, text="Help", command = self.displayHelp)
        helpButton.grid(row=1,column=2)

        #Label(master, text="The administrator email will receive\nall information regarding all alerts",
        #fg="green",bg="black").grid(column=1, row=0)
        #self.adminEmailDisplay = Label(master, text=self.adminEmail)
        #self.adminEmailDisplay.grid(column=1, row=1)


    def buttonBox(self):
        pass

    def addEmail(self):
        email = EmailInput(self, title="Add Email").get()
        if len(email)>0:
            emailFile = open("emailTester.txt","a")
            #emailComposite = email.split(",")
            #emailTuple = (emailComposite[0], emailComposite[1])
            email = email+"\n"
            self.emailList.append(email)
            emailFile.write(email)
            emailFile.close()
            self._emailListbox.insert(END, (email,""))
            self.update()


    def deleteEmail(self, event=None):
        if MsgBox.askyesno("Delete Email?","Are you sure you want to delete selected email?"):
            index = self.emailList[eval(self._emailListbox.curselection()[0])]
            self.emailList.remove(index)
            self._emailListbox.delete(0,END)
            emailFile = open("emailTester.txt","w")
            for item in self.emailList:
                emailFile.write(item)
                item = item[ :-1]
                item = item.split(",")
                self._emailListbox.insert(END, (item[0], item[1]))
            emailFile.close()
    
    def displayHelp(self, event=None):
        helpText = open("EmailScreenHelp.txt","r").read()
        MsgBox.showinfo(title="VSAS Email Settings - Help", message=helpText)

    def cancel(self, event=None):
        if MsgBox.askyesno("Done?",
                           "All changes have been saved.\nReturn to VSAS Main?"):
            self._parent.focus_set()
            self.destroy()

