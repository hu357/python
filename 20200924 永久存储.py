永久存储
pickle
存放:pickling
读取:unpickling
>>> import pickle
>>> my_list = [123,3.24,'小甲鱼',['another list']]
>>> pickle_file = open('my_list.pkl','wb')
>>> pickle.dump(my_list,pickle_file)
>>> pickle_file.close()

>>> pickle_file = open('my_list.pkl','rb')
>>> my_list2 = pickle.load(pickle_file)
>>> print(my_list2)
[123, 3.24, '小甲鱼', ['another list']]
dump 内存到硬盘；load 硬盘到内存