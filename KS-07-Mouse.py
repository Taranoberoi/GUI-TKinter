from tkinter import *

win = Tk()


def left(event):
    print("Left Print")


def right(event):
    print("right print")



def middle(event):
    print("click print")



frame = Frame(win, width=200, height=200)
frame.bind("<Button-1>",left)
frame.bind("<Button-2>",right)
frame.bind("<Button-3>",middle)
frame.pack()

win.mainloop()
