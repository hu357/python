from tkinter import *
import math as m

root = Tk()

w = Canvas(root,width=200,height=100)
w.pack()

center_x=100
center_y=50
r=50

point = [
    # 左上点
    center_x - int(r*m.sin(2*m.pi/5)),
    center_y - int(r*m.cos(2*m.pi/5)),
    # 右上点
    center_x + int(r*m.sin(2*m.pi/5)),
    center_y - int(r*m.cos(2*m.pi/5)),
    # 左下角
    center_x - int(r*m.sin(m.pi/5)),
    center_y + int(r*m.cos(m.pi/5)),
    # 顶点
    center_x,
    center_y -r,
    # 右下点
    center_x + int(r*m.sin(m.pi/5)),
    center_y + int(r*m.cos(m.pi/5)),
    
    ]

w.create_polygon(point,outline="green",fill="yellow")
#不设置fill="yellow"，默认为黑色填充，设置为空字符串时是透明颜色
mainloop()



