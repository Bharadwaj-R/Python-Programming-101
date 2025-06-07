thelist=list(range(1,11))
print('the list contains following elements : ')
for i in range(len(thelist)):
    print(thelist[i],end=' ')
split=int(input('\nhow many numbers in the first list : '))
newlist1=list(thelist[:split])
newlist2=list(thelist[split:])
print('the new lists are :',newlist1,newlist2)
