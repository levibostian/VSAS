"""
Previous Recordings Screen
"""

from Tkinter import *
import tkMessageBox as MsgBox
from PreviousRecordingsListScreen import PreviousRecordingsListScreen
from datetime import date

class PreviousRecordingsScreen(Toplevel):
    def __init__(self,parent):
        Toplevel.__init__(self,parent,height=400,width=400)
        self.transient(parent)
        self.title("VSAS - View Previous Recordings")

        self._parent = parent

        body  = Frame(self)
        self._initialFocus = self.body(body)
        body.pack(padx=5,pady=5)

        self.buttonbox()

        self.grab_set()

        #self.bind("<F1>",self.dispayHelp)

        if not self._initialFocus:
            self._initialFocus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self._initialFocus.focus_set()

        self._parent.wait_window(self)
        
    def body(self, master):

    	self.result = None

     	self._today = date.today()

     	MODE =[("One Week", "week"),
               ("One Month", "month"),
               ("One Year", "year")]

     	self._variable = StringVar()
     	self._variable.set("week")

     	radioButtonList = []

     	for text, mode in MODE:
            b = Radiobutton(self, text = text, variable=self._variable,
                            value=mode, indicatoron=0)
            b.pack(anchor=W,padx=2,pady=2)
            radioButtonList.append(b)

        return radioButtonList[0]

    def buttonbox(self):
        # add standard button box.

        box = Frame(self)

        w = Button(box, text="OK", width=10, command = self.ok,
                   default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady =5)
        w = Button(box, text="Cancel",width=10,command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def validate(self):
    	if self._variable != None:
    	   return 1
	else:
	    MsgBox.showwarning(
                "Invalid choice",
                "Please make a selection")
	    return 0

    def calculateDate(self):
        monthDict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31,
                     8:31, 9:30, 10:31, 11:30, 12:31}
        newDay = self._today.day
        newMonth = self._today.month
        newYear = self._today.year
        if self._variable.get() == "week":
            newDay -= 7
            if newDay <= 0:
                newMonth -= 1
                if newMonth == 0:
                    newMonth = 12
                    newYear -= 1
                newDay = monthDict[newMonth] + newDay
        elif self._variable.get() == "month":
            newMonth -= 1
            if newMonth == 0:
                newMonth = 12
                newYear -= 1
        else:
            newYear -= 1
        self.result = str(date(newYear,newMonth,newDay))

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def apply(self):
        self.calculateDate()
        previousRecordingsList = open("testPreviousRecordings.txt","r").readlines()
        listOfEvents = []
        for item in previousRecordingsList:
            index = previousRecordingsList.index(item)
            item = item[ :-1].split(",")
            dateOfInterest=item[0]
            if (dateOfInterest[0:10] >= self.result and
                dateOfInterest[0:10] <= str(self._today)):
                listOfEvents.append(item)
        if len(listOfEvents) == 0:
            MsgBox.showinfo("No Events",
                            "There are currently no events to show for this time period.")
        else:
            PreviousRecordingsListScreen(self._parent, listOfEvents)

    def cancel(self, event = None):
        if MsgBox.askyesno("Leave now?",
                           "Do you want to leave?"):
            self._parent.focus_set()
            self.destroy()
