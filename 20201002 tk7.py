from tkinter import *

root = Tk()

text = Text(root,width=30,height=2)
#width=30是30个字符的平均宽度，height=2有2行
text.pack()

text.insert(INSERT,"I love \n")#插入数据，INSERT表示输入光标所在的位置（左上角）
text.insert(END,"FishC.com!")#插入数据,END最末尾插入

mainloop()
#可进行随意的编辑
