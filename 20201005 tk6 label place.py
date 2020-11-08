from tkinter import *

root = Tk()

Label(root,bg="red").place(relx=0.5,rely=0.5,relheight=0.75,relwidth=0.75,anchor=CENTER)
#relheight=0.75,relwidth=0.75相对高度和相对宽度，都是相对于副组件
Label(root,bg="yellow").place(relx=0.5,rely=0.5,relheight=0.5,relwidth=0.5,anchor=CENTER)
Label(root,bg="green").place(relx=0.5,rely=0.5,relheight=0.25,relwidth=0.25,anchor=CENTER)

mainloop()
