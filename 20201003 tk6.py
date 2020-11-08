from tkinter import *
import hashlib

root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,"I love FishC.com!")

def getIndex(text,index):
    return tuple(map(int,str.split(text.index(index),".")))
    #转换为元组返回
    #index(index)返回基于给定索引的索引绝对值

start = "1.0"#从第一行第零列开始
while True:
    pos = text.search("o",start,stopindex=END)
    #查找字母o,stopindex设置停止位置
    if not pos:
        break#如果没有找到就跳出循环
    print ("找到啦，位置是:" + str(getIndex(text,pos)))
    start = pos + "+1c"
    #"+1c"指向下一个字符

mainloop()
#search的返回值是以"line.column"的索引形式返回
#再tuple一下，就转变成元组了
#map(int,['1','3'])就是把字符串['1','3']变成数字[1,3],注意这时候是一个列表的形式
#if 条件为假，就调用getIndex，传入"I love FishC.com!"和1.3
