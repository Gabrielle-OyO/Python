
m=int(input('m= '))
n=int(input('n= '))

fm=1
for num in range(1,m+1):
    fm*=num
fn=1
for num in range(1,n+1):
    fn*=num
fm_n=1
for num in range(1,m-n+1):
    fm_n*=num

f=fm//fn//fm_n
print(f)


def fac(num):
    result=1
    for n in range(1,num+1):
        result*=n
    return result
m=int(input('m= '))
n=int(input('n= '))

facc=fac(m)//fac(n)//fac(m-n)
print(facc)

import math
m=int(input('m= '))
n=int(input('n= '))

facc=math.factorial(m)//math.factorial(n)//math.factorial(m-n)
print(facc)
