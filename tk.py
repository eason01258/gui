import tkinter as tk


win = tk.Tk() #建立主視窗

#標題
win.title('test')
#大小
#win.geometry('400x200')  # 預設大小 寬X高
win.minsize(width = 800, height = 600) # 最小size
#win.maxsize(width = 1024, height = 768) # 最大size
# 拉伸大小
# win.resizable(False, False) #寬,高 鎖定
win.resizable(1, 1) # 1 = True 0 = False


#ICON 圖標
win.iconbitmap('./av8u8-pzeku-001.ico') #.ico

#顏色
win.config(bg='skyblue')

# 透明度
win.attributes('-alpha', 0.8) # 1~0 1= 100 %, 0 = 0%

# 置頂
win.attributes('-topmost', 1) # 1 = True 0 = False


img = tk.PhotoImage(file = './hema.png')

#function
def hi():
	print('hi')

#Button
btn = tk.Button()#text = '按我', bg = 'red')
#btn.config(width = 10, height = 5)
btn.config(image = img) #button 圖示
btn.config(command = hi) # button
btn.pack()




win.mainloop() # 常駐主視窗剛