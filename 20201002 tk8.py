from tkinter import *

root = Tk()

text = Text(root,width=30,height=5)#height改为5行
text.pack()

text.insert(INSERT,"I love \n")
text.insert(END,"FishC.com!")

def show():
    print("呦，我被点了一下~")

b1 = Button(text,text="点我点我",command=show)#被点下的时候触发show的函数
text.window_create(INSERT,window=b1)#window_create表示window窗口组件
#window=b1表示按钮的实例

mainloop()
