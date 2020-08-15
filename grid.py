# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 23:27:29 2020

@author: 奕盛
"""

import tkinter as tk

win = tk.Tk()

win.title('')
win.geometry('')


# Grid 網格佈局
user = tk.Label(text='User')
user.grid(row=0,column=0)


password = tk.Label(text='Password')
password.grid(row = 1, column = 0)


user_entry = tk.Entry(bg='#323232',font='微軟正黑體 20') # font = ''
user_entry.grid(row = 0, column = 1,rowspan=2) #rowspan 跨行


#password_entry = tk.Entry(bg='#323232')
#password_entry.grid(row = 1, column = 1,columnspan=2)  columnspan 跨列


win.mainloop()





'''
       column0  column1
  row0   00       01
  row1   10       11

'''