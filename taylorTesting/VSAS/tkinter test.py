from Tkinter import *
from time import sleep


def main():
	from Tkinter import *
	from time import sleep

	root = Tk()
	var = StringVar()
	var.set('hello')

	l = Label(root, textvariable = var)
	l.pack()

	for i in range(6):
	    sleep(1) # Need this to slow the changes down
	    var.set('goodbye' if i%2 else 'hello')
	    root.update_idletasks()

main()