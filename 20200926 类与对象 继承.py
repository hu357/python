我们试图模拟一个场景，里边有一只乌龟和十条鱼，乌龟通过吃鱼来补充体力，当乌龟体力消耗殆尽或者鱼被吃光则游戏结束
现在我们想要扩展游戏，给鱼类进行细分，有金鱼(Goldfish)，鲤鱼(Crap)，三文鱼(Salmon)，还有鲨鱼(Shark)

继承
class DerivedClassName(BaseClassName):#括号内称为基类，父类或超类，括号前称为子类
	...
	
>>> class Parent:
	def hello(self):
		print('正在调用父类的方法...')

		
>>> class Child(Parent):
	pass

>>> p = Parent()
>>> p.hello()
正在调用父类的方法...
>>> c = Child()
>>> c.hello()
正在调用父类的方法...
#如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性，对父类不受影响
#父类中的私有方法-子类的对象调用-需要输入父类的名字
>>> class Child(Parent):
	def hello(self):
		print('正在调用子类的方法...')

		
>>> c = Child()
>>> c.hello()
正在调用子类的方法...
>>> p.hello()
正在调用父类的方法...
#self就是指向对象自己的指针，每个对象都有一个self,指向自己被分配的内存空间

import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print('我的位置是：',self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃^_^')
            self.hungry = False
        else:
            print('太撑了，吃不下了！！')
>>> fish = Fish()
>>> fish.move()
我的位置是： -1 0
>>> fish.move()
我的位置是： -2 0
>>> goldfish = Goldfish()
>>> goldfish.move()
我的位置是： 5 1
>>> shark = Shark()
>>> shark.eat()
吃货的梦想就是天天有的吃^_^
>>> shark.eat()
太撑了，吃不下了！！
>>> shark.move()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    shark.move()
  File "E:/practice/20200926 类和对象 继承 吃鱼游戏1.py", line 9, in move
    self.x -= 1
AttributeError: 'Shark' object has no attribute 'x'

-调用未绑定的父类方法
-使用super函数
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print('我的位置是：',self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃^_^')
            self.hungry = False
        else:
            print('太撑了，吃不下了！！')

>>> shark = Shark()
>>> shark.move()
我的位置是： 3 10
>>> shark.move()
我的位置是： 2 10
>>> Fish.__init__(shark)
>>> shark.move()
我的位置是： 5 3

多重继承
class DerivedClassName(Base1,Base2,Base3):
	......
	
>>> class Base1:
	def foo1(self):
		print('我是foo1，我为Base1代言...')

		
>>> class Base2:
	def foo2(self):
		print('我是foo2，我为Base2代言...')

		
>>> class C(Base1,Base2):
	pass

>>> c = C()
>>> c.foo1()
我是foo1，我为Base1代言...
>>> c.foo2()
我是foo2，我为Base2代言...