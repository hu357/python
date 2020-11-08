from tkinter import *

root = Tk()

Scale(root,from_=0,to=42,tickinterval=5,resolution=5,length=200).pack()
#tickinterval设置显示刻度即每5就显示刻度，resolution控制步长也就是精度,默认步长是1
#length=200长度为200像素
Scale(root,from_=0,to=200,tickinterval=10,orient=HORIZONTAL,length=600).pack()
#tickinterval=10每间隔10就会显示一个数字
#length=600，这样才足够存放
mainloop()
