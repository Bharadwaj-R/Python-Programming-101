"""
doing all the basic operations on given 2 numbers
and also evaluating the expression a**b/b*a
the result should be 5.33 if a=2 and b=3
"""

a=int(input("enter the first number: "))
b=int(input("input the second number: "))
add=a+b
diff=a-b
pro=a*b
div=a/b
remainder=a%b
print('sum=',add)
print('difference =',diff)
print('product = ',pro)
print('division =',div)
print('remainder =',remainder)
result=a**b/b*a
print('result of the expression is ',result)

