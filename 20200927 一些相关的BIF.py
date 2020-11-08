一些相关的BIF
--issubclass(class,classinfo)#class 检索候选的类是否是它的子类
1.一个类被认为是其自身的子类
2.classinfo可以是类对象组成的元组，只要class与其中任何一个候选类的子类，则返回True
>>> class A:
	pass

>>> class B(A):
	pass

>>> issubclass(B,A)
True
>>> issubclass(B,B)
True
>>> issubclass(B,object)#object是一个所有类的父类
True
>>> class C:
	pass

>>> issubclass(B,C)
False

--isinstance(object,classinfo)#第一个传入一个实例对象，第二个传入一个类
1.如果第一个参数不是对象，则永远返回False
2.如果第二个参数不是类或者由类对象组成的元组，会抛出一个TypeError异常
isinstance()与 type()区别
type() 不会认为子类是一种父类类型，不考虑继承关系
isinstance() 会认为子类是一种父类类型，考虑继承关系
如果要判断两个类型是否相同推荐使用 isinstance()
>>> b1 = B()
>>> isinstance(b1,B)
True
>>> isinstance(b1,A)
True
>>> isinstance(b1,C)
False
>>> isinstance(b1,(A,B,C))
True

--hasattr(object,name)#测试一个对象里面是否有指定的属性,object是对象,name是属性
attr = attribute:属性
>>> class C:
	def __init__(self,x=0):
		self.x = x

		
>>> c1 = C()
>>> hasattr(c1,'x')
True
>>> hasattr(c1,x)#要对属性加引号
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    hasattr(c1,x)
NameError: name 'x' is not defined

--getattr(object,name[,default])
getattr()函数用于返回一个对象属性值
>>> getattr(c1,'x')
0
>>> getattr(c1,'y')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    getattr(c1,'y')
AttributeError: 'C' object has no attribute 'y'
>>> getattr(c1,'y','您所访问的属性不存在....')
'您所访问的属性不存在....'

--setattr(object,name,value)
>>> setattr(c1,'y','fishc')
>>> getattr(c1,'y','您所访问的属性不存在....')
'fishc'

--delattr(object,name)#删除对象中指定的属性
>>> delattr(c1,'y')
>>> delattr(c1,'y')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    delattr(c1,'y')
AttributeError: y


--property(fget=None,fset=None,fdel=None,doc=None)#通过属性来设置属性
>>> class C:
	def __init__(self,size=10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size = value
	def delSize(self):
		del self.size
	x = property(getSize,setSize,delSize)

	
>>> c1 = C()
>>> c1.getSize()
10
>>> c1.x
10
>>> c1.x = 18
>>> c1.x
18
>>> c1.size
18
>>> c1.getSize()
18
>>> del c1.x
>>> c1.x
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c1.x
  File "<pyshell#45>", line 5, in getSize
    return self.size
AttributeError: 'C' object has no attribute 'size'
property()括号内的参数位置决定方法的作用:读取，赋值，删除