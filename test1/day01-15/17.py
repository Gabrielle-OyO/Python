

#斐波那契数列

a=0
b=1
febo=int(input('输出斐波那契额数列个数：'))
for _ in range(febo):
    a,b=b,a+b
    print(a,end=' ')
print()

fibo=[1,1]
for num in range(2,20):
    sum=fibo[num-2]+fibo[num-1]
    fibo.append(sum)#把结果录入数组中
print(fibo)
print(len(fibo))