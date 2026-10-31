"xie78.2  yh54.6  bb68"


a=input("请输入商品名")
b=int(input("请输入数量"))
if (a=="shoes"):
    s=78.2*b
elif (a=="colthes"):
    s=54.5*b
else:s=68*b
print("总价",s)
c=int(input("顾客已付："))
SSS=s-c
print("需要处理",SSS)
