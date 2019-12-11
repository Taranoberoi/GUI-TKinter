from tkinter import *

# function for button
def funct():
    print("Look I got clicked")


root = Tk()
root.title("First Programme")
root.geometry("800x800")

# Label inside the windows

label = Label(root,text="Check this out").grid(row=1,column=2)
label2 = Label(root,text="Check this second statement").grid(row=1,column=5)
ent = Entry(root,text="Enter the string value",bg="yellow",fg="black",width=50).grid(row=3,column=5)
# padx and pady button will resize he Button
button = Button(root,text="Click Me",pady=170, command = funct).grid(row=8,column=5)

root.mainloop()
