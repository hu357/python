try:
    f = open('我为什么是一个文件.txt','w')
    print(f.write('我存在了!'))
    sum = 1 + '1'
except  (OSError,TypeError):
    print('出错啦T_T')
finally:
    f.close()
    
