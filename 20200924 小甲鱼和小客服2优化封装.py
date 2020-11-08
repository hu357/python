def save_file(boy,girl,count):#封装保存文件
    file_name_boy = 'boy_' +str(count) + '.txt'
    file_name_girl = 'girl_' +str(count) + '.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):#封装分割文件
    f = open('record.txt',encoding='utf-8')

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role,content) = each_line.split(':',1)
            #这里的split第二个参数1的意思是分割一次，返回两段字符串的意思
            #我们这里进行字符串分割
            if role == '小甲鱼':
                boy.append(content)
            if role == '小客服':
                girl.append(content)
        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count += 1

    save_file(boy,girl,count)

    f.close()

split_file('record.txt')
