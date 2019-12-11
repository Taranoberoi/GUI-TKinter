from tkinter import *

def mul():
    print("\n")
    for i in range(1,11):
        m = int(number.get())
        print(i,"*",m,"=",(i*m))



win = Tk()

win.geometry("800x800")
win.title("Multiplication Table")

number = StringVar()
a = StringVar()
b = StringVar()
c = StringVar()

label = Label(win,text="Multiplication",font='20')
label.grid(row=5,column=10)

enter = Entry(win, textvariable=number,justify='center')
enter.grid(row=12,column=10)

button = Button(win,text="Enter the Table Value",command = mul)
button.grid(row=20,column=20)

QUIT = Button(win,text='QUIT',command = win.destroy)
QUIT.grid(row=25,column=25)


win.mainloop()