



import datetime
start=datetime.datetime.now()#⏲

perfect_number=[]
for i in range(2,1001):
    factor_sum=[]
    for j in range(1,int(i/2)+1):
        if i%j ==0:
            factor_sum.append(j)

    if sum(factor_sum)==i:
        print(f"{i}:{factor_sum}")
        perfect_number.append(factor_sum)
print(perfect_number)


end=datetime.datetime.now()
print(f"程序运行时间：{end-start}秒")