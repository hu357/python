from tkinter import *

root = Tk()

v = IntVar()#多个按钮只需要一个变量

Radiobutton(root,text='One',variable=v,value=1).pack(anchor=W)
Radiobutton(root,text='Two',variable=v,value=2).pack(anchor=W)
Radiobutton(root,text='Three',variable=v,value=3).pack(anchor=W)

mainloop()
