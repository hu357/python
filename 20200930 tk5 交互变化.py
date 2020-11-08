from tkinter import*#将tkinter这个模块所有东西都导入

def callback():
    var.set('吹吧你，我才不信呢')

root = Tk()#生成一个root窗口

frame1 = Frame(root)
frame2 = Frame(root)


var = StringVar()#tkinter的字符串变量StringVar，实例化var,是一个StringVar变量
var.set('您所下载的影片含有未成年人限制内容，\n请在家长的陪同下观看！')#设置变量内容
textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
#\n将所输入的文字换行输出
#justify=LEFT将输出文字左对齐
textLabel.pack(side= LEFT)


photo = PhotoImage(file = 'stop.gif')#实例化PhotoImage就可以得到图片对象
imgLabel = Label(frame1,image=photo)
imgLabel.pack()

theButton = Button(frame2, text = '我已满18周岁', command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()
