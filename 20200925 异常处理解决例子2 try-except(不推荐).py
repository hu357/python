try:
    int('abc')
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except:
    print('出错啦T_T')
