from tkinter import *


m1 = PanedWindow(showhandle=True,sashrelief=SUNKEN)
#showhandle显示手柄，sashrelief分割线样式，SUNKEN向下凹
m1.pack(fill=BOTH,expand=1)

left = Label(m1,text="left pane")
m1.add(left)

m2 = PanedWindow(orient=VERTICAL,showhandle=True,sashrelief=SUNKEN)
m1.add(m2)#加到右边，左边是Label，右边是PanedWindow

top = Label(m2,text="top pane")
m2.add(top)

bottom = Label(m2,text="bottom pane")
m2.add(bottom)

mainloop()
