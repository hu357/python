from tkinter import *

root = Tk()

text = Text(root,width=30,height=5,undo=True,autoseparators=False)
#autoseparators=False(因为这个选项是让Tkinter在认为一次完整的操作结束后自动插入"分隔符")
#然后绑定键盘事件,每次输入就用edit_separator()方法人为的插入一个"分隔符"
text.pack()

text.insert(INSERT,"I love FishC.com!")

def callback(event):
    text.edit_separator()

text.bind('<Key>',callback)#绑定Key事件

def show():
    text.edit_undo()

Button(root,text="撤销",command=show).pack()

mainloop()
