


radius=float(input('圆的半径：'))
perimeter=2*3.14*radius
area=3.14*radius*radius
print('周长：%.2f' %perimeter)
print('面积：%.2f' %area)

year=int(input('输入年份：'))
is_leap=year % 4 == 0 and year % 100 != 0 or\
    year % 400 == 0
print(is_leap)