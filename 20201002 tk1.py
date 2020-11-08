from tkinter import *

master = Tk()

theLB = Listbox(master,selectmode=EXTENDED)
theLB.pack()

for item in ['鸡蛋','鸭蛋','鹅蛋','李狗蛋']:
    theLB.insert(END,item)#END,是变量，表示每一项的最后，插入鸡蛋变成1...

#theLB.delete(0,END)#第一个数是起始位置，第二个数是结束位置
theButton = Button(master,text='删除它',command=lambda x=theLB:x.delete(ACTIVE))
#ACTIVE表示当前选中的值
theButton.pack()
mainloop()
