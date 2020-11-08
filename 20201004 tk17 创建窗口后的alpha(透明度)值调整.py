from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    top.attributes("-alpha",0.5)#attributes设置属性，alpha设置透明度
    #在选项前添加横杠(-)并用字符串的方式表示，用逗号(,)隔开选项和值
    top.title("FishC Demo")

    msg = Message(top,text="I love FishC.com")
    msg.pack()

Button(root,text="创建顶级窗口",command=create).pack()

mainloop()
