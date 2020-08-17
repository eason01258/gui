# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:38:46 2020

@author: 奕盛
"""
import tkinter as tk




win = tk.Tk()

win.geometry("400x400+800+300")



def change(self):
    s_value = s.get() # 讀取拉桿的value
    win.attributes("-alpha", s_value/100) # 設置視窗透明度
    
    
    
    
# 方向, 寬度, 長度
s = tk.Scale (orient='horizontal',length=600, width = 200)  # 
# 設置範圍 mini 10 ~ max 100
s.config(from_=10, to=100)
# 顯示value, 間隔刻度, 解析度, 設置顯示位數
s.config(showvalue=1, tickinterval=10, resolution=10, digits=1)
# Label
s.config(label="Tkinter Slider")
# 直接設置初始值
s.set(50)

s.config(command=change)
s.pack()




win.mainloop()
