from tkinter import *

root = Tk()

variable = StringVar()
variable.set("one")
#设置选项的默认值
w = OptionMenu(root,variable,"one","two","three")
w.pack()

mainloop()
