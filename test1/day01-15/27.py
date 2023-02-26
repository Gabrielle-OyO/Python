

def foo():
    global b
    b='global'

    def bar():
        c=True
        print(a)
        print(b)
        print(c)

    bar()

if __name__ =='__main__':
    a=100
    b='zyy'
    foo()

#闭包
def main():
    #todo sth
    pass

if __name__ == '__main__':
    main()