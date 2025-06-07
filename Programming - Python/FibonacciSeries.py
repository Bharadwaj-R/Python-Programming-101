a=0
b=1
c=0
n=int(input('enter the number of terms:'))
print(a,',',b,sep='',end='')
for i in range(1,n-1):
    c=a+b
    print(',',c,sep='',end='',)
    a,b=b,c
