from tkinter import *

root = Tk()

w = Canvas(root,width=200,height=100,background="white")
#单位是像素
w.pack()

w.create_line(0,50,200,50,fill="yellow")#黄色横线
#这四个参数描述的是起点和终点的坐标
w.create_line(100,0,100,100,fill="red",dash=(4,4))
#dash=(4,4)设置虚线
w.create_rectangle(50,25,150,75,fill="blue")

mainloop()
