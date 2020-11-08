from tkinter import *

root = Tk()

def callback(event):
    print(event.keysym) #event.char
     #char属性就是当前按下的字符

frame = Frame(root,width=200,height=200)
frame.bind("<KeyPress>",callback)
#组件必须获得焦点才会响应键盘来的消息
frame.focus_set()#获得焦点
frame.pack()

mainloop()
