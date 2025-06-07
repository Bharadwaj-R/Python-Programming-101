start=int(input('enter the start of range : '))
end=int(input('enter the end of range : '))
fact=0
for n in range(start,end+1):
    for i in range(1,n):
        if n%i==0:
            fact=fact+1
    if fact==1:
        print(n,end=' ')
    fact=0
