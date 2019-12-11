from tkinter import *

class Myclass:
    def __init__(self,win):
        frame = Frame(win)
        frame.pack()

        self.button = Button(frame, text="Click Me", command=self.printMsg)
        self.button.pack(side=LEFT)

        self.quit = Button(frame, text="QUIT", command=frame.quit)
        self.quit.pack(side=LEFT)


    def printMsg(self):
        print("It is working!!!!!!")


win = Tk()
win.geometry("400x400")
win.title("Claases for Tkinter")
b = Myclass(win)


win.mainloop()
