from tkinter import *

root = Tk()

username = Label(root, text="Username")
password = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

username.grid(row=0,column=0,sticky=E)
password.grid(row=1,column=0,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

btn = Button(root,text="Login")
btn.grid(columnspan=2)
root.mainloop()