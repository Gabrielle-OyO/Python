

list1=[1,3,5,7,100]

list1.append(200)
list1.insert(1,200)

list1.extend([30,66])
print(list1)
print(len(list1))

list1+=[1000,2000]
print(list1)
print(len(list1))

if 3 in list1:
    list1.remove(3)

if 1234 in list1:
    list1.remove(1234)

print(list1)

list1.pop(0)
print(list1)
list1.pop(len(list1)-1)
print(list1)

list1.clear()
print(list1)


fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

fruits2=fruits[1:4]
print(fruits2)

fruits3=fruits[:]
print(fruits3)

fruits4=fruits[-3:-1]
print(fruits4)
fruits5=fruits[::-1]
print(fruits5)

print()

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list1)
print(list2)
list3=sorted(list1,reverse=True)
print(list3)

print()
list4=sorted(list1,key=len)
print(list1)
print(list2)
print(list3)
print(list4)

list.sort(reverse=True)
print(list1)