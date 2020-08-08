# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:26:01 2020

@author: 奕盛
"""

import tkinter as tk
win = tk.Tk()
win.geometry('400x200') 
win.config(bg = '#323232')



def get_():
    t = en.get() # 取的en的值
    lb.config(text = t)

# 標籤值
lb = tk.Label(bg='#323232',fg='white',text='This is lable') 
lb.pack()


# 輸入值類似input
en = tk.Entry()
en.pack()


btn = tk.Button(text = 'OK',command = get_) # command 點選button執行get_函式
btn.pack()




win.mainloop()
