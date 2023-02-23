


username=input('用户名：')
password=input('密码：')
if username == 'admin' and password == '123456':
    print('succeed！')
else:
    print('failed!')

# if  elif  else


x=float(input('x='))
if x > 1 :
    y = 3*x-5
elif x>=-1:
    y=x+2
else:
    y=5*x+3
print('f(%.2f) = %.2f' % (x,y))