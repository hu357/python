#Label 在界面上输出描述性的标签
import tkinter as tk

app = tk.Tk()#Tk()类生成了一个顶层窗口的实例，top level级别的窗口（root窗口）实例化Tk,容纳GUI程序
app.title('Fishc Demo')#设置标题栏

theLabel = tk.Label(app,text = '我的第二个窗口程序')#显示文本，也可显示图标，图片
theLabel.pack()#用于自动调节组件自身的尺寸以及位置

app.mainloop()#主事件循环
