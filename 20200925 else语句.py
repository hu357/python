try:
	print(int('123'))
except ValueError as reason:
	print('出错啦:' + str(reason))
else:
	print('无任何异常！')
