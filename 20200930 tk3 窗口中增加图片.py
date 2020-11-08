from tkinter import*#将tkinter这个模块所有东西都导入

root = Tk()#生成一个root窗口


textLabel = Label(root,
                  text='您所下载的影片含有未成年人限制内容，\n请在家长的陪同下观看！',
                  justify=LEFT,
                  padx=10)
#\n将所输入的文字换行输出
#justify=LEFT将输出文字左对齐
textLabel.pack(side= LEFT)


photo = PhotoImage(file = 'stop.gif')#实例化PhotoImage就可以得到图片对象
imgLabel = Label(root,image=photo)
imgLabel.pack()

mainloop()
