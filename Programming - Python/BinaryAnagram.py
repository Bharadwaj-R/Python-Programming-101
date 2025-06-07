def binary(n):
    s=r=p=0
    while n!=0:
        r=n%2
        s=s+(r*(10**p))
        n=n//2
        p+=1
    return(s)

n1=int(input('enter a number : '))
n2=int(input('enter a number : '))
n1=str(binary(n1))
n2=str(binary(n2))
count1=0
count2=0
for i in range(len(n1)):
    if n1[i]=='1':
        count1+=1
for i in range(len(n2)):
    if n2[i]=='1':
        count2+=1
               
if count1==count2:
    print('binary anagrams')
else:
    print('not binary anagrams')
