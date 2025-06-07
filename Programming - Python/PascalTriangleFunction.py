def pascal(n):
    s=0
    for i in range(1,n+1):
        for k in range(n+1,i,-1):
            print('   ',end='')
        for j in range(1,i+1):
            if j==1:
                s=1
                print('   %3d'%s,end='')
            else:
                s=int((s*(i-j+1))/(j-1))
                print('   %3d'%s,end='')
        print()
n=int(input('enter number or rows : '))
pascal(n)
