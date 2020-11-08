from tkinter import *
import webbrowser

root = Tk()

text = Text(root,width=30,height=5)
text.pack()


text.insert(INSERT,"I love FishC.com")

text.tag_add("link","1.7","1.16")
text.tag_config("link",foreground="blue",underline=True)
#underline=True设置下划线在1.7到1.16

def show_arrow_cursor(event):
    text.config(cursor="arrow")

def show_xterm_cursor(event):
    text.config(cursor="xterm")

def click(event):
    webbrowser.open("http://www.fishc.com")
    #webbrowser用于打开网页的一个成熟的模块

text.tag_bind("link","<Enter>",show_arrow_cursor)
#tag_bind绑定事件，<Enter>为当鼠标进入的意思
text.tag_bind("link","<Leave>",show_xterm_cursor)
#<Leave>为当鼠标离开的意思
text.tag_bind("link","<Button-1>",click)
#<Button-1>表示左键点击

mainloop()
