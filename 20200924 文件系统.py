文件系统
模块就是可用代码段的打包
模块是一个包含所有你定义的函数和变量的文件，后缀为.py,模块可以被别的程序引入，以使用该模块中的函数等功能
OS:Operating System
我们所知道常用的操作系统就有：Windows,Mac,OS,Linux,UNIX等，这些操作系统底层对于文件系统的访问工作原理是不一样的
因此你可能就要针对不同的系统来考虑使用哪些文件系统模块......这样的做法是非常不友好且麻烦的，因为这样就意味着当你
的程序运行环境一改变，你就要相应的去修改大量的代码来应付
有了OS模块，我们不需要关心什么操作系统下使用什么模块，OS模块会帮你选择正确的模块并调用

os模块中关于文件/目录常用的函数使用方法
函数名                         使用方法
getcwd()                    返回当前工作目录
chdir(path)                 改变工作目录
listdir(path='.')           列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）
mkdir(path)                 创建单层目录，如该目录已存在抛出异常
makedirs(path)              递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突
remove(path)                删除文件
rmdir(path)                 删除单层目录，如该目录非空则抛出异常
removedirs(path)            递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
rename(old, new)            将文件old重命名为new
system(command)             运行系统的shell命令
walk(top)                   遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])以下是支持路径操作中常用到的一些定义，支持所有平台
os.curdir                   指代当前目录（'.'）
os.pardir                   指代上一级目录（'..'）
os.sep                      输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）
os.linesep                  当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）
os.name                     指代当前使用的操作系统（包括：'posix',  'nt', 'mac', 'os2', 'ce', 'java'）


os.path模块中关于路径常用的函数使用方法
函数名                                 使用方法
basename(path)                  去掉目录路径，单独返回文件名
dirname(path)                   去掉文件名，单独返回目录路径
join(path1[, path2[, ...]])     将path1, path2各部分组合成一个路径名
split(path)                     分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在
splitext(path)                  分离文件名与扩展名，返回(f_name, f_extension)元组
getsize(file)                   返回指定文件的尺寸，单位是字节
getatime(file)                  返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getctime(file)                  返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getmtime(file)                  返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
                        以下为函数返回 True 或 False
exists(path)                    判断指定路径（目录或文件）是否存在
isabs(path)                     判断指定路径是否为绝对路径
isdir(path)                     判断指定路径是否存在且是一个目录
isfile(path)                    判断指定路径是否存在且是一个文件
islink(path)                    判断指定路径是否存在且是一个符号链接
ismount(path)                   判断指定路径是否存在且是一个挂载点#挂载点就是盘符
samefile(path1, paht2)          判断path1和path2两个路径是否指向同一个文件


>>> import random
>>> secert = random.randint(1,10)
>>> secert
3
>>> import os
>>> os.getcwd()
'E:\\BaiduNetdiskDownload\\python-3.8.2'#工作目录
>>> os.listdir('E:\\')#E盘中的所有文件名
#$RECYCLE.BIN是一个回收站

>>> os.system('cmd')
-1073741510
>>> os.system('calc')#打开计算机
0
>>> os.listdir(os.curdir)#返回当前目录
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'practice', 'pycharm-professional-2020.1.2.exe', 'python-3.8.2-amd64.exe', 'python-3.8.2.exe', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', '免责声明.url', '安装步骤.jpg', '实验一.py', '实验三.py', '实验二.py', '实验四.py', '点击查看：管家团队旗下微信公众号.url']



>>> os.path.getatime('E:\\test.txt')
1600908184.3611193
>>> import time
>>> time.gmtime(os.path.getatime('E:\\test.txt'))
time.struct_time(tm_year=2020, tm_mon=9, tm_mday=24, tm_hour=0, tm_min=43, tm_sec=4, tm_wday=3, tm_yday=268, tm_isdst=0)
>>> time.localtime(os.path.getatime('E:\\test.txt'))
time.struct_time(tm_year=2020, tm_mon=9, tm_mday=24, tm_hour=8, tm_min=43, tm_sec=4, tm_wday=3, tm_yday=268, tm_isdst=0)
>>> time.localtime(os.path.getmtime('E:\\test.txt'))
time.struct_time(tm_year=2020, tm_mon=9, tm_mday=24, tm_hour=10, tm_min=44, tm_sec=41, tm_wday=3, tm_yday=268, tm_isdst=0)
>>> time.localtime(os.path.getctime('E:\\test.txt'))
time.struct_time(tm_year=2020, tm_mon=9, tm_mday=24, tm_hour=8, tm_min=41, tm_sec=47, tm_wday=3, tm_yday=268, tm_isdst=0)
