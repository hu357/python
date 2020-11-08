from tkinter import *

OPTIONS = [
    "California",
    "458",
    "FF",
    "ENZO",
    "LaFerrari"
    ]

root = Tk()

variable = StringVar()
variable.set(OPTIONS[0])
#把第一个设置为默认值
w = OptionMenu(root,variable,*OPTIONS)
#*OPTIONS自动将列表拆开
w.pack()

mainloop()
