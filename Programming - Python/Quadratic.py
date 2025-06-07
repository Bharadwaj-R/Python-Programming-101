import math
a=int(input('enter a : '))
b=int(input('enter b : '))
c=int(input('enter c : '))
dis=b**2-4*a*c
if dis<0:
    print('imaginary roots!!')
else:
    root1=(-b+math.sqrt(dis))/(2*a)
    root2=(-b-math.sqrt(dis))/(2*a)
    print('roots are',root1,'and',root2)
