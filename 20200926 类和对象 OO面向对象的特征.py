对象
对象 = 属性(静态特征) + 方法(动态动作)
属性：变量
方法：函数
类名是以大写字母开头的
类就是个模型，对象就是当下模型的实物
类-->对象：量产
class Turtle:#Python 中的类名约定以大写字母开头
    """关于类的一个简单例子"""
    #属性
    color = 'green'
    weigh = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    #方法
    def climb(self):
        print('我正在很努力地向前爬......')

    def run(self):
        print('我正在飞快地向前跑......')

    def bite(self):
        print('咬死你咬死你!!')

    def eat(self):
        print('有得吃，真满足^_^')

    def sleep(self):
        print('困了，睡了，晚安，Zzzz')
        
>>> tt = Turtle()
>>> Turtle()
<__main__.Turtle object at 0x0000017A02073D30>
>>> tt.climb()
我正在很努力地向前爬......
>>> tt.bite()
咬死你咬死你!!
>>> tt.eat()
有得吃，真满足^_^
>>> tt.sleep()
困了，睡了，晚安，Zzzz


OO面向对象的特征
OO = Object Oriented 面向对象

-封装(信息隐蔽技术)
>>> list1 = [2,1,7,5,3]
>>> list1.sort()
>>> list1
[1, 2, 3, 5, 7]
>>> list1.append(1)
>>> list1.append(9)
>>> list1
[1, 2, 3, 5, 7, 1, 9]

-继承(继承是子类自动共享父类之间数据和方法的机制)
>>> class Mylist(list):
	pass

>>> list2 = Mylist()
>>> list2.append(5)
>>> list2.append(3)
>>> list2.append(7)
>>> list2
[5, 3, 7]
>>> list2.sort()
>>> list2
[3, 5, 7]

-多态(不同对象对同一方法响应不同的行动)
多态就是一个方法可以被多种实例调用
多态:可对不同类型的对象执行相同的操作，而这些操作能够正常运行
>>> class A:
	def fun(self):
		print('我是小A....')

		
>>> class B:
	def fun(self):
		print('我是小B...')

		
>>> a = A()
>>> b = B()
>>> a.fun()#都调用fun函数,但实现结果不一样
我是小A....
>>> b.fun()
我是小B...