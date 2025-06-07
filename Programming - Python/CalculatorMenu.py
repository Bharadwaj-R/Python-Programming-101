x=int(input('enter the first number:'))
y=int(input('enter the second number'))
operator=input('enter the operator +, -, *, /, //, %')
result=0
if operator=='+':
    result=x+y
elif operator=='-':
    result=x-y
elif operator=='*':
    result=x*y
elif operator=='/':
    result=x/y
elif operator=='//':
    result=x//y
elif operator=='%':
    result=x%y
else:
    print('not a valid operator! Use a valid operator!')
print(result)
