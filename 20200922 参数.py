形式参数(parameter)
实际参数(argument)
>>>def MyFirstFunction(name):
'函数定义过程中的name是叫形参'
#因为Ta只是一个形式，表示占据一个形参位置
print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')
函数文档
>>> MyFirstFunction.__doc__#打印属性，用双下横线
'函数定义过程中的name是叫形参'

>>> help(MyFirstFunction)
Help on function MyFirstFunction in module __main__:

MyFirstFunction(name)
    函数定义过程中的name是叫形参

>>> print.__doc__
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

关键字参数
>>> def SaySome(name,words):
	print(name + '->' + words)
>>> SaySome('小甲鱼','让编程改变世界！')
小甲鱼->让编程改变世界！
>>> SaySome(name='小甲鱼',words='让编程改变世界')
小甲鱼->让编程改变世界

默认参数
默认参数是定义了关键值的参数
>>> def SaySome(name='小甲鱼',words='让编程改变世界'):
	print(name + '->' + words)
>>> SaySome()
小甲鱼->让编程改变世界
>>> SaySome('老甲鱼')
老甲鱼->让编程改变世界

收集参数(可变参数)
>>> def test(*parans):
	print('参数的长度是:',len(parans));
	print('第二个参数是:',parans[1]);
>>> test(1,'小甲鱼',5,6,7,8)
参数的长度是: 6
第二个参数是: 小甲鱼

>>> def test(*parans,exp):
	print('参数的长度是:',len(parans),exp);
	print('第二个参数是:',parans[1]);
>>> test(1,'小甲鱼',5,6,7,8,exp=9)
参数的长度是: 6 9
第二个参数是: 小甲鱼

>>> def test(*parans,exp=9):
	print('参数的长度是:',len(parans),exp);
	print('第二个参数是:',parans[1]);
>>> test(1,'小甲鱼',5,6,7,8)
参数的长度是: 6 9
第二个参数是: 小甲鱼