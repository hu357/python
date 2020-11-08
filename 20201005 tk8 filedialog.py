# messagebox
# filedialog
# colorchooser
# 这三个模块在python2中是独立的，分别是tkMessageBox、tkFileDialog、tkColorChooser需导入才能使用
# python3中全部收归到tkinter模块下。

from tkinter import filedialog
from tkinter import *

root = Tk()

def callback():
    fileName =filedialog.askopenfilename(filetypes=[("PNG",".png"),("GIF",".gif"),("JPG",".jpg"),("Python",".py")])    # defaultextension=".py",可以不用加后缀搜索
    print(fileName)

Button(root,text="打开文件",command=callback).pack()

mainloop()
