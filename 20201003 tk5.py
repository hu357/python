from tkinter import *
import hashlib#获得md5

root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,"I love FishC.com!")
contents = text.get("1.0",END)#获得全部内容

def getSig(contents):
    m = hashlib.md5(contents.encode())#进行编码，编成二进制,获得md5的值
    return m.digest()#调用digest方法获得摘要

sig = getSig(contents)

def check():
    contents = text.get("1.0",END)#重新获得contents内容
    if sig != getSig(contents):
        print("警报：内容发生变动！")
    else:
        print("风平浪静~")

Button(root,text="检查",command=check).pack()


mainloop()
