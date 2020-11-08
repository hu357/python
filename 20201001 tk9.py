from tkinter import *

master = Tk()

def test():
    if e1.get() == '小甲鱼':
        print('正确')
        return True
    else:
        print('错误')
        e1.delete(0,END)#清空输入框
        return False

v = StringVar()

e1 = Entry(master,textvariable=v,validate='focusout',validatecommand=test)
#validate='focusout'当焦点移出时会调用test
#Entry组件是支持验证输入内容的合法性的，比如要求输入数字，你输入了字母那就是非法，实现该功能，需要通过设置
#validate,validatecommand,invalidcommand选项
#首先启用验证的‘开关’是validate选项，该选项的设置的值有
#值            含义
#'focus'        当Entry组件获得或失去焦点的时候验证
#'focusin'      当Entry组件获得焦点的时候验证
#'focusout'     当Entry组件失去焦点的时候验证
#'key'          当输入框被编辑的时候验证
#'all'          当出现上边任何一种情况的时候验证
#'none'         1.关闭验证功能
#               2.默认设置该选项(即不启用验证)
#               3.注意，是字符串的'none',而非None

#其次是validatecommand选项指定一个验证函数，该函数只能返回True或False表示验证的结果，一般情况下验证函数只需要知道输入框的内容即可，可以通过Entry()组件的get()方法获得该字符串
e2 = Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)

mainloop()
