from tkinter import *

root = Tk()

one = Label(root,text="tata",bg="blue",fg="white")
one.pack()
two = Label(root,text="teteeee",bg="red",fg="white")
#fill=X fa que el complement es faci tan gran com el pare
two.pack(fill=X)
three = Label(root,text="papapapa",bg="yellow",fg="white")
#fill=Y fa que el complement es faci tan gran com el pare
three.pack(side=LEFT,fill=Y)
root.mainloop()