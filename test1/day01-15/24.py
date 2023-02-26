

def is_palindrome(num):
    temp=num
    total=0
    while temp>0:
        total=total*10+temp%10
        temp //= 10
    return total == num

if __name__=='__main__':
    num=int(input('输入正整数：'))
    if is_palindrome(num) :
        print('%d是回文素数'%num)
    else:
        print('%d不是回文素数'%num)
