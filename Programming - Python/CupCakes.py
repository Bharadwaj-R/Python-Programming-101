t=int(input('enter the number of test cases : '))
for j in range(t):
    n=int(input('enter the number of total cupcakes : '))
    left=0
    for i in range(1,n):
        r=n%i
        if r>left:
            left=r
    print(n-left)

        
