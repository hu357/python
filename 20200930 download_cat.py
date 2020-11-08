import urllib.request

response = urllib.request.urlopen('http://placekitten.com/500/600')
cat_img = response.read()
#图片也是文件，它也是二进制数据组成的
with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
#程序在哪，图片就会保存在哪
#with关键字是可以自动的关闭文件
#with as 可以在open文件后自动close文件,方便操作



