函数与过程
函数(function):有返回值
过程(procedure)是简单，特殊并且没有返回值的
python只有函数没有过程
>>> def hello():
	print('hello FishC!')
>>> temp = hello()
hello FishC!
>>> temp
>>> print(temp)
None
>>> type(temp)
<class 'NoneType'>

返回值
>>> def hello():
	print('hello FishC!')
>>> temp = hello()
hello FishC!
>>> temp
>>> print(temp)
None
>>> type(temp)
<class 'NoneType'>

>>> def back():
	return [1,'小甲鱼',3,6,7]
>>> back()
[1, '小甲鱼', 3, 6, 7]
>>> def back():
	return 1,'小甲鱼',3,6,7
>>> back()
(1, '小甲鱼', 3, 6, 7)

函数变量的作用域问题
局部变量(Local Variable)
全局变量(Global Variable),不要在函数内部去修改，Python会在内部新建一个名字一样的局部变量
