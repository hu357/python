# messagebox
# filedialog
# colorchooser
# 这三个模块在python2中是独立的，分别是tkMessageBox、tkFileDialog、tkColorChooser需导入才能使用
# python3中全部收归到tkinter模块下。

from tkinter import messagebox
from tkinter import *

print(messagebox.askokcancel("FishC Demo","发射核弹"))

mainloop()
