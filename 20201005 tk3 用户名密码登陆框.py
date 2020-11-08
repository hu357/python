from tkinter import *

root = Tk()

Label(root,text="用户名").grid(row=0,sticky=W)#row=0行为0
Label(root,text="密码").grid(row=1,sticky=W)#sticky=W左对齐,默认居中

Entry(root).grid(row=0,column=1)#输入用户名
Entry(root,show="*").grid(row=1,column=1)#输入密码

mainloop()
