from tkinter import *

master = Tk()

v = StringVar()

def test(content,reason,name):#有三个参数
    if content=="小甲鱼":
        print ("正确！")
        print(content,reason,name)
        return True
    else:
        print ("错误！")
        print(content,reason,name)
        return False

testCMD = master.register(test)


e1 = Entry(master,textvariable=v,validate="focusout",validatecommand=(testCMD,"%P","%v","%W"))
#validatecommand(f,s1,s2,...)f就是你‘冷却后’的验证函数，s1,s2,s3,这些是额外的选项，这些选项合作作为参数依次传给f函数
#使用隐藏技能冷却就是调用register()方法将验证函数包装起来
e2 = Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)

mainloop()
