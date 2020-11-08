from tkinter import *

root = Tk()

photo = PhotoImage(file='bg.gif')
theLabel = Label(root,
                 text = '学Python\n到 FishC',
                 justify=LEFT,#左对齐
                 image=photo,
                 compound=CENTER,
                 font=('隶书',20),
                 fg='black')

theLabel.pack()

mainloop()
