字典：{}
用 dict() 函数创建字典
工厂函数（类型）
str(),int(),list(),tuple()....
fromkeys(...)
dict.fromkeys(S[,v])->New dict with keys from S and values equal to v(v defaults to None).
#S是字典的键值
>>> dict1 = {}
>>> dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict1.fromkeys((1,2,3),'Number')
{1: 'Number', 2: 'Number', 3: 'Number'}
>>> dict1.fromkeys((1,2,3),('one','two','three'))
{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
>>> dict1.fromkeys((1,3),'数字')
{1: '数字', 3: '数字'}#不会修改，而是新创建一个字典

访问字典的方法
keys()#返回字典键的引用
>>> dict1 = dict1.fromkeys(range(32),'赞')
>>> dict1
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> for eachKey in dict1.keys():
	print(eachKey)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
values()
>>> for eachValue in dict1.values():
	print(eachValue)

	
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
items()#返回字典的像
>>> for eachItem in dict1.items():
	print(eachItem)

	
(0, '赞')
(1, '赞')
(2, '赞')
(3, '赞')
(4, '赞')
(5, '赞')
(6, '赞')
(7, '赞')
(8, '赞')
(9, '赞')
(10, '赞')
(11, '赞')
(12, '赞')
(13, '赞')
(14, '赞')
(15, '赞')
(16, '赞')
(17, '赞')
(18, '赞')
(19, '赞')
(20, '赞')
(21, '赞')
(22, '赞')
(23, '赞')
(24, '赞')
(25, '赞')
(26, '赞')
(27, '赞')
(28, '赞')
(29, '赞')
(30, '赞')
(31, '赞')
>>> print(dict1[31])
赞
>>> dict1.get(32)
>>> print(dict1.get(32))
None
>>> dict1.get(32,'木有')#没有即返回木有
'木有'
>>> dict1.get(31,'木有')#有即返回赞
'赞'

in 和 not in 
>>> 31 in dict1
True
>>> 32 in dict1
False

在字典中，查找的是键而不是值
在序列里，查找的是元素的值而不是索引号
>>> dict1.clear()#清空字典
>>> dict1
{}

>>> a = {'姓名':'小甲鱼'}
>>> b = a
>>> b
{'姓名': '小甲鱼'}
>>> a = {}#是给a赋一个新的空字典，clear是把原有的清空
>>> a
{}
>>> b
{'姓名': '小甲鱼'}

>>> a
{'姓名': '小甲鱼'}
>>> b
{'姓名': '小甲鱼'}
>>> a.clear()
>>> a
{}
>>> b
{}

copy()是浅拷贝，id 地址不同，不会被干扰
浅拷贝就是申请了新的内存空间然后附上同样的值
赋值就是直接申请一个指针然后指向原来的内存空间
>>> a = {1:'one',2:'two',3:'three'}
>>> b = a.copy()
>>> c = a
>>> a
{1: 'one', 2: 'two', 3: 'three'}
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> id(a)
2387780705216
>>> id(b)
2387781157632
>>> id(c)#赋值，仍然为原来的id地址
2387780705216
>>> c[4] = 'four'
>>> c
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> a
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}

pop()给定键弹出对应的值
popitem()是弹出一个像
>>> a.pop(2)
'two'
>>> a.popitem()#随机，没有顺序
(4, 'four')
setdefault()#在字典中找不到对应的键时进行添加
>>> a
{1: 'one', 3: 'three'}
>>> a.setdefault('小白')
>>> a
{1: 'one', 3: 'three', '小白': None}
>>> a.setdefault(5,'five')
'five'
>>> a
{1: 'one', 3: 'three', '小白': None, 5: 'five'}

update()#利用字典的映射关系去更新另外一个字典
>>> b = {'小白':'狗'}
>>> a.update(b)
>>> a
{1: 'one', 3: 'three', '小白': '狗', 5: 'five'}