对象，函数，模块
def 定义函数
>>> def MyFirstFunction():
	print('这是我创建的第一个函数！')
	print('我表示很激动.....')
>>> MyFirstFunction()
这是我创建的第一个函数！
我表示很激动.....

>>> def MySecondFunction(name):
	print(name + '我爱你！')
>>> MySecondFunction('小甲鱼')
小甲鱼我爱你！

>>> def add(num1,num2):
	result = num1 + num2
	print(result)
>>> add(2,5)
7

>>> def add(num1,num2):
	return  (num1 + num2)
>>> print(add(5,6))
11
