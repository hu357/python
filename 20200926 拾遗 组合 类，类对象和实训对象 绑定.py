组合(把类的实例化放到一个新类里面)
现在要求定义一个类，叫水池，水池里要有乌龟和鱼
class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池里总公有乌龟 %d 只, 小鱼 %d 条！' %(self.turtle.num,self.fish.num))

>>> pool = Pool(1,10)
>>> pool.print_num()
水池里总公有乌龟 1 只, 小鱼 10 条！
同时给x，y给两个对象内各自的num成员（见Turtle和Fish的定义）赋初值
Fish对象和Turtle对象的构造函数都是有参数的，所以Pool的构造函数就需要两个参数，一个给了Fish一个给了Turtle
整性 是x = self.num存入的是一个值
.num的意思是实例对象的实例对象

Mix-in

类，类对象和实训对象
类定义         C
类对象         C
实例对象    a  b  c
>>> class C:
	count = 0

	
>>> a = C()
>>> b = C()
>>> c = C()
>>> a.count
0
>>> b.count
0
>>> c.count
0
>>> c.count += 10#生成了一个count覆盖了类count
>>> c.count
10
>>> a.count
0
>>> b.count
0
>>> C.count
0
>>> C.count += 100
>>> a.count
100
>>> b.count
100
>>> c.count
10
一般调用一个实例对象当中的函数时是要加()的，而这里c.count是变量不用括号
类中定义的属性在没有赋值的时候指向类属性地址，定义后开辟新的内存空间存放
属性的名字和方法相同，就会把方法覆盖掉
>>> class C:
	def x(self):
		print('X-man!')

		
>>> c = C()
>>> c.x()
X-man!
>>> c.x = 1#实例化后的c   创建一个x=1的属性，它属于c
>>> c.x
1
>>> c.x()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c.x()
TypeError: 'int' object is not callable
#--不要试图在一个类里边定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展
#--用不同的词性命名，如属性名用名词，方法名用动词

到底什么是绑定？
Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念
>>> class BB:
	def printBB():
		print('no zuo no die')

		
>>> BB.printBB()
no zuo no die
>>> bb = BB()
>>> bb.printBB()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    bb.printBB()
TypeError: printBB() takes 0 positional arguments but 1 was given


>>> class CC:
	def setXY(self,x,y):
		self.x = x
		self.y = y
	def printXY(self,x,y):
		print(self.x,self.y)

		
>>> dd = CC()
>>> dd.__dict__#查属性
{}#返回字典类型
>>> CC.__dict__
mappingproxy({'__module__': '__main__', 'setXY': <function CC.setXY at 0x00000148A7190C10>, 'printXY': <function CC.printXY at 0x00000148A7190DC0>, '__dict__': <attribute '__dict__' of 'CC' objects>, '__weakref__': <attribute '__weakref__' of 'CC' objects>, '__doc__': None})
>>> dd.setXY(4,5)
>>> dd.__dict__
{'x': 4, 'y': 5}
>>> CC.__dict__#用类对象
mappingproxy({'__module__': '__main__', 'setXY': <function CC.setXY at 0x00000148A7190C10>, 'printXY': <function CC.printXY at 0x00000148A7190DC0>, '__dict__': <attribute '__dict__' of 'CC' objects>, '__weakref__': <attribute '__weakref__' of 'CC' objects>, '__doc__': None})
相当于实例对象只存储参数，当要调用的时候就把参数和本身传入到类运算中
类中定义的属性和方法是静态变量，就算是类对象删除了，它们依然是存放在内存中的
类对象.__dict__查看内置方法
#-属性和方法是定义在静态空间里的
#类定义完了就变成了类对象，是动态的
>>> del CC
>>> ee = CC()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    ee = CC()
NameError: name 'CC' is not defined
>>> dd.printXY()
4  5 （本该为4  5，以下是自己出错的）
>>> dd.printXY()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dd.printXY()
TypeError: printXY() missing 2 required positional arguments: 'x' and 'y'