N=int(input('enter the value of N (no. of rows) : '))
M=int(input('enter the value of M (no. of columns) : '))
list1=[]
arr=[]
for i in range(N):
    for j in range(M):
        item=int(input('enter the element : '))
        list1.append(item)
    arr.append(list1)
    list1=[]
print('original array : ')
for i in range(N):
    for j in range(M):
        print('%-3d'%arr[i][j],end=" ")
    print()
R=int(input('enter the value of R (repetetion in row) : '))
C=int(input('enter the value of C (repetetion in column) : '))
for i in range(R):
    for j in range(N):
        for k in range(M):
            print(str(arr[j][k])*C,end=' ')
    print()

        
