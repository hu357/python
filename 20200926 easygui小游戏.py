import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎进入第一个界面小游戏^_^')

    msg = '请问你知道椰子吗?'
    title = '椰子家人'
    choices = {'老皮','老肥','碎崽儿'}

    choice = g.choicebox(msg,title,choices)

    #note that we convert choice to string,in case
    #the user cancelled the choice,and we got None.
    g.msgbox('你的选择是:' + str(choice), '结果')

    msg = '你希望重新开始吗？'
    title = '请选择'

    if g.ccbox(msg,title): #show s Continue/Cancel dialog
        pass #user chose Continue
    else:
        sys.exit(0)#user chose Cancel

    
