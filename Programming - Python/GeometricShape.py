"""
Finding the area and perimeter of circle, rectangle, and area of right angled triangle
For circle -    area = pi*r*r      perimeter = 2*pi*r
For rectangle - area = l*b         perimeter = 2*(l+b)
for triangle -  area = (1/2)*b*h
"""

pi=3.14
r=int(input("enter the radius of circle: "))
perimeter=2*pi*r
print('perimeter of circle = ',perimeter)
area=pi*r*r
print('area of circle = ', area)
l=int(input('enter the length of rectangle: '))
b=int(input('enter the breadth of rectnagle: '))
perimeter=2*(l+b)
print('perimeter of rectangle is = ',perimeter)
area=l*b
print('area of rectangle = ',area)
base=int(input('enter the base of the triangle: '))
height=int(input('enter the height of the triangle: '))
area=(1/2)*base*height
print('area of right angled triangel is = ', area)
