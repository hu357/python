from tkinter import *

root = Tk()

GIRLS = ['西施','貂蝉','王昭君','杨玉环']

v = []

for girl in GIRLS:
    v.append(IntVar())#IntVar()用于存放每个按钮的状态,将它追加到列表里去
    b = Checkbutton(root,text=girl,variable = v[-1])#text=girl一次显示每一个名字
    #variable = v[-1]每一次都要拿它最后一个元素
    b.pack(anchor=W)#设置左对齐，上北N下南S左西W右东E

    
mainloop()
