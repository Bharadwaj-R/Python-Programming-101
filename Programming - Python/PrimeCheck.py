n=int(input('enter a number to check prime or nor : '))
fact=0
for i in range(1,n):
    if n%i==0:
        fact=fact+1
if fact>1:
    print('not a prime')
else:
    print('prime')
