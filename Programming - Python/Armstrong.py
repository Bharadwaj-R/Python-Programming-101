n=int(input('enter a number : '))
m=n
count=0
r=0
s=0
while m!=0:
    m=m//10
    count=count+1
m=n
while m!=0:
    r=m%10
    s=s+(r**count)
    m=m//10
if s==n:
    print('Armstrong number')
else:
    print('not an Armstrong number')
