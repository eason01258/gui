# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:54:33 2020

@author: 奕盛
"""

import tkinter as tk


win = tk.Tk()
win.title('')

win.geometry('200x200+800+400')

# Pack 佈局 

# btn = tk.Button(text="Button")
# btn.pack(side='top')


# btn = tk.Button(text="Button")
# btn.pack(side='left')


# btn = tk.Button(text="Button")
# btn.pack(side='bottom')


# btn = tk.Button(text="Button")
# btn.pack(side='right')





# place 佈局

btn = tk.Button(text="Button")
btn.place(anchor = 'center' ,x= 100, y =100 ,width=100, height=50)  #anchor n, ne, e, se, s, sw, w, nw, or center



# grid 佈局

btn = tk.Button(text = 'Button')
btn.grid(row = 0, column = 0)



# pack() 跟 grid() 不能同時存在
# place() 可以與兩者兼容

win.mainloop()