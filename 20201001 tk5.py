from tkinter import *

root = Tk()

group = LabelFrame(root,text='最好的脚本语言是?',padx=5,pady=5)#进行分组
group.pack(padx=10,pady=10)

LANGS = [
    ('Python',1),
    ('Perl',2),
    ('Ruby',3),
    ('Lua',4)]#将这四个放进一个框架里

v = IntVar()#多个按钮只需要一个变量

for lang,num in LANGS:
    b = Radiobutton(group,text=lang,variable=v,value=num)
    #indicatoron指示器（小圆点），indicatoron=False变成按钮形式
    b.pack(anchor=W)

mainloop()
