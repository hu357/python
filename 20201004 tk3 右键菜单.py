from tkinter import *

root = Tk()

def callback():
    print("你好~")

menubar=Menu(root)
menubar.add_command(label="撤销",command=callback)
menubar.add_command(label="重做",command=root.quit)

frame=Frame(root,width=300,height=300)
frame.pack()

def popup(event):
    menubar.post(event.x_root,event.y_root)
    #只要有menubar.post，就会在指定位置弹出菜单

frame.bind("<Button-3>",popup)
#绑定鼠标右键，1是左键，2是中间键，3是右键
mainloop()
