内嵌函数和闭包
global 关键字
不能修改全局变量，否则屏蔽(Shadowing)
>>> count = 5#全局变量
>>> def Myfun():
	count = 10#局部变量
	print(10)
>>> Myfun()
10
>>> print(count)#Shadowing
5

>>> def Myfun():
	global count
	count = 10
	print(10)
>>> Myfun()
10
>>> print(count)
10

内嵌函数
函数可以嵌套定义
>>> def fun1():
	print('fun1()正在被调用....')
	def fun2():
		print('fun2()正在被调用....')
	fun2()
>>> fun1()
fun1()正在被调用....
fun2()正在被调用....

闭包
如果在一个内部函数里对外部作用域（但不是在全局作用域的）的变量进行引用，那么内部函数就会被认为是闭包
>>> def FunX(x):
	def FunY(y):
		return x*y
	return FunY
>>> i = FunX(8)
>>> i
<function FunX.<locals>.FunY at 0x00000265907714C0>
>>> type(i)
<class 'function'>
>>> i(5)
40
>>> FunX(8)(5)
40

>>> def Fun1():
	x = 5
	def Fun2():
		x *= x
		return x
	return Fun2()
>>> Fun1()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    Fun1()
  File "<pyshell#39>", line 6, in Fun1
    return Fun2()
  File "<pyshell#39>", line 4, in Fun2
    x *= x
UnboundLocalError: local variable 'x' referenced before assignment#被屏蔽
>>> def Fun1():
	x = [5]
	def Fun2():
		x[0] *= x[0]
		return x[0]
	return Fun2()
>>> Fun1()
25

>>> def Fun1():
	x = 5
	def Fun2():
		nonlocal x#强制说明x不是一个局部变量
		x *= x
		return x
	return Fun2()
>>> Fun1()
25