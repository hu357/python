from tkinter import *

root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.tag_config("tag1",background="yellow",foreground="red")
text.tag_config("tag2",foreground="blue")
#相当于tag2在tag1之前，tag1覆盖tag2

text.tag_lower("tag2")#降低优先级

text.insert(INSERT,"I love FishC.com",("tag2","tag1"))

mainloop()
