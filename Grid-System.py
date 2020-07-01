# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:16:51 2020

@author: Robin Singh
"""

from tkinter import *

root = Tk()


# Creating a Label Widget
myLabel1 = Label(root,text="Hello World!")
myLabel2 = Label(root,text="My Name is Robin Singh")

#Showing it on the screen



myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)


root.mainloop()