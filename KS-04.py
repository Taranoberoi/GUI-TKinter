from tkinter import *


# def fun():
#     print("Welcome to Fun World")
#
#
#
# win = Tk()
# win.geometry("800x800")
# win.title("Vin Search")
#
# Vin = Label(win,text="Enter the Vin")
# entry_Vin = Entry(win)
# Submit1 = Button(win,text = "Submit",command = fun)
#
#
# Vin.grid(row=0,column=8)
# entry_Vin.grid(row=0,column=9)
# Submit1.grid(row=8,column=10)
#
# win.mainloop()

### using bind

def fun(event):
    print("Welcome to Fun World")



win = Tk()
win.geometry("800x800")
win.title("Vin Search")

Vin = Label(win,text="Enter the Vin")
entry_Vin = Entry(win)
Submit1 = Button(win,text = "Submit")
Submit1.bind("<Button-1>",fun)



Vin.grid(row=0,column=8)
entry_Vin.grid(row=0,column=9)
Submit1.grid(row=8,column=10)

win.mainloop()
