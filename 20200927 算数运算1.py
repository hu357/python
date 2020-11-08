算术运算
>>> a = int('123')
>>> a
123
>>> b = int('456')
>>> b
456
>>> a + b
579
>>> class New_int(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

	
>>> a = New_int(3)
>>> b = New_int(5)
>>> a + b
-2
>>> a - b
8

   #>>> class Try_int(int):
   #    def __add__(self,other):
   #        return self + other
   #    def __sub__(self,other):
   #        return self - other#
   #     
   #>>> a = Try_int(3)
   #>>> b = Try_int(5)#会出现无限递归，程序会崩溃
>>> class Try_int(int):
	def __add__(self,other):
		return int(self) + int(other)#返回就是整型相加的值
	def __sub__(self,other):
		return int(self) - int(other)#返回就是整形相减的值

	
>>> a = Try_int(3)
>>> b = Try_int(5)
>>> a + b
8
>>> a - b
-2

>>> class int(int):
	def __add__(self,other):
		return int.__sub__(self,other)

	
>>> a = int('5')
>>> a
5
>>> b = int(3)
>>> a + b
2


>>> class Nint(int):
	def __radd__(self,other):
		return int.__sub__(self,other)

	
>>> a = Nint(5)
>>> b = Nint(3)
>>> a + b
8
>>> a - b
2
>>> 1 + b#进行b - 1,self = b
2

>>> class int(int):
	def __rsub__(self,other):
		return int.__sub__(self,other)

	
>>> a = int(5)
>>> 3 - a
2
相当于  #>>> class int(int):
            #def __rsub__(self,other):
                #return int.__sub__(other,self)