"""
Actual view of the Previous Recordings.
"""

from Tkinter import *
import tkMessageBox as MsgBox
from multilistbox import MultiListbox
import tkSimpleDialog

class PreviousRecordingsListScreen(Toplevel):

    def __init__(self, parent, listOfEvents, interval):
        Toplevel.__init__(self,parent,height=400,width=400)
        self.transient(parent)
        self.title("VSAS - View Previous Recordings " + interval.title())

        self._parent = parent

        self._listOfEvents = listOfEvents

        body  = Frame(self)
        self._initialFocus = self.body(body)
        body.pack(padx=5,pady=5)

        self.buttonbox()

        self.grab_set()

        self.bind("<F1>",self.displayHelp)


        if not self._initialFocus:
            self._initialFocus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.bind("<F1>", self.displayHelp)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self._initialFocus.focus_set()

        self._parent.wait_window(self)

    def body(self, master):
        self._canvas = Canvas(master)
        frame = Frame(self._canvas)
        verticalScrollBar = Scrollbar(master,command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=verticalScrollBar.set)

        verticalScrollBar.pack(side=RIGHT, fill=Y)
        self._canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self._canvas.create_window((4,4), window=frame, anchor=NW,
                             tags='frame')

        frame.bind('<Configure>', self.OnFrameConfigure)

        self.populate(frame)

    def populate(self,frame):
        Label(frame,text="DATE").grid(row=0,column=0)
        #Label(frame,text="SECURITY THREAT").grid(row=0,column=1)
        #Label(frame,text="DURATION (sec)").grid(row=0,column=2)
        Label(frame,text="LINK").grid(row=0,column=0,sticky=W)
        for row in xrange(1,len(self._listOfEvents)):
            item = self._listOfEvents[row-1]
            Label(frame, text=item[0]).grid(row=row, column=0)
            #Label(frame, text=item[1]).grid(row=row, column=1)
            #Label(frame, text=item[2]).grid(row=row, column=2)
            text = Text(frame, height=1)
            text.grid(row=row, column=1, rowspan=1)
            text.insert(INSERT, item[2])

    def OnFrameConfigure(self,event):
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

    def buttonbox(self):

        box = Frame(self)

        Button(box, text="OK", width = 10, command=self.cancel,
                   default=ACTIVE).pack(side=LEFT)
        Button(box, text="Help", width = 10, command=self.displayHelp).pack(side=LEFT)

        self.bind("&lt;Return>", self.cancel)
        self.bind("&lt;Escape>", self.cancel)

        box.pack()

    def displayHelp(self, event=None):
        helpText = open("vsasGUI/PreviousRecordingsListHelp.txt", "r").read()
        MsgBox.showinfo(title="VSAS Previous Events - Help", message=helpText)

    def cancel(self, event=None):

        self._parent.focus_set()
        self.destroy()
