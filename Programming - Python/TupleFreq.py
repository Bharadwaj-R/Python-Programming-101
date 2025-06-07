thelist=[]
n=int(input('enter number of tuples to include : '))
freq=0
newlist=[]
finallist=[]
for i in range(n):
    inptup=tuple(input('enter elements of tuple separated by space : ').split())
    thelist.append(inptup)
for i in range(n):
    for j in range(n):
        if(thelist[i]==thelist[j]):
           freq=freq+1
    newlist.append(thelist[i]+tuple(str(freq),))
    freq=0
for i in range(n):
    for j in range(i+1,n):
        if newlist[i]==newlist[j] and newlist.count(newlist[j])>1:
            newlist[j]='*'
    if newlist[i]!='*':
        finallist.append(newlist[i])

print(finallist)
