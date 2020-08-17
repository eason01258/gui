# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:16:04 2020

@author: 奕盛
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()  # 宣告變輛 var 為字串
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2)   # textvariable 文字變量
#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False # 設置全局變量
def hit_me():
    global on_hit # 變量傳至function
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)
b.pack()


window.mainloop()