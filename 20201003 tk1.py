from tkinter import *

root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,"I love FishC.com")#插入文本

text.tag_add("tag1","1.7","1.12","1.14")
#1.7第一行第八列(行从1开始，列从0开始),到第一行13列，最后单独的第一行15列
#最后一个没有配对就是单独标记
#text.tag_add("tag2","1.7","1.12","1.14")
text.tag_config("tag1",background="yellow",foreground="red")
#tag_config()设置Tags样式,foreground字体颜色
#text.tag_config("tag2",foreground="blue")

mainloop()
