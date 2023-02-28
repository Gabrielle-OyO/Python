

f=[x for x in range(1,10)]
print(f)

f=[x+y for x in 'ABCDE' for y in '1234567']
print(f)

import sys
f=[x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f))
print(f)

f=(x ** 2 for x in range(1,1000))
print(sys.getsizeof(f))
print(f)

for val in f:
    print(val)

    ##########################


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=a,a+b
        yield a

def main():
    for val in fib(20):
        print(val)

if __name__ =='__main__':
    main()