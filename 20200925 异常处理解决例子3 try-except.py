try:
    f = open('我为什么是一个文件.txt','w')
    print(f.write('我存在了!'))
    sum = 1 + '1'
    f.close()
except  (OSError,TypeError):
    print('出错啦T_T')#出错没有关闭，所以并没有保存起来
