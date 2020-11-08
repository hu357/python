构造和析构
--魔法方法总是被双下划线包围，例如__init__
--魔法方法的“魔力”体现在它们总能够在适当的时候被自动调用
new在内存给对象开盘存储空间地址，init初始化对象属性，str直接调用对象返回内容
构造函数
__init__(self[,...])
>>> class Rectangle:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def getPeri(self):
		return (self.x + self.y)*2
	def getArea(self):
		return self.x * self.y

	
>>> rect = Rectangle(3,4)
>>> rect.getPeri()
14
>>> rect.getArea()
12

__new__(cls[,...])#返回对象
1.__new__是给一个对象分配内存的方法
2.重新定义后，必须调用父类的内存分配方法
new就是对继承的类的参数的操作
>>> class CapStr(str):
	def __new__(cls,string):
		string = string.upper()
		return str.__new__(cls,string)

	
>>> a = CapStr('i love fishc.com!')
>>> a
'I LOVE FISHC.COM!'

析构函数，释放空间
__del__(self)#垃圾回收机制
>>> class C:
	def __init__(self):
		print('我是__init__方法，我被调用了...')
	def __del__(self):
		print('我是__del__方法，我被调用了...')

		
>>> c1 = C()
我是__init__方法，我被调用了...
>>> c2 = c1
>>> c3 = c2
>>> del c3
>>> del c2
>>> del c1
我是__del__方法，我被调用了...

