w=float(input())
t=float(input())
if (w+0.5<t) and w%5==0:
    print('%.2f'%(t-w-0.5))
else:
    print(t)
