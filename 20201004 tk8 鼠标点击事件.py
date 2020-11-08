from tkinter import *

root = Tk()

def callback(event):#形参来获取对应的事件描述
    print("点击位置:" + str(event.x) + "," + str(event.y))
    #event.x，event.y表示相对于应用程序左上角的位置

frame = Frame(root,width=200,height=200)
#创建框架，在框架里响应事件
frame.bind("<Button-1>",callback)
#绑定鼠标右键,为callback方法
frame.pack()

mainloop()
