from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text="button 1",fg="green")
button2 = Button(topFrame, text="button 2",fg="red")
button3 = Button(topFrame, text="button 3",fg="yellow")
button4 = Button(botFrame, text="button 4",fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()