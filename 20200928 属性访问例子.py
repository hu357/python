class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(name,value)
            #或者self.__dict__[name] = value
            #这个魔法方法是对属性赋值时才会触发，而字典不是属性，所以不会触发
            #self.__dict__是字典，所以不会触发给属性赋值的魔法方法

    def getArea(self):
        return self.width * self.height
