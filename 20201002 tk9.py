from tkinter import *

root = Tk()

text = Text(root,width=30,height=30)
text.pack()

photo = PhotoImage(file="bg.gif")

def show():
    text.image_create(END,image=photo)
    #操作图片image_create,image=photo表示图片的实例等于photo

b1 = Button(text,text="点我点我",command=show)
text.window_create(INSERT,window=b1)

mainloop()
