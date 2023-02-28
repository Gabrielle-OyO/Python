


t = ('骆昊', 38, True, '四川成都')
print(t)
print(t[0])
print(t[3])

for member in t:
    print(member)

#t[0]='zyy'
person=list(t)
print(person)

person[0]='zyyyyy'
person[1]='1000'

print(person)

fruits_list=['apple','banana','orange']
fruits_tuple=tuple(fruits_list)
print(fruits_tuple)

import sys
print(sys.getsizeof(t))
print(sys.getsizeof(person))