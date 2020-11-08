from tkinter import *

root = Tk()

LANGS = [
    ('Python',1),
    ('Perl',2),
    ('Ruby',3),
    ('Lua',4)]

v = IntVar()#多个按钮只需要一个变量
v.set(1)

for lang,num in LANGS:
    b = Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)
    #indicatoron指示器（小圆点），indicatoron=False变成按钮形式
    b.pack(fill=X)#fill=X表示横向填充,Y表示纵向


mainloop()
