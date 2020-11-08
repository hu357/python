集合(集合内的元素都具有唯一性，无序性（不能索引集合中的某一个元素）)
>>> num = {}
>>> type(num)
<class 'dict'>
>>> num = {1,2,3,4,5}#没有体现映射关系
>>> type(num)
<class 'set'>

>>> num2 = {1,2,3,4,5,5,4,3,2}
>>> num2
{1, 2, 3, 4, 5}#重复的元素被自动剔除

如何创建一个集合
-一种是直接把一堆元素用花括号括起来
-一种是使用set()工厂函数
>>> set = set([1,2,3,4,5,5])
>>> set
{1, 2, 3, 4, 5}
去掉重复元素
>>> num1 = [1,2,3,4,5,5,3,1,0]
>>> temp = []
>>> for each in num1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5, 0]


>>> num1 = list(set(num1))#去掉重复元素的列表
>>> num1
[0, 1, 2, 3, 4, 5]

如何访问集合中的值
-可以使用for把集合中的数据一个个读取出来
-可以通过 in 和 not in 判断一个元素是否在集合中已经存在
>>> num2
{1, 2, 3, 4, 5}
>>> 1 in num2
True
>>> '1' in num2
False
>>> num2.add(6)#添加
>>> num2
{1, 2, 3, 4, 5, 6}
>>> num2.remove(5)#移除
>>> num2
{1, 2, 3, 4, 6}

不可变集合
frozen :冰冻的，冻结的
>>> num3 = frozenset([1,2,3,4,5])
>>> num3.add(0)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    num3.add(0)
AttributeError: 'frozenset' object has no attribute 'add'