

list=[1,3,5,7,100]
print(list)

list0=['hello']*3
print(list0)
print(len(list))

print(list[0])
print(list[4])

print(list[-1])
print(list[::-1])
print(list[-3])

print('#############')
list[2]=300
print(list)

for index in range(len(list)):
    print(list[index])

for elem in list:
    print(elem)

for index,elem in enumerate(list):
    print(index,elem)




