

str='hello,world,hello,zyy!'

print(len(str))
print(str.capitalize())
print(str.title())
print(str.upper())
print(str.find('yy'))
print(str.find('shit'))
# 引起异常
# print(str.index('or'))
# print(str.index('shit'))

print(str.startswith('He'))
print(str.startswith('he'))

print(str.endswith('!'))

print(str.center(50,'*'))
print(str.rjust(50,'-'))

str0='abc123456'
print(str0.isdigit())
print(str0.isalpha())
print(str0.isalnum())

str1='   zyyyyyy@132.com    '
print(str1)
print(str1.strip())

a,b=5,10
print('%d * %d = %d' %(a,b,a*b) )

print('{0}*{1}={2}'.format(a,b,a*b))

print(f'{a}*{b}={a*b}')



