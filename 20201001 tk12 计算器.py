from tkinter import *

master = Tk()

frame = Frame(master)
frame.pack(padx=10,pady=10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()#计算好的值

def test(content):
    return content.isdigit()
        
testCMD = master.register(test)
#register修饰符暗示编译程序相应的变量将被频繁地使用，如果可能的话，应将其保存在CPU的寄存器中，以加快其存储速度。这个关键字请求编译器尽可能的将变量存在CPU内部寄存器中以提高效率
e1 = Entry(frame,width=10,textvariable=v1,validate="key",validatecommand=(testCMD,"%P")).grid(row=0,column=0)
#P%相当于把你的输入传到函数的参数里
#validatecommand(f,s1,s2,...)f就是你‘冷却后’的验证函数，s1,s2,s3,这些是额外的选项，这些选项合作作为参数依次传给f函数
#使用隐藏技能冷却就是调用register()方法将验证函数包装起来
Label(frame,text='+').grid(row=0,column=1)

e2 = Entry(frame,width=10,textvariable=v2,validate="key",validatecommand=(testCMD,"%P")).grid(row=0,column=2)

Label(frame,text='=').grid(row=0,column=3)

e3 = Entry(frame,width=10,textvariable=v3,state='readonly').grid(row=0,column=4)#width=10可变字体的平均宽度乘以10个字符

def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))#v3.set值设为result

Button(frame,text='计算结果',command=calc).grid(row=1,column=2,pady=5)#设置按钮

mainloop()

