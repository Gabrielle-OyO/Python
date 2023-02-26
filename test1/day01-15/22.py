

def foo():
    print('hello')
def foo():
    print('hello world')

foo()

''''''
from module221 import foo
foo()

from module222 import foo
foo()

''''''

import module221 as m1
import module222 as m2

m1.foo()
m2.foo()

def foo():
    pass
def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()

#test.py
import module3

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
