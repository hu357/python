from tkinter import *

root = Tk()

def callback():
    print("你好~")

menubar=Menu(root)

filemenu = Menu(menubar,tearoff=True)
#tearoff除了虚线外，点击虚线可以分出第二个窗口
filemenu.add_command(label="打开",command=callback)

filemenu.add_command(label="保存",command=callback)
filemenu.add_separator()
#分割线
filemenu.add_command(label="退出",command=root.quit)
menubar.add_cascade(label="文件",menu=filemenu)
#menu=filemenu关联下一级菜单
editmenu = Menu(menubar,tearoff=False)#编辑
editmenu.add_command(label="剪切",command=callback)
editmenu.add_command(label="拷贝",command=callback)
editmenu.add_command(label="粘贴",command=callback)
menubar.add_cascade(label="编辑",menu=editmenu)


root.config(menu=menubar)


mainloop()
