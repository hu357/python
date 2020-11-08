lambda 表达式
>>> def ds(x):
	return 2*x+1
>>> ds(5)
11
>>> lambda x : 2*x+1
<function <lambda> at 0x00000297E7E518B0>
>>> g = lambda x : 2*x+1#不用考虑申请和释放资源
>>> g(5)
11

>>> def add(x,y):
	return x+y
>>> add(3,4)
7
>>> lambda x,y : x + y
<function <lambda> at 0x00000297E7E51820>
>>> g = lambda x,y : x + y
>>> g(3,4)
7
lambda 表达式的作用
-Python写一些执行脚本时，使用 lambda 就可以省下定义函数过程，比如说我们只是需要写个简单的脚本来管理服务器时间，我们就不需要专门定义一个函数然后再写调用，使用 lambda 就可以使得代码更加精简
-对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，有时候给函数起个名字也是比较头疼的问题，使用 lambda 就不需要考虑命名的问题了
-简化代码的可读性，由于普通的屌丝函数阅读经常要跳到开头 def 定义部分，使用 lambda 函数可以省去这样的步骤


两个牛逼的BIF
filter()过滤器功能#把任何非 True 的内容过滤掉
>>> filter(None, [1, 0 , False , True])
<filter object at 0x00000297E7E469D0>
>>> list(filter(None, [1, 0 , False , True]))
[1, True]

>>> def odd(x):
	return x % 2
>>> temp = range(10)
>>> show = filter(odd,temp)
>>> list(show)
[1, 3, 5, 7, 9]
>>> list(filter(lambda x : x % 2, range(10)))
[1, 3, 5, 7, 9]

map()会根据提供的函数对指定序列做映射
有两个内置函数：一个函数和一个可迭代的序列
功能：将序列的每一个元素作为函数的参数进行运算加工，直到可迭代序列的每个元素都加工完毕，返回所有加工后的元素构成的新序列
1.映射就是让指定的参数乖乖站好
2.然后挨个进入指定的函数处理
3.然后把运算后的值再排好队，挨个返回
>>> list(map(lambda x : x * 2, range(10)))#0，1，2，3，4，5，6，7，8，9分别乘以2
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]