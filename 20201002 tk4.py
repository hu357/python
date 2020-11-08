#创建一个指定范围的Scale组件其实非常容易，你只需指定它的from和to两个选项即可
#但由于from本身是Python的关键字，所以为了区分需要在后边紧跟一个下划线:from_
from tkinter import *

root = Tk()

Scale(root,from_=0,to=42).pack()#垂直
Scale(root,from_=0,to=200,orient=HORIZONTAL).pack()#orient=HORIZONTAL设置为水平



mainloop()
