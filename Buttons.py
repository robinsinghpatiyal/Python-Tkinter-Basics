# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:16:51 2020

@author: Robin Singh
"""

from tkinter import *
 
root = Tk()

def myClick():
    myLabel = Label(root, text = " Just Clilcked a Button!")
    myLabel.pack()

myButton = Button(root, text = "Click Me!",command=myClick)
myButton.pack()


root.mainloop()