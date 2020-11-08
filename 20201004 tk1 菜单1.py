from tkinter import *

root = Tk()

def callback():
    print("你好~")

menubar=Menu(root)
menubar.add_command(label="hello",command=callback)
#add_command添加内容
menubar.add_command(label="quit",command=root.quit)

root.config(menu=menubar)
#将menu选项跟我们创建好的菜单进行关联
#关联的话用config来设置选项的内容
#menubar就会添加入root窗口

mainloop()
