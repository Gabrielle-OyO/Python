


#while

import random
answer=random.randint(1,100)
counter=0
while True:
    counter+=1
    number=int(input('请输入：'))
    if number<answer:
        print('大一点')
    elif number>answer:
        print('小一点')
    else:
        print('恭喜你答对了')
        break

print('你一共猜了%d次'%counter)
if counter>7:
    print('大笨蛋')