class CountList:
    def __init__(self,*args):#*args是不定长参数
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)#开始时初始化为0
        #fromkeys()用于创建一个字典，以序列中元素做字典的键，value为字典所有键对应的初始值

    def __len__(self):
        return len(self,values)

    def __getitem__(self,key):#key是相应的下标
        self.count[key] += 1
        return self.values[key]
