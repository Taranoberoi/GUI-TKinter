from tkinter import *

win = Tk()
win.geometry("800x800")
label = Label(win,text="Main Label",bg="RED",fg="Black")
label.pack() ## by ading argument to make it dynamic

sublabel = Label(win,text="Sub Label",bg="Green",fg="Black")
sublabel.pack(fill=X)


sublabel2 = Label(win,text="Sub Label 2",bg="Yellow",fg="Black")
sublabel2.pack(side=LEFT,fill=Y)

Tframe = Frame(win)
Tframe.pack()
Bframe = Frame(win)
Bframe.pack(side=BOTTOM)

button1 = Button(Tframe,text="Button1",fg="Red")
button2 = Button(Tframe,text="Button2",fg="Yellow")
button3 = Button(Bframe,text="Button3",fg="Blue")
button4 = Button(Bframe,text="Button4",fg="Green")

button1.pack()
button2.pack()
button3.pack()
button4.pack()


win.mainloop()