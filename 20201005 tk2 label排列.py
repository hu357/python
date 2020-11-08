from tkinter import *

root = Tk()

Label(root,text="red",bg="red",fg="white").pack(fill=X)#横向填充
#bg="red"背景颜色,fg="white"字体颜色
Label(root,text="green",bg="green",fg="black").pack(fill=X)#横向填充
Label(root,text="blue",bg="blue",fg="white").pack(fill=X)#横向填充

Label(root,text="red",bg="red",fg="white").pack(side=LEFT)#横向排列
Label(root,text="green",bg="green",fg="black").pack(side=LEFT)
Label(root,text="blue",bg="blue",fg="white").pack(side=LEFT)

mainloop()
