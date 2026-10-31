print('请输入3个数')
a=input('请输入第一个数：')
b=input('请输入第二个数：')
c=input('请输入第三个数：')
a=float(a)
b=float(b)
c=float(c)
if a+b>c and a+c>b and b+c>a:

    import math
    p = float((a + b + c) / 2)
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    if s>0:
         print('三角形的面积为：%.2f'%s)
    else:
         print('不能组成三角形')
else:
    print('不能组成三角形')