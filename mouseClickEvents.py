from tkinter import *

root = Tk()

def printLeftClick(event):
    print("Left Click")

def printMidleClick(event):
    print("Middle Click")

def printRightClick(event):
    print("Right Click")


frame = Frame(root,width=300,height=250)
frame.bind("<Button-1>",printLeftClick)
frame.bind("<Button-2>",printMidleClick)
frame.bind("<Button-3>",printRightClick)

frame.pack()


root.mainloop()