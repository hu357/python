import tkinter as tk

class APP:
    def __init__(self,master):
        frame = tk.Frame(master)#
        frame.pack(side=tk.LEFT,padx=10,pady=10)#调整位置,padx.pady是间距


        self.hi_there = tk.Button(frame,text='打招呼',bg='black',fg = 'white',command=self.say_hi)#设置按钮
        self.hi_there.pack()

    def say_hi(self):
        print('互联网的朋友们大家好，我是小甲鱼!')

root = tk.Tk()#创建一个顶层窗口
app = APP(root)#实例化APP,将root作为参数

root.mainloop()#进入主事件循环
