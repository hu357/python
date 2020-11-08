OOA:面向对象分析
OOD:面向对象设计
OOP:面向对象编程

self是什么？
Python的self相当于C++的this指针
self定义的方法只能对象自己使用不能类调用
self的作用主要表示这个变量是类中的公共变量
类在定义是将self写进第一个参数
>>> class Ball:
	def setName(self,name):
		self.name = name
	def kick(self):
		print('我叫%s,该死的，谁踢我...' % self.name)

		
>>> a = Ball()
>>> a.setName('球A')
>>> b = Ball()
>>> b.setName('球B')
>>> c = Ball()
>>> c.setName('土豆')
>>> a.kick()
我叫球A,该死的，谁踢我...
>>> b.kick()
我叫球B,该死的，谁踢我...
>>> c.kick()
我叫土豆,该死的，谁踢我...

Python的魔法方法
__init__(self)将init方法称为构造方法
__init__(self,param1,param2...)
init方法就是车的基本要素,重写就是改装
意思就是将外面传进来的参数赋值给类内的变量
注意：这里的__init__前后是各两个下划线
>>> class Ball:
	def __init__(self,name):
		self.name = name
	def kick(self):
		print('我叫%s,该死的，谁踢我...' % self.name)

		
>>> b = Ball('土豆')
>>> b.kick()
我叫土豆,该死的，谁踢我...
系统会自动调用构造函数，通过构造函数对类进行初始化操作

公有和私有？
>>> class Person:
	name = '小甲鱼'

	
>>> p = Person()
>>> p.name
'小甲鱼'

name mangling名字改编，名字重组
在Python中定义私有变量只需要在变量名或函数名前加上"__"两个下划线,那么这个函数或变量就会为私有的了
._类名__变量名
>>> class Person:
	__name = '小甲鱼'
	def getName(self):
		return self.__name

	
>>> p = Person()
>>> p.getName()
'小甲鱼'
>>> p._Person__name
'小甲鱼'