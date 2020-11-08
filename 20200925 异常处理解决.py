try- except 语句
try:
    检测范围
except  Exception[as reason]:
    出现异常(Exception)后的处理代码
    
    
try- finally 语句
try:
    检测范围
except Exception[as reason]:
    出现异常(Exception)后的处理代码
finally：
    无论如何都会被执行的代码
    
raise 语句
>>> raise
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise
RuntimeError: No active exception to reraise
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> raise ZeroDivisionError('除数为零的异常')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    raise ZeroDivisionError('除数为零的异常')
ZeroDivisionError: 除数为零的异常