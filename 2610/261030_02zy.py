print('请确保正确输入')
print('请输入两个数和一个运算符')
a=float(input('请输入一个数：'))
b=input("请输入一个计算符号：'+'-'×(*)'÷(/)' :")
c=float(input('请输入另一个数：'))
if b=='+':
    result = a + c
    print("{a}+{c}={result}".format(a=a, c=c, result=result))
elif b=='-':
    result = a - c
    print("{a}+{c}={result}".format(a=a, c=c, result=result))
elif b=='*':
    result = a * c
    print("{a}+{c}={result}".format(a=a, c=c, result=result))
elif b=='/':
    result = a / c
    print("{a}+{c}={result}".format(a=a, c=c, result=result))
else:
    print('输入错误')
