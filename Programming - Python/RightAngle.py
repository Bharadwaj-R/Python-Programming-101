a=int(input('enter the first side (A) :'))
b=int(input('enter the second side (B) :'))
c=int(input('enter the third side (C) :'))
if (a>b and a>c) and (a**2==b**2+c**2):
    print('right angled opposite to A')
elif(b>a and b>c) and (b**2==a**2+c**2):
    print('right angled opposite to B')
elif(c>a and c>b) and (c**2==a**2+b**2):
    print('right angled opposite to C')
else:
    print('not a right angled triangls')
