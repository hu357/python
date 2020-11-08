#为了在组件上安装垂直滚动条，你需要做两件事
#1.设置该组件的yscrollbarcommand选项为Scrollbar组件的set()方法
#2.设置Scrollbar组件的command选项为该组件的yview()方法

from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side = RIGHT,fill=Y)#右边Y轴填充

lb = Listbox(root,yscrollcommand=sb.set)#yscrollcommand表示垂直#里边滚动会调用sb.set，同时修改滚动条的位置

for i in range(1000):
    lb.insert(END,i)

lb.pack(side=LEFT,fill=BOTH)

sb.config(command=lb.yview)#调用config方法来设置它某个选项的值

mainloop()
