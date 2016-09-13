from tkinter import *

root = Tk()

def printName(event):
    print("Hallo im now learning python 3")
#2 maneres de associar una funcio a un widget
#button_1 = Button(root,text="Print my name", command=printName)
button_1 = Button(root,text="Print my name", command=printName)
button_1.bind("<Button-1>",printName)
button_1.pack()



root.mainloop()