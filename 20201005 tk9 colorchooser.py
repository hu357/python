# messagebox
# filedialog
# colorchooser
# 这三个模块在python2中是独立的，分别是tkMessageBox、tkFileDialog、tkColorChooser需导入才能使用
# python3中全部收归到tkinter模块下。

from tkinter import colorchooser
from tkinter import *

root = Tk()

def callback():
    filename = colorchooser.askcolor()
    print(filename)

Button(root,text="选择颜色",command=callback).pack()

mainloop()
