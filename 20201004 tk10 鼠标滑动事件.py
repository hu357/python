from tkinter import *

root = Tk()

def callback(event):
    print("当前位置: "  ,event.x,event.y)

frame = Frame(root,width=200,height=200)
frame.bind("<Motion>",callback)
#当鼠标进入组件时，就会无时无刻的响应，不用点击
frame.pack()

mainloop()
