def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('请输入一个正整数:'))
result= factorial (number)
print("%d 的阶乘是 : %d" % (number,result))
#factorial(5)=5*factorial(4)
#factorial(4)=4*factorial(3)
#factorial(3)=3*factorial(2)
#factorial(2)=2*factorial(1)
#factorial(1)=1 (return)
