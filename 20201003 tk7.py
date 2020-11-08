from tkinter import *
import hashlib

root = Tk()

text = Text(root,width=30,height=5,undo=True)
#undo=True开启了text组件的撤销功能
text.pack()

text.insert(INSERT,"I love FishC.com!")

def show():
    text.edit_undo()

Button(root,text="撤销",command=show).pack()

mainloop()
