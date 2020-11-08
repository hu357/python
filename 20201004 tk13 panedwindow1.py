from tkinter import *


m = PanedWindow(orient=VERTICAL)
#默认为水平，这里的orient=VERTICAL设置为垂直
m.pack(fill=BOTH,expand=1)

top = Label(m,text="top pane")
m.add(top)#用add方式添加进去

bottom = Label(m,text="bottom pane")
m.add(bottom)

mainloop()
