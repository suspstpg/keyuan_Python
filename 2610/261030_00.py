# A=int(input('请输入分数:'))
# if A>=0 and A<=100:
#     print('输入正确')
#     if A>=90:
#         print('A')
#     elif A>=80:
#         print('B')
#     elif A>=70:
#         print('C')
#     elif A>=60:
#         print('D')
#     else:
#         print('F')
# else:
#     print('输入错误')
A=int(input('请输入分数:'))
if A>=0 and A<=100:
    print('输入正确')
    if A>=90:
       
        if A>=80:
            
            if A>=70:
                
                if A>=60:
                    print('D')
                else:
                    print('F')         
            else:
                print('C')
        else:
            print('B')
    else:
        print('A')



else:
    print('输入错误')
  

  