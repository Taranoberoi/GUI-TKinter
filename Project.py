### This Project capture things Like Font in label
### Capture Data in Entry Field and call the function using command


from tkinter import *

def myclick():
    #value = ent.get() another way of getting value in variable
    mylabel = Label(win,text= ent.get())
    mylabel.grid()


win = Tk()
win.title("Vin Search")
win.geometry("900x900")


label = Label(win,text= "Vin Search Box", font =("courier",'20'))
label.grid(row=8,column=8)

ent = Entry(win,width=25)
ent.grid(row=40,column=10)
ent.insert(0,"Please Enter the Vin") # insert just by default enter the valye in Entry box


button = Button(win,text="Click the button",command=myclick)
button.grid()


win.mainloop()
