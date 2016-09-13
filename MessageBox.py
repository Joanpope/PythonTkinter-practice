from tkinter import *
import tkinter.messagebox

root = Tk()
# *** alert window ****
tkinter.messagebox.showinfo('Window Title', 'Monkey Business')

# **** confirm window ****

answer = tkinter.messagebox.askquestion('Question 1','Do you like Monkey Business?')

if answer == 'yes':
    print('monkeeeeeys ruleeeee!!!')
elif answer == 'no':
    print('monkeys dont rule :(')


root.mainloop()
