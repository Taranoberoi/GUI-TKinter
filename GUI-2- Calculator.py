from tkinter import *

def button_click(number):
    current = data.get()
    data.delete(0,END)
    data.insert(0,str(current)+str(number))

def button_clear():
    data.delete(0,END)

def button_equal():
    Sec_num = data.get()
    data.delete(0,END)
    if math == "addition":
        data.insert(0,Val+int(Sec_num))
    if math== "subtraction":
        data.insert(0,Val - int(Sec_num))
    if math== "division":
        data.insert(0,Val / int(Sec_num))
    if math == "multiply":
        data.insert(0,Val * int(Sec_num))

def button_add():
    first_num = data.get()
    global Val
    global math
    math = "addition"
    Val = int(first_num)
    data.delete(0,END)

def button_Div():
    first_num = data.get()
    global Val
    global math
    math = "division"
    Val = int(first_num)
    data.delete(0,END)

def button_Mul():
    first_num = data.get()
    global Val
    global math
    math = "multiply"
    Val = int(first_num)
    data.delete(0,END)

def button_sub():
    first_num = data.get()
    global Val
    global math
    math = "subtraction"
    Val = int(first_num)
    data.delete(0,END)

win = Tk()
frame = Frame(win)
frame.grid()
win.title("Calculator")
win.geometry("400x400")


data= Entry(win,text="",width=48,borderwidth=5)
data.grid(row=0,column=0,columnspan=3,ipady=8)


button1 = Button(win,text="1",padx=40,pady=10,command=lambda: button_click(1))
button2 = Button(win,text="2",padx=40,pady=10,command=lambda: button_click(2))
button3 = Button(win,text="3",padx=40,pady=10,command=lambda: button_click(3))
button4 = Button(win,text="4",padx=40,pady=10,command=lambda: button_click(4))
button5 = Button(win,text="5",padx=40,pady=10,command=lambda: button_click(5))
button6 = Button(win,text="6",padx=40,pady=10,command=lambda: button_click(6))
button7 = Button(win,text="7",padx=40,pady=10,command=lambda: button_click(7))
button8 = Button(win,text="8",padx=40,pady=10,command=lambda: button_click(8))
button9 = Button(win,text="9",padx=40,pady=10,command=lambda: button_click(9))
button0 = Button(win,text="0",padx=40,pady=10,command=lambda: button_click(0))
button_add = Button(win,text="+",padx=40,pady=10,command=button_add)
button_sub = Button(win,text="-",padx=40,pady=10,command=button_sub)
button_equal = Button(win,text="=",padx=40,pady=10,command=button_equal)
button_Mul = Button(win,text="*",padx=40,pady=10,command=button_Mul)
button_Div = Button(win,text="/",padx=40,pady=10,command=button_Div)
button_clear = Button(win,text="Clear",padx=130,pady=30,borderwidth=3,command=button_clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=1)
button_add.grid(row=4,column=0)
button_sub.grid(row=4,column=2)

button_equal.grid(row=5,column=1)
button_Mul.grid(row=5,column=2)
button_Div.grid(row=5,column=0)

button_clear.grid(row=6,column=0,columnspan=3)


win.mainloop()
