# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 23:19:23 2020

@author: 奕盛
"""

import tkinter as tk
import random
# 處理複製功能
import pyperclip

win = tk.Tk()
win.title('Random X,Y Generator')
#win.geometry(長X寬+x+y)
win.geometry('400x300+500+200')
win.config(bg='#323232')


title_text = tk.Label(text='Random X,Y Generator',fg = 'skyblue', bg = '#323232')
#obj.config(fort='字型 大小')
title_text.config(font='微軟正黑體 15')
title_text.pack()


# 最小值 文字 與 輸入框
min_range = tk.Label(text="Min range", fg="white", bg="#323232")
min_range.pack()
min_entry = tk.Entry()
min_entry.pack()


# 最大值 文字 與 輸入框
max_range = tk.Label(text="Max range", fg="white", bg="#323232")
max_range.pack()
max_entry = tk.Entry()
max_entry.pack()



# 顯示 X,Y 座標
x_show = tk.Label(text="", fg="white", bg="#323232")
x_show.pack()
y_show = tk.Label(text="", fg="white", bg="#323232")
y_show.pack()


def gen_xy ():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    # random.randint(最小值, 最大值)
    x = str(random.randint(min_val, max_val))
    y = str(random.randint(min_val, max_val))
    x_show.config(text="X: " + x)
    y_show.config(text="Y: " + y)

def copy ():
    xy = x_show.cget("text") + "\n" + y_show.cget("text")
    pyperclip.copy(xy)
  
# 生成及複製按鈕
generate_btn = tk.Button(text="Generate", command= gen_xy)
generate_btn.pack()
copy_btn = tk.Button(text="Copy", command= copy)
copy_btn.pack()


win.mainloop()


