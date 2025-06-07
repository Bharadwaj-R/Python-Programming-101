a=int(input('enter a number : '))
b=int(input('enter a number : '))
min=a if a<b else b
gcd=0
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        gcd=i
print('the GCD of',a,'and',b,'is',gcd)
