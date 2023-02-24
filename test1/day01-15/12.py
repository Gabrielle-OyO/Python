

row=int(input('输入行数：'))
for i in range(row):
    for _ in range(i+1):    #'_'是循环标志
        print('*',end='')   #end=' '将结果输入到同一行 或者 添加空格
    print()


for i in range(row):
    for j in range(row):
        if j<row-i-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()

for i in range(row):
    for _ in range(row-i-1):
        print(' ',end='')
    for _ in range(2*i+1):
            print('*',end='')
    print()
