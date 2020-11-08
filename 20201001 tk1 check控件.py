from tkinter import *

root = Tk()#先创建root窗口，根窗口

v = IntVar()#用tk变量表示按钮是否被选中，作为一个反馈

c = Checkbutton(root,text = '测试一下',variable = v)#variable = v用于表示按钮的状态是否被按下
c.pack()

l = Label(root,textvariable=v)#v是用来存放Checkbutton的选中状态
#选中为1，未选中为0
l.pack()

mainloop()
