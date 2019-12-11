###Frames with Radio Buttons###

from tkinter import *

win = Tk()

label = Label(win,text = "MY First GUI")
label.pack()
win.title("CHECK THIS OUT")
topfram = Frame(win)
topfram.pack()
bottomfram = Frame(win)
bottomfram.pack(side=BOTTOM)

button1 = Button(topfram,text="TopFrame Input",fg="Green")
button2 = Button(topfram,text="TopFrame Input",fg="red")
button3 = Button(topfram,text="TopFrame Input",fg="Blue")
button4 = Button(bottomfram,text="Bottom Frame Input",fg="Yellow")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
button4.pack(side=BOTTOM)

win.mainloop()
