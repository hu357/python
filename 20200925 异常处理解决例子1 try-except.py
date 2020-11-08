try:
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except  OSError as reason:
    print('文件出错啦T_T\n错误的原因是：'+ str(reason))
except  TypeError as reason:
    print('类型出错啦T_T\n错误的原因是：'+ str(reason))



try:
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except  (OSError,TypeError):
    print('出错啦T_T')
