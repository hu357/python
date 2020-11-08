from tkinter import *
import math as m

root = Tk()

w = Canvas(root,width=400,height=200)
w.pack() 

def paint(event):
    x1,y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2,fill="red")#用小圆点来表示

w.bind("<B1-Motion>",paint)
#绑定<B1-Motion>，表示绑定鼠标左键，绑定paint方法

Label(root,text="按住鼠标左键并移动，开始绘制你的理想蓝图吧......").pack(side=BOTTOM)

mainloop()
##以左上角为坐标原点，以右为X正方向，以下为Y正方向