

import datetime
start=datetime.datetime.now()

sushu=[]
for i in range(2,101):
    flag=0
    for j in range(2,i-1):
        if i%j == 0:
            flag=1
            break
        else:
            flag=0
    if flag==0:
            sushu.append(i)

print(sushu)

end=datetime.datetime.now()
print(f'running:{end-start}')