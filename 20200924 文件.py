文件
Ctrl + s#保存到磁盘
什么是文件
.exe可执行文件
.txt
.ppt
.jpg图片格式
.mp4视频格式
.avi视频格式
文件打开模式
打开模式                执行操作
   'r'          以只读方式打开文件（默认）
   'w'          以写入的方式打开文件，会覆盖已存在的文件
   'x'          如果文件已经存在，使用此模式打开将引发异常
   'a'          以写入模式打开，如果文件存在，则在末尾追加写入
   'rb'         以二进制模式打开文件
   't'          以文本模式打开（默认）
   '+'          可读写模式（可添加到其他模式中使用）
   'U'          通用换行符支持
   
文件对象方法
文件对象方法                              执行操作
f.close()                       关闭文件
f.read([size=-1])	            从文件读取size个字符，当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回
f.readline([size=-1])	        从文件中读取并返回一行（包括行结束符），如果有size有定义则返回size个字符
f.write(str)	                将字符串str写入文件
f.writelines(seq)	            向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
f.seek(offset, from)	        在文件中移动文件指针，从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
f.tell()	                    返回当前在文件中的位置
f.truncate([size=file.tell()])	截取文件到size个字节，默认是截取到文件指针当前位置

#报错的，关闭文件重新打开，可能此时指针已经指向文件末尾了
#提醒一下：list()是从文件指针位置开始到末尾的，不是输出整个文档内容！
>>> f = open('E:\\record.txt')
>>> f.read()
'wuioqhgvbvbjkashflIVNUZXYSYEWTQYUQGDdgyaegdaikv'
>>> f
<_io.TextIOWrapper name='E:\\record.txt' mode='r' encoding='cp936'>
>>> f.close()
>>> f = open('E:\\record.txt')
>>> f.read(5)#读出前5个字符
'wuioq'
>>> f.tell()#当前文件指针的位置
5#一个中文字符占2个字节
#encoding=utf-8一个中文字符占3个字节
>>> f.seek(15,0)
15
>>> f.readline()#从第15个字节开始读取一行
'hflIVNUZXYSYEWTQYUQGDdgyaegdaikv'

>>> f.seek(0,0)#重新定位指针
0
>>> for each_line in f:#以行输出
	print(each_line)

	
wuioqhgvbvbjkashflIVNUZXYSYEWTQYUQGDdgyaegdaikv


>>> f = open('E:\\test.txt','w')
>>> f.write('我爱鱼C工作室')
7
>>> f.close()


一个任务
任务：将文件(record.txt)中的数据进行分割并按照以下和规律保存起来:
-小甲鱼的对话单独保存为boy_*.txt的文件(去掉"小甲鱼:")
-小客服的对话单独保存为girl_*.txt的文件(去掉"小客服:")
-文件中总共有三段对话，分别保存为boy_1.txt,girl_1.txt,boy_2.txt,girl_2.txt,boy_3.txt,girl_3.txt共6个文件
（提示：文件中不同的对话间已经使用"=========="分割）


f = open('record.txt',encoding='utf-8')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        (role,line_spoken) = each_line.split(':',1)
        #这里的split第二个参数1的意思是分割一次，返回两段字符串的意思
        #我们这里进行字符串分割
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_sopken)
    else:
        #文件的分别保存操作
        file_name_boy = 'boy_' +str(count) + '.txt'
        file_name_girl = 'girl_' +str(count) + '.txt'

        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

f.close()
