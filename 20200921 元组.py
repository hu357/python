元组：戴上了枷锁的列表
由于和列表是近亲关系，所以元组和列表在实际使用上是非常相似的
列表可以任意修改其中的元素（插入，删除等），而元组不能改变
元素不能修改元素，但可以直接修改元组整体
-创建和访问一个元组tuple(),最重要的是逗号
创建列表[]
temp = 2,3,4
temp = (1,)
temp = 1,
<<<8 * (8)
<<<64
<<<8 * (8,)
<<<(8,8,8,8,8,8,8,8)  
type(temp)查类别
-更新和删除一个元组
temp[:2]是表示index为2的前部分的元组
>>> temp = temp[:2] + ('意境',) + temp[2:]
>>> temp
('小甲鱼', '黑夜', '意境', '迷途', '小布丁')
del temp 删除元组
-元组相关的操作符

