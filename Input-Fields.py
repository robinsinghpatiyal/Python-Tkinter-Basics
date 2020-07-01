# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:16:51 2020

@author: Robin Singh
"""

from tkinter import *
 
root = Tk()

e = Entry(root,width=50,borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name")#default text in the box

#Getting data from the input bar


def myClick():
    myLabel = Label(root, text =e.get())#gets the data and displays it
    myLabel.pack()

myButton = Button(root, text = "Enter you name",command=myClick)
myButton.pack()


root.mainloop()