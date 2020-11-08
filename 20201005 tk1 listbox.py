from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack(fill=BOTH,expand=True)#fill=BOTH填充副组件
#expand=True将副组件额外的空间填满(延长拉伸窗口)

for i in range(10):#初始化listbox
    listbox.insert(END,str(i))
    #用insert来添加，END添加到末尾，str(i)变成字符串添加进去

mainloop()
