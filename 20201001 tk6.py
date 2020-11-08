from tkinter import *

root = Tk()

e = Entry(root)
e.pack(padx=20,pady=20)

e.delete(0,END)#将输入框中内容清空
e.insert(0,'默认文本...')#插入内容

mainloop()
