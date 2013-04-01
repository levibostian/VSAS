# scrollbar-example-1.py

from Tkinter import *
from datetime import date
from random import choice, randint


class App:
    def __init__(self):
        self.root = Tk()

        self.root.title("Previous Recordings")

        self.canvas = Canvas(self.root)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(self.root, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor=NW,
                                  tags='self.frame')

        self.frame.bind('<Configure>', self.OnFrameConfigure)

        self.populate()
        self.root.mainloop()

    def populate(self):
        Label(self.frame, text="LABEL", font=("bold")).grid(row=0,column=0)
        Label(self.frame, text="DATE").grid(row = 0, column = 1)
        Label(self.frame, text="SECURITY THREAT").grid(row=0, column =2)
        for row in xrange(1,100):
            month = randint(1,12)
            if month in [9,4,6,11]:
                day=randint(1,30)
            elif month in [1,3,5,7,8,10,12]:
                day=randint(1,31)
            else:
                day=randint(1,28)
            Label(self.frame,text=str(date(2013,month,day))).grid(row=row,column=1)
            Label(self.frame, text=choice(['red','orange','yellow'])).grid(row=row, column=2)
            
    def OnFrameConfigure(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

app=App()
