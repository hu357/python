from tkinter import *

root = Tk()

def callback():
    print ("正中靶心！")

Button(root,text="点我",command=callback).place(relx=0.5,rely=0.5,anchor=CENTER)
#relx=0.5,rely=0.5相对距离，相对副组件的位置(坐标)
#0.5表示正中间,1表示最右边,0表示最左边
#anchor=CENTER表示居中显示
mainloop()
