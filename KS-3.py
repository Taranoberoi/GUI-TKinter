from tkinter import *
from cx_Oracle import *

win = Tk()
win.geometry("800x800")

tframe = Frame(win)
tframe.pack()
bframe = Frame(win)
bframe.pack()

label = Label(win,text="CHECK THIS OUT",fg="Black",bg="RED")
label.pack(side=LEFT)

button1 = Button(tframe,text="CLick 1")
button1.pack()

win.mainloop()
