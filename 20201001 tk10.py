from tkinter import *

root = Tk()

def test():
    if e1.get() == '小甲鱼':
        print('正确')
        return True
    else:
        print('错误')
        e1.delete(0,END)#清空输入框
        return False

def test2():
    print('我被调用了......')
    return True

v = StringVar()

e1 = Entry(root,textvariable=v,validate='focusout',validatecommand=test,invalidcommand=test2)
#validate='focusout'当焦点移出时会调用test
#invalidcommand选项指定的函数只有在validatecommand的返回值为False的时候才能被调用
e2 = Entry(root)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)

mainloop()
