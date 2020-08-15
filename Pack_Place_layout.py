# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:54:33 2020

@author: 奕盛
"""

import tkinter as tk


win = tk.Tk()

win.geometry('200x200+800+400')

#

btn = tk.Button(text="Button")
btn.place(anchor = 'center' ,x= 100, y =100 ,width=100, height=50)



win.mainloop()