from tkinter import *

def func():
    print("yes its working")



def resize():
    print("yes its working resize")
    win.geometry("1000x1000")


def default():
    print("yes its working default")
    win.geometry("600x600")



win = Tk()
win.geometry("600x600")
menu = Menu(win)
## to configure menu in window
win.config(menu=menu)
subMenu = Menu(menu)

menu.add_cascade(label="Family", menu=subMenu)
subMenu.add_command(label="Daddy", command=func)
subMenu.add_command(label="Mommy", command=func)
subMenu.add_command(label="Son", command=func)
subMenu.add_command(label="Resize", command=resize)
subMenu.add_command(label="default", command=default)
subMenu.add_command(label="EXit", command=quit)

## add another menu like File

editMenu = Menu(menu)
menu.add_cascade(label="COUNTRY", menu=subMenu)
subMenu.add_command(label="US", command = func)
subMenu.add_command(label="INDIA", command = func)


win.mainloop()